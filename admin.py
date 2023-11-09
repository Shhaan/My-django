from django.contrib import admin
from .models import team,book
# Register your models here.
admin.site.register(team)
class booking(admin.ModelAdmin):
    list_display = ('id','F_name' ,'S_name','phone', 'team1', 'team2' , 'date')
admin.site.register(book,booking)

