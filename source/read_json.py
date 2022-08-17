import json
person = '{"name":"Bob","languages":["English","French","Japanese"]}'
person_dict=json.loads(person)
print(person_dict)
print(person_dict['languages'])

