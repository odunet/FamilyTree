from unittest import TestCase
from unittest.mock import patch, Mock
from package.person import Person
from package.gender import Gender

# Create test Family


class TestFamily():
    def marriedFather(self):
        father = Person('mathew', 'male')
        mother = Person('mary', 'female')
        child1 = Person('regina', 'female')
        child2 = Person('ronald', 'male')
        father.setSpouse(mother)
        mother.setChildren(child1)
        mother.setChildren(child2)
        father.setChildren(child1)
        father.setChildren(child2)
        return father

    def marriedMother(self):
        father = Person('mathew', 'male')
        mother = Person('mary', 'female')
        child1 = Person('regina', 'female')
        child2 = Person('ronald', 'male')
        father.setSpouse(mother)
        mother.setChildren(child1)
        mother.setChildren(child2)
        father.setChildren(child1)
        father.setChildren(child2)
        return mother


class TestMember(TestCase):

    # class variables
    testFather = TestFamily().marriedFather()
    testMother = TestFamily().marriedMother()

    def setUp(self):
        self.person = Person('shippit', 'female')

    def test_PersonInstance(self):
        self.assertEqual(isinstance(self.person, Person), True)

        # Check getter methods
        self.assertEqual(self.person.getName(), "shippit")
        self.assertEqual(self.person.getGender(), Gender('female'))
        self.assertEqual(self.person.getMother(), None)
        self.assertEqual(self.person.getFather(), None)
        self.assertEqual(self.person.getSpouse(), None)
        self.assertEqual(self.person.getChildren(), [])

    def test_SetMother(self):
        dummyMother_1 = Person('john', 'male')
        dummyMother_2 = 'jane'
        dummyMother_3 = Person('jane', 'female')

        # check if gender is checked
        self.person.setMother(dummyMother_1)
        self.assertEqual(self.person.getMother(), None)

        # check if error is raised
        self.assertRaises(ValueError, self.person.setMother, dummyMother_2)

        # check success case
        self.person.setMother(dummyMother_3)
        self.assertEqual(self.person.getMother().getName(), 'jane')

    def test_SetFather(self):
        dummyFather_1 = Person('jane', 'female')
        dummyFather_2 = 'john'
        dummyFather_3 = Person('john', 'male')

        # check if gender is checked
        self.person.setFather(dummyFather_1)
        self.assertEqual(self.person.getMother(), None)

        # check if error is raised
        self.assertRaises(ValueError, self.person.setFather, dummyFather_2)

        # check success case
        self.person.setFather(dummyFather_3)
        self.assertEqual(self.person.getFather().getName(), 'john')

    def test_SetSpouse(self):
        dummySpouse_1 = Person('jane', 'female')
        dummySpouse_2 = 'john'
        dummySpouse_3 = Person('john', 'male')

        # check if gender is checked
        self.person.setSpouse(dummySpouse_1)
        self.assertEqual(self.person.getMother(), None)

        # check if error is raised
        self.assertRaises(ValueError, self.person.setFather, dummySpouse_2)

        # check success case
        self.person.setSpouse(dummySpouse_3)
        self.assertEqual(self.person.getSpouse().getName(), 'john')

    def test_SetChildren(self):
        dummyChild_1 = 'john'
        dummyChild_2 = Person('john', 'male')

        # check if error is raised
        self.assertRaises(ValueError, self.person.setChildren, dummyChild_1)

        # check success case
        self.person.setChildren(dummyChild_2)
        self.assertIn('john', [child.getName()
                               for child in self.person.getChildren()])

    def test_getPaternalGrandmother(self):
        # Should assert true since child has not father
        self.assertEqual(self.person.getPaternalGrandmother(), None)

    def test_getMaternalGrandmother(self):
        # Should assert true since child has not Mother
        self.assertEqual(self.person.getMaternalGrandmother(), None)

    @patch('package.person.Person.getPaternalGrandmother', side_effect=([None,
                                                                         Person('mama', 'female').setChildren(
                                                                             Person('jane', 'female')),
                                                                         Person('mama', 'female').setChildren(Person('john', 'male'))]))
    def test_getPaternalUncle(self, mock_getPaternalGrandmother):
        father = Person('mattew', 'male')
        father.setChildren(self.person)
        self.person.setFather(father)

        # check that not granmother results in None
        self.assertEqual(self.person.getPaternalUncle(), None)

        # check that a grandmother with only female children left results in PERSON_NOT_FOUND
        self.assertEqual(
            self.person.getPaternalUncle().strip(), 'PERSON_NOT_FOUND')

        # check that a grandmother with male children results in John
        self.assertEqual(self.person.getPaternalUncle().strip(), 'john')

    @patch('package.person.Person.getPaternalGrandmother', side_effect=([None,
                                                                         Person('mama', 'female').setChildren(
                                                                             Person('john', 'male')),
                                                                         Person('mama', 'female').setChildren(Person('jane', 'female'))]))
    def test_getPaternalAunt(self, mock_getPaternalGrandmother):
        father = Person('mattew', 'male')
        father.setChildren(self.person)
        self.person.setFather(father)

        # check that not granmother results in None
        self.assertEqual(self.person.getPaternalAunt(), None)

        # check that a grandmother with only male children left in PERSON_NOT_FOUND
        self.assertEqual(self.person.getPaternalAunt().strip(),
                         'PERSON_NOT_FOUND')

        # check that a grandmother with female children results in Equal
        self.assertEqual(self.person.getPaternalAunt().strip(), 'jane')

    @patch('package.person.Person.getMaternalGrandmother', side_effect=([None,
                                                                         Person('mama', 'female').setChildren(
                                                                             Person('john', 'male')),
                                                                         Person('mama', 'female').setChildren(Person('jane', 'female'))]))
    def test_getMaternalAunt(self, mock_getPaternalGrandmother):
        mother = Person('mattew', 'female')
        mother.setChildren(self.person)
        self.person.setMother(mother)

        # check that not granmother results in None
        self.assertEqual(self.person.getMaternalAunt(), None)

        # check that a grandmother with only male children left results in PERSON_NOT_FOUND
        self.assertEqual(self.person.getMaternalAunt().strip(),
                         'PERSON_NOT_FOUND')

        # # check that a grandmother with female children results in Jane
        self.assertEqual(self.person.getMaternalAunt().strip(), 'jane')

    @patch('package.person.Person.getMaternalGrandmother', side_effect=([None,
                                                                         Person('mama', 'female').setChildren(
                                                                             Person('jane', 'female')),
                                                                         Person('mama', 'female').setChildren(Person('john', 'male'))]))
    def test_getMaternalUncle(self, mock_getPaternalGrandmother):
        mother = Person('mattew', 'female')
        mother.setChildren(self.person)
        self.person.setMother(mother)

        # check that not granmother results in None
        self.assertEqual(self.person.getMaternalUncle(), None)

        # check that a grandmother with only female children left results in PERSON_NOT_FOUND
        self.assertEqual(self.person.getMaternalUncle().strip(),
                         'PERSON_NOT_FOUND')

        # # check that a grandmother with male children results in 'John'
        self.assertEqual(self.person.getMaternalUncle().strip(), 'john')

    def test_getSisterInLaw(self):
        husband = Person('angle', 'male')
        husband.setMother(self.testMother)
        husband.setSpouse(self.person)

        # check that result is not when person has no spouse
        self.assertEqual(self.person.getSisterInlaw(), None)

        # check that a sister inlaw is regine --> see TestFamily Class
        self.person.setSpouse(husband)
        self.assertEqual(self.person.getSisterInlaw().strip(), 'regina')

    def test_getBrotherInLaw(self):
        wife = Person('angle', 'male')
        wife.setMother(self.testMother)
        wife.setSpouse(self.person)

        # check that result is not when person has no spouse
        self.assertEqual(self.person.getBrotherInlaw(), None)

        # check that a brother inlaw is ronald --> see TestFamily Class
        self.person.setSpouse(wife)
        self.assertEqual(self.person.getBrotherInlaw().strip(), 'ronald')

    def test_getSiblings(self):
        # check that result is not when person has no mother
        self.assertEqual(self.person.getSiblings(), None)

        # check that number of children of test family is greater than or equal to 1
        self.person.setMother(self.testMother)
        self.assertGreaterEqual(
            len(self.person.getSiblings().split(' ')), 1)

    def test_getSon(self):
        # check that result is not when person has no child
        self.assertEqual(self.person.getSon(), None)

        # check that the test mother has ronald as son
        self.assertGreaterEqual(
            self.testMother.getSon().strip(), 'ronald')

    def test_getDaughter(self):
        # check that result is not when person has no child
        self.assertEqual(self.person.getDaughter(), None)

        # check that the test mother has ronald as daughter
        self.assertGreaterEqual(
            self.testMother.getDaughter().strip(), 'regina')
