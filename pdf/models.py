from django.db import models

class Common(models.Model):
     year1=models.IntegerField()
     file1=models.FileField('Image_view',upload_to="image",default="")

##highschool
class Highschool(Common):
    sub=models.CharField(max_length=34)

#statelevel
class Statelevel(Common):
    exam=models.CharField(max_length=45)

###india
class India(Common):
    exam1=models.CharField(max_length=34)

##quiz general ques.
class Genquiz(models.Model):
    ques=models.CharField(max_length=100)
    op1=models.CharField(max_length=90)
    op2 = models.CharField(max_length=90)
    op3 = models.CharField(max_length=90)
    op4 = models.CharField(max_length=90)
    correct = models.CharField(max_length=90)

#Constitu
class Scc(models.Model):
    ques=models.CharField(max_length=100)
    op1=models.CharField(max_length=90)
    op2 = models.CharField(max_length=90)
    op3 = models.CharField(max_length=90)
    op4 = models.CharField(max_length=90)
    correct = models.CharField(max_length=90)

####Blog post
class Blogpost(models.Model):
    img = models.ImageField(upload_to="blog_post")
    title = models.CharField(max_length=60)
    dec = models.TextField(max_length=1000)
    cat = models.CharField(max_length=30)

