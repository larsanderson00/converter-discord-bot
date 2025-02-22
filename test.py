import re

cad = r"\d+[.]?\d+\s?CAD"
usd = r"\d+[.]?\d+\s?USD"

f = r"\d+\s?F"
c = r"\d+\s?C"

message = "I don't have that much money. Only 2000.00 CAD but if you give me 30 then I'll have 50cad which is an ok amount not quite 60Cad but still."
temp = "It's hot like 30f or maybe 10c. Oh wait, that isn't hot. It's more like 50 C or 200 F"

pattern = re.compile(c, re.IGNORECASE)
x = re.findall(pattern, temp)

print(x)