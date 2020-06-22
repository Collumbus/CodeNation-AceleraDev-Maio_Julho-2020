from django.db import models


class User(models.Model):
    name = models.CharField('Name', max_length=50)
    last_login = models.DateField('Last Login', auto_now=True)
    email = models.EmailField('E-mail', max_length=254)
    password = models.CharField('Password', max_length=50)


    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField(max_length=50)
    status = models.BooleanField(default=False)
    env = models.CharField(max_length=20)
    version = models.CharField(max_length=5)
    address = models.GenericIPAddressField(protocol="IPV4", default="0.0.0.0")

    def __str__(self):
        return self.name


class Event(models.Model):
    level = models.CharField(max_length=20)
    data = models.TextField()
    arquivado = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)
    agent = models.ForeignKey(Agent, on_delete=models.deletion.CASCADE)
    user = models.ForeignKey(User, on_delete=models.deletion.CASCADE)

    def __str__(self):
        return self.level


class Group(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    group = models.OneToOneField(Group, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
