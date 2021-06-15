from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack
# Create your tests here.
class SnacKTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
        username='tester',
        email='tester@test.com',
        password='test',
        )

        self.snack = Snack.objects.create(
        name='testsnack',
        purchaser = self.user,
        description = 'testing sanck',
        )

    def test_home(self):
        url = reverse('home')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'home.html')

    def test_snack_detail(self):
        url = reverse('snack_detail', args='1')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'snack_detail.html')

    def test_snack_create(self):
        url = reverse('snack_create')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'snack_create.html')

    def test_snack_update(self):
        url = reverse('snack_update', args='1')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'snack_update.html')

    def test_snack_delete(self):
        url = reverse('snack_delete', args='1')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'base.html')
        self.assertTemplateUsed(response, 'snack_delete.html')
