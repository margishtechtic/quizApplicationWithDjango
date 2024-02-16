from django.forms import ModelForm
from .models import Recruitment_teams
from .models import Exams  ,Students ,Questions
from django import forms

class Recruitment_teams_form(ModelForm):
    class Meta:
        model = Recruitment_teams
        fields = '__all__'


class Exams_form(ModelForm):
    class Meta:
        model = Exams
        fields = '__all__'


class Students_form(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'


# class Students_Results_form(ModelForm):
#     class Meta:
#         model = Students_Results
#         fields = '__all__'



class Questions_form(ModelForm):
    class Meta:
        model = Questions
        fields = '__all__'



# class Attempts_log_form(ModelForm):
#     class Meta:
#         model = Attempts_log
#         fields = '__all__'