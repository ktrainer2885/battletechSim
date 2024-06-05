import unittest
import src.model.battleMech as battleMech


class MyTestCase(unittest.TestCase):
    def test_something(self):
        mech = battleMech.BattleMech('../../resources/megamek/standardMech.mtf')
        self.assertEqual(mech.chassis, 'Archer')  # add assertion here


if __name__ == '__main__':
    unittest.main()
