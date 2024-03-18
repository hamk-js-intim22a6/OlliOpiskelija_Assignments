d = {"mouse": "hiiri", "keyboard": "näppäimistö", "monitor": "näyttö"}
print(d["mouse"]) # print value of key "mouse"
if "mouse" in d: # check if key "mouse" exists
    print("Found mouse")
d["keyboard"] = "näppis" # change value
print(d["keyboard"]) 
d["printer"] = "tulostin" # add new key-value pair
del d["monitor"] # remove key-value pair
for key in d: # loop through keys
    print(f"{key} = {d[key]}")

for key, value in d.items(): # loop through key-value pairs
    print(f"{key} = {value}")
    
