from django.db import models
from django.db.models import signals
from django.db.models.signals import pre_save,post_save,pre_delete,post_delete
from django.dispatch import receiver

# Create your models here.
class Author(models.Model):
    name=models.CharField(max_length=255)
    
    
class Book(models.Model):
    title=models.CharField(max_length=255)
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    
class RelatedRecord(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    info=models.CharField(max_length=255)

@receiver(post_save,sender=Book)
def create_related_user(sender,instance,created,**kwargs):
     if created:
         print(f"Creating related record for book: {instance.title}")
        # Attempt to create a record in a related table
         RelatedRecord.objects.create(book=instance, info="Some info")
    
