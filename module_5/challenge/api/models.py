from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator


LEVEL_CHOICES = [
    ('CRITICAL', 'CRITICAL'),
    ('DEBUG', 'DEBUG'),
    ('WARNING', 'WARNING'),
    ('INFO', 'INFO'),
]


class User(models.Model):
  name = models.CharField(max_length=50)
  last_login = models.DateTimeField(auto_now_add=True)
  email = models.EmailField(validators=[EmailValidator()])
  password = models.CharField(max_length=50,
                              validators=[MinLengthValidator(8)])

class Agent(models.Model):
  name = models.CharField(max_length=50)
  status = models.BooleanField()
  env = models.CharField(max_length=20)
  version = models.CharField(max_length=5)
  address = models.GenericIPAddressField(protocol='IPv4')


class Event(models.Model):
  level = models.CharField(max_length=20, choices=LEVEL_CHOICES)
  data = models.TextField()
  arquivado = models.BooleanField()
  date = models.DateField(auto_now_add=True)
  agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)


class Group(models.Model):
  name = models.CharField(max_length=50)


class GroupUser(models.Model):
  group = models.ForeignKey(Group, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
