from constants import *

def isSingleType(instanceObject):
    for singleType in SINGLE_TYPES:
        if isinstance(instanceObject, singleType):
            return True
    return False

def getModelNameForKey(key):
    return str(key).title() + "Model"

class ModelResults:
    def __init__(self):
        self.interfaces = "//\n//  {{Type your classe name here}}.h\n//  {{Type your project name here}}\n//\n//  Created by json-model-generator.\n//  Copyright (c) 2015 Taqtile. All rights reserved.\n//\n\n#import \"JSONModel.h\""
        self.protocols = ""
        self.implementations = ""

    def addInterfaceWithDictionary(self, dictionary, name):
        self.interfaces += "\n\n@interface " + name + " : JSONModel\n"
        self.protocols += "\n@protocol " + name + " <NSObject>\n"

        for key in dictionary:

            #TODO: Add logic to recursively call addInterfaceWithDictionary

            if (isinstance(dictionary[key], dict)):
                self.interfaces += "@property (nonatomic) id <" + getModelNameForKey(key) + "> " + str(key) + ";\n"


            if (isSingleType(dictionary[key])):
                self.interfaces += SINGLE_TYPES[type(dictionary[key])] + str(key) + ";\n"


        self.interfaces += "@end\n"
        self.protocols += "@end\n"

    def getInterfaces(self):
        return self.interfaces
