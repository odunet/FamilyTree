from unittest import TestCase
from unittest.mock import patch, Mock
from package.familyTree import Person, FamilyTree


class TestTree(TestCase):

    def setUp(self):
        self.familyTree = FamilyTree()

    def test_TreeInstance(self):
        self.assertEqual(isinstance(self.familyTree, FamilyTree), True)

        # Check initialized attribute
        self.assertEqual(self.familyTree.Node, {})

    def test_addPatriach(self):
        patriarch = Person('king', 'male')

        # check that family tree is empty without the patriarch
        self.assertEqual(len(self.familyTree.Node), 0)

        # check that family tree has one element after adding patriarch
        self.familyTree.addPatriarch(patriarch)
        self.assertEqual(len(self.familyTree.Node), 1)

    def test_addMatriach(self):
        matriarch = Person('queen', 'female')
        patriarch = Person('queen', 'male')

        # check that family tree is empty without the patriarch
        self.assertEqual(len(self.familyTree.Node), 0)

        # check that family tree has one element after adding patriarch
        self.familyTree.addMatriarch(matriarch)
        self.assertEqual(len(self.familyTree.Node), 1)

    def test_addChild(self):
        mother = Person('queen', 'female')
        father = Person('king', 'male')
        mother.setSpouse(father)
        child = Person('jane', 'male')

        # check that mother has no children before adding child
        self.assertEqual(len(mother.getChildren()), 0)

        # check that mother has 1 child after adding child
        self.familyTree.addChild(child, mother)
        self.assertEqual(len(mother.getChildren()), 1)

    def test_addSpouse(self):
        wife = Person('queen', 'female')
        husband = Person('king', 'male')

        # check that wife has not spouse prior to adding spouse
        self.assertEqual(wife.getSpouse(), None)

        # check that mother has 1 child after adding child
        self.familyTree.addSpouse(wife, husband)
        self.assertEqual(wife.getSpouse().getName(), husband.getName())

    def test_getRelationship(self):
        father = Person('joe', 'male')
        son = Person('joejnr', 'male')
        father.setChildren(son)

        # test if relationship does not exit
        relationship = 'iDontExist'
        self.assertEqual(self.familyTree.getRelationship(
            father, relationship), None)

        # test functionality of function, where relationship points to getSon
        relationship = 'Son'
        self.assertEqual(self.familyTree.getRelationship(
            father, relationship).strip(), 'joejnr')
