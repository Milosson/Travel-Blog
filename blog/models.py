from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


STATUS = ((0, "Draft"), (1, "Published"))

class Post(models.Model):
    """
    A model representing a blog post.
    """

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)  

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        status_label = "Draft" if self.status == 0 else "Published"
        created_on_formatted = self.created_on.strftime('%Y-%m-%d %H:%M:%S')
        return f"The title of this post is: {self.title} > By Author : {self.author} > {status_label} > Created on: {created_on_formatted}"

class Comment(models.Model):
    """
    A model representing a comment on a blog post.
    """

    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter"
    )
    body = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        created_on_formatted = self.created_on.strftime('%Y-%m-%d %H:%M:%S')
        return f"Comment {self.body} > By Author : {self.author} > Created on: {created_on_formatted}"
