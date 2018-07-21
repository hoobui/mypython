# def mygen():
#     yield 'hello'
#     a=10+20
#     yield a
#     yield [1,2,3]
#
# if __name__ == '__main__':
#     n=mygen()
#     for i in n:
#         print(i)
#
#     for i in n:
#         print(i)

def block(obj):
    block = []
    counter = 0
    for i in obj:
        block.append(i)
        counter += 1
        if counter == 10:
            yield block
            counter = 0
            block = []
    if block:
        yield block


if __name__ == '__main__':
    with open('/tmp/passwd', 'r') as f:
        for i in block(f):
            print(i)
            print()
