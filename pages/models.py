from django.db import models

# Create your models here.
# NEW: This is your Project model
# NEW: This is your Experience model
#Data Structure for Models & step 1

class Experience(models.Model):
    job_title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    duration = models.CharField(max_length=50) # Example: "Jan 2023 - Present"
    description = models.TextField()

    def __str__(self):
        return self.job_title
    
class Hero(models.Model):
    name = models.CharField(max_length=100)
    welcome_text = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name
    
class About(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100, default="Tech") # e.g., Python, Crypto, NYSC
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    content = models.TextField()

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.name} on {self.post.title}"
    
    
class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name} - {self.subject}"
    
    
class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100) # e.g., CEO, Tech Lead, Client
    quote = models.TextField()
    image = models.ImageField(upload_to='testimonials/', blank=True, null=True)
    stars = models.IntegerField(default=5) # 1 to 5 stars

    def __str__(self):
        return f"{self.name} - {self.role}"
    
    
class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100) # e.g., Founder & Lead Developer
    image = models.ImageField(upload_to='team/')
    twitter = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    
class Project(models.Model):
    CATEGORY_CHOICES = [
        ('app', 'App'),
        ('product', 'Product'),
        ('branding', 'Branding'),
        ('books', 'Books'),
    ]
    
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='app')
    image = models.ImageField(upload_to='portfolio/')
    link = models.URLField(blank=True, null=True) # Link to GitHub or Live site
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title