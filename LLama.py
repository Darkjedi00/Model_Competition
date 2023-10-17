import pprint
import json

with open('data_with_context.json', 'r', encoding='utf8') as iFile:
    data = json.load(iFile)
    for key, value in data.items():
        pprint.pprint(value)
        break


    # Read in the JSON file
with open('data_with_context.json', 'r', encoding='utf8') as iFile:
    data = json.load(iFile)

# Initialize an empty list to store the labels
labels = []

# Iterate over each key-value pair in the JSON data
for key, value in data.items():
    # Extract the "Label" value from the current item and append it to the labels list
    comment_label = value["Label"]
    labels.append(comment_label)