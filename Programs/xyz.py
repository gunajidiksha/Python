
# n=input("enter value : ")
# list=[n]
# for i in range (n):
#     list.append(i)
# for i in range (n):
#     print(list[i])


# input size
# rows_size = int(input())

# for i in range(1 , rows_size) :
#     print(i + end=" ")

# x = 'From marquard@uct.ac.za'
# print(x[8])

# print(len('banana')*7)
# greet = 'Hello Bob'
# print(greet.upper())
# data = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
# pos = data.find('.')
# print(data[pos:pos+3])
# x = '40'
# y = int(x) + 2
# print(y)
# x = 'From marquard@uct.ac.za'

# print(x[14:17])

text = "X-DSPAM-Confidence:    0.8475"
x = text.find(':')
a = text[(x+4):30]
print(a)