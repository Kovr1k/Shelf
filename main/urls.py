from django.urls import path, include
from .views import *

urlpatterns = [
    path("", MainNull.as_view(), name="mainNull"),
    path("<filter>/", Main.as_view(), name="main"),
    path("book/<id>/", BookPage.as_view(), name="book"),
    path("books/createBook/", CreateBook.as_view(), name="createBook"),
    path("book/<bookId>/createChapter", CreateChapter.as_view(), name="createChapter"),
    path("book/<bookId>/<chapterId>/updateChapter", UpdateChapter.as_view(), name="updateChapter"),
    path("book/<bookId>/<chapterId>/deleteChapter", DeleteChapter.as_view(), name="deleteChapter"),
]