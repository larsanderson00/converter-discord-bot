# Converter Discord Bot
This bot is to be used inside a discord server. It can convert from Canadian Dollars to US Dollars and vice versa as well as from Celcius to Fahrenheit and the reverse.

## Why I made this
All the discord converter bots I could find online were where you had to call them explicitly. 
I wanted one that would analyze each message and when it saw a specific pattern showing that you were talking about currency or 
weather then it would automatically convert it to the other one and send info in a new message.
This adds convenience and ease to it since you don't have to remember fancy calls for it.

## Examples
<img width="679" height="219" alt="Example of discord bot converting from C to F" src="https://github.com/user-attachments/assets/35283845-d9dc-4f28-8a92-af1ce5c5adf8" />
<img width="678" height="205" alt="Example of discord bot converting from CAD to USD" src="https://github.com/user-attachments/assets/836a4832-2fa7-4cd5-b654-4f1131ad6770" />

It isn't case sensitive as displayed here making it so you can write it as 20CAD or 20cAd or 20 CAd etc and all of those will be automatically converted into USD and sent back.

The bot analyzes the message to see if it finds a match to it's given regex patterns. As long as you have a number followed by either a C or F or USD or CAD then it will automatically convert it.

## Dependencies
* Currency Exchange Rate (Updated daily and whenever the script first starts up) -> https://open.er-api.com
* Python -> 3.12
* discord.py -> 2.4.0
* python-dotenv
* requests -> 2.32.3
