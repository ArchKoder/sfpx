from sfdxUtilitesConstants import DUPLICATE_ARGUMENTS
from ObjectMap import ObjectMap

class Argument:
    def __init__(this,name,shortName, **kwargs):
        this.name = name.lower()
        this.shortName = shortName.lower()
        this.inputStatement = kwargs.get('inputStatement',None)
        this.nonVerboseInput = kwargs.get(nonVerboseInput,None)

    def __eq__(this, __o: object) -> bool:
        if (this.shortName == __o.shortName) or (this.name == __o.name):
            return True

    def __repr__(this) -> str:
        return '--'+this.name+' -'+this.shortName

    def askInput(this):
        if (this.inputStatement == None):
            return input('Enter '+this.name+' :\n')
        return input(this.inputStatement)

    def verboseInput(this):
        if this.nonVerboseInput != None:
            return this.nonVerboseInput()
        return None


class Command:

    def __init__(this,name,optionalArguments,compulsoryArguments) -> None:
        this.optionalArguments = set(optionalArguments)
        this.compulsoryArguments = set(compulsoryArguments)
        this.valueMap = ObjectMap()
        this.initializeValueMap()
        this.name = name.lower()

    def initializeValueMap(this):
        for arg in this.optionalArguments:
            argValue = this.valueMap.get(arg,None)
            if(argValue != None):
                raise Exception(DUPLICATE_ARGUMENTS)
            else:
                this.valueMap.set(arg,None)


    def setArguments(this, arguments2ValueMap):
        for k,v in arguments2ValueMap:
            if v != None:
                this.valueMap.set(k,v)
            else:
                this.valueMap.pop(k)

    def getVerboseStatus(this):
        if(len(this.gerVerboseCommands) == 0):
            return False
        return True

    def gerVerboseCommands(this):
        verboseCommands = set()
        for argument in this.compulsoryArguments:
            if(this.valueMap.get(argument,None)==None):
                verboseCommands.add(argument)

        return verboseCommands


    def askVerboseInputs(this):
        for arguments in this.getVerboseCommands():
            this.valueMap.set(arguments,arguments.askInput())

    def getNonVerboseArguments(this):
        nonVerboseArguements = set()
        for arguments in this.

    def generateCommandString(this):
        this.askVerboseInputs()

