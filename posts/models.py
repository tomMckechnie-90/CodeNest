from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from cloudinary.models import CloudinaryField
from cloudinary import CloudinaryImage

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

# The post model
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts', default=1)
    content = models.TextField()
    image = CloudinaryField('image', default='default-post_e4kyej', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    excerpt = models.TextField(blank=True)
    likes = models.ManyToManyField(User, related_name='liked_posts') # this will track the likes

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:  # Generate slug only if it doesn't exist
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.title} | written by {self.author}"
    
    def total_likes(self):
        return self.likes.count() # A helper method to count the total number of likes for a post.
    
    def get_image_url(self):
        # Return the correct URL for the image, whether it's Cloudinary or default
        if isinstance(self.image, str):
            return CloudinaryImage(self.image).build_url()
        elif self.image:
            return self.image.url
        else:
            return CloudinaryImage('default-post_e4kyej').build_url()


# The comments model

class Comment (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    approved = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return f"Comment by {self.user.username} on {self.post.title}"