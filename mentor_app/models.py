from django.db import models
from django.utils.text import slugify

# Create your models here.
class Mentor(models.Model):
    name = models.CharField(max_length=100)
    expertise = models.CharField(max_length=200)
    experience = models.IntegerField()
    email = models.EmailField(unique=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='mentors/', null=True, blank=True)
    social_twitter = models.URLField(max_length=200, blank=True)
    social_facebook = models.URLField(max_length=200, blank=True)
    social_instagram = models.URLField(max_length=200, blank=True)
    social_linkedin = models.URLField(max_length=200, blank=True)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Course(models.Model):
    CATEGORY_CHOICES = [
        ('web_dev', 'Web Development'),
        ('mobile_dev', 'Mobile Development'),
        ('data_science', 'Data Science'),
        ('design', 'Design'),
        ('marketing', 'Marketing'),
        ('business', 'Business'),
    ]
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE, related_name='courses')
    image = models.ImageField(upload_to='courses/', null=True, blank=True)
    duration = models.IntegerField(help_text='Duration in weeks')
    students_enrolled = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0.0)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateTimeField()
    location = models.CharField(max_length=200)
    image = models.ImageField(upload_to='events/', null=True, blank=True)
    max_participants = models.IntegerField()
    current_participants = models.IntegerField(default=0)
    mentors = models.ManyToManyField(Mentor, related_name='events')
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to='testimonials/', null=True, blank=True)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.company}"

class Newsletter(models.Model):
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
