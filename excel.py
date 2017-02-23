#coding:utf-8
import xlrd
import xlwt


f =xlrd.open_workbook(r'D:\b.xls')

table = f.sheets()[0]
alldata = []

rows = table.nrows
cols = table.ncols

s = xlwt.Workbook()
sheet1 = s.add_sheet('sheet1',cell_overwrite_ok=True)
a = [0,10,13,18]
for i in range(1,rows):
    for q,w in zip(range(0,cols),a):
        data = table.cell(i, q).value
        if w == 13:
            data = data[1:-1]
        sheet1.write(i,w,data)

s.save(r'D:\c.xls')
'''
alldata = table.row_values(1)

row_number = table.nrows
lis = []
for row in range(1,row_number):
    data = table.row_values(row)
    #print(data[0])
    if 'cisco' in data[0] or 'F63' in data[0]:
        if  'avai' in data[0]:
            data = data[0][::-1]
            sn = re.search(r'\"\S+?\"',data)
            lis.append(sn.group())
for i in lis:
    c = i[::-1]
    print(c)
a=[]
for i in lis:
    if i[::-1] in lis[lis.index(i):]:
        a.append(i[::-1])
    #print(i[::-1])
#print(a)
'''
'''
a = []
for i in lis:
    if i in lis[lis.index(i)+1:]:
        a.append(i[::-1])
b = set(a)
b = sorted(b)
for i in b:
    print(i)

'''


'''

f =xlrd.open_workbook(r'D:\av.xlsx')

table = f.sheets()[0]
row_number = table.nrows
cisco1812 = []
cisco1841 = []
cisco1921 = []
shijiwangtong = []
cisco = []
soundwind = []
order = []
voip = []
xunshi = []

for i in range(1,row_number):
    data = table.row_values(i)
    if  '1812' in data[0]:
        cisco1812.append(data)
    elif  '1921' in data[0]:
        cisco1921.append(data)
    elif u'\u4e16\u7eaa\u7f51\u901a' in data[0]:
        shijiwangtong.append(data)
    elif '1841' in data[0]:
        cisco1841.append(data)
    elif 'cisco' in data[0]:
        cisco.append(data)
    elif 'sound' in data[0]:
        soundwind.append(data)
    elif 'VOI' in data[0]:
        voip.append(data)
    elif 'newrock' in data[0]:
        xunshi.append(data)
    else:
        order.append(data)
print(len(order))
print('cisco1812:'+str(len(cisco1812)))
print('cisco1921:'+str(len(cisco1921)))
print ('世纪网通:'+str(len(shijiwangtong)))
print('cisco1841:'+str(len(cisco1841)))
print('cisco:'+str(len(cisco)))
print('soundwind:'+str(len(soundwind)))
print('上海迅时:'+str(len(xunshi)))
print('VOIP:'+str(len(voip)))
sum = len(cisco1812)+len(cisco1921)+len(shijiwangtong)+len(cisco1841)+len(cisco)+len(soundwind)+len(xunshi)+len(voip)
print(sum)
'''