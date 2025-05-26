from pydantic import BaseModel, EmailStr

class EmailBase(BaseModel):
    email_to: EmailStr = "codeblinders5@gmail.com"
    body_title: str = "Jinja Template"
    body_name: str = "Tanishqua Bansal"

class EmailAsyncIn(EmailBase):
    subject: str = "Email from FastAPI Asynchronous"
    
class EmailBackIn(EmailBase):
    subject: str = "Email from FastAPI Background"

class EmailCeleryIn(EmailBase):
    subject: str = "Email from FastAPI Celery"