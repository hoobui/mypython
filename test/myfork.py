# import os
# print('abcd')
# os.fork()
# print('hello')

# import os
#
# print('abcdef')
#
# pid = os.fork()
# if pid:
#     print('In parent')
# else:
#     print('In Chlid')
#
# print('Done')

import subprocess
import os


def ping(host):
    rc = subprocess.call(
        'ping -c2 -i0.2 %s &> /dev/null' % host,
        shell=True
    )
    if rc:
        print('%s is down' % host)
    else:
        print('%s is up' % host)


if __name__ == '__main__':
    ips = ['176.121.207.%s' % i for i in range(1, 255)]
    for i in ips:
        pis = os.fork()
        if not pis:
            ping(i)
            exit()
