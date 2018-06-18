
class status:

    test_unit = {}
    pass_case = {}
    fail_case = {}
    error_case = {}
    skip_case = {}
    info_case = {}

    def pass_test(self, tc_id, tc_Message):
        self.pass_case[tc_id] = tc_Message
        return self.pass_case

    def fail_test(self, tc_id, tc_Message):
        self.fail_case[tc_id] = tc_Message
        return self.fail_case

    def error_test(self, tc_id, tc_Message):
        self.error_case[tc_id] = tc_Message
        return self.error_case

    def skip_test(self, tc_id, tc_Message):
        self.skip_case[tc_id] = tc_Message
        return self.skip_case

    def info_test(self, tc_id, tc_Message):
        self.info_case[tc_id] = tc_Message
        return self.info_case

    def create_module_dict(self, ModuleName):
        self.test_unit['Module_Name'] = ModuleName
        self.test_unit['Pass_Cases'] = self.pass_case
        self.test_unit['Fail_Cases'] = self.fail_case
        self.test_unit['Error_Cases'] = self.error_case
        self.test_unit['Skip_Cases'] = self.skip_case
        self.test_unit['Info_Cases'] = self.info_case


# st = status()
# st.pass_test('001','Message')
# st.fail_test('001','Message')
# st.error_test('001','Message')
# st.create_module_dict('Login')
# print(st.test_unit)