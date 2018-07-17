# sum = 0
# counter = 1
# count = 154
#
#
# while counter <= count:
#     sum += counter
#     counter += 1
#
# print(sum)

# while True:
#     yn = input('Continue(y/n): ')
#     if yn in ['n','N']:
#         break
#     print('running')

sum = 0
counter = 0

while counter < 100:
    counter += 1
    if counter % 2:
        continue
    sum += counter
print(sum)