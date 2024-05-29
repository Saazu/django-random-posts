import requests
from django.shortcuts import redirect, render
from .models import Post
import random


def homeview(request):
    random_post_id = random.randint(1, 100)
    if request.method == "POST":
        response = requests.get(
            f"https://jsonplaceholder.typicode.com/posts/{random_post_id}"
        )
        post_data = response.json()
        Post.objects.create(
            userId=post_data["userId"], title=post_data["title"], body=post_data["body"]
        )
        return redirect("success")
    return render(request, "home.html")


def successview(request):
    posts = Post.objects.all()
    return render(request, "success.html", {"posts": posts})
