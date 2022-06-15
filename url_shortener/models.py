import random
import string
from django.db import models
from django.contrib.auth.models import User

class Url(models.Model):
    short_url = models.SlugField(max_length=15, blank=True, primary_key=True)
    long_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    valid_until = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='urls')
    
    def save(self, *args, **kwargs):
        if not self.short_url:
            self.short_url = self.generate_short_url()
        super().save(*args, **kwargs)
    
    def generate_short_url(self):
        return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))
    
    def __str__(self):
        return self.short_url