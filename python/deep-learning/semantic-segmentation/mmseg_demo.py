"""
It reads a video (sys.argv[1]) . I tested only with MP4 container, don't know if all codecs are supported.
Configuration is hardcoded. It is old code (2019/10/17). Needs mmdet and mmcv
"""

from mmdet.apis import init_detector, inference_detector, show_result
import mmcv
import sys

if len(sys.argv) != 2:
  sys.exit("A video path is needed to work")
  

config_file = 'configs/cityscapes/mask_rcnn_r50_fpn_1x_cityscapes.py'
checkpoint_file = 'checkpoints/mask_rcnn_r50_fpn_1x_city_20190727-9b3c56a5.pth'

# build the model from a config file and a checkpoint file
model = init_detector(config_file, checkpoint_file, device='cuda:0')

"""
# test a single image and show the results
img = 'test.jpg'  # or img = mmcv.imread(img), which will only load it once
result = inference_detector(model, img)
# visualize the results in a new window
show_result(img, result, model.CLASSES)
# or save the visualization results to image files
show_result(img, result, model.CLASSES, out_file='result.jpg')
"""



# test a video and show the results
video = mmcv.VideoReader(sys.argv[1])
for frame in video:
    result = inference_detector(model, frame)
    show_result(frame, result, model.CLASSES, wait_time=1)
