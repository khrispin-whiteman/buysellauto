from django.core.mail import send_mail
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from tinymce.models import HTMLField

from BuySellAuto import settings
from store.models import User


class AgentType(models.Model):
    agent_type = models.CharField('Agent Type', max_length=200)

    def __str__(self):
        return self.agent_type

    class Meta:
        verbose_name_plural = 'Agent Types'
        verbose_name = 'Agent Type'


class Agent(models.Model):
    is_agent_model = models.BooleanField(default=True, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField('Company Name', max_length=200, default='N/A')
    agent_type = models.ForeignKey(AgentType, default='', on_delete=models.CASCADE)
    experience = models.CharField('Experiance', max_length=200, default='')
    # about = HTMLField(help_text='About me...', default='')
    description = HTMLField(help_text='Services offered...')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name_plural = 'Agents'
        verbose_name = 'Agent'

    # @receiver(post_save, sender=User)
    # def update_user_profile(sender, instance, created, **kwargs):
    #     if created:
    #         Profile.objects.create(user=instance)
    #     instance.profile.save()

    @receiver(post_save, sender=User)
    def create_or_update_user_profile(sender, instance, created, **kwargs):
        global emails
        if created:
            # send email to admin of new account created
            subject = 'Account Created!'
            message = 'Hi %s, Welcome! Thank you registering as an agent with Buy and Sell Auto. ' % (instance.first_name)
            from_email = settings.EMAIL_HOST_USER
            send_mail(subject, message, from_email, recipient_list=['khrispinwhiteman@gmail.com', instance.email],
                      fail_silently=True)
