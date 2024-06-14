import unittest

from src.model.helpers.internalStructureReader import internalStructureReader


class MyTestCase(unittest.TestCase):
    def test_something(self):
        isReader = internalStructureReader()
        internalStruct = isReader.get_internal_structure('60', 'Standard', True)
        self.assertEqual(internalStruct['Head'], '3')
        self.assertEqual(internalStruct['CTorso'], '20')
        self.assertEqual(internalStruct['Torsos'], '14')
        self.assertEqual(internalStruct['Arms'], '10')
        self.assertEqual(internalStruct['Legs'], '14')
        self.assertEqual(internalStruct['Mass'], '6.0')



if __name__ == '__main__':
    unittest.main()
