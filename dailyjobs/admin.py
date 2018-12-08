from django.contrib import admin

# Register your models here.


from .models import Dailyjobs  

class DailyjobsAdmin(admin.ModelAdmin):
	list_display = ('pub_date','testname','parameters','user','state')

admin.site.register(Dailyjobs , DailyjobsAdmin)

