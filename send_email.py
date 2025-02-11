import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from dotenv import load_dotenv

PORT = 587
EMAIL_SERVER = "smtp.gmail.com"

# Loading environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

sender_email = "amithshinde23@gmail.com"
# password_email = "-----"
env_file_path = 'C:/Users/amith/Desktop/Projects/auomate_emails/.env'


def get_env_variable(env_file, variable_name):
    with open(env_file, 'r') as file:
        for line in file:
            name, value = line.strip().split('=', 1)
            if name == variable_name:
                return value


password_email = get_env_variable(env_file_path, "PASSWORD")


def send_email(subject, receiver_email, name, due_date, invoice_no, amount):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg["From"] = formataddr(("Sai Fibernet", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
        Hi {name},
        I just wanted to drop you a quick note to remind you that {amount} 
        To ensure uninterrupted access to your internet services and to avoid any service interruptions, we kindly request that you settle the outstanding amount by the due date."""
    )

    msg.add_alternative(
        f"""\
        <html>
        <body>
        <p>Hi {name},</p>
        <p>I just wanted to drop you a quick note to remind you that {amount}/-. </p>
        <p>To ensure uninterrupted access to your internet services and to avoid any service interruptions, we kindly request that you settle the outstanding amount by the due date.</p>
        <p>Best regards,</p>
        <p><b>Sai Fibernet</b></p>
        </body>
        </html>
        """,
        subtype="html",
    )

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    send_email(
        subject="Invoice Reminder",
        name="Amith Shinde",
        receiver_email="eng21cs0034@dsu.edu.in",
        due_date="11,Aug 2023",
        invoice_no="INV-2023",
        amount="50000",
    )
