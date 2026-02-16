from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    phone=models.CharField(max_length=200)

class Questions(models.Model):

    user=models.ForeignKey(User,on_delete=models.CASCADE)

    created_at=models.DateTimeField(auto_now_add=True)

    query=models.TextField()  


    def __str__(self):
        return self.query
    
class Answers(models.Model):

    query=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name="answers")#to get all answers

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="answers")

    created_at=models.DateTimeField(auto_now_add=True)

    solution=models.TextField()

    def __str__(self):
        return self.solution
    

class UpVote(models.Model):

    solution=models.ForeignKey(Answers,on_delete=models.CASCADE,related_name="upvotes")

    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="upvotes")

    query=models.ForeignKey(Questions,on_delete=models.CASCADE,related_name="upvotes")

    created_at=models.DateTimeField(auto_now_add=True)