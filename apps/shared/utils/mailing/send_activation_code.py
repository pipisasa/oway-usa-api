from django.template.loader import render_to_string

from apps.shared.mails.mail_helpers import send_mail
from apps.users.models import User


def send_activation_code(user: User):
    activation_code = user.activation_code

    context = {
        "activation_code": activation_code
    }

    message = render_to_string('mailing/send_activation_code.html', context)
    send_mail(
        subject="Новый активационный код/New activation code",
        message=message,
        recipient_list=[user.email]
    )