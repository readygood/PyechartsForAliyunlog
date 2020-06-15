import datetime
from datalist import Datalist
import json

class Source:

    def __init__(self, sourcedata = 'sourcedata', dates = (datetime.date.today() - datetime.timedelta(days=1)), datas = Datalist('zuultotaldata', 'zuulnormaldata', 'zuulerrordata')):

        self.sourcedata = sourcedata
        self.dates = dates
        self.datas = datas

    def sourcedatas(self):

        with open(self.sourcedata, 'r') as f1:

            s = f1.readlines()
            y = json.loads(json.dumps(eval(s[-1])))

            y[str(self.dates)] = self.datas.get_last_linecount()

            with open(self.sourcedata, 'w+') as f2:

                f2.write(str(y))

        return y
test = Source()

test.sourcedatas()
