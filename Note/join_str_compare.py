# coding:utf-8

from random import randint
import time

strlist = [str(randint(-10, 10)) for _ in range(100000)]


start = time.time()
s = ""
for sl in strlist:
    s += sl

end = time.time()
print(end - start)

start = time.time()
sl = "".join(strlist)

end = time.time()
print(end - start)