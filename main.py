import json
contents = []

try:
    with open("./medicine.json", 'r') as f:
        contents = json.load(f)
except Exception as e:
    print(e)

my_list = [item['brandName'] for item in contents["value"]]

with open('./temp.txt', 'w') as f:
    for item in my_list:
        f.write(item)
        f.write("\n")
