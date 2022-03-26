from django.db import models
class Car(models.Model):
    tarihSaat = models.DateTimeField(verbose_name='Tarih ve Saat')
    Latitude = models.FloatField(verbose_name='Enlem')
    Longitude = models.FloatField(verbose_name='Boylam')
    VehicleID = models.IntegerField(verbose_name='Arac ID')
    UserID = models.IntegerField(verbose_name='Kullanıcı ID')

    def __str__(self):
        return f'{self.id}'

