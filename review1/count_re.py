import re
from collections import Counter


# def count_ip(fname,count):
#     ccount=re.compile(count)
#     result={}
#
#     with open(fname) as obj:
#         for i in obj:
#             m=ccount.search(i)
#             if m:
#                 key=m.group()
#                 result[key]=result.get(key,0)+1
#
#     return result
#
#
# if __name__ == '__main__':
#     fname='weblog_file'
#     ip='^(\d+\.){3}\d+'
#     print(count_ip(fname,ip))
#     browser='Firefox|Chome|MSIE'
#     print(count_ip(fname,browser))

class CountPatt:
    def __init__(self, fname):
        self.fname = fname

    def count_ip(self, ip):
        countip = re.compile(ip)
        result = Counter()

        with open(self.fname) as obj:
            for i in obj:
                m = countip.search(i)
                if m:
                    result.update([m.group()])
        return result


if __name__ == '__main__':
    c = CountPatt('weblogfile')
    ip = '^(\d+\.){3}\d+'
    browser = 'Firefox|Chrome|MSIE'
    a = c.count_ip(ip)
    print(a)
    print(a.most_common(3))
    print(c.count_ip(browser))
