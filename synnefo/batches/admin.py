from django.contrib import admin
from.models import * 
# Register your models here.

class Department_display(admin.ModelAdmin):
    list_display=['dept']
  
class Batch_display(admin.ModelAdmin):
    list_display=['bach']

class Teacher_display(admin.ModelAdmin):
    list_display=['name','dept']

class Student_display(admin.ModelAdmin):
    list_display=['sname','bach','teacher']

admin.site.register(Department,Department_display)  
admin.site.register(Batch,Batch_display)
admin.site.register(Teacher,Teacher_display)
admin.site.register(Student,Student_display)

