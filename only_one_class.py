# 把所有标注里都改为一个类 0
import os
path = 'D:ATR/atr_data/val_anno/'
dirs = os.listdir(path)
for txt_file in dirs:
    f = open(path+txt_file, 'r')
    file = open('D:ATR/atr_data/val_txt/' + txt_file, 'a')
    for line in f.readlines():
        temp = '0' + line[1:]
        file.write(temp)
    
    f.close()
    file.close()
    
