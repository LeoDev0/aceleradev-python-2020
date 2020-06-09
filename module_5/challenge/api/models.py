from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator
from django.core.exceptions import ValidationError


def levelValidator(level):
  level = level.upper()
  if level not in ['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']:
    raise ValidationError('Level must be CRITICAL, DEBUG, ERROR, WARNING or INFO')


class User(models.Model):
  name = models.CharField(max_length=50)
  last_login = models.DateTimeField(auto_now_add=True)
  email = models.EmailField(validators=[EmailValidator()])
  password = models.CharField(max_length=50,
                              validators=[MinLengthValidator(
                                8,
                                "Password must be at least 8 characters long"
                              )])


class Agent(models.Model):
  name = models.CharField(max_length=50)
  status = models.BooleanField()
  env = models.CharField(max_length=20)
  version = models.CharField(max_length=5)
  address = models.GenericIPAddressField(protocol='IPv4')


class Event(models.Model):
  level = models.CharField(max_length=20, validators=[levelValidator])
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
