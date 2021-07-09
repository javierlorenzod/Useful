"""
Quick & dirty script used to launch PifPaf over all subfolders inside a folder. It saves the keypoints estimated in a subfolder for each sequence. 

Notice that it is quite hardcoded and it could be deprecated since the last activity of this script is on 2019/10/17.

You need to install loguru (a predefined logger, quite useful) and openpifpaf, in order to call it with system externally.
"""
import argparse
import glob
import os
from loguru import logger  # pip install loguru

parser = argparse.ArgumentParser(description='PifPaf processing of dataset')
parser.add_argument('-dstd', '--dataset_dir', type=str, required=True)
parser.add_argument('-kpsd', '--keypoints_dir', type=str, required=True)
parser.add_argument('-bid', '--begin_index', type=int, required=False, default=0)

args = parser.parse_args()

frames_directory = args.dataset_dir
kps_dir = args.keypoints_dir
beginning_index = args.begin_index
for i, j in enumerate(sorted(glob.glob(f"{frames_directory}*/"))):
    if i < beginning_index:
        logger.warning(f"Video {i:04d} processed")
        continue
    output_folder = f"{kps_dir}video_{i:04d}/"
    os.makedirs(output_folder)
    logger.info(f"Processing video {i:04d}")
    os.system(f"python -m openpifpaf.predict {j}*.png --output-directory {output_folder} --output-types json --checkpoint resnet152")
