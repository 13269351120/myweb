from django.contrib import admin

# Register your models here.


from .models import Post  

class PostAdmin(admin.ModelAdmin):
	list_display = ('pub_date','testname','parameters','user','state')

admin.site.register(Post , PostAdmin)

