from fastapi import FastAPI, BackgroundTasks, UploadFile, File, Form
from starlette.responses import JSONResponse
from starlette.requests import Request
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pydantic import BaseModel, EmailStr
from typing import List


conf = ConnectionConfig(
    MAIL_USERNAME='ibshittu01@students.unilorin.edu.ng',
    MAIL_PASSWORD='goatheadman',
    MAIL_FROM="mail@oneshot.io",
    MAIL_PORT=587,
    MAIL_SERVER='smtp.gmail.com',
    MAIL_TLS=True,
    MAIL_SSL=False,
    USE_CREDENTIALS=True,
    # VALIDATE_CERTS=False
)


async def send(email, token) -> JSONResponse:

    template = f"""
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
            <div style=" display: flex; align-items: center; justify-content: center; flex-direction: column;">
                <h3> password reset email </h3>
                <br>
                <p>Thanks for choosing OneShot, please 
                click on the link below to verify your account</p> 
                <a style="margin-top:1rem; padding: 1rem; border-radius: 0.5rem; font-size: 1rem; text-decoration: none; background: #0275d8; color: white;"
                 href="http://localhost:8000/reset-password?token={token}">
                    Verify your email
                <a>
                <p style="margin-top:1rem;">If you did not register for OneShot, 
                please kindly ignore this email and nothing will happen. Thanks<p>
            </div>
        </body>
        </html>
    """

    message = MessageSchema(
        subject="OneShot Password recorvery",
        # List of recipients, as many as you can pass
        recipients=[email],
        body=template,
        subtype="html"
    )

    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})


async def send_new_account_mail(email: str, full_name: str):
    full_name = full_name
    template = f"""
        <!DOCTYPE html>
        <html>
        <head>
        </head>
        <body>
            <div style=" display: flex; align-items: center; justify-content: center; flex-direction: column;">
                <h3> Welcome to OneShot - The contest platform, {full_name}  </h3>
                <br>
                <p>Thanks for choosing OneShot, please 
                click on the link below to visit OneShot</p> 
                <a style="margin-top:1rem; padding: 1rem; border-radius: 0.5rem; font-size: 1rem; text-decoration: none; background: #0275d8; color: white;"
                 href="http://localhost:8000/">
                    OneShot
                <a>
                <p style="margin-top:1rem;">Welcome to OneShot - The contest platform  <p>
            </div>
        </body>
        </html>
    """

    message = MessageSchema(
        subject="Welcome to OneShot",
        # List of recipients, as many as you can pass
        recipients=[email],
        body=template,
        subtype="html"
    )
    fm = FastMail(conf)
    await fm.send_message(message)
    return JSONResponse(status_code=200, content={"message": "email has been sent"})
