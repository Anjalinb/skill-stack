from django.db import models
from programs.models import Course
from accounts.models import User

class Module(models.Model):

    title=models.CharField(max_length=200)

    course=models.ForeignKey(Course,on_delete=models.CASCADE)

    description=models.TextField()

    created_at=models.DateTimeField(auto_now_add=True)

    updated_at=models.DateTimeField(auto_now=True)

    trainer=models.ForeignKey(User,on_delete=models.CASCADE)

    module_no=models.PositiveIntegerField(default=0)


    def __str__(self):

        return self.title

    def save(self,*args,**kwargs):

        last_module_obj=Module.objects.filter(course=self.course).last()

        if last_module_obj:

            self.module_no=last_module_obj.module_no+1

        else:
            self.module_no=1

        return super().save(*args,**kwargs)