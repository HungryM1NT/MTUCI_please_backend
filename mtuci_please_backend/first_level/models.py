from django.db import models


class Person(models.Model):

    class Gender(models.TextChoices):
        MAN = 'М', 'Мужчина'
        WOMAN = 'Ж', 'Женщина'

    photo = models.FileField(upload_to='persons_images')
    surname = models.CharField(max_length=128)
    name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    gender = models.CharField(max_length=10,
                              choices=Gender.choices,
                              default=Gender.MAN)

    def __str__(self):
        return f'{self.surname} {self.name} {self.middle_name}'