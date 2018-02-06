# jabber = open('sample.txt', 'r')
#
# for line in jabber:
#     if 'jabberwock' in line.lower():
#         print(line, end='')
#
# jabber.close()
# with open('sample.txt', 'r') as jabber:
#     for line in jabber:
#         if 'JAB' in line.upper():
#             print(line, end='')

with open('sample.txt', 'r') as jabber:
    lines = jabber.read()
#print(lines)

print('==='*20)

for line in lines[::-1]:
    print(line, end='')

