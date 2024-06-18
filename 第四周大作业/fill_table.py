# -*- coding: utf-8 -*-
import json
import os
from connect_database import session_scope
from data_model import DataInfo
from datetime import datetime

# 1. get json data structure

basic_path = 'single-vehicle-side-example/'

def load_json(json_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data_list = json.load(file)
        return data_list
    
data_info_path = 'single-vehicle-side-example/data_info.json'

def find_highest_precision(number):
    highest_precision = 0
    
    
    str_number = str(number)
        
    # find the position of .
    dot_position = str_number.find('.')
    
    # if has point
    if dot_position != -1:
        return dot_position
        '''
        # calculate numbers after point
        precision = len(str_number) - dot_position - 1
            
        # update
        highest_precision = max(highest_precision, precision)
        '''
    return 0
    #return highest_precision


data_list = load_json(data_info_path)
maxx = 0
number = 0
with session_scope() as session:
    
    for entry in data_list:
        # get basic infomation
        d1 = DataInfo()
        d1.image_path = entry.get('image_path')
        d1.image_id = d1.image_path[6:12]
        d1.image_timestamp =  datetime.fromtimestamp(int(entry.get('image_timestamp')) / 1000000)
            
        d1.pointcloud_path = entry.get('pointcloud_path')
        d1.point_cloud_stamp =  datetime.fromtimestamp(int(entry.get('point_cloud_stamp')) / 1000000)
        
        d1.calib_camera_intrinsic_path = entry.get('calib_camera_intrinsic_path')
        d1.calib_lidar_to_camera_path = entry.get('calib_lidar_to_camera_path')
        d1.label_camera_std_path = entry.get('label_camera_std_path')
        d1.label_lidar_std_path = entry.get('label_lidar_std_path')
        
        
        # get information from path
        #pointcloud_path  size 
        d1.velodyne_size = os.path.getsize(os.path.join(basic_path + d1.pointcloud_path))
        
        # calib_camera_intrinsic_path  cam_D cam_K
        calib_camera_path = os.path.join(basic_path + d1.calib_camera_intrinsic_path)
        intrinsic = load_json(calib_camera_path)
        d1.camera_intrinsic_cam_D = intrinsic["cam_D"]
        d1.camera_intrinsic_cam_K = intrinsic["cam_K"]
        
        # calib_lidar_to_camera_path rotation translation
        calib_lidar_path = os.path.join(basic_path + d1.calib_lidar_to_camera_path)
        lidar_to_camera = load_json(calib_lidar_path)
        d1.lidar_to_camera_rotation = lidar_to_camera["rotation"]
        d1.lidar_to_camera_translation = lidar_to_camera["translation"]
        
        # label_camera_std_path  json 
        label_camera_path = os.path.join(basic_path + d1.label_camera_std_path)
        label_camera =load_json(label_camera_path)[0]
        d1.label_camera_type = label_camera["type"]
        d1.label_camera_occluded_state = label_camera["occluded_state"]
        d1.label_camera_truncated_state = label_camera["truncated_state"]
        d1.label_camera_alpha = label_camera["alpha"]
        d1.label_camera_2d_box = label_camera["2d_box"]
        d1.label_camera_3d_dimensions = label_camera["3d_dimensions"]
        d1.label_camera_3d_location = label_camera["3d_location"]
        d1.label_camera_rotation = label_camera["rotation"]
    
        # label_lidar_std_path  json 
        label_lidar_path = os.path.join(basic_path + d1.label_lidar_std_path)
        label_lidar = load_json(label_lidar_path)[0]
        
        d1.label_lidar_type = label_lidar["type"]
        d1.label_lidar_occluded_state = label_lidar["occluded_state"]
        d1.label_lidar_truncated_state = label_lidar["truncated_state"]
        d1.label_lidar_alpha = label_lidar["alpha"]
        d1.label_lidar_2d_box = label_lidar["2d_box"]
        d1.label_lidar_3d_dimensions = label_lidar["3d_dimensions"]
        d1.label_lidar_3d_location = label_lidar["3d_location"]
        d1.label_lidar_rotation = label_lidar["rotation"]
        '''
        if(find_highest_precision(d1.label_lidar_rotation) > maxx):
            maxx = find_highest_precision(d1.label_lidar_rotation)
            number = d1.label_lidar_rotation
        elif(find_highest_precision(d1.label_camera_rotation) > maxx):
            maxx = find_highest_precision(d1.label_camera_rotation)
            number = d1.label_camera_rotation
        '''
        session.add(d1)
    
print(maxx) 
print(number)   
