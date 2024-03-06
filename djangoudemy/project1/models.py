from django.db import models
import uuid
# from django.core.exceptions import ValidationError


from django.db.models.signals import post_save , post_delete
# Create your models here.


# def MaxValueValidator(value):
#         if not isinstance(value, int) or value > 4:
#             raise ValidationError("The maximum value of the answer key should be less than or equal to 4")
        
# def MinValueValidator(value):
#             if not isinstance(value, int) or value < 1:
#                 raise ValidationError("The minimum value of the answer key should be greater than zero.")



class Recruitment_teams(models.Model):
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key =True , editable = False)
    dept_name = models.CharField(max_length = 50 ,unique=True)

    def __str__(self):
        return self.dept_name


class Exams(models.Model):
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key =True , editable = False)
    dept_id = models.ForeignKey(Recruitment_teams, on_delete = models.CASCADE)
    exam_name = models.CharField(max_length = 256 , null=True , blank = True,unique=False)
    exam_code = models.CharField(max_length=10,unique=True ,null=False , blank = False)

    def __str__(self):
        return self.exam_code   


class Students(models.Model):
    id = models.UUIDField(default = uuid.uuid4 , unique = True , primary_key =True , editable = False)
    name = models.CharField(max_length=100 , editable = True)
    email = models.EmailField(max_length = 50 , editable = True)
    contact = models.IntegerField()
    exam_code = models.ForeignKey(Exams , on_delete = models.CASCADE)
    
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
    is_ans_true = models.BooleanField(default = False , editable = True , null = True)
    attempted = models.BooleanField(default = False)

    class Meta:
        unique_together = ('que_id', 'stu_id',)

    def __int__(self):
        return self.stu_id




def createDepartment(sender,instance,created, **kwargs):
    print("department created")
    print(instance,created)



def deleteaction(sender,instance, **kwargs):
    print("department deleted")
    print(instance)

post_save.connect(createDepartment, sender= Recruitment_teams)
post_delete.connect(deleteaction , sender = Recruitment_teams)

