from utils import create_summary, create_todolist
from core import DATABASE
from pydantic import BaseModel

meeting_collection = DATABASE["meeting_collection"]

# 
class Meeting(BaseModel):
    meeting_id: str
    meeting_title: str
    meeting_start_time: str
    meeting_content: str
    summary_content: str
    todo_list: str

# 
def push_data(meeting_id: str, meeting_title: str, meeting_start_time: str, meeting_content: str):

    summary_content = create_summary(meeting_content)
    todo_list = create_todolist(meeting_content)

    data = Meeting(
        meeting_id=meeting_id,
        meeting_title=meeting_title,
        meeting_start_time=meeting_start_time,
        meeting_content=meeting_content,
        summary_content=summary_content,
        todo_list=todo_list
    )

    meeting_collection.insert_one(data.dict())
    return {"message": "Data uploaded successfully!"}