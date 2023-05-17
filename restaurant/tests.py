from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from .models import Menu
class MenuTest (TestCase):
    def test_get_item(self) :
        item = Menu.objects.create(id=5 ,title = "Pizza", price = 2.0, inventory = 10)
        itemstr = item.get_item()
        self.assertEqual(itemstr,"Pizza : 2.0")