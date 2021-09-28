import os
import random
import shutil
import json
import numpy as np


def decode_jsonfile(json_dict):
    output = np.zeros(13)
    shapes = json_dict['shapes']
    for item in shapes:
        if item['label'] == 'a':
            output[0] = item['points'][0][0] # x1
            output[1] = item['points'][0][1] # y1
            output[2] = item['points'][1][0] # x2
            output[3] = item['points'][1][1] # y2
        elif item['label'] == 'a1':
            output[4] = item['points'][0][0] # pt1 x
            output[5] = item['points'][0][1] # pt1 y
        elif item['label'] == 'a2':
            output[6] = item['points'][0][0] # pt2 x
            output[7] = item['points'][0][1] # pt2 y
        elif item['label'] == 'a3':
            output[8] = item['points'][0][0] # pt3 x
            output[9] = item['points'][0][1] # pt3 y
        elif item['label'] == 'a4':
            output[10] = item['points'][0][0] # pt4 x
            output[11] = item['points'][0][1] # pt4 y
    output[12] = 1
    output = [str(round(a, 3)) for a in output]
    output = ' '.join(output)
    return output


def generator(in_path, out_path, train_rate):

    train_path = os.path.join(out_path, 'train')
    val_path = os.path.join(out_path, 'val')
    os.makedirs(train_path, exist_ok=True)
    os.makedirs(val_path, exist_ok=True)

    file_lists = os.listdir(in_path)
    file_lists = [a for a in file_lists if not a.endswith('.json')]
    random.shuffle(file_lists)

    train_lists = file_lists[:int(len(file_lists)*train_rate)]
    val_lists = file_lists[int(len(file_lists)*train_rate):]

    train_label_txt = open(os.path.join(out_path, 'train.txt'), 'w', encoding='utf-8')
    val_label_txt = open(os.path.join(out_path, 'val.txt'), 'w', encoding='utf-8')

    for filename in train_lists:
        json_name = os.path.join(in_path, filename.split('.')[0] + '.json')
        if not os.path.exists(json_name):
            continue

        json_file = open(json_name, "r+", encoding="utf8")
        json_dict = json.loads(json_file.read())
        json_dict.pop("imageData")
        if(len(json_dict['shapes'])!=5):
            continue
        shutil.copy(os.path.join(in_path, filename), os.path.join(train_path))
        train_label_txt.write('# train/' + filename + '\n')
        txt = decode_jsonfile(json_dict)
        train_label_txt.write(txt + '\n')
    train_label_txt.close()

    for filename in val_lists:
        json_name = os.path.join(in_path, filename.split('.')[0] + '.json')
        if not os.path.exists(json_name):
            continue

        json_file = open(json_name, "r+", encoding="utf8")
        json_dict = json.loads(json_file.read())
        json_dict.pop("imageData")
        if (len(json_dict['shapes']) != 5):
            continue
        shutil.copy(os.path.join(in_path, filename), os.path.join(val_path))
        val_label_txt.write('# val/' + filename + '\n')
        txt = decode_jsonfile(json_dict)
        val_label_txt.write(txt + '\n')
    val_label_txt.close()


if __name__ == '__main__':
    in_path = r'D:\Work\Data\label_test'
    out_path = r'D:\Work\Data\idcard'
    train_rate = 0.9
    generator(in_path, out_path, train_rate)




