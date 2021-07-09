"""
Written on 2019/10/17. Maybe nuscenes API has changed a lot.
"""

from nuscenes.nuscenes import NuScenes
from nuscenes.map_expansion.map_api import NuscenesMap
import pickle
import os
from loguru import logger  # pip install loguru
import argparse

parser = argparse.ArgumentParser(description="Nuscenes reader which filters categories and logs the number of sequences containing that categories. It saves the processed nuscenes in a pickle file in order to save time on the same execution.")
parser.add_argument('-ndr', '--nuscenes-data-rootcene', type=str, required=True)
parser.add_argument('-nout', '--nuscenes-out-file', type=str, required=False, default='nuscenes.pkl')
parser.add_argument('-c', '--categories', nargs="+", default=['human.pedestrian.adult', 'human.pedestrian.police_officer', 'human.pedestrian.construction_worker'])
args = parser.parse_args()

nuscenes_output_file = args.nuscenes_out_file
nusc_map_bos = NuscenesMap(dataroot=args.nuscenes_data_rootcene, map_name='boston-seaport')

if not os.path.isfile(nuscenes_output_file):
    nusc = NuScenes(version='v1.0-trainval', dataroot=args.nuscenes_data_rootcene)
    with open(nuscenes_output_file, 'wb') as output:
        pickle.dump(nusc, output, pickle.HIGHEST_PROTOCOL)
else:
    with open(nuscenes_output_file, 'rb') as input:
        nusc = pickle.load(input)

categories = args.categories
valid_scenes = []
for scene_number, scene in enumerate(nusc.scene):
    logger.info(f"Checking scene {scene_number} with token {scene['token']}")
    token = scene['first_sample_token']
    is_valid_scene = False
    while token != '' and is_valid_scene is False:
        sample = nusc.get('sample', token)
        for ann in sample['anns']:
            ann_rec = nusc.get('sample_annotation', ann)
            inst_rec = nusc.get('instance', ann_rec['instance_token'])
            cat_rec = nusc.get('category', inst_rec['category_token'])
            if any(cat_rec['name'] == category for category in categories):
                is_valid_scene = True
                valid_scenes.append(scene_number)
                logger.info(f"Scene {scene_number} contains pedestrians")
                break
        token = sample['next']
logger.info(f"{len(valid_scenes)} / {len(nusc.scene)} sequences with pedestrians")
