from fastapi import APIRouter, File, UploadFile
from database import push_meeting_data, push_user_data
from utils import extract_text_from_txt
import os

router = APIRouter()

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@router.post("/push_data/")
def push_data(file: UploadFile = File(...), meeting_id: str = None, meeting_start_time: str = None, user_email: str = None):

    with open(f"{UPLOAD_FOLDER}/{file.filename}", "wb") as buffer:
        buffer.write(file.file.read())
    
    file = f"{UPLOAD_FOLDER}/{file.filename}"

    content = extract_text_from_txt(file)
    user_id = user_email.split("@")[0]

    push_meeting_data(meeting_id=meeting_id, meeting_title=file.filename, meeting_start_time=meeting_start_time, meeting_content=content)
    push_user_data(user_id=user_id, user_email=user_email, meeting_id=meeting_id)

    return {"message": "Data pushed successfully!"}