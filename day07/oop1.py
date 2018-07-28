# class BearTony:
#     def __init__(self, size, color, phone, email):
#         self.size = size
#         self.color = color
#         self.vendor = Vendor(phone, email)
#
#     def speak(self):
#         print('hello')
#
#
# class Vendor:
#     def __init__(self, phone, email):
#         self.phone = phone
#         self.email = email
#
#     def call(self):
#         print('calling %s' % self.phone)
#
#
# if __name__ == '__main__':
#     # tidy = BearTony('small', 'orange ')
#     # print((tidy.color))
#     # tidy.speak()
#     # tidy.size
#     bigbear = BearTony('red', 'middle', '434541554', 'jhsjdhhsdh')
#     print(bigbear.color)
#     bigbear.vendor.call()

# class Hotel:
#     def __init__(self, price=200, cutoff=1.0, br=15):
#         self.price = price
#         self.cutoff = cutoff
#         self.br = br
#
#     def calc(self, days=1):
#         return (self.price * self.cutoff + self.br) * days
#
#
# if __name__ == '__main__':
#     stdroom = Hotel()
#     bigbed = Hotel(220, 0.9)
#     print(stdroom.calc())
#     print(stdroom.calc(2))
#     print(bigbed.calc())
#     print(bigbed.calc(2))

# class A:
#     def foo(self):
#         print('is foo')
#     def hello(self):
#         print('hello A')
# class B(A):
#     def bar(self):
#         print('B bar')
#     def hello(self):
#         print('hello B')
#
# class C(B):
#     def hello(self):
#         print('hello c')
#
# if __name__ == '__main__':
#     c=C()
#     c.foo()
#     c.bar()
#     c.hello()


class Book:
    def __init__(self, tittle, author, pages):
        self.tittle = tittle
        self.author = author
        self.pages = pages

    def __str__(self):
        return '<<%s>>' % self.tittle

    def __call__(self):
        print('<<%s>> is written by %s' % (self.tittle, self.author))


if __name__ == '__main__':
    pybook = Book('Core Python', 'Wysley', 900)
    print(pybook)
    pybook()
