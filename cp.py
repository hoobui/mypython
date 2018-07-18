import sys

def copy(src_obj, dst_obj):
    src_file = open(src_obj, 'rb')
    dst_file = open(dst_obj, 'wb')

    while True:
        data = src_file.read(4096)
        if not data:
            break
        dst_file.write(data)

    src_file.close()
    dst_file.close()


copy(sys.argv[1], sys.argv[2])
