from django.contrib import admin
from .models import Category, Post



#for configuring categories in admin

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('image_tag','title','description','url','add_date')
    search_fields = ('title',)

#for configuring POST in admin

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 5 # list 5  no: of posts at a time

    class Media:
        js= ('https://cdn.tiny.cloud/1/no-api-key/tinymce/6/tinymce.min.js','js/script.js',)



# Register your models here.


admin.site.register(Category,CategoryAdmin)
# need to declare the classes/models associated
admin.site.register(Post,PostAdmin)





