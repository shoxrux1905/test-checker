from django.contrib import admin

from apps.assignments.models import Question, Assignment, Group

admin.site.register(Question)
admin.site.register(Assignment)
admin.site.register(Group)