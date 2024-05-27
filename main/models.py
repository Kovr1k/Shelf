from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class BookGenres(models.Model):
    name = models.CharField("Название жанра", max_length=100, default='')

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.name}'

class Book(models.Model):
    name = models.CharField("Название", max_length=100, default='')
    bookGenres = models.ManyToManyField(BookGenres)
    dateOfPublication = models.DateField("Дата публикации", null=True, blank=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    cover = models.ImageField("Обложка", upload_to='covers', blank=True)
    description = models.TextField("Описание", max_length=3500, default="")
    ageLimit = models.IntegerField("Возрастное ограничение", default=16, blank=True, null=True)
    published = models.BooleanField(default=False)
    shortDescription = models.TextField("Краткое описание сюжета", max_length=550, default="")
    topic = models.CharField("Тематика", max_length=80, default='', blank=True)

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.name}'
    
class BookСhapter(models.Model):
    name = models.CharField("Название", max_length=100, default='')
    screensaver = models.ImageField("Заставка", upload_to='screensavers', blank=True)
    number = models.IntegerField("Номер главы в книге", blank=True, null=True)
    text = models.TextField("Текст главы", blank=True)
    book = models.ForeignKey("Book", on_delete=models.CASCADE, null=True, blank=True)

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.name}'
    
class LikeBook(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, null=True, related_name="like")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.user} {self.book}'
    
class СommentBook(models.Model):
    book = models.ForeignKey("Book", on_delete=models.CASCADE, null=True, blank=True, related_name="comment")
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(max_length=300, blank=True, null=True)
    date = models.DateTimeField("Дата и время публикации", null=True, blank=True, default=timezone.now)

    def get_absolute_url(self):
        return f'/'

    def __str__(self):
        return f'{self.user} {self.book}'