def chuanHoa(string):
    arr = string.split(' ')
    newStr = ''
    for i in arr:
        i = str(i).capitalize()
        newStr += ' ' + i
    return newStr


string = "dao NHU anh"
print(chuanHoa(string))
lines = []
with open('test.txt') as f:
    lines = f.readlines()
    print(lines)

for i in lines:
    if i == '\n':
        lines.remove(i)
# newf = open('new.txt', 'w+')
new = []
for i in lines:
    new.append((chuanHoa(i)))
new.sort()
# print(new)
# for i in new:
#     newf.writelines(i)

print(new)
countName = 0
countFName = 0
for i in new:
    k = i.split(' ')
    if k[-1] == 'Anh' or k[-1] == 'Anh\n':
        countName = countName + 1
    if k[1] == 'Nguyen':
        countFName = countFName + 1
print('Số người Anh:' + str(countName))
print('Số người họ Nguyễn: ' + str(countFName))