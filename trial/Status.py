
class status:

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

# st = status()
#
# st.pass_Test('001','Jo bhi hai')
# st.pass_Test('002','Jo bhi tha')

# print(st.pass_case.items()[0])
# print(next(iter(st.pass_case.keys())))
# for key, value in st.pass_case.items():
#     print(key)
#     print(value)