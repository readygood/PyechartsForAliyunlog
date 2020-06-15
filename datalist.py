import json

class Datalist:

    def __init__(self, totalfile, normalfile, errorfile):

        self.totalfile = totalfile
        self.normalfile = normalfile
        self.errorfile = errorfile


    def get_last_linecount(self):

        with open(self.totalfile, 'rb') as f1, open(self.normalfile, 'rb') as f2, open(self.errorfile, 'rb') as f3:

            offset = -5

            while True:

                f1.seek(offset, 2)
                f2.seek(offset, 2)
                f3.seek(offset, 2)

                lines1, lines2, lines3 = f1.readlines(), f2.readlines(), f3.readlines()

                if len(lines1) > 1 and len(lines2) > 1 and len(lines3) > 1:

                    total_last_line, normal_last_line, error_last_line = lines1[-1], lines2[-1], lines3[-1]

                    break

                offset *= 2

        return [int(json.loads(total_last_line.decode())[0]['count']),
                int(json.loads(normal_last_line.decode())[0]['count']),
                int(json.loads(error_last_line.decode())[0]['count']),
                float("%.4f" % (100 - (int(json.loads(error_last_line.decode())[0]['count']) / int(json.loads(total_last_line.decode())[0]['count'])) * 100))]
