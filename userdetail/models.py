from django.db import models
from django.conf import settings
# Create your models here.

User = settings.AUTH_USER_MODEL


class Detail(models.Model):
    avatar = models.ImageField(
        upload_to='avatar/', default='avatar/no-img.jpg')
    user = models.OneToOneField(
        User, verbose_name="detail", on_delete=models.CASCADE)
