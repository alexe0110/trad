import smtplib
from email.message import EmailMessage

from celery import Celery

from src.config import SMTP_PASS, SMTP_USER

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 465

celery = Celery("tasks", broker="redis://localhost:6379")


def get_email_template_dashbord(username: str) -> EmailMessage:
    email = EmailMessage()
    email["Subject"] = "Натрейдил Отчет Дашборд"
    email["From"] = SMTP_USER
    email["To"] = "alexe0110@ya.ru"

    email.set_content(
        "<div>"
        f'<h1 style="color: red;">Здравствуйте, {username}, а вот и ваш отчет. Зацените 😊</h1>'
        '<img src="https://static.vecteezy.com/system/resources/previews/008/295/031/original/custom-relationship'
        "-management-dashboard-ui-design-template-suitable-designing-application-for-android-and-ios-clean-style-app"
        '-mobile-free-vector.jpg" width="600">'
        "</div>",
        subtype="html",
    )
    return email


@celery.task()
def send_email_report_dashboard(username: str) -> None:
    email = get_email_template_dashbord(username)
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASS)
        server.send_message(email)
