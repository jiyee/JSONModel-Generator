from constants import *

def isSingleType(instanceObject):
    for singleType in SINGLE_TYPES:
        if isinstance(instanceObject, singleType):
            return True
    return False

class ModelResults:
    def __init__(self):
        self.interfaces = "//\n//  {{Type your classe name here}}.h\n//  {{Type your project name here}}\n//\n//  Created by json-model-generator.\n//  Copyright (c) 2015 Taqtile. All rights reserved.\n//\n\n#import \"JSONModel.h\""
        self.protocols = ""
        self.implementations = ""

    def addInterfaceWithDictionary(self, dictionary, name):
        self.interfaces += "\n@interface " + name + " : JSONModel"
        self.protocols += "@protocol " + name + " <NSObject>"

        for key in dictionary:

            #TODO: Add logic to recursively call addInterfaceWithDictionary
            if (isSingleType(dictionary[key])):
                self.interfaces += SINGLE_TYPES[type(dictionary[key])] + str(key) + ";\n"


        self.interfaces += "@end"
        self.protocols += "@end"

    def getInterfaces(self):
        return self.interfaces
