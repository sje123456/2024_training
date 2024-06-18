- data_example:
"image_id":"000000"
"image_path": "image/000000.jpg",
"image_timestamp": "1604988999001000",
"pointcloud_path": "velodyne/000000.pcd",
"point_cloud_stamp": "1604988999006000",
"calib_camera_intrinsic_path": "calib/camera_intrinsic/000000.json",
"calib_lidar_to_camera_path": "calib/lidar_to_camera/000000.json",
"label_camera_std_path": "label/camera/000000.json",
"label_lidar_std_path": "label/lidar/000000.json"
"label_camera_type": "Car",
"label_camera_occluded_state": 0,
"label_camera_truncated_state": 0,
"label_camera_alpha": 0.338885815438449,
"label_camera_2d_box_xmin": 0,
"label_camera_2d_box_ymin": 527.938232,
"label_camera_2d_box_xmax": 69.723068,
"label_camera_2d_box_ymax": 637.4556269999999
"label_camera_3d_dimensions_h":0.850836 
"label_camera_3d_dimensions_w": 2.073565
"label_camera_3d_dimensions_l": 4.337498
"label_camera_3d_location_x": 32.83248
"label_camera_3d_location_y": 9.513366
"label_camera_3d_location_z": -1.261215
"label_camera_rotation": -1.615145
"label_lidar_type": "Car",
"label_lidar_occluded_state": 0,
"label_lidar_truncated_state": 0,
"label_lidar_alpha": 0.3092128173071816,
"label_lidar_2d_box_xmin": 0,
"label_lidar_2d_box_ymin": 527.938232,
"label_lidar_2d_box_xmax": 69.723068,
"label_lidar_2d_box_ymax": 637.4556269999999
"label_lidar_3d_dimensions_h": 2.036748 
"label_lidar_3d_dimensions_w": 2.073565
"label_lidar_3d_dimensions_l": 4.252306
"label_lidar_3d_location_x": 32.84116
"label_lidar_3d_location_y": 9.75075
"label_lidar_3d_location_z": -1.040589
"label_lidar_rotation": -1.578873
"camera_intrinsic_cam_D":[ -0.382041,0.335649,0.000523,0.000634,0.0],
"camera_intrinsic_cam_K":[3996.487567,0.0,955.58618,0.0,3963.430994,527.646219,0.0, 0.0,1.0]
"lidar_to_camera_rotation": [[ 0.006283,-0.999979,-0.001899],[    -0.005334, 0.001865, -0.999984],[ 0.999966,0.006293,-0.005322]],
"lidar_to_camera_translation": [[ -0.298036],[-0.666812],[ -0.516927]]
"velodyne_size":3.73 MB


- create_table_sql
CREATE TABLE data_info (
    image_id VARCHAR(255) PRIMARY KEY,
    image_path VARCHAR(255),
    image_timestamp BIGINT,
    pointcloud_path VARCHAR(255),
    point_cloud_stamp BIGINT,
    calib_camera_intrinsic_path VARCHAR(255),
    calib_lidar_to_camera_path VARCHAR(255),
    label_camera_std_path VARCHAR(255),
    label_lidar_std_path VARCHAR(255),
    label_camera_type VARCHAR(255),
    label_camera_occluded_state TINYINT,
    label_camera_truncated_state TINYINT,
    label_camera_alpha FLOAT,
    label_camera_2d_box_xmin FLOAT,
    label_camera_2d_box_ymin FLOAT,
    label_camera_2d_box_xmax FLOAT,
    label_camera_2d_box_ymax FLOAT,
    label_camera_3d_dimensions_h FLOAT,
    label_camera_3d_dimensions_w FLOAT,
    label_camera_3d_dimensions_l FLOAT,
    label_camera_3d_location_x FLOAT,
    label_camera_3d_location_y FLOAT,
    label_camera_3d_location_z FLOAT,
    label_camera_rotation FLOAT,
    label_lidar_type VARCHAR(255),
    label_lidar_occluded_state TINYINT,
    label_lidar_truncated_state TINYINT,
    label_lidar_alpha FLOAT,
    label_lidar_2d_box_xmin FLOAT,
    label_lidar_2d_box_ymin FLOAT,
    label_lidar_2d_box_xmax FLOAT,
    label_lidar_2d_box_ymax FLOAT,
    label_lidar_3d_dimensions_h FLOAT,
    label_lidar_3d_dimensions_w FLOAT,
    label_lidar_3d_dimensions_l FLOAT,
    label_lidar_3d_location_x FLOAT,
    label_lidar_3d_location_y FLOAT,
    label_lidar_3d_location_z FLOAT,
    label_lidar_rotation FLOAT,
    camera_intrinsic_cam_D JSON,
    camera_intrinsic_cam_K JSON,
    lidar_to_camera_rotation JSON,
    lidar_to_camera_translation JSON,
    velodyne_size VARCHAR(255)
);
