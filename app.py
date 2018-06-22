import json

json_string = '''

{"menu": {
  "id": "file",
  "value": "File",
  "popup": {
    "menuitem": [
      {"value": "New", "onclick": "CreateNewDoc()"},
      {"value": "Open", "onclick": "OpenDoc()"},
      {"value": "Close", "onclick": "CloseDoc()"}
    ]
  }
}}

'''


data = json.loads(json_string)

# print(type(data['menu']['popup']['menuitem']))
num = 1
for item in data['menu']['popup']['menuitem']:
    print("num: {num} item: {item}".format(num=num, item=item['value']))
    num += 1