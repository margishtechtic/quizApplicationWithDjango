from django.contrib import admin

# Register your models here.
from .models import Recruitment_teams ,Exams, Students , Questions , Students_Results , Attemps_log

admin.site.register(Recruitment_teams)
admin.site.register(Exams)
admin.site.register(Students)
admin.site.register(Questions)
admin.site.register(Students_Results)
admin.site.register(Attemps_log)