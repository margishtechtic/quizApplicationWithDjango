from django.shortcuts import render ,redirect

from django.http import HttpResponse

from django.urls import reverse


from .forms import Recruitment_teams_form ,Questions_form
from .models import Recruitment_teams ,Exams ,Questions


def department(request):
    qry = Recruitment_teams.objects.all()
    return  render(request , 'department.html' ,{'qry' : qry})


def createNewDepartment(request):
    form = Recruitment_teams_form()
    if request.method == "POST":
        form = Recruitment_teams_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department')
    
    return  render ( request, 'createNewDepartment.html', {'form':form})

def update_department(request,id):
    team = Recruitment_teams.objects.get(id= id)
    form = Recruitment_teams_form(instance= team)
    if request.method == "POST":
        form = Recruitment_teams_form(request.POST ,instance= team)
        if form.is_valid():
            form.save()
            return redirect('department')
    
    return  render ( request, 'createNewDepartment.html', {'form':form})


def delete_department(request,id):
    team = Recruitment_teams.objects.get(id= id)
    if request.method == "POST":
                team.delete()
                return redirect('department')
    return  render ( request, 'delete_department.html')


def newExamCreation(request,id):
    rec = Recruitment_teams.objects.get(pk=id)
    # print(rec.id)
    new_exam = Exams(dept_id=rec)
    new_exam.save()
    url = 'http://127.0.0.1:8000/department/show_exams/' + id
    return redirect(url)


def delete_exam(request,dept_id,exam_id):
    exam = Exams.objects.get(id= exam_id)
    if  request.method=="POST":
        exam.delete()
        url = 'http://127.0.0.1:8000/department/show_exams/' + dept_id
        return redirect(url)
    return  render ( request, 'delete_exam.html',{'exam_id':exam_id,'dept_id':dept_id})



def show_questions(request ,exam_id,dept_id):
     questions = Questions.objects.filter(exam_id = exam_id)
    #  print(questions[0].exam_id)
     context = {'questions' : questions , 'exam_id':exam_id}
     return render(request , 'showQuestions.html' , context=context)



def createQuestion(request,exam_id,dept_id):
    #  exam = Exams.objects.get(id=exam_id)
     form = Questions_form()


    # #  new_row = Questions(exam_id=exam.id)

    #  if request.method=='POST':
    #       question_form.exam_id = exam_id
    #       question_form = Questions_form(request.POST)
    #       question_form.save()
     
     if request.method == 'POST':
        form = Questions_form(request.POST)
        if form.is_valid():
            # Set exam_id from URL parameter
            # form.instance.exam_id = exam_id
            form.save()


     context = {'exam_id':exam_id ,'dept_id':dept_id ,'form' : form}
     return render(request ,'createQuestion.html',context)
    


def question(request,que_id):
    return render(request , 'question.html' ,{'que_id':que_id})



def update_question(request,dept_id,exam_id,que_id):
    question = Questions.objects.get(id= que_id)
    que_form = Questions_form(instance= question)
    if request.method == "POST":
        que_form = Questions_form(request.POST,instance= question)
        if que_form.is_valid():
            que_form.save()
            url = f"http://127.0.0.1:8000/department/show_exams/{dept_id}/show_questions/{exam_id}"
            return redirect(url)
    
    return  render ( request, 'createQuestion.html', {'form':que_form})
    



def delete_question(request,dept_id,exam_id,que_id):
    question = Questions.objects.get(id= que_id)
    question.delete()
    url = f"http://127.0.0.1:8000/department/show_exams/{dept_id}/show_questions/{exam_id}"
    return redirect(url)


def show_Exams(request,id):
    exams = Exams.objects.filter(dept_id=id)
    return  render(request , 'show_Exams.html',{'exams':exams , 'dept':id})



def student(request):
    return  render(request , 'student.html')




def htmlpage(request):     
    return render(request,'home.html') 
    