from .gender import Gender


class Person():
    """
    Class used to represent a single member of the Family structure.
    It also provides methosd to manage the relationships with other members of the larger family tree

    ...

    Attributes
    ----------
    gender : String
        a string representing the gender of the Person
    name : String
        a string representing the name of the Person

    Methods
    ----------

    This class provides numerous methods for setting and getting relationship between this Person 
    and others persons related to him/her in the larger family tree.
    """

    def __init__(self, name, gender):
        self.__name = name
        self.__gender = Gender(gender)
        self.__mother = None
        self.__father = None
        self.__spouse = None
        self.__children = []

    def __str__(self):
        return f"Name: {self.__name}"

    def __repr__(self):
        return f"Name: {self.__name}, Gender: {self.__gender}, Spouse: { self.getSpouse() }, Children: {self.__children}"

    # Getter Methods (Constructor Attributes)

    def getName(self):
        return self.__name

    def getGender(self):
        return self.__gender

    def getMother(self):
        return self.__mother

    def getFather(self):
        return self.__father

    def getSpouse(self):
        return self.__spouse

    def getChildren(self):
        return self.__children

    # Setter Methods (Constructor Attributes)
    def setName(self, data):
        if not isinstance(data, str):
            raise ValueError(
                'Data provided in setName Not an instance of String')
        self.__name = data

    def setGender(self, data):
        if not isinstance(data, str):
            raise ValueError(
                'Data provided in setGender Not an instance of String')
        if data == 'female' or data == 'Female' or data == 'f' or data == 'F':
            return 'female'
        elif data == 'male' or data == 'Male' or data == 'm' or data == 'M':
            return 'male'
        else:
            raise ValueError(
                'Error: Please enter a valid gender, i.e. Male or Female')
        self.__gender = data

    def setMother(self, data):
        if not isinstance(data, Person):
            raise ValueError(
                'Data provided in setMother Not an instance of Person')
        if data.getGender() != 'female':
            print(f'SET_MOTHER_FAILED: {data.getName()} not a female')
            return
        self.__mother = data

    def setFather(self, data):
        if not isinstance(data, Person):
            raise ValueError(
                'Data provided in setFather Not an instance of Person')
        if data.getGender() != 'male':
            print(f'SET_MOTHER_FAILED: {data.getName()} not a male')
            return
        self.__father = data

    def setSpouse(self, data):
        if not isinstance(data, Person):
            raise ValueError(
                'Data provided in setSpouse Not an instance of Person')
        if self.getGender() == data.getGender():
            print(
                f'SET_SPOUSE_FAILED: Both person have {data.getGender()} gender')
        self.__spouse = data

    def setChildren(self, data):
        if not isinstance(data, Person):
            raise ValueError(
                'Data provided in setChildren Not an instance of Person')
        self.__children.append(data)
        return self

    # Get extended family
    def getPaternalGrandmother(self):
        if not self.getMother():
            return None
        if not self.getFather().getMother():
            return None
        return self.getFather().getMother()

    def getMaternalGrandmother(self):
        if not self.getMother():
            return None
        if not self.getMother().getMother():
            return None
        return self.getMother().getMother()

    def getPaternalUncle(self):
        perternalGrandMother = self.getPaternalGrandmother()
        if perternalGrandMother == None:
            return None
        allSiblings = perternalGrandMother.getChildren()
        results = []
        for item in allSiblings:
            if item.__name != self.getFather().__name and item.getGender() == 'male':
                results.append(item.__name)
        if results:
            resultStr = ''
            for result in results:
                resultStr += result + ' '
            return resultStr
        else:
            return 'PERSON_NOT_FOUND'

    def getMaternalUncle(self):
        maternalGrandmother = self.getMaternalGrandmother()
        if maternalGrandmother == None:
            return None
        allSiblings = maternalGrandmother.getChildren()
        results = []
        for item in allSiblings:
            if item.__name != self.getMother().__name and item.getGender() == 'male':

                results.append(item.__name)
        if results:
            resultStr = ''
            for result in results:
                resultStr += result + ' '
            return resultStr
        else:
            return 'PERSON_NOT_FOUND'

    def getPaternalAunt(self):
        paternalGrandmother = self.getPaternalGrandmother()
        if paternalGrandmother == None:
            return None
        allSiblings = paternalGrandmother.getChildren()
        results = []
        for item in allSiblings:
            if item.__name != self.getFather().__name and item.getGender() == 'female':
                results.append(item.__name)
        if results:
            resultStr = ''
            for result in results:
                resultStr += result + ' '
            return resultStr
        else:
            return 'PERSON_NOT_FOUND'

    def getMaternalAunt(self):
        maternalGrandMother = self.getMaternalGrandmother()
        if maternalGrandMother == None:
            return None
        allSiblings = maternalGrandMother.getChildren()
        results = []
        for item in allSiblings:
            if item.__name != self.getMother().__name and item.getGender() == 'female':
                results.append(item.__name)
        if results:
            resultStr = ''
            for result in results:
                resultStr += result + ' '
            return resultStr
        else:
            return 'PERSON_NOT_FOUND'

    def getSisterInlaw(self):
        if not self.getSpouse():
            return None
        if not self.getSpouse().getMother():
            return None
        allSiblings = self.getSpouse().getMother().getChildren()
        results = []
        for item in allSiblings:
            if item.__name != self.getSpouse().__name and item.getGender() == 'female':
                results.append(item.__name)
        if results:
            resultStr = ''
            for result in results:
                resultStr += result + ' '
            return resultStr
        else:
            return 'PERSON_NOT_FOUND'

    def getBrotherInlaw(self):
        if not self.getSpouse():
            return None
        if not self.getSpouse().getMother():
            return None
        allSiblings = self.getSpouse().getMother().getChildren()
        results = []
        for item in allSiblings:
            if item.__name != self.getSpouse().__name and item.getGender() == 'male':
                results.append(item.__name)
        if results:
            resultStr = ''
            for result in results:
                resultStr += result + ' '
            return resultStr
        else:
            return 'PERSON_NOT_FOUND'

    def getSiblings(self):
        if not self.getMother():
            return None
        results = []
        for person in self.getMother().getChildren():
            if person.__name != self.__name:
                results.append(person.__name)
        if results:
            resultStr = ''
            for result in results:
                resultStr += result + ' '
            return resultStr
        else:
            return 'PERSON_NOT_FOUND'

    def getDaughter(self):
        if not self.getChildren():
            return None
        results = []
        for person in self.getChildren():
            if person.getGender() == 'female':
                results.append(person.__name)
        if results:
            resultStr = ''
            for result in results:
                resultStr += result + ' '
            return resultStr
        else:
            return 'PERSON_NOT_FOUND'

    def getSon(self):
        if not self.getChildren():
            return None
        results = []
        for person in self.getChildren():
            if person.getGender() == 'male':
                results.append(person.__name)
        if results:
            resultStr = ''
            for result in results:
                resultStr += result + ' '
            return resultStr
        else:
            return 'PERSON_NOT_FOUND'
