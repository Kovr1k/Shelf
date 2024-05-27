from .models import *
from accounts.models import UserData
from django.forms import ModelForm, TextInput, ModelChoiceField, Select, DateInput, CharField, IntegerField, ImageField, Textarea

class bookForm(ModelForm): 
    class Meta:
        model = Book
        fields = ['name', 'bookGenres', 'cover', 'description', 'shortDescription', 'topic']

        widgets = {
            
        }
    def __init__(self, *args, **kwargs):
        super(bookForm, self).__init__(*args, **kwargs)
        self.fields['shortDescription'].widget = Textarea(attrs={
            'id': 'shortDescription',})

class bookPublishedBtn(ModelForm): 
    class Meta:
        model = Book
        fields = ['published']

        widgets = {

        }

class createChapterForm(ModelForm): 
    class Meta:
        model = BookСhapter
        fields = ['name', 'screensaver', 'text', 'number', 'book']

        widgets = {

        }

class commentBookForm(ModelForm): 
    class Meta:
        model = СommentBook
        fields = ['text', 'book', 'user']

        widgets = {

        }