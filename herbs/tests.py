# from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import TestCase

from .models import Herbs
class SpicesTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="test@email.com",
            password="secret",
        )
        cls.herb = Herbs.objects.create(
            author=cls.user,
            title="A good title",
            image = "https://marketplace.canva.com/EAE8vy3ug1o/1/0/1600w/canva-good-morning-instagram-post-vD94ud4DLAU.jpg",
            body="Nice body content",
            notes = "These are some notes"
        )


    def test_herb_model(self):
        self.assertEqual(self.herb.author.username, "testuser")
        self.assertEqual(self.herb.title, "A good title")
        self.assertEqual(self.herb.image, "https://marketplace.canva.com/EAE8vy3ug1o/1/0/1600w/canva-good-morning-instagram-post-vD94ud4DLAU.jpg")
        self.assertEqual(self.herb.body, "Nice body content")
        self.assertEqual(self.herb.notes, "These are some notes")
        self.assertEqual(str(self.herb), "A good title")

# Create your tests here.
