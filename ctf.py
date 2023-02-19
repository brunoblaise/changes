enc = '灩捯䍔䙻ㄶ形楴獟楮獴㌴摟潦弸弰摤捤㤷慽'
flag = ''

for i in range(len(enc)):
    flag += chr(ord(enc[i]) >> 8)
    flag += chr(ord(enc[i]) - (ord(flag[-1]) << 8))

print(flag)