import threading
print("hello")

def greet_user():
    print("greet_user hello")
greet_user()

with open('/Users/mac/PycharmProjects/helloWord/test.txt') as file_object:
    contents = file_object.read()
    print(contents)

filename = '/Users/mac/PycharmProjects/helloWord/readLine.txt'
with open(filename) as file_object:
    for line in file_object:
        print(line)

filename2 = '/Users/mac/PycharmProjects/helloWord/write.txt'
with open(filename2, 'w') as file_object:
    file_object.write("I love programming.111 \n")
    file_object.write("I love programming.222 \n")

map = ['1','2','3']
for m in map:

    print(m)