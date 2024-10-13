from django.contrib import admin
from app.models import Author,Book,RelatedRecord

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(RelatedRecord)