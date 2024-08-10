from django.db import models
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.
class Post(models.Model):
    """
    A model representing a blog post.

    Attributes:
        title (str): The title of the post.
        slug (str): A slugified version of the title, used for URLs.
        author (User): The author of the post, linked to the User model.
        content (str): The main content of the post.
        created_on (datetime): The date and time the post was created.
        status (int): The publication status of the post (0 for Draft, 1 for Published).
        excerpt (str): An optional short excerpt from the post.
    """
    def __str__(self):
        status_label = "Draft" if self.status == 0 else "Published"
        created_on_formatted = self.created_on.strftime('%Y-%m-%d %H:%M:%S')
        return f"The title of this post is: {self.title} > By Author : {self.author} > {status_label} > Created on: {created_on_formatted}"
    class Meta:
        ordering = ["-created_on"]
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    update_on = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    
    def __str__(self):
        created_on_formatted = self.created_on.strftime('%Y-%m-%d %H:%M:%S')
        return f"Comment {self.body} > By Author : {self.author} > Created on: {created_on_formatted}"
    
    class Meta:
        ordering = ["-created_on"]
        
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)
    