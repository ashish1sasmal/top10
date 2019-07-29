# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myapp.models import Employee

class EmployeeAdmin(admin.ModelAdmin):
	list_display=['id','eno','ename','esal','eaddr']

admin.site.register(Employee,EmployeeAdmin)