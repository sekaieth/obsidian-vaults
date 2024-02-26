# [[Data Formats#XML | XML]]
Import XML file
```python
import xml.etree.ElementTree as ET
tree = ET.parse('lab.xml')
root = tree.getroot()

print(root)
```

The tree will be nested arrays of information, and you get information by either diving through arrays to statically assign variables, or extensive looping.

# [[Data Formats#JSON | JSON]]
import JSON file
```json
import json
json_file = open('lab.json')
data = json.load('json_file')
jone_file.close()

print(data['device']['hostname'])
```
The data will be in key:value pairs, which makes parsing a bit easier as the keys are strings, so you can give, for example, the device and hostname to retrieve the device's hostname.  You could also do 'device' and 'interfaces' to retrieve an array of interface objects, for example.

# [[Data Formats#YAML | YAML]]
Import YAML file
```
import yaml
yaml_file = open('lab.yaml')
data = yaml.safe_load(yaml_file)
yaml_file.close()

print(data)
```
The data will be in key:value pairs (actually a Python dictionary), just like in JSON