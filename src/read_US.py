from read_general import ReadGeneral
import csv
class ReadUS(ReadGeneral):
    dirname = ''
    def __init__(self, directory):
        self.dirname = directory
    def read_all(self, dirname):
        with open(dirname, 'r') as f:
            reader = csv.reader(f)
            result = list(reader)
        return result[0:11]