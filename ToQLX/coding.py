#-*- coding:utf-8 -*-
print("build by hg56th56gd6g")
#储存魔数(编码名称,魔数,魔数长度,解魔数后的编码名称)
Boms=(
    ("utf8_bom",b"\xEF\xBB\xBF",3,"utf-8"),
    ("utf16_le_bom",b"\xFF\xFE",2,"utf-16-le"),
    ("utf16_be_bom",b"\xFE\xFF",2,"utf-16-be"),
    ("utf32_le_bom",b"\xFF\xFE\x00\x00",4,"utf-32-le"),
    ("utf32_be_bom",b"\x00\x00\xFE\xFF",4,"utf-32-be")
)
#给Boms每一项的[0]分配索引,储存时+1,因为没找到时返回0
IdxMap=dict()
a=1
for b in Boms:
    IdxMap[b[0]]=a
    a+=1
#...
print("支持处理的编码有py自带的和%s,名字必须完全相同"%",".join(a[0] for a in Boms))
print("可以使用命令行python coding.py来运行(之后根据提示输入),也支持作为库import")
print("库指南,提供了以下几个函数(此处的字符串在py3中指字节串):")
print("GetCoding(Data);输入一个字符串,根据头部魔数(bom)返回一个编码(字符串),没有魔数会返回None")
print("ChangeCoding(Data,IC,OC);输入字符串,输入数据的编码(字符串),输出数据的编码(字符串),返回一个重新编码过的字符串")
########
def GetCoding(Data):
    for a in Boms:
        if Data[:a[2]:]==a[1]:
            return a[0]
    return None
########
def ChangeCoding(Data,IC,OC):
    #解
    a=IdxMap.get(IC,0)
    if a:
        a=Boms[a-1]
        Data=Data[a[2]::].decode(a[3])
    else:
        Data=Data.decode(IC)
    #编
    a=IdxMap.get(OC,0)
    if a:
        a=Boms[a-1]
        Data=a[1]+Data.encode(a[3])
    else:
        Data=Data.encode(OC)
    return Data
########
if __name__=="__main__":
    while True:
        a=input("继续(y)/退出?: ")
        if a!="y":
            break
        else:
            I=input("输入文件 的路径(可以拖进来自动填充): ")
            I=I.strip("\"")
            IC=input("输入文件 的编码: ")
            O=input("输出文件 的路径(可以拖进来自动填充): ")
            O=O.strip("\"")
            OC=input("输出文件 的编码: ")
            with open(I,"rb") as I:
                with open(O,"wb") as O:
                    O.write(ChangeCoding(I.read(),IC,OC))
            print("OK..")
            print("========")