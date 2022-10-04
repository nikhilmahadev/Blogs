import html

from django.db import models
from django.utils.html import format_html
# from tinymce.models import HTMLField
#  importing for displaying the image on the admin category

# Create your models here.

 #category model

class Category(models.Model):
    cat_id=models.AutoField(primary_key=True) #cat_id as primary key for Category model
    title=models.CharField(max_length=100) #category title
    description=models.TextField() #conatins description of category
    url=models.CharField(max_length=100) #url for the category
    image=models.ImageField(upload_to='category/') #image for the category
    add_date=models.DateTimeField(auto_now_add=True,null=True) #creation date-time of category is auto added
                                                         #date_time can also be null


# to show the image in the category table
    def image_tag(self):
        return format_html('<img src="/media/{}" style="width:40px; height:40px; border-radius:50%;" />'.format(self.image))



# to show the cat options for filter in the post table
    def __str__(self):
        return self.title
#post model

class Post(models.Model):
    post_id= models.AutoField(primary_key=True)  # post_id as primary key for Post model
    title = models.CharField(max_length=100)  # Post title
    content = models.TextField()  # HTMLField() tinymce editor for writing content
    # models.TextField() basic editor  contains Content of post
    url = models.CharField(max_length=100)  # url for the post
    cat=models.ForeignKey(Category,on_delete=models.CASCADE) #deletes the post if the post category is deleted
    image = models.ImageField(upload_to='post/')  # image for the post

