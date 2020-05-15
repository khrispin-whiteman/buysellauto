from django.db import models

# Create your models here.
from tinymce.models import HTMLField

from store.models import User


class AgentType(models.Model):
    agent_type = models.CharField('Agent Type', max_length=200)

    def __str__(self):
        return self.agent_type

    class Meta:
        verbose_name_plural = 'Agent Types'
        verbose_name = 'Agent Type'


class Agent(models.Model):
    is_agent_model = models.BooleanField(default=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    company_name = models.CharField('Company Name', max_length=200, default='N/A')
    agent_type = models.ForeignKey(AgentType, default='', on_delete=models.CASCADE)
    experience = models.CharField('Experiance', max_length=200, default='')
    #about = HTMLField(help_text='About me...', default='')
    description = HTMLField(help_text='Services offered...')

    def __str__(self):
        return self.user.get_full_name()

    class Meta:
        verbose_name_plural = 'Agents'
        verbose_name = 'Agent'