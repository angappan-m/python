import os

root_dir = 'test'

try:
    for i in range(1000):
        os.mkdir(os.path.join(root_dir, str(i)))  # test/1
except Exception as e:
    pass

for j in os.listdir(root_dir):
    new_dir = os.path.join(root_dir, str(j))
    for k in range(10000):
        f = open(os.path.join(new_dir, 'text_'+str(k)+'.txt'), "a+")
        for l in range(1, 100):
            f.write(str(l)+" ")
        f.close()
        print(os.path.join(new_dir, 'text_'+str(k)+'.txt'))
