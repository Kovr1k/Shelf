from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from .models import *
from django.views.generic import UpdateView
from transliterate import translit, get_available_language_codes
from django.db.models import Q
from accounts.models import UserData
from .forms import *

    # Получение ID пользователя
    # current_user = request.user
    # print (current_user.id)


class MainNull(View):
    def get(self, request):
        filter = 'New'
        return redirect('main', filter)
    def post(self, request):
        filter = 'New'
        return redirect('main', filter)

class Main(View):
    def get(self, request, filter):
        if request.user.is_authenticated:
            filter = str(filter)
            autors = User.objects.all()
            likes = LikeBook.objects.all()
            bookList = Book.objects.none()

            genres = {}
            for item in BookGenres.objects.all(): 
                genres.update({translit(item.name, 'ru', reversed=True): item.name})

            if(filter == "Popular"):
                bookList = Book.objects.all()
                bookList = sorted(bookList, key=lambda likes: likes.like.count())
                bookList = list(reversed(bookList))
            elif(filter == "New"):
                bookList = Book.objects.order_by('-dateOfPublication')
            else:
                for key, value in genres.items():
                    if(filter == key):
                        for obj in (Book.objects.all()):
                            for el in obj.bookGenres.all():
                                if str(el.name) == str(value):
                                    bookList |= Book.objects.filter(name=obj)
                        bookList = sorted(bookList, key=lambda likes: likes.like.count())
                        bookList = list(reversed(bookList))                           
            
            
            allАilters = []
            for item in genres.keys():
                allАilters.append(item)
            allАilters.extend(['Popular', 'New', 'Search'])
            if(filter not in allАilters):
                return HttpResponse("Не найдено")
            

            query = self.request.GET.get('q')
            if(query != None):
                filter='Search'
                queryList = query.split()
                for item in queryList:
                    bookList |= Book.objects.filter(
                    Q(name__icontains = str(item)) | Q(autor__first_name__icontains = str(item)))
                bookList = sorted(bookList, key=lambda likes: likes.like.count())
                bookList = list(reversed(bookList))   
            
            data = {
                'bookList': bookList,
                'autors': autors,
                'likes': likes,
                'genres': genres,
            }
            return render(request, "main/main.html", data)
        else:
            return redirect('login')
    def post(self, request):
        return render(request, "main/main.html")
    
class BookPage(View):
    def get(self, request, id):
        id = int(id)
        current_user = request.user
        book = Book.objects.get(id=id)
        bookChapters = BookСhapter.objects.filter(book=id)
        bookChapters = sorted(bookChapters, key=lambda bookChapters: bookChapters.number)
        commentsBook = СommentBook.objects.filter(book=id)
        btnValueFalse = ""
        if book.published == False:
            btnValueFalse = "Опубиковать"
        elif book.published == True:
            btnValueFalse = "Снять с публикации"
        form = createChapterForm()
        formComment = commentBookForm()
        formUpdateBook = bookForm(instance=book)

        data = {
            'book':book,
            'bookChapters':bookChapters,
            'current_user': current_user,
            'btnValueFalse': btnValueFalse,
            'form': form,
            'formComment': formComment,
            'commentsBook': commentsBook,
            'formUpdateBook': formUpdateBook,
        }
        return render(request, "main/book.html", data)
    def post(self, request, id):
        id = int(id)
        current_user = request.user
        book = Book.objects.get(id=id)
        bookChapters = BookСhapter.objects.filter(book=id)
        if book.published == False:
            btnValueFalse = "Опубиковать"
        elif book.published == True:
            btnValueFalse = "Снять с публикации"

        form = bookForm()

        if 'public' in request.POST:
            if request.method =='POST':
                form = bookPublishedBtn(request.POST)
                if form.is_valid():
                    if book.published == False:
                        book.published = True
                    elif book.published == True:
                        book.published = False
                    book.save()
                    return redirect('book', id=id)    
            form = bookPublishedBtn()
        elif 'likeBookBtn' in request.POST:
            if request.method =='POST':
                if LikeBook.objects.filter(book=book, user=current_user).exists() == True:
                    LikeBook.objects.get(book=book, user=current_user).delete()
                    return redirect('book', id=id)
                elif LikeBook.objects.filter(book=book, user=current_user).exists() == False:
                    LikeBook.objects.create(book=book, user=current_user)
                    return redirect('book', id=id)
        elif 'comment' in request.POST:
            if request.method =='POST':
                form = commentBookForm(request.POST)
                if form.is_valid():  
                    form.instance.book = book
                    form.instance.user = current_user
                    form.save()
                    return redirect('book', id=id)
                form = commentBookForm()
        elif 'updateBook' in request.POST:
            if request.method =='POST':
                form = bookForm(request.POST, request.FILES, instance=book)
                print('123')
                if form.is_valid():
                    print('Сработало')
                    form.save()
                    return redirect('book', id=book.id)
        elif 'deleteBook' in request.POST:
            if request.method =='POST':
                    Book.objects.get(id=book.id).delete()
                    return redirect('main', filter='New')
        
        data = {
            'book':book,
            'bookChapters':bookChapters,
            'current_user': current_user,
            'form': form,
            'btnValueFalse': btnValueFalse,
        }
        return render(request, "main/book.html", data)
    
class CreateChapter(View):
    def get(self, request, bookId):
        form = createChapterForm()


        data = {
            'form': form,
        }
        return render(request, "main/createChapter.html", data)
    def post(self, request, bookId):
        bookChapters = BookСhapter.objects.filter(book=bookId)

        if request.method =='POST':
            form = createChapterForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.book = Book.objects.get(id=bookId)
                number = len(bookChapters) + 1
                form.instance.number = number
                form.save()
                return redirect('book', id=bookId)
            form = createChapterForm()

        data = {
            'form': form,
        }
        return render(request, "main/createChapter.html", data)
    
class UpdateChapter(View):
    def get(self, request, bookId, chapterId):
        chapter = BookСhapter.objects.get(id=chapterId, book=bookId)
        form = createChapterForm(instance=chapter)


        data = {
            'form': form,
            'chapter': chapter,
        }
        return render(request, "main/updateChapter.html", data)
    def post(self, request, bookId, chapterId):
        bookChapters = BookСhapter.objects.filter(book=bookId)
        chapter = BookСhapter.objects.get(id=chapterId, book=bookId)
        number = chapter.number
        if request.method =='POST':
            form = createChapterForm(request.POST, request.FILES, instance=chapter)
            if form.is_valid():
                form.instance.book = Book.objects.get(id=bookId)
                form.save()
                chapter.number = number
                chapter.save()
                return redirect('book', id=bookId)

        data = {
            'chapter': chapter,
            'form': form,
        }
        return render(request, "main/updateChapter.html", data)
    
class DeleteChapter(View):
    def get(self, request, bookId, chapterId):
        chapterToDelete = BookСhapter.objects.get(id = chapterId, book=bookId)
        if chapterToDelete.book.autor == request.user:
            chapterList = BookСhapter.objects.filter(book=bookId)
            chapterList = sorted(chapterList, key=lambda chapterList: chapterList.number)
            indexDeleteEl = chapterList.index(BookСhapter.objects.get(id = chapterId, book=bookId))
            listAfterIndexDeleteEl = chapterList[indexDeleteEl:]
            i = len(listAfterIndexDeleteEl) - 1
            while i > 0:  
                if listAfterIndexDeleteEl[i] != chapterToDelete:
                    listAfterIndexDeleteEl[i].number = listAfterIndexDeleteEl[i - 1].number
                i -= 1
            
            for el in listAfterIndexDeleteEl:
                for obj in chapterList:
                    if el == obj:
                        obj = el
                        obj.save()
         
            BookСhapter.objects.get(id = chapterId, book=bookId).delete()
        return redirect('book', id=bookId)
    def post(self, request, bookId, chapterId):
        return redirect('book', id=bookId)
    
class CreateBook(View):
    def get(self, request):
        list = Book.objects.all()
        if request.method =='GET':
            form = bookForm(request.GET, request.FILES)
            if form.is_valid():
                form.save()
                return redirect('profile', filter='Drafts')
        
        form = bookForm()
        data = {
            'list': list,
            'form': form,
        }
        return render(request, "main/createBook.html", data)
    def post(self, request):
        list = Book.objects.all()
        if request.method =='POST':
            form = bookForm(request.POST, request.FILES)
            if form.is_valid():
                form.instance.autor = request.user
                form.save()
                return redirect('profile', filter='Drafts')
        
        form = bookForm()
        data = {
            'list': list,
            'form': form,
        }
        return render(request, "main/createBook.html", data)
    
