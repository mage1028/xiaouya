"""
用于生成645透传报文 修改能耗区间
"""
x = input('请输入7位表号：')
A = input('请输入能耗区间一（格式：XXXXXX 代表xx.xxxx KW ):')
B = input('请输入能耗区间二（格式：XXXXXX 代表xx.xxxx KW ):')
C = input('请输入能耗区间三（格式：XXXXXX 代表xx.xxxx KW):')
x = int(x)
A = int(A)
B = int(B)
C = int(C)
def spilt1(x):
    L = [str(int(x) - (int(x / 100) * 100)),str(int(x/100)-(int(x/10000)*100)),
       str(int(x/10000)-(int(x/1000000)*100)),str(int(x/1000000))]
    return L
#eg：分离电表号，将1662233分离成33,22,66,01
def spilt2(x):
    L = [ hex(int(str((int(x ) - int(x / 100) * 100)), 16) + 0x33),hex(int(str(int(x/10000)),16)+0x33),
        hex(int(str((int(x/100)-int(x/10000)*100)),16)+0x33),
       ]
    return L
#eg:分离数据区，将993366分离成99,66,CC
L=spilt1(x)+['00','00','68','14','15','32','34','C3','37','35','33','33','33','33','33','33','33']+spilt2(A)+spilt2(B)+spilt2(C)

s=0
for i in L:
    s=s+int(i,16)
while s>=0xFF:
    s=s-0x100

#校验和的运算判别

L=L+[hex(s),'16']
print(L)
