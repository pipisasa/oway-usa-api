from typing import List, Dict

from django.core import mail

from otaku_api import settings


def send_mail(
    subject: str,
    message: str,
    recipient_list: List[str],
    email_account: Dict[str, str] = settings.EMAIL_ACCOUNTS['base'],
):
    username = email_account["EMAIL_USER"]
    mail.send_mail(
        subject=subject,
        message=message,
        from_email=username,
        recipient_list=recipient_list,
        auth_user=username,
        auth_password=email_account["EMAIL_PASSWORD"],
        html_message=message
    )
