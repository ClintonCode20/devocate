from django.contrib import admin
from .models import Advocate, Link, Company
# Register your models here.

admin.site.register([Advocate, Link, Company])