from discord import Client, Intents
import re
from dotenv import load_dotenv
import os
import requests
load_dotenv()

# Functions
def c_to_f(c_temp):
    c_temp = float(c_temp.lower().replace('c', ''))
    f_temp = (c_temp * 9/5) + 32
    return f"{c_temp}C -> {round(f_temp, 1)}F"

def f_to_c(f_temp):
    f_temp = float(f_temp.lower().replace('f', ''))
    c_temp = (f_temp - 32) * 5/9
    return f"{f_temp}F -> {round(c_temp, 1)}C"

def get_cad_exchange_rate():
    url = "https://open.er-api.com/v6/latest/USD"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        cad_rate = data["rates"]["CAD"]
        return cad_rate
    else:
        return None

def cad_to_usd(cad, rate):
    cad = float(cad.lower().replace('cad', ''))
    # Change to import what the current exchange rate is
    usd = cad / rate
    return f"{cad:.2f}CAD -> {round(usd, 2):.2f}USD"
    

def usd_to_cad(usd, rate):
    usd = float(usd.lower().replace('usd', ''))
    # Change to import what the current exchange rate is
    cad = usd * rate
    return f"{usd:.2f}USD -> {round(cad, 2):.2f}CAD"

# Regex
# Money requires minimum 2 digits
cad = r"\d*[.]?\d+\s?CAD(?!\S)"
usd = r"\d*[.]?\d+\s?USD(?!\S)"

f = r"[-]?\d*[.]?\d+\s?F(?!\S)"
c = r"[-]?\d*[.]?\d+\s?C(?!\S)"

# Compiled Patterns
f_pattern = re.compile(f, re.IGNORECASE)
c_pattern = re.compile(c, re.IGNORECASE)

usd_pattern = re.compile(usd, re.IGNORECASE)
cad_pattern = re.compile(cad, re.IGNORECASE)

class Client(Client):
    # Predefined function: This will be run whenever the bot turns on
    async def on_ready(self):
        global cad_rate
        print(f'Logged on as {self.user}!')
        cad_rate = get_cad_exchange_rate()

        if cad_rate != None:
            print(f'Current USD to CAD Rate is {cad_rate}')
        
    # Predefined function: When message is sent to server, this is called
    async def on_message(self, message):    
        # This keeps bot from replying to itself
        if message.author == self.user:
            return
        
        f_temps = re.findall(f_pattern, message.content)
        c_temps = re.findall(c_pattern, message.content)
        
        usd_money = re.findall(usd_pattern, message.content)
        cad_money = re.findall(cad_pattern, message.content)
        
        if len(f_temps) == 0 and len(c_temps) == 0 and len(usd_money) == 0 and len(cad_money) == 0:
            return
        else:    
            amounts = []
            
            if f_temps != None:
                for i in f_temps:
                    amounts.append(f_to_c(i))
                
            if c_temps != None:
                for i in c_temps:
                    amounts.append(c_to_f(i))
            
            if usd_money != None:
                for i in usd_money:
                    amounts.append(usd_to_cad(i, cad_rate))
                
            if cad_money != None:
                for i in cad_money:
                    amounts.append(cad_to_usd(i, cad_rate))
            
            converted_amounts = ""
            for x in amounts:
                converted_amounts += f"{x}\n"
                
            await message.channel.send(converted_amounts)

# These give us permissions
intents = Intents.default()

intents.message_content = True

# This runs the bot
client = Client(intents = intents)
client.run(os.getenv("DISCORD_TOKEN"))