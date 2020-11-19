#!/bin/env python3

import json
import argparse

import functions

version = "0.1"

# Read Input from command line
parser = argparse.ArgumentParser(prog="Arcweave2UE4.py", description='Process a json file creating a UE4 dialogue Tree.')

parser.add_argument("file", action="store")

args = parser.parse_args()

print("Arcweave2UE4 version " + version)
print("made by Tarrke. This software is delivered as is and the author will not take any responsabilities for whatever you do with it.")

# Read Data
print("Parsing " + args.file)
with open(args.file) as json_file:
    data = json.load(json_file)
    #print(json.dumps(data, indent=2))

# Manipulate Data
## Find the starting element ie title contains "Start Dialogue"
#print( data["elements"])
for p in data["elements"]:
    if "Dialogue Start" in data["elements"][p]["title"]:
        startingPoint = p
        break

print("Starting point hash: " + startingPoint)

toTreat = []
toTreat.append(startingPoint)

## Find links from hash
seen = set()
while len(toTreat) > 0:
    id = toTreat.pop(0)
    # print(id)
    if id in data["jumpers"]:
        print("add an end dialogue element")
        continue
    print("add a line element with content")
    print(data["elements"][id]["content"])
    ids = functions.findLinksFromNode(data, id)
    for id in ids:
        if id not in seen:
            toTreat.append(id)
    # print(len(toTreat))



#sourceid
#targetid


# Export Output
output = """Some string to output
and because I'm smart it's
a multiline string."""

# Make the output to the clipboard
functions.copyToClipboard(output)


