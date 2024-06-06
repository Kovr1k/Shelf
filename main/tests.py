from django.test import TestCase
from .models import *

class SimpleTests(TestCase):
    def setUp(self):
        # Настройка контекста для тестов
        User.objects.create(username='Test', password='123456')

    def test_home_page_status_code(self):
        # Тест на доступность главной страницы
        response = self.client.get('/', follow=True)
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        # Тест на использование правильного шаблона
        response = self.client.get('/books/createBook/')
        self.assertTemplateUsed(response, 'main/createBook.html')

    def test_home_page_does_not_contain_incorrect_html(self):
        # Тест на отсутствие неправильного HTML на главной странице
        response = self.client.get('/New/', follow=True)
        self.assertNotContains(response, 'Пидор')