from django.contrib import admin
from .models import Mentor, Mentee, Topic, Mentor_Topic

# Register your models here.
admin.site.register(Mentor)
admin.site.register(Mentee)
admin.site.register(Topic)
admin.site.register(Mentor_Topic)
