import glob, os
import urllib.request

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

# 보존했던 folder명 기입
files = glob.glob("./bean_sprouts/*")

array = []

for i in range(2000):
    array.append(i+1)

z = 0
# file명 바꾸기 
for i in files:
    new_name = "./bean_sprouts/bean_sprouts_{}.jpg".format(array[z])
    os.rename(i, new_name)
    z = z + 1
