from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from PIL import Image

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_on = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(blank=True, editable=False)
    image = models.ImageField(default='not_approved.jpg', upload_to='post_images', null=True)

    def __str__(self):
        return self.title + str(self.image)

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __unicode__(self):
        return self.title




    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 800 or img.width > 800:
            output_size = (640, 480)
            img.thumbnail(output_size)
            img.save(self.image.path)



class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.TextField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)


    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        # return self.text
        return 'Comment {} by {}'.format(self.text, self.author)

