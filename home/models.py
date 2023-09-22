from django.db import models

# Create your models here.

class Services(models.Model):
    name = models.CharField(max_length=120)
    icon = models.FileField(upload_to='services/icons/')
    about = models.TextField()

    def __str__(self):
        return self.name

class Staff(models.Model):
    image = models.ImageField(upload_to='staff/images/')
    name = models.CharField(max_length=120)
    job = models.CharField(max_length=120)
    facebook_url = models.TextField(blank=True, null=True)
    twitter_url = models.TextField(blank=True, null=True)
    google_url = models.TextField(blank=True, null=True)
    linkedln_url = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name}-{self.job}"

class Blog(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateField()
    author = models.ForeignKey(Staff, on_delete=models.CASCADE)
    text = models.TextField()
    image = models.ImageField(upload_to='blog/images/')

    def __str__(self):
        return self.title

class Album(models.Model):
    name = models.CharField(max_length=95)
    hash_tag = models.CharField(max_length=80, blank=True, null=True)
    image = models.ImageField(upload_to='album/images/')

    def __str__(self):
        return self.name

class Message_to_Admin(models.Model):
    full_name = models.CharField(max_length=200)
    subject = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField()
    company_name = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f"From {self.full_name} to Admin new Message"
