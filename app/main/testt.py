list1 = ['a','b','c']
print('\n'.join(list1))
print(['{}\t{}'.format(str(x[0]).zfill(10), x[1]) for x in list(enumerate(list1, start=10))])

with open(r'C:\Users\v-junlia.FAREAST\Desktop\New Text Document.txt', 'w') as f:
    f.write('\n'.join(['{}\t{}'.format(str(x[0]).zfill(10), x[1]) for x in list(enumerate(list1, start=10))]))