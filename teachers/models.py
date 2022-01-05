from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Teacher(models.Model):
    user = models.OneToOneField(User, related_name="teacher", on_delete=models.CASCADE)
    avatar = models.ImageField("profil rasmi", upload_to='profile_images/', null=True, blank=True)
    class_name = models.CharField("sinfi", max_length=50, blank=True)
    info = models.TextField("Ma'lumot", blank=True)
    image = models.ImageField("Rasmi", upload_to='teacher_images/', null=True, blank=True)

    def __str__(self):
        return str(self.user.username)

@receiver(post_save, sender=User)
def user_created(sender, instance, created, *args, **kargs):
    if created:
        Teacher.objects.create(user=instance)
    else:
        pass


class BrithDays(models.Model):
    name = models.CharField("Ismi", max_length=150)
    day = models.DateField("Tugilgan kuni")
    image = models.ImageField("Rasmi", upload_to="birday_user/", blank=True)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField("Ismi", max_length=50)
    surname = models.CharField("Familiyasi", max_length=50)
    tel_number = models.PositiveIntegerField("telfon")

    def __str__(self):
        return f"{self.name}, {self.surname}"