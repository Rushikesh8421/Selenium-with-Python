# file = open('test.txt')
# print(file.read(5))
#
# for line in file.readlines():
#     print(line)
# file.close()

with open('test.txt','r') as reader:
    content = reader.readlines()
    with open('test.txt','w') as writer:
        for line in reversed(content):
            writer.write(line)