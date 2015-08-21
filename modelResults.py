from constants import *

def isSingleType(instanceObject):
    for singleType in PROPERTY_DECLARATIONS:
        if isinstance(instanceObject, singleType):
            return True
    return False

def getModelNameForKey(key):
    return (str(key).title() + "Model").replace("_", "")

class ModelResults:
    def __init__(self, projectName, className, dictionary):
        self.interfaceHeader = "//\n//  " + className + ".h\n//  " + projectName + "\n//\n//  Created by json-model-generator: https://github.com/adrianovalente/JSONModel-Generator\n//  Copyright (c) 2015 json-model-generator. All rights reserved.\n//\n\n#import \"JSONModel.h\""
        self.implementationHeader = "//\n//  " + className + ".m\n//  " + projectName + "\n//\n//  Created by json-model-generator: https://github.com/adrianovalente/JSONModel-Generator\n//  Copyright (c) 2015 json-model-generator. All rights reserved.\n//\n\n#import \"" + className + ".h\""
        self.interfaces = ""
        self.protocols = ""
        self.implementations = ""
        self.__addInterfaceWithDictionary__(dictionary, className)

    def __addInterfaceWithDictionary__(self, dictionary, name):
        interface = "\n\n@interface " + name + " : JSONModel\n"

        self.implementations += "\n@implementation " + name + "\n@end\n\n"
        doLater = []

        for key in dictionary:

            if (isSingleType(dictionary[key])):
                interface += PROPERTY_DECLARATIONS[type(dictionary[key])] + str(key) + ";\n"

            if (isinstance(dictionary[key], dict)):
                interface += "@property (nonatomic, strong) " + getModelNameForKey(key) + " *" + str(key) + ";\n"
                doLater.append({"dictionary": dictionary[key], "name": getModelNameForKey(key)})

            if (isinstance(dictionary[key], list)):
                if len(dictionary[key]) > 0:
                    if (isSingleType(dictionary[key][0])):
                        interface += "@property (nonatomic, strong) NSArray *" + str(key) + "; // of " + APPLE_VAR_TYPES[type(dictionary[key][0])] + "\n"
                    elif (isinstance(dictionary[key][0], dict)):
                        interface += "@property (nonatomic, strong) NSArray <" + getModelNameForKey(key) + "> *" + str(key) + ";\n"
                        doLater.append({"dictionary": dictionary[key][0], "name": getModelNameForKey(key)})
                        self.protocols += "\n@protocol " + getModelNameForKey(key) + " <NSObject>\n@end"
                else:
                    doLater.append({"dictionary": {}, "name": getModelNameForKey(key)})

        interface += "@end\n"

        for task in doLater:
            self.__addInterfaceWithDictionary__(task["dictionary"], task["name"])

        self.interfaces += interface

    def showResults(self):
        print "\nThanks for using JSONModel Generator!\n"
        print "Here are the interface file: \n\n"
        print self.interfaceHeader
        print self.protocols
        print self.interfaces

        print "\n\nHere are the implementation file: \n\n"
        print self.implementationHeader
        print self.implementations
