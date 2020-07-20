from django.core.mail import send_mail
from colector.models import Emails, Error, Station


def sendn(st):
    mails_list = list(Emails.objects.filter(station=st))
    error_msg = str(Error.objects.all().order_by('-id')[0])
    delivered = send_mail('Wash Tek Report ' + str(st),
                          error_msg,
                          'service@5minutes-bg.com',
                          mails_list,
                          fail_silently=False, )
    print(delivered)
    return error_msg
