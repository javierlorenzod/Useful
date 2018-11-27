# Darknet related issues and solutions

1. **Use YOLO on folder**: In order use YOLOv3 detector (in this case) to process every image in an specific folder/path, do the following:
```bash
ls <folder-path>/*.* -d -1 | ./darknet detect cfg/yolov3.cfg yolov3.weights
```
