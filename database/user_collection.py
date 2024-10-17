from core import DATABASE
from pydantic import BaseModel

user_collection = DATABASE["user_collection"]

# 
class User(BaseModel):

    user_id: str
    user_name: str
    user_email: str
    meeting_id: str

# 
def push_data(user_id: str, user_email: str, meeting_id: str):

    data = User(
        user_id=user_id,
        user_email=user_email,
        meeting_id=meeting_id
    )

    user_collection.insert_one(data.dict())
    return {"message": "Data uploaded successfully!"}