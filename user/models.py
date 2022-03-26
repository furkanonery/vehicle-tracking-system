from datetime import timedelta
from django.db import models

# Create your models here.

class GirisZamanlari(models.Model):
    tarihSaat = models.DateTimeField(verbose_name='Tarih ve Saat')
    kullaniciAdi = models.CharField(max_length=50,verbose_name='Kullanıcı Adı')

    def __str__(self):
        return f'{self.kullaniciAdi} {self.tarihSaat+timedelta(hours=3)}'

class CikisZamanlari(models.Model):
    tarihSaat = models.DateTimeField(verbose_name='Tarih ve Saat')
    kullaniciAdi = models.CharField(max_length=50,verbose_name='Kullanıcı Adı')

    def __str__(self):
        return f'{self.kullaniciAdi} {self.tarihSaat+timedelta(hours=3)}'
