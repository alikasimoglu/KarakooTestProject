from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import get_object_or_404

from accounts.models import Customer
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


@receiver(post_save, sender=Customer)
def is_registred(sender, instance, **kwargs):
    company = Company.objects.get(company_email=instance.profile.email)
    if instance.profile.email == company.company_email:
        company.is_registered = 1
        company.save()
