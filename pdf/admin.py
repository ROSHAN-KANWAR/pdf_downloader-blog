from django.contrib import admin
from .models import Highschool,Statelevel,India,Genquiz,Scc,Blogpost
##highscgool
@admin.register(Highschool)
class HighAdmin(admin.ModelAdmin):
    list_display = ['id','sub','file1','year1']

##statelevel

@admin.register(Statelevel)
class StatelevelAdmin(admin.ModelAdmin):
    list_display = ['id','exam','file1','year1']

##india
@admin.register(India)
class IndiaAdmin(admin.ModelAdmin):
    list_display = ['id','exam1','file1','year1']


###quiz general
@admin.register(Genquiz)
class GeneralAdmin(admin.ModelAdmin):
   list_display = ['id','ques','op1','op2','op3','op4','correct']

##Sccques
@admin.register(Scc)
class SccAdmin(admin.ModelAdmin):
   list_display = ['id','ques','op1','op2','op3','op4','correct']

##blogpost
@admin.register(Blogpost)
class BlogpostAdmin(admin.ModelAdmin):
    list_display = ['id','img','title','dec','cat']
