import json

sampleJson = """{"key1": "value1", "key2": "value2"}"""

d = json.loads(sampleJson)

print(d['key2'])