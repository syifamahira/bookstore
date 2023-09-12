
from django.test import TestCase, Client
from main import views

class AppTest(TestCase):
    def test_main_html_url_exists(self):
        response = Client().get('/')
        self.assertEqual(response.status_code, 200)
   
    def test_view_html(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'main.html')
