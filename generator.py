import json
from modelResults import *

def importFileWithName(name):
    json_file = open(name)
    json_string = json_file.read()
    return json.loads(json_string)

# TODO: Remove this code as soon as my class work :D
# def doSomeStuffWithDictionary(dictionary):
#     for key in dictionary:
#         if isinstance(dictionary[key], dict):
#             doSomeStuffWithDictionary(dictionary[key])
#         else:
#             if (isSingleType(dictionary[key])):
#                 addSingleProperty(dictionary, key)

def main():
    model = ModelResults()
    model.addInterfaceWithDictionary(importFileWithName("test.txt"), "Teste")
    print model.getInterfaces()


main()
