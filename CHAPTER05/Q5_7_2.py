d = [['0001','Male','Yamada','Tarou','25','Tokyo'],
    ['0002','Male','Satou','Takeshi','27','Kanagawa'],
    ['0003','Female','Tanaka','Yuko','25','Saitama'],
    ['0004','Male','Suzuki','Ichirou','35','Hokkaido']]

m = {}

for re in d:
    k = re[0]
    i = re[1:]
    m[k] = i

for k,i in m.items():
    print(k,i)
