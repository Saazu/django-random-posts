from django.test import Client, TestCase
from django.urls import reverse
from .models import Post
from django.contrib.messages import get_messages


class PostTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.home_url = reverse("home")
        self.success_url = reverse("success")

    def test_home_view(self):
        response = self.client.get(self.home_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home.html")

    def test_success_view_with_no_posts(self):
        response = self.client.get(self.success_url)
        self.assertEqual(response.status_code, 200)
        messages = list(get_messages(response.wsgi_request))
        self.assertEqual(len(messages), 1)
        self.assertEqual(str(messages[0]), "No posts available yet.")
        self.assertTemplateUsed(response, "success.html")

    def test_success_view_with_posts(self):
        post = Post.objects.create(
            userId=1, title="Test Post", body="This is a test post."
        )
        response = self.client.get(self.success_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "success.html")
        self.assertContains(response, post.title)
        self.assertContains(response, post.body)

    def test_retrieve_post(self):
        response = self.client.post(self.home_url)
        self.assertRedirects(response, self.success_url)
        self.assertEqual(Post.objects.count(), 1)
