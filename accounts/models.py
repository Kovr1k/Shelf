from django.db import models
from django.contrib.auth.models import User
from main.models import BookGenres

    
class UserData(models.Model):
    VK = models.CharField("VK", max_length=50, default='', blank=True)
    Instagram = models.CharField("Instagram", max_length=50, default='', blank=True)
    Telegram = models.CharField("Telegram", max_length=50, default='', blank=True)
    AboutMe = models.TextField("О себе", max_length=700, default='', blank=True)
    bookGenres = models.ManyToManyField(BookGenres, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    photo = models.ImageField("Аватар", upload_to='photos', blank=True)
    showLikedBooks = models.BooleanField(default=False)

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.user}'