from django.shortcuts import render, redirect, HttpResponse
from django.views.generic.base import View
from .models import *
from .forms import *
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from main.models import BookGenres, Book, LikeBook
from django.db.models import F
from django.contrib.auth import logout

class ProfileNull(View):
    def get(self, request):
        filter = 'Written'
        return redirect('profile', filter)
    def post(self, request):
        filter = 'Written'
        return redirect('profile', filter)

class Profile(View):
    def get(self, request, filter):
        if request.user.is_authenticated:
            current_user = request.user
            bookList = Book.objects.none()
            emptyText = ''
            if filter == 'Written':
                userBooks = Book.objects.filter(autor=current_user, published=True)
                bookList = userBooks.order_by('-dateOfPublication')
                emptyText = 'Здесь ещё ничего нет. <a href=\"/New/\">Напишешь?</a>'
            elif filter == 'Drafts':
                userBooks = Book.objects.filter(autor=current_user, published=False)
                bookList = userBooks.order_by('-dateOfPublication')
                emptyText = 'Здесь ещё ничего нет. <a href=\"/New/\">Напишешь?</a>'
            elif filter == 'Liked':
                likeList = LikeBook.objects.filter(user=current_user)
                for item in likeList:
                    likedBook = Book.objects.filter(name=item.book)
                    bookList |= likedBook
                emptyText = 'Ты ничего не лайкнул:( Вперёд <a href=\"/New/\">читать!</a>'

            userProfile = UserData.objects.filter(user=current_user)   
            
            allАilters = ['Written', 'Drafts', 'Liked']
            if(filter not in allАilters):
                return HttpResponse("Не найдено")

            userUpdate = UserData.objects.get(user=current_user)
            form = updateUserDataForm(instance=userUpdate)

            data={
                'userProfile' : userProfile,
                'bookList': bookList,
                'emptyText': emptyText,
                'form': form,
                'userUpdate': userUpdate,
            }
            return render(request, "registration/profile.html", data)
        else:
            return redirect('login')
    def post(self, request, filter):
        current_user = request.user
        userUpdate = UserData.objects.get(user=current_user)
        filter = 'Written'

        if request.method =='POST':
            form = updateUserDataForm(request.POST, request.FILES, instance=userUpdate)
            if form.is_valid():
                form.save()
                return redirect('profile', filter=filter)

        data={
                'form': form,
                'userUpdate': userUpdate,
            }
        return render(request, "registration/profile.html", data)

class ProfileAnyUser(View):
    def get(self, request, id, filter):
        if request.user.is_authenticated:
            current_user = request.user
            bookList = Book.objects.none()
            emptyText = ''
            idUserPage = [id]
            userProfile = UserData.objects.filter(user=id)

            if str(current_user.id) == str(id):
                filter = 'Written'
                return redirect('profile', filter)

            if filter == 'Written':
                userBooks = Book.objects.filter(autor=id, published=True)
                bookList = userBooks.order_by('-dateOfPublication')
                emptyText = 'Пользователь ещё ничего не опубликовал.'
            elif filter == 'Liked':
                if userProfile[0].showLikedBooks == True:          
                    likeList = LikeBook.objects.filter(user=id)
                    for item in likeList:
                        likedBook = Book.objects.filter(name=item.book)
                        bookList |= likedBook
                    emptyText = 'Пользователь ничего не лайкнул.'
                else:
                    emptyText = 'Пользователь скрыл список понравившихся книг.'



            allАilters = ['Written', 'Liked']
            if(filter not in allАilters):
                return HttpResponse("Не найдено")

            data={
                'userProfile' : userProfile,
                'bookList': bookList,
                'emptyText': emptyText,
                'idUserPage': idUserPage,
            }
            return render(request, "registration/profileAnyUser.html", data)
        else:
            return redirect('login')
    def post(self, request, id, filter):
        return redirect('profileNull')

class Register(View):
    def get(self, request):
        list = User.objects.all()
        if request.method =='GET':
            form = registerForm()    
        data = {
            'list': list,
            'form': form,
        }
        return render(request, "registration/register.html", data)
    def post(self, request):
        list = User.objects.all()
        if request.method =='POST':
            form = registerForm(request.POST)
            if form.is_valid():
                form.save()
                user = User.objects.get(username = str(form.cleaned_data['username']))
                group = Group.objects.get(name='regular')
                user.groups.add(group)
                UserData.objects.create(user=user)
                return redirect('login')
        else:
            form = registerForm()
        
        
        data = {
            'list': list,
            'form': form,
        }
        return render(request, "registration/register.html", data)
    
def logout_view(request):
    logout(request)
    return redirect('login')