import hashlib


def hash(filename):
    with open(filename, 'rb') as file:
        while True:
            data = file.read(4096)
            if not data:
                break
            m = hashlib.md5()
            m.update(data)
    return m.hexdigest()


if __name__ == '__main__':
    print(hash('/etc/passwd'))
    print(hash('/tmp/passwd'))
