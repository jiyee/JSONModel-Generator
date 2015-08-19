import json
from modelResults import *

def importFileWithName(name):
    json_file = open(name)
    json_string = json_file.read()
    return json.loads(json_string)

def main():

    projectName = raw_input("What's yout project name? ")
    className = raw_input("What's the name of this class? ")
    model = ModelResults(projectName, className, importFileWithName("test.txt"))
    print model.getInterfaces()


main()
