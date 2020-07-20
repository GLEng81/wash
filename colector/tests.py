#from django.test import TestCase
from background_task import background
from django.core.mail import send_mail
from colector.models import Error


@background(schedule=10)
def notify_someone():
    send_mail(
        'Subject',
        'Msg body',
        'serveice@5minutes-bg.com',
        ['lambrev@gmail.com'],
        fail_silently=False,
    )


notify_someone(repeat=10, repeat_until=None)

