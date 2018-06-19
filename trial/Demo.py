import unittest
from trial.Status import status


class Test_suit(unittest.TestCase):
    st = status()

    def test_1(self):
        self.st.pass_test('001', 'Pass with pradeep','T')
        self.st.fail_test('002', 'Fail with anil')
        self.st.error_test('003', 'Error with ankur')
        self.st.skip_test('004', 'Skip with ankit')
        self.st.info_test('005', 'Info with sachin')
        self.st.create_module_dict('Login With Facebook')

    def test_2(self):
        self.st.pass_test('006', 'Pass with pradeep','T')
        self.st.fail_test('007', 'Fail with anil')
    #     self.st.error_test('003', 'Error with ankur')
    #     self.st.skip_test('004', 'Skip with ankit')
    #     self.st.info_test('005', 'Info with sachin')
        self.st.create_module_dict('Login With Twiter')

if __name__ == '__main__':
    unittest.main()