from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from mainsite.models import Company


@receiver(post_save, sender=Company)
def is_accepted(sender, instance, **kwargs):
    if instance.is_accepted == 1 and instance.is_email_sent == 0:
        try:
            send_mail(
                f'Registraion Invitation for {instance.company_email}',
                f'Please register yourself and your company in XYZ website via the following link http://127.0.0.1:8009/accounts/signup/customer/',
                'testcod77@gmail.com',
                [instance.company_email],
            )
            instance.is_email_sent = 1
            instance.save()

        except Exception as e:
            print(e)
