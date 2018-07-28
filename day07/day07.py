class u2w:
    def __init__(self, fname):
        self.fname = fname

    @staticmethod
    def pduan(fname):
        with open(fname) as src_fobj:
            if '\r\n' in src_fobj:
                with open('/tmp/passwd_linux.txt', 'w') as dst_fobj:
                    for line in src_fobj:
                        line = line.rstrip() + '\n'
                        dst_fobj.write(line)

            else:
                with open('/tmp/passwd_windows.txt', 'w') as dst_fobj:
                    for line in src_fobj:
                        line = line.rstrip() + '\r\n'
                        dst_fobj.write(line)
        return fname


if __name__ == '__main__':
    u2w.pduan('/tmp/passwd')
