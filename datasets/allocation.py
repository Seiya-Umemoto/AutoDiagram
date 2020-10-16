import shutil, random, os

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

classes = [
    # 'cabbage',
    # 'carrot',
    # 'eggs',
    # 'onion',
    'bean_sprouts',
    'chicken',
    'green_onions',
    'potatoes',
]

dst_dir1 = './ver1/Training_michi'
dst_dir2 = './ver1/Testing_michi'

for c in classes:
    lists = []

    dst_c1 = dst_dir1 + "/" + c
    if not os.path.exists(dst_c1):
        os.mkdir(dst_c1)
        
    dst_c2 = dst_dir2 + "/" + c
    if not os.path.exists(dst_c2):
        os.mkdir(dst_c2)

    os.chdir(c)
    num_images = len([name for name in os.listdir('.') if os.path.isfile(name)])
    num_train = int(num_images * 0.8)
    os.chdir('..')

    count = 1
    while count <= num_train:
        num = random.randrange(1, num_images+1)
        if num not in lists:
            lists.append(num)
            src1 = './{}/{}_{}.jpg'.format(c, c, num)
            shutil.copy(src1, dst_c1)
            count += 1        

    for i in range(1, num_images+1):
        if i not in lists:
            src2 = './{}/{}_{}.jpg'.format(c, c, i)           
            shutil.copy(src2, dst_c2)  