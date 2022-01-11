import hashlib
from .utils import send_transaction
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
from django.utils import timezone


# Creo il modello User aggiungendo un campo per l'IP e la funzione write_on_chain per attribuire hash e txid al post

class User(AbstractUser):
    pass
    ip = models.GenericIPAddressField(null=True)


# Creo il modello per la pubblicazione dei Post

class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE)
    title = models.CharField(max_length=200, default="", editable=True)
    datetime = models.DateTimeField(auto_now_add=True)
    created_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    published_date = models.DateTimeField(blank=True, null=True)
    hash = models.CharField(max_length=32, default=None, null=True)
    txId = models.CharField(max_length=66, default=None, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    def write_on_chain(self):
        self.hash = hashlib.sha256(self.content.encode('utf-8')).hexdigest()
        self.txId = send_transaction(self.hash)
        self.save()
