from fastapi import FastAPI, BackgroundTasks
from schemas import EmailAsyncIn, EmailBackIn, EmailCeleryIn
from send_mail import send_email_async, send_email_background, send_email_celery

app = FastAPI()

@app.post('/send-email/asynchronous')
async def send_email_asynchronous(data: EmailAsyncIn):
    subject = data.subject
    email_to = data.email_to
    body = {
        "title": data.body_title,
        "name": data.body_name
    }
    await send_email_async(subject, email_to, body)
    return "Success -> Mail sent!"

@app.post('/send-email/backgroundtasks')
def send_email_background_tasks(background_task: BackgroundTasks, data: EmailBackIn):
    subject = data.subject
    email_to = data.email_to
    body = {
        'title': data.body_title,
        'name': data.body_name
    }
    send_email_background(background_task, subject, email_to, body)
    return "Success -> Mail will be sent in background!"

@app.post('/send-email/celery')
def send_email_celery_redis(data: EmailCeleryIn):
    subject = data.subject
    email_to = data.email_to
    body = {
        "title": data.body_title,
        "name": data.body_name
    }
    send_email_celery.delay(subject, email_to, body)
    return "Success -> Mail will be sent with Celery using Redis!"