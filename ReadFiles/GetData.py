import csv
from array import *


def get_data():
    with open('/Users/ICHI01/PycharmProjects/SeleniumPython/DataFiles/Workbook1.csv') as csvFile:
        read = csv.reader(csvFile)
        UserPass = []
        for row in read:
            UserPass.append(row)
        return UserPass
