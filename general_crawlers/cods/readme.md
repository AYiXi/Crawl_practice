jsonString = {"zczj":"","userId":"","xzqh":"","q":"百度","longitudeApp":"","um":"","t":"common","isDeepSearch":"false","osname":"Android+6.0.1(MuMu)","dimensionApp":"","version":"v1.4.2","jglx":"","clrq":"","currentPage":1,"misskey":"%7B%22sw%22%3A1053%2C%22sh%22%3A1872%2C%22dpi%22%3A416%2C%22point1%22%3A%7B%22x%22%3A0.0%2C%22y%22%3A0.0%7D%2C%22point2%22%3A%7B%22x%22%3A122.04932%2C%22y%22%3A306.5871%7D%7D","channel":"common","userCookie":"541947bc4f0e45fbb579a539788e42f5"}
sign = md5(quote(jsonString) + 'A523B4A5C52203AA9C2D97F6CB45CB35')


// 不能固定, 值都要随机
misskey = '{"sw":1053,"sh":1872,"dpi":416,"point1":{"x":0.0,"y":0.0},"point2":{"x":122.04932,"y":306.5871}}'


case1: 
    jsonString = %7B%22zczj%22%3A%22%22%2C%22userId%22%3A%22%22%2C%22xzqh%22%3A%22%22%2C%22q%22%3A%22%E7%99%BE%E5%BA%A6%22%2C%22longitudeApp%22%3A%22%22%2C%22um%22%3A%22%22%2C%22t%22%3A%22common%22%2C%22isDeepSearch%22%3A%22false%22%2C%22osname%22%3A%22Android+6.0.1%28MuMu%29%22%2C%22dimensionApp%22%3A%22%22%2C%22version%22%3A%22v1.4.2%22%2C%22jglx%22%3A%22%22%2C%22clrq%22%3A%22%22%2C%22currentPage%22%3A1%2C%22misskey%22%3A%22%257B%2522sw%2522%253A1053%252C%2522sh%2522%253A1872%252C%2522dpi%2522%253A416%252C%2522point1%2522%253A%257B%2522x%2522%253A0.0%252C%2522y%2522%253A0.0%257D%252C%2522point2%2522%253A%257B%2522x%2522%253A122.04932%252C%2522y%2522%253A306.5871%257D%257D%22%2C%22channel%22%3A%22common%22%2C%22userCookie%22%3A%22541947bc4f0e45fbb579a539788e42f5%22%7D
    sign = 141b31a3eb6da27c0bf53f97141d88f3
    sign-fmd5 = %7B%22zczj%22%3A%22%22%2C%22userId%22%3A%22%22%2C%22xzqh%22%3A%22%22%2C%22q%22%3A%22%E7%99%BE%E5%BA%A6%22%2C%22longitudeApp%22%3A%22%22%2C%22um%22%3A%22%22%2C%22t%22%3A%22common%22%2C%22isDeepSearch%22%3A%22false%22%2C%22osname%22%3A%22Android+6.0.1%28MuMu%29%22%2C%22dimensionApp%22%3A%22%22%2C%22version%22%3A%22v1.4.2%22%2C%22jglx%22%3A%22%22%2C%22clrq%22%3A%22%22%2C%22currentPage%22%3A1%2C%22misskey%22%3A%22%257B%2522sw%2522%253A1053%252C%2522sh%2522%253A1872%252C%2522dpi%2522%253A416%252C%2522point1%2522%253A%257B%2522x%2522%253A0.0%252C%2522y%2522%253A0.0%257D%252C%2522point2%2522%253A%257B%2522x%2522%253A122.04932%252C%2522y%2522%253A306.5871%257D%257D%22%2C%22channel%22%3A%22common%22%2C%22userCookie%22%3A%22541947bc4f0e45fbb579a539788e42f5%22%7DA523B4A5C52203AA9C2D97F6CB45CB35

case2:
    jsonString = %7B%22zczj%22%3A%22%22%2C%22userId%22%3A%22%22%2C%22xzqh%22%3A%22%22%2C%22q%22%3A%22%E7%99%BE%E5%BA%A6%E5%85%B3%E7%88%B1%22%2C%22longitudeApp%22%3A%22%22%2C%22um%22%3A%22%22%2C%22t%22%3A%22common%22%2C%22isDeepSearch%22%3A%22false%22%2C%22osname%22%3A%22Android+6.0.1%28MuMu%29%22%2C%22dimensionApp%22%3A%22%22%2C%22version%22%3A%22v1.4.2%22%2C%22jglx%22%3A%22%22%2C%22clrq%22%3A%22%22%2C%22currentPage%22%3A1%2C%22misskey%22%3A%22%257B%2522sw%2522%253A1053%252C%2522sh%2522%253A1872%252C%2522dpi%2522%253A416%252C%2522point1%2522%253A%257B%2522x%2522%253A419.3822%252C%2522y%2522%253A118.21791%257D%252C%2522point2%2522%253A%257B%2522x%2522%253A977.693%252C%2522y%2522%253A129.90979%257D%257D%22%2C%22channel%22%3A%22common%22%2C%22userCookie%22%3A%22541947bc4f0e45fbb579a539788e42f5%22%7D
    sign = 9e2bdcdcd82e9087b1a7b1fdc520a78d
    sign-fmd5 = %7B%22zczj%22%3A%22%22%2C%22userId%22%3A%22%22%2C%22xzqh%22%3A%22%22%2C%22q%22%3A%22%E7%99%BE%E5%BA%A6%E5%85%B3%E7%88%B1%22%2C%22longitudeApp%22%3A%22%22%2C%22um%22%3A%22%22%2C%22t%22%3A%22common%22%2C%22isDeepSearch%22%3A%22false%22%2C%22osname%22%3A%22Android+6.0.1%28MuMu%29%22%2C%22dimensionApp%22%3A%22%22%2C%22version%22%3A%22v1.4.2%22%2C%22jglx%22%3A%22%22%2C%22clrq%22%3A%22%22%2C%22currentPage%22%3A1%2C%22misskey%22%3A%22%257B%2522sw%2522%253A1053%252C%2522sh%2522%253A1872%252C%2522dpi%2522%253A416%252C%2522point1%2522%253A%257B%2522x%2522%253A419.3822%252C%2522y%2522%253A118.21791%257D%252C%2522point2%2522%253A%257B%2522x%2522%253A977.693%252C%2522y%2522%253A129.90979%257D%257D%22%2C%22channel%22%3A%22common%22%2C%22userCookie%22%3A%22541947bc4f0e45fbb579a539788e42f5%22%7DA523B4A5C52203AA9C2D97F6CB45CB35


Login:
    https://ss.cods.org.cn:8443/APPService/usercenter/validateLogin?jsonString=%257B%2522user_pswd%2522%253A%252211111111%2522%252C%2522osname%2522%253A%2522Android%2B6.0.1%2528MuMu%2529%2522%252C%2522dimensionApp%2522%253A%2522%2522%252C%2522version%2522%253A%2522v1.4.2%2522%252C%2522longitudeApp%2522%253A%2522%2522%252C%2522user_name%2522%253A%252218990252222%2522%252C%2522channel%2522%253A%2522common%2522%252C%2522userCookie%2522%253A%2522541947bc4f0e45fbb579a539788e42f5%2522%257D&sign=6fbd6537a5c7c8988c8a9d06450c8c63
    {"user_pswd":"11111111","osname":"Android+6.0.1(MuMu)","dimensionApp":"","version":"v1.4.2","longitudeApp":"","user_name":"18990252222","channel":"common","userCookie":"541947bc4f0e45fbb579a539788e42f5"}
    userCookie: 
        "userCookie", UUID.randomUUID().toString().replace("-", "")