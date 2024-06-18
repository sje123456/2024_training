from fastapi import FastAPI, HTTPException
from starlette.responses import FileResponse
from pydantic import BaseModel
from connect_database import session_scope
from data_model import DataInfo
import os
import uvicorn

app = FastAPI(title = "image_id query")


@app.get("/api/image/{image_id}")
async def read_image_data(image_id: str):
    with session_scope() as session:
        image_id = image_id.zfill(6)
        data = session.query(DataInfo).filter(DataInfo.image_id == image_id).first()
        if data is None:
            raise HTTPException(status_code=404, detail="Image not found")
        
        download_url = f"http://localhost:8000/static/image/{data.image_id}.jpg"
        response = {
            "image_id": data.image_id,
            "image_url" : download_url,
            #calib
            "camera_intrinsic":
            {
                "cam_D": data.camera_intrinsic_cam_D,
                "cam_K": data.camera_intrinsic_cam_K,
            },
            "lidar_to_camera":
            {
                "rotation": data.lidar_to_camera_rotation,
                "translation": data.lidar_to_camera_translation,
            },
            
            #lidar
            "label_lidar" : [
                {
                    "type": data.label_lidar_type,
                    "occluded_state": data.label_lidar_occluded_state,
                    "truncated_state": data.label_lidar_truncated_state,
                    "alpha": data.label_lidar_alpha,
                    "2d_box": data.label_lidar_2d_box,
                    "3d_dimensions": data.label_lidar_3d_dimensions,
                    "3d_location": data.label_lidar_3d_location,
                    "rotation": data.label_lidar_rotation
                }
            ]
        }
    
        return response

@app.get("/static/image/{image_name}.jpg")
async def static_file(image_name: str):
    image_path = '/home/sss/data_cleaning/single-vehicle-side-example/image/' + image_name +'.jpg'
    
    if not os.path.exists(image_path):
       raise HTTPException(status_code=404, detail="Image not found")
   
    response = FileResponse(image_path, media_type="image/jpeg")
    response.headers["Content-Disposition"] = "attachment; image_name=" + image_name
    return response

if __name__ == '__main__':
    #注意，run的第一个参数 必须是文件名:应用程序名
    uvicorn.run("query:app", port=8000,  reload=True)