import glob
import random
import os
from PIL import Image


# 函数定义
def read_split_data(data_path, raw_path, ratio):
    test_split_ratio = ratio


    dirs = glob.glob(os.path.join(data_path, '*'))
    dirs = [d for d in dirs if os.path.isdir(d)]  # 只保留dirs中文件夹的部分，不考虑文件的部分


    print(f'Totally {len(dirs)} classes: {dirs}')


    for path in dirs:
        # 对每个类别单独处理
        path = path.split('/')[-1]
        # print(path)

        os.makedirs(f'{raw_path}/train', exist_ok=True)
        os.makedirs(f'{raw_path}/test', exist_ok=True)
        os.makedirs(f'{raw_path}/train/{path}', exist_ok=True)
        os.makedirs(f'{raw_path}/test/{path}', exist_ok=True)


        files = glob.glob(os.path.join(data_path, path, '*'))  # 直接读取文件夹下的全部图片（前提是文件夹里的所有文件都是图片）
        #print(os.path.join(data_path, path, '*'))
        #files += glob.glob(os.path.join(raw_path, path, '*.JPG'))
        #files += glob.glob(os.path.join(raw_path, path, '*.png'))


        random.shuffle(files)


        boundary = int(len(files)*test_split_ratio)  # 训练集和测试集的边界
        print('len(files):',len(files))
        print('boundary:',boundary)
        print(files)


        for i, file in enumerate(files):
            if file.endswith('jpg') or file.endswith('png'):
                img = Image.open(file)
                if i <= boundary:
                    img.save(os.path.join(f'{raw_path}/test/{path}', file.split('/')[-1].split('.')[0]+'.jpg'))
                else:
                    img.save(os.path.join(f'{raw_path}/train/{path}', file.split('/')[-1].split('.')[0]+'.jpg'))


    test_files = glob.glob(os.path.join(f'{raw_path}/test/', '*', '*.jpg'))
    train_files = glob.glob(os.path.join(f'{raw_path}/train/', '*', '*.jpg'))


    print(f'Totally {len(train_files)} files for training')
    print(f'Totally {len(test_files)} files for test')


# 函数调用
# 当前已在 data 目录下
data_path = './data/fruit30_train'
raw_path = './data'
# 测试集比例
ratio = 0.2


read_split_data(data_path,raw_path, ratio)