import requests
from django.shortcuts import redirect, render
from .models import Post
from django.contrib import messages
import random


def homeview(request):
    random_post_id = random.randint(1, 100)
    if request.method == "POST":
        try:
            response = requests.get(
                f"https://jsonplaceholder.typicode.com/posts/{random_post_id}"
            )
            post_data = response.json()
            Post.objects.create(
                userId=post_data["userId"],
                title=post_data["title"],
                body=post_data["body"],
            )
            return redirect("success")
        except requests.exceptions.RequestException as e:
            messages.error(request, f"Error fetching post: {e}")
    return render(request, "home.html")


def successview(request):
    posts = Post.objects.all()
    if not posts:
        messages.info(request, "No posts available yet.")
    return render(request, "success.html", {"posts": posts})
