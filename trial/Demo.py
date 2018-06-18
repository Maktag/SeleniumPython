import unittest
from trial.Status import status


class Test_suit(unittest.TestCase):
    st = status()

    def test_1(self):
        self.st.pass_test('001','Pass with a and b user.')

    def test_2(self):
        self.st.pass_test('002','Pass with a and b user.')

    def test_3(self):
        self.st.pass_test('002','Pass with a and b user.')

    def test_4(self):
        self.st.create_module_dict('Login With Twitter')
        print("This is Three: ", self.st.test_unit)


if __name__ == '__main__':
    unittest.main()