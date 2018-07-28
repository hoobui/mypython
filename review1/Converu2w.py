import os


class Convert:
    def __init__(self, fname):
        self, fname = fname

    def to_linux(self):
        dst_fname = os.path.splitext(self.fname)[0] + '.linux'
        with open(self.fname, 'r') as src_obj:
            with open(dst_fname, 'w') as dst_obj:
                for i in src_obj:
                    i = i.rsplit() + '\n'
                    dst_obj.write(i)

    def to_windows(self):
        dst_fname = os.path.splitext(self.fname)[0] + '.windows'
        with open(self.fname, 'r') as src_obj:
            with open(dst_fname, 'w') as dst_obj:
                for i in src_obj:
                    i = i.rsplit() + '\r\n'
                    dst_obj.write(i)


if __name__ == '__main__':
    c = Convert('/tmp/passwd')
    c.to_linux()
    c.to_windows()
