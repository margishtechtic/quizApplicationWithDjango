from django.forms import ModelForm
from .models import Recruitment_teams
from .models import Exams  ,Students ,Questions ,Attemps_log
from django import forms



class Recruitment_teams_form(ModelForm):
    class Meta:
        model = Recruitment_teams
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Recruitment_teams_form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label



class Exams_form(ModelForm):
    class Meta:
        model = Exams
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Exams_form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label


class Students_form(ModelForm):
    class Meta:
        model = Students
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(Students_form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label


# class Students_Results_form(ModelForm):
#     class Meta:
#         model = Students_Results
#         fields = '__all__'



class Questions_form(ModelForm):
    def __init__(self, *args, **kwargs):
        super(Questions_form,self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
            visible.field.widget.attrs['placeholder'] = visible.field.label

    class Meta:
        model = Questions
        fields = '__all__'



class Attempts_log_form(ModelForm):
    class Meta:
        model = Attemps_log
        fields = '__all__'