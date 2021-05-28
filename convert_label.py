import xml.etree.ElementTree as ET
import os
classes = ["1","2","3",'4','5','6','7']


def convert(size, box):
    dw = 1./size[0]
    dh = 1./size[1]
    x = (box[0] + box[1])/2.0
    y = (box[2] + box[3])/2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x*dw
    w = w*dw
    y = y*dh
    h = h*dh
    return (x,y,w,h)




def convert_annotation(image_id):  # 转换这一张图片的坐标表示方式（格式）,即读取xml文件的内容，计算后存放在txt文件中。
#     in_file = open('D:/ATR/train_anno/%s'%image_id)
    in_file = 'D:/ATR/train_anno/%s'%image_id
    image_id=image_id.split('.')[0]
    out_file = open('D:/ATR/train_anno/%s.txt'%image_id, 'w')
    
#     utf8_parser = ET.XMLParser(encoding='utf-8')
#     tree=ET.parse(in_file, parser=utf8_parser)
#     f = open(in_file)
#     xml_text = f.read()
#     root = ET.fromstring(xml_text)
#     f.close()
    f = open(in_file, encoding='utf8') # 方便处理带有中文的xml文件
    xml_text = f.read()
    root = ET.fromstring(xml_text)
    f.close()
#     root = tree.getroot()

    size = root.find('size')
    w = int(size.find('width').text)
    h = int(size.find('height').text)

    for obj in root.iter('object'):
        difficult = obj.find('difficult').text
        cls = obj.find('name').text
        if cls not in classes or int(difficult) == 1:
            print("new class: ", cls)
            continue
        cls_id = classes.index(cls)
        xmlbox = obj.find('bndbox')
        b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text), float(xmlbox.find('ymax').text))
        bb = convert((w,h), b)
        out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n')


# if not os.path.exists('J:\VOC2012\coco_label/'):
#     os.makedirs('J:\VOC2012\coco_label/')  # 新建一个 labels 文件夹，用于存放yolo格式的标签文件：000001.txt
path = 'D://ATR//train_anno//'
import sys
sys.setdefaultencoding='utf-8'
i = 0
f = os.listdir(path)
for image_id in f:
#     print(image_id)
#     i += 1
#     if i== 10:
#         break
    convert_annotation(image_id)  # 转换这一张图片的坐标表示方式（格式）
