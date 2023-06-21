from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Car
# Create your tests here.

class GamesTest(TestCase):

    def setUp(self):
        self.purchaser = get_user_model().objects.create(username="tester",password="tester")
        self.Game = Car.objects.create(name="tester", purchaser=self.purchaser, price=2,desc='abs')

    def test_home_page_status(self):
        url = reverse('cars_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code,200)

    def test_home_page_response(self):
        url = reverse('cars_list')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'cars/cars-list.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_home_page_context(self):
        url = reverse('cars_list')
        response = self.client.get(url)
        game_list = response.context['Car']
        self.assertEqual(len(game_list), 1)
        self.assertEqual(game_list[0].name, "tester")
        self.assertEqual(game_list[0].price,2)
        self.assertEqual(game_list[0].purchaser.username, "tester")
        self.assertEqual(game_list[0].desc, "abs")
        

    def test_detail_page_status_code(self):
        url = reverse('cars_detail',args=(1,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_detail_page_template(self):
        url = reverse('cars_detail',args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'cars/cars-detail.html')
        self.assertTemplateUsed(response, '_base.html')

    def test_detail_page_context(self):
        url = reverse('cars_detail',args=(1,))
        response = self.client.get(url)
        game_detail = response.context['car']
        self.assertEqual(game_detail.name, "tester")
        self.assertEqual(game_detail.price,2)
        self.assertEqual(game_detail.purchaser.username, "tester")
        self.assertEqual(game_detail.desc, "abs")
        

    
    def test_create_view(self):
        obj={
            'name':"test2",
            'purchaser':self.purchaser.id,
            'price': 2,
            'desc' :"abs"
        }

        url = reverse('cars_create')
        response = self.client.post(path=url,data=obj,follow=True)
        self.assertEqual(len(Car.objects.all()),2)
        # self.assertRedirects(response, reverse('cars_list'))

    def test_update_view(self):
        obj={
            'name':"test2",
            'purchaser':self.purchaser.id,
            'price': 2,
            'desc' :"abs"
        }

        url = reverse('cars_update', args=(1,))
        response = self.client.post(path=url,data=obj,follow=True)
        # self.assertEqual(len(Game.objects.all()),2)
        self.assertRedirects(response, reverse('cars_list'))

    
    def test_delete_view(self):
       

        url = reverse('cars_delete', args=(1,))
        response = self.client.post(path=url,follow=True)
        # self.assertEqual(len(Game.objects.all()),0)
        self.assertRedirects(response, reverse('cars_list'))


    def test_str_method(self):
        self.assertEqual(str(self.Game),"tester")


    def test_create_response(self):
        url = reverse('cars_create')
        response = self.client.get(url)
        self.assertTemplateUsed(response,'cars/cars-create.html')
        self.assertTemplateUsed(response, '_base.html')


    def test_update_response(self):
        url = reverse('cars_update', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response,'cars/cars-update.html')
        self.assertTemplateUsed(response, '_base.html')


    def test_delete_response(self):
        url = reverse('cars_delete', args=(1,))
        response = self.client.get(url)
        self.assertTemplateUsed(response,'cars/cars-delete.html')
        self.assertTemplateUsed(response, '_base.html')