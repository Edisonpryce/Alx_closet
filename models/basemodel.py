from datetime import datetime
from uuid import uuid4

class BaseModel:
    def __int__(self):
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
