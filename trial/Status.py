from trial.createHtml import Prepare_report
import pyscreenshot as ImageGrab
import os


class status:

    def __init__(self):
        if not os.path.exists('test_report'):
            os.makedirs('test_report')
        if not os.path.exists('test_report/images'):
            os.makedirs('test_report/images')

    test_unit = {}
    test_case_with_status = {}
    test_modules_name = []

    def pass_test(self, tc_id, tc_Message, *save_screenshot):
        self.test_case_with_status[tc_id] = tc_Message+'P'
        for ar in save_screenshot:
            if ar == 'T':
                ImageGrab.grab_to_file('test_report/images/'+tc_id+'.png')
        return self.test_case_with_status

    def fail_test(self, tc_id, tc_Message, *save_screenshot):
        self.test_case_with_status[tc_id] = tc_Message+'F'
        for ar in save_screenshot:
            if ar == 'T':
                ImageGrab.grab_to_file('test_report/images/' + tc_id + '.png')
        return self.test_case_with_status

    def error_test(self, tc_id, tc_Message, *save_screenshot):
        self.test_case_with_status[tc_id] = tc_Message+'E'
        for ar in save_screenshot:
            if ar == 'T':
                ImageGrab.grab_to_file('test_report/images/' + tc_id + '.png')
        return self.test_case_with_status

    def skip_test(self, tc_id, tc_Message, *save_screenshot):
        self.test_case_with_status[tc_id] = tc_Message+'S'
        for ar in save_screenshot:
            if ar == 'T':
                ImageGrab.grab_to_file('test_report/images/' + tc_id + '.png')
        return self.test_case_with_status

    def info_test(self, tc_id, tc_Message, *save_screenshot):
        self.test_case_with_status[tc_id] = tc_Message+'I'
        for ar in save_screenshot:
            if ar == 'T':
                ImageGrab.grab_to_file('test_report/images/' + tc_id + '.png')
        return self.test_case_with_status

    def create_module_dict(self, ModuleName):
        self.test_modules_name.append(ModuleName)
        self.test_unit['Module_Name'] = ModuleName
        self.test_unit['All_Cases'] = self.test_case_with_status
        print(self.test_unit)
        Prepare_report(self.test_unit,self.test_modules_name,ModuleName)