# mmpretrain
mim train mmpretrain ./data/resnet50_finetune.py --work-dir=./exp
The best checkpoint with 89.2496 accuracy/top1 at 5 epoch is saved to best_accuracy_top1_epoch_5.pth.

mim test mmpretrain ./data/resnet50_finetune.py --checkpoint ./exp/best_accuracy_top1_epoch_5.pth
Epoch(test) [90/90]    accuracy/top1: 89.2496  data_time: 0.0025  time: 0.0797
<img width="153" alt="荔枝" src="https://github.com/xiaohui82/mmpretrain/assets/135036586/8ca23256-5358-4697-a23d-1bc24102175d">

[{'pred_scores': array([7.5542850e-10, 1.4910975e-10, 4.5218535e-06, 3.7455513e-07,
       2.2469354e-07, 5.3803206e-10, 8.2638849e-08, 1.7923638e-10,
       3.8696845e-07, 1.2231578e-07, 1.4823028e-08, 6.9380314e-11,
       4.1925286e-08, 2.4498534e-09, 8.4193683e-09, 8.3366375e-10,
       1.1008288e-09, 2.0380394e-07, 3.9870991e-09, 3.2833691e-11,
       5.9055469e-07, 9.9995279e-01, 4.8196844e-06, 2.1565240e-08,
       3.5685673e-05, 1.1456332e-07, 2.1066435e-09, 1.7251640e-09,
       1.9260908e-09, 3.1243241e-11], dtype=float32), 'pred_label': 21, 'pred_score': 0.9999527931213379, 'pred_class': '荔枝'}]
     
