from django.db import models
import uuid

# Create your models here.



class Recruitment_teams(models.Model):
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key =True , editable = False)
    dept_name = models.CharField(max_length = 50 ,unique=True)

    def __str__(self):
        return self.dept_name
    

class Exams(models.Model):
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key =True , editable = False)
    dept_id = models.ForeignKey(Recruitment_teams, on_delete = models.CASCADE)

    def __int__(self):
        return self.id
    

class Students(models.Model):
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key =True , editable = False)
    name = models.CharField(max_length=100 , editable = True)
    email = models.EmailField(max_length = 50 , editable = True)
    contact = models.IntegerField()
    address = models.TextField(null = True , blank =True)
    experience = models.IntegerField()
    # gender = models.Choices(('Male' , 'Male') , ('Female' , 'Female') , ('Other' , 'Other'))

    def __str__(self):
        return self.name
    


class Students_Results(models.Model):
    stu_id = models.OneToOneField(Students , on_delete = models.CASCADE)
    exam_id = models.ForeignKey(Exams,on_delete = models.CASCADE)
    result = models.IntegerField()
    # attempted = models.BooleanField()
    def __int__(self):
        return self.stu_id




class Questions(models.Model):
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key =True , editable = False)
    exam_id = models.ForeignKey(Exams , on_delete= models.CASCADE)
    questions = models.TextField(editable = True)
    options = models.JSONField(default={"1":"", "2": "", "3": "", "4": ""})
    true_option = models.IntegerField()


    def __str__(self):
        return self.questions



class Attemps_log(models.Model):
    que_id = models.ForeignKey(Questions , on_delete = models.CASCADE)
    stu_id = models.ForeignKey(Students , on_delete = models.CASCADE)
    stu_ans = models.IntegerField(editable= True)
    is_ans_true = models.BooleanField(default = None)

    def __int__(self):
        return self.stu_id
