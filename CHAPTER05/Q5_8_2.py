d = [['01','0001','Male','Yamada','Tarou','25','Tokyo'],
    ['01','0002','Male','Satou','Takeshi','27','Kanagawa'],
    ['01','0003','Female','Tanaka','Yuko','25','Saitama'],
    ['02','0001','Male','Smith','Mike','22','NewJersey'],
    ['02','0002','Male','Turner','Tom','27','Kansas'],
    ['02','0003','Male','Jackson','David','25','Florida']]

m = {}

for re in d:
    k = (re[0],re[1])
    i = re[2:]
    m[k] = i

for k,i in m.items():
    print(k,i)
