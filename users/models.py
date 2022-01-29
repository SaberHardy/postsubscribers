from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', default='default.png',
                              validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return self.user.username
