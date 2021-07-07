# Entrypoint into application
from package.familyTree import FamilyTree, Person
import sys
from datetime import datetime


class Main:

    """
    This class serves as the interface between the user input and the Family tree class

    ...

    Attributes
    ----------
    instructionFile : String
        a string containing the path to the instruction file. This value is supplied by the user in the CLI
    initializationFile : String
        a string containing the path to the initialization file. This value is provided by the application. The 
        initialization file is at: './lib/initialization_DONT_MODIFY.txt'
    Person : Object
        an object that represents an individual member of the family tree
    FamilyTree : Object
        an object representing the entire family tree

     Methods
    ----------
    addPatriarch(String: patriarch)
        Parameter: Name of the partriarch (String)
        Returns: None
        Detail: Method interfaces with the Family tree to add a Patriarch to the family tree

    addMatriarch(String: matriach)
        Parameter: Name of the martriarch (String)
        Returns: None
        Detail: Method interfaces with the Family tree to add a Matriarch to the family tree

    addChild(String: child, String: mother)
        Parameter: Name of the child (String), Name of the child (String) 
        Returns: None
        Detail: Method interfaces with the Family tree to add a child to the family tree

    addSpouse(String: wife, String: husband)
        Parameter: Name of the wife (String), Name of the husband (String)
        Returns: None
        Detail: Method interfaces with the Family tree to add a spouse to a current member of the family

    getRelationship(String: Person, String: Relationship)
        Parameter: Name of a member of the tree (String), Type of relationship (String)
        Returns: None
        Detail: Method interfaces with the Family tree to retrieve the person having the specified 
        relationship specified person.

    readFiletoList(String: filename)
        parameter: The is the string representing the path the file containing the command
        Returns: None
        Detail: Method retrieves commands from the supplied text file and parses to the responsible 
        method within the class to handle

    initiate()
        parameter: None
        Returns: None
        Detail: This method firsts run all the command in the initialization file and moves on to run
        the commands in the instructionFile.
    """

    def __init__(self, instructionFile, Person, FamilyTree, initiationFile='./lib/initialization_DONT_MODIFY.txt'):
        self.initialtionFile = initiationFile
        self.instructionFile = instructionFile
        self.Person = Person
        self.FamilyTree = FamilyTree()
        self.members = {}

    def addPatriarch(self, *args):
        self.members[args[0]] = self.Person(args[0], args[1])
        self.FamilyTree.addPatriarch(self.members[args[0]])

    def addMatriarch(self, *args):
        self.members[args[0]] = self.Person(args[0], args[1])
        self.FamilyTree.addMatriarch(self.members[args[0]])

    def addChild(self, *args):
        if args[0] not in list(self.members.keys()):
            print(f'PERSON_NOT_FOUND: {args[0]}')
            return
        self.members[args[1]] = self.Person(args[1], args[2])
        self.FamilyTree.addChild(self.members[args[1]], self.members[args[0]])

    def addSpouse(self, *args):
        if args[0] not in list(self.members.keys()):
            print(f'PERSON_NOT_FOUND: {args[0]}')
            return
        self.members[args[1]] = self.Person(args[1], args[2])
        self.FamilyTree.addSpouse(self.members[args[1]], self.members[args[0]])

    def getRelationship(self, *args):
        commandList = [
            'Paternal-Aunt',
            'Paternal-Uncle',
            'Maternal-Aunt',
            'Maternal-Uncle',
            'Brother-In-Law',
            'Sister-In-Law',
            'Son',
            'Daughter',
            'Siblings'
        ]

        if args[1] in commandList:
            if args[0] not in list(self.members.keys()):
                print(f'PERSON_NOT_FOUND: {args[0]}')
                return
            result = self.FamilyTree.getRelationship(
                self.members[args[0]], args[1])
            print(result)
        else:
            print(
                f'COMMAND NOT VALID: USE ONLY Supported RELATIONSHIP: {args[1]} not a supported relationship')

    def readFiletoList(self, file):
        commandSwitch = {
            'ADD_PATRIARCH': self.addPatriarch,
            'ADD_MATRIARCH': self.addMatriarch,
            'ADD_CHILD': self.addChild,
            'ADD_SPOUSE': self.addSpouse,
            'GET_RELATIONSHIP': self.getRelationship
        }
        with open(file, 'r') as f:
            instructions = f.readlines()

        results = []
        for count, instruction in enumerate(instructions):
            item = instruction.strip().split(" ")
            if item[0] != 'ADD_PATRIARCH' or item[0] != 'ADD_MATRIARCH':
                if len(item) < 3:
                    print(
                        f'OPERATION ON LINE {count+1} FAILED: CHECK FOR EMPTY LINE OR INCOMPLETE ARGUMENTS IN INPUT FILE')
                    continue
            method = commandSwitch.get(item[0], None)
            if not method:
                continue
            method(*tuple(item[1:]))

    def initiate(self):
        print(f'BEGINNING OF INITIALIZATION -----------  {datetime.now()}')
        self.readFiletoList(self.initialtionFile)
        print('END OF INITIALIZATION -----------')
        print('\n')
        print('***********************************************************')
        print(f'BEGINNING OF INSTRUCTION -----------  {datetime.now()}')
        self.readFiletoList(self.instructionFile)
        print('END OF INSTRUCTION -----------')


if __name__ == '__main__':
    args = sys.argv
    if "--help" in args or len(args) == 1:
        print("Shippit Family Tree: Kindly review ReadMe file for instructions")
    else:
        """
        Initialize family data structure with previously sopplied values
        """
        Main(args[1], Person, FamilyTree).initiate()
