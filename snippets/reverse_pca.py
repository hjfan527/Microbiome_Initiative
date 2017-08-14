import json
import cgi

data = cgi.FieldStorage()

print(data)

print('Content-type: application/json\n\n')
print(json.dumps(data))