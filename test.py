# coding=utf-8 

# 导入推理工具包
from mmpretrain import ImageClassificationInferencer


# 设置推理配置文件和训练权重
inferencer = ImageClassificationInferencer('./data/resnet50_finetune.py', pretrained='./exp/best_accuracy_top1_epoch_5.pth')


# 对指定图片做推理
result = inferencer("./img/荔枝.png", show=True)

print(result)