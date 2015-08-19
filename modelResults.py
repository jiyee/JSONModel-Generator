from constants import *

def isSingleType(instanceObject):
    for singleType in PROPERTY_DECLARATIONS:
        if isinstance(instanceObject, singleType):
            return True
    return False

def getModelNameForKey(key):
    return str(key).title() + "Model"

class ModelResults:
    def __init__(self, projectName, className, dictionary):
        self.interfaces = "//\n//  " + className + ".h\n//  " + projectName + "\n//\n//  Created by json-model-generator: https://github.com/adrianovalente/JSONModel-Generator\n//  Copyright (c) 2015 Adriano Valente. All rights reserved.\n//\n\n#import \"JSONModel.h\""
        self.protocols = ""
        self.implementations = ""
        self.__addInterfaceWithDictionary__(dictionary, className)

    def __addInterfaceWithDictionary__(self, dictionary, name):
        self.interfaces += "\n\n@interface " + name + " : JSONModel\n"
        self.protocols += "\n@protocol " + name + " <NSObject>\n"
        doLater = []

        for key in dictionary:

            if (isSingleType(dictionary[key])):
                self.interfaces += PROPERTY_DECLARATIONS[type(dictionary[key])] + str(key) + ";\n"

            if (isinstance(dictionary[key], dict)):
                self.interfaces += "@property (nonatomic) id <" + getModelNameForKey(key) + "> " + str(key) + ";\n"
                doLater.append({"dictionary": dictionary[key], "name": getModelNameForKey(key)})

            if (isinstance(dictionary[key], list)):
                if len(dictionary[key]) > 0:
                    if (isSingleType(dictionary[key][0])):
                        self.interfaces += "@property (nonatomic, strong) NSArray *" + str(key) + "; // of " + APPLE_VAR_TYPES[type(dictionary[key][0])] + "\n"
                    elif (isinstance(dictionary[key], dict)):
                        self.interfaces += "@property (nonatomic, strong) NSArray <" + getModelNameForKey(key) + "> *" + str(key) + ";\n"
                        doLater.append({"dictionary": dictionary[key][0], "name": getModelNameForKey(key)})
                else:
                    doLater.append({"dictionary": {}, "name": getModelNameForKey(key)})

        self.interfaces += "@end\n"
        self.protocols += "@end\n"

        for task in doLater:
            self.__addInterfaceWithDictionary__(task["dictionary"], task["name"])

    def getInterfaces(self):
        return self.interfaces
