import glob, os
import urllib.request

# 보존했던 folder명 기입
files = glob.glob("./save/*")

array = []

for i in range(2000):
    array.append(i+1)

z = 0
# file명 바꾸기 
for i in files:
    new_name = "img_{:04d}.jpg".format(array[z])
    os.rename(i, new_name)
    z = z + 1


