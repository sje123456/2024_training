# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, Integer,  DateTime, Float, JSON, DECIMAL
from sqlalchemy.ext.declarative import declarative_base
from connect_database import engine

Base = declarative_base()

class DataInfo(Base):
    __tablename__ = 'data_info'
    
    image_id = Column(String(255), primary_key=True)
    image_path = Column(String(255))
    image_timestamp = Column(DateTime)
    pointcloud_path = Column(String(255))
    point_cloud_stamp = Column(DateTime)
    calib_lidar_to_camera_path = Column(String(255))
    label_camera_std_path = Column(String(255))
    label_lidar_std_path = Column(String(255))
    label_camera_type = Column(String(255))
    label_camera_occluded_state = Column(Integer)
    label_camera_truncated_state = Column(Integer)
    label_camera_alpha = Column(DECIMAL(21,19))
    label_camera_2d_box = Column(JSON)
    label_camera_3d_dimensions = Column(JSON)
    label_camera_3d_location = Column(JSON)
    label_camera_rotation = Column(DECIMAL(13,11))
    label_lidar_type = Column(String(255))
    label_lidar_occluded_state = Column(Integer)
    label_lidar_truncated_state = Column(Integer)
    label_lidar_alpha = Column(DECIMAL(21,19))
    label_lidar_2d_box = Column(JSON)
    label_lidar_3d_dimensions = Column(JSON)
    label_lidar_3d_location = Column(JSON)
    label_lidar_rotation = Column(DECIMAL(13,11))
    camera_intrinsic_cam_D = Column(JSON)
    camera_intrinsic_cam_K = Column(JSON)
    lidar_to_camera_rotation = Column(JSON)
    lidar_to_camera_translation = Column(JSON)
    velodyne_size = Column(String(255))
    
Base.metadata.drop_all(engine)    
Base.metadata.create_all(engine)

