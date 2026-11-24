from django.db import models
from accounts.models import User

class Course(models.Model):

    LANGUAGE_CHOICES=[
        ('python','python'),
        ('c','c'),
        ('java','java'),
    ]

    title=models.CharField(max_length=200)

    description=models.TextField()

    fee=models.PositiveIntegerField()

    duration=models.CharField(max_length=200)

    language=models.CharField(max_length=200,choices=LANGUAGE_CHOICES)

    trainer=models.ForeignKey(User,on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)

    cover_pic=models.ImageField(upload_to="cover_pics",null=True)

    def __str__(self):

        return self.title
