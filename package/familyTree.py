from .person import Person
from package.person import Person

# Family Tree


class FamilyTree:
    """
    A class used to represent a Family structure and manipulate data in the tree

    ...

    Attributes
    ----------
    None

    Methods
    -------
    addPatriarch(object = Person)
            Parameters
            ----------
            Patriarch : Object
                A Person Object


            Returns
            -------
            None
                Method, stores a Person object as the Patriarch in the tree

    addMatriarch(object = Person)
            Parameters
            ----------
            Matriarch : Person
                A Person Object


            Returns
            -------
            None
                Method, stores a Person object as the Matriarch in the tree

    addChild(object = Person, Object = Person)
            Parameters
            ----------
            Child : Person
                A Person Object

            Mother: Person
                A Person Object


            Returns
            -------
            None
                Method, stores a child in the family tree under a mother

    addSpouse(object = Person, Object = Person)
            Parameters
            ----------
            wife : Person
                A Person Object

            husband: Person
                A Person Object


            Returns
            -------
            None
                Method, adds a spouse to a current member of the family

    getRelationship(object = Person, String = Relationship)
            Parameters
            ----------
            Person : Person
                A Person Object

            Relationship: String
                A String, representing a possible relationship in the family tree


            Returns
            -------
            None
                Method, the person that has the "Relationship" with the provided "Person" 
    """

    def __init__(self):
        self.Node = {}

    def addPatriarch(self, person):
        if not isinstance(person, Person):
            raise ValueError('Invalid value for either mother or child')
        if len(list(self.Node.keys())) == 2:
            print('ADD_PATRIARCH_FAILED: PATRIARTCH ALREADY EXISTS')
            return
        if len(list(self.Node.keys())) == 1:
            for spouse in list(self.Node.keys()):
                if self.Node[spouse].getGender() == 'male':
                    print('ADD_PATRIARCH_FAILED: PATRIARTCH ALREADY EXISTS')
                    return
                else:
                    self.Node.update({str(person.getName()): person})
                    # Set spouse in each member
                    self.Node[spouse].setSpouse(self.Node[str(
                        person.getName())])
                    self.Node[str(person.getName())
                              ].setSpouse(self.Node[spouse])

        else:
            self.Node.update({str(person.getName()): person})

    def addMatriarch(self, person):
        if not isinstance(person, Person):
            raise ValueError('Invalid value for either mother or child')
        if len(list(self.Node.keys())) == 2:
            print('ADD_MATRIARCH_FAILED: MATRIARTCH ALREADY EXISTS')
            return
        if len(list(self.Node.keys())) == 1:
            for spouse in list(self.Node.keys()):
                if self.Node[spouse].getGender() == 'female':
                    print('ADD_MATRIARCH_FAILED: MATRIARTCH ALREADY EXISTS')
                    return
                else:
                    self.Node.update({str(person.getName()): person})
                    # Set spouse in each member
                    self.Node[spouse].setSpouse(self.Node[str(
                        person.getName())])
                    self.Node[str(person.getName())
                              ].setSpouse(self.Node[spouse])
        else:
            self.Node.update({str(person.getName()): person})

    def addChild(self, child, mother):
        if not isinstance(mother, Person) or not isinstance(child, Person):
            raise ValueError('Invalid value for either mother or child')
        if mother.getSpouse() == None:
            self.Node.update({str(child.getName()): child})
            print("CHILD_ADDITION_FAILED: MOTHER NEEDS TO BE MARRIED TO HAVE A CHILD.")
            return
        if mother.getGender() != 'female':
            print("CHILD_ADDITION_FAILED: MOTHER NEEDS TO BE A WOMAN.")
            return
        # set child's immediate family records
        child.setMother(mother)
        child.setFather(mother.getSpouse())
        child.getFather().setChildren(child)
        child.getMother().setChildren(child)
        print(f'CHILD_ADDED: {child.getName()}')

    def addSpouse(self, wife, husband):
        if not isinstance(wife, Person) or not isinstance(husband, Person):
            raise ValueError('Invalid value for either wife or husband')
        if wife.getSpouse() or husband.getSpouse():
            print(
                'SPOUSE_ADDITION_FAILED: EITHER THE MAN OR THE WOMAN WAS PREVIOSULY MARRIED.')
            return
        if wife.getGender() == husband.getGender():
            print(
                f'SPOUSE_ADDITION_FAILED: BOTH PERSONS {wife.getName()} and {husband.getName()} HAVE THE SAME GENDER')
            return
        # set spouses records
        wife.setSpouse(husband)
        husband.setSpouse(wife)
        print(f'SPOUSE_ADDED: {wife.getName()} added to {husband.getName()} ')

    def getRelationship(self, person, relationship):

        # Relationship switch
        switchRelationship = {
            'Paternal-Aunt': person.getPaternalAunt(),
            'Paternal-Uncle': person.getPaternalUncle(),
            'Maternal-Aunt': person.getMaternalAunt(),
            'Maternal-Uncle': person.getMaternalUncle(),
            'Brother-In-Law': person.getBrotherInlaw(),
            'Sister-In-Law': person.getSisterInlaw(),
            'Son': person.getSon(),
            'Daughter': person.getDaughter(),
            'Siblings': person.getSiblings()
        }
        return switchRelationship.get(relationship, None)

    def printFamilyTree(self):
        print(self.Node)
