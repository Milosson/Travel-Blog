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
