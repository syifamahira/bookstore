
from django.test import TestCase, Client
from main import views

class AppTest(TestCase):
    def test_main_html_url_exists(self):
        response = Client().get('/main/html/')
        self.assertEqual(response.status_code, 404)
    def test_mainlist_xml_url_exists(self):
        response = Client().get('/main/xml/')
        self.assertEqual(response.status_code, 404)
    def test_main_json_url_exists(self):
        response = Client().get('/main/json/')
        self.assertEqual(response.status_code, 404)
    def test_view_html(self):
        response = Client().get('/')
        self.assertTemplateUsed(response, 'main.html')
