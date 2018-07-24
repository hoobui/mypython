import re
from collections import Counter


# def count_ip(fname, patt):
#     cpatt = re.compile(patt)
#     result = {}
#
#     with open(fname) as obj:
#         for line in obj:
#             m = cpatt.search(line)
#             if m:
#                 key = m.group()
#                 result[key] = result.get(key, 0) + 1
#     return result
#
#
# if __name__ == '__main__':
#     fname = '/root/桌面/nsd2018/nsd1802/python/day08/access_log'
#     ip = '^(\d+\.){3}\d+'
#     print(count_ip(fname, ip))
#     br='Firefox|Chrome|MSIE'
#     print(count_ip(fname, br))


class CountIp:
    def __init__(self, fname):
        self.fname = fname

    def __call__(self, patt):
        cpatt = re.compile(patt)
        result = Counter()

        with open(fname) as obj:
            for line in obj:
                m = cpatt.search(line)
                if m:
                    result.update([m.group()])
        return result


if __name__ == '__main__':
    fname = '/root/桌面/nsd2018/nsd1802/python/day08/access_log'
    ip = '^(\d+\.){3}\d+'
    c = CountIp(fname)
    a = c(ip)
    print(a)





