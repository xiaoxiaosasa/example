# 这是解决扫码枪读码为byte类型，且存在粘包，替换所用的


s = b'\x06NGhttp://www.baidu.com\r\n'

print(s.replace(b'\x06',b'').replace(b'NG',b'').decode().strip())

# 输出结果
# http://www.baidu.com
