# SMTP simple mail transfer protocol
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


mensaje = MIMEMultipart()
mensaje["From"] = "hola mundo"
mensaje["To"] = "test@gmail.com"
mensaje["Subject"] = "Hola mundo"
cuerpo = MIMEText("Hola mundo")
mensaje.attach(cuerpo)

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("test@gmail.com", "password")
    smtp.send_message(mensaje)
    print("Correo enviado...")
