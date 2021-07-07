from unittest import TestCase
from shippit import Main
from package.familyTree import Person, FamilyTree

# modules to store I/O in string
from io import StringIO
import sys
s = StringIO()
stdout = sys.stdout
sys.stdout = s


class TestShippit(TestCase):

    def setUp(self):
        self.shippit_main = Main(
            'tests/integration/instruction.txt', Person, FamilyTree)

    # Test instance creating
    def test_ShippitInstance(self):
        self.assertEqual(isinstance(self.shippit_main, Main), True)

    # Test full application integration
    def testIntegration(self):
        self.shippit_main.initiate()
        sys.stdout = stdout
        result = s.getvalue()
        resultList = result.split('\n')
        self.assertIn('dominique ', resultList)
        self.assertIn('albus ', resultList)
        self.assertIn('hugo ', resultList)
        self.assertIn('lily ', resultList)
