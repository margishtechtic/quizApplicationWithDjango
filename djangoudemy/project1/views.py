from django.shortcuts import render ,redirect

from django.http import HttpResponse,HttpResponseRedirect
from django.core.paginator import Paginator

from django.urls import reverse

from django.contrib.auth import login , authenticate ,logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User
from django.contrib import messages

from .forms import Recruitment_teams_form ,Questions_form ,Students_form,Exams_form , Attempts_log_form

from .models import Recruitment_teams ,Exams ,Questions ,Students , Attemps_log



@login_required(login_url='dept-login')
def department(request):
    qry = Recruitment_teams.objects.all()
    return  render(request , 'department.html' ,{'qry' : qry})



@login_required(login_url='dept-login')
def createNewDepartment(request):
    form = Recruitment_teams_form()
    if request.method == "POST":
        form = Recruitment_teams_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('department')
    
    return  render ( request, 'createNewDepartment.html', {'form':form})



@login_required(login_url='dept-login')
def update_department(request,id):
    team = Recruitment_teams.objects.get(id= id)
    form = Recruitment_teams_form(instance= team)
    if request.method == "POST":
        form = Recruitment_teams_form(request.POST ,instance= team)
        if form.is_valid():
            form.save()
            return redirect('department')
    
    return  render ( request, 'createNewDepartment.html', {'form':form})


@login_required(login_url='dept-login')
def delete_department(request,id):
    team = Recruitment_teams.objects.get(id= id)
    if "goback" in request.POST:
        return redirect('department')
    elif "delete" in request.POST:
        team.delete()
        return redirect('department')

    return  render ( request, 'delete_department.html')



@login_required(login_url='dept-login')
def show_Exams(request,id):
    exams = Exams.objects.filter(dept_id=id)
    return  render(request , 'show_Exams.html',{'exams':exams , 'dept':id})


@login_required(login_url='dept-login')
def newExamCreation(request,id):
    
    rec = Recruitment_teams.objects.get(pk=id)
    exam_form = Exams_form()
    if request.method == 'POST':
        exam_form = Exams_form(request.POST)
        if exam_form.is_valid():
            exam_form.save()
            url = f"http://127.0.0.1:8000/department/show_exams/{rec.id}"
            return redirect(url)
        
    return  render ( request, 'createNewExam.html' ,{'form':exam_form})

@login_required(login_url='dept-login')
def delete_exam(request,dept_id,exam_id):
    exam = Exams.objects.get(id= exam_id)
    if "goback" in request.POST:
        return redirect('http://127.0.0.1:8000/department/show_exams/' + dept_id)
    elif "delete" in request.POST:
        exam.delete()
        return redirect('http://127.0.0.1:8000/department/show_exams/' + dept_id)

    return  render ( request, 'delete_exam.html',{'exam_id':exam_id,'dept_id':dept_id})


@login_required(login_url='dept-login')
def show_questions(request ,exam_id,dept_id):
     questions = Questions.objects.filter(exam_id = exam_id)
    #  print(questions[0].exam_id)
     context = {'questions' : questions , 'exam_id':exam_id}
     return render(request , 'showQuestions.html' , context=context)


@login_required(login_url='dept-login')
def createQuestion(request,exam_id,dept_id):
    #  exam = Exams.objects.get(id=exam_id)
     form = Questions_form()

     if request.method == 'POST':
        form = Questions_form(request.POST)
        if form.is_valid():
            # Set exam_id from URL parameter
            # form.instance.exam_id = exam_id
            form.save()
            url = f"http://127.0.0.1:8000/department/show_exams/{dept_id}/show_questions/{exam_id}"
            return redirect(url)



     context = {'exam_id':exam_id ,'dept_id':dept_id ,'form' : form}
     return render(request ,'createQuestion.html',context)
    

@login_required(login_url='dept-login')
def question(request,que_id):
    return render(request , 'question.html' ,{'que_id':que_id})


@login_required(login_url='dept-login')
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
    


@login_required(login_url='dept-login')
def delete_question(request,dept_id,exam_id,que_id):
    question = Questions.objects.get(id= que_id)
    question.delete()
    url = f"http://127.0.0.1:8000/department/show_exams/{dept_id}/show_questions/{exam_id}"
    return redirect(url)






def student(request):
    stu_form = Students_form()
    if request.method == "POST":
        # print(request.POST)
        # print(type(request.POST))
        stu_form = Students_form(request.POST)
        if stu_form.is_valid():
            student = stu_form.save()
            return redirect(f'http://127.0.0.1:8000/student/{student.id}/{student.exam_code}')
        


    context = {'form':stu_form}
    return  render(request , 'student.html',context)


def student_quiz(request,stu_id,exam_code):
    student  = Students.objects.get(id=stu_id)
    return render(request , 'student_quiz.html' , {'student':student})




index = 0
def student_question(request,stu_id,exam_code):
    student = Students.objects.get(id=stu_id)
    exam_id = Exams.objects.get(exam_code=exam_code).id   
    questions = Questions.objects.filter(exam_id = exam_id)
    
    global index,submit

    is_ans_true = False
    attempted = False
    stu_response = None
    attempt = None
    
    if request.method == "POST":
        try:
            stu_response = request.POST['options']
            attempted = True
        except:
            stu_response = None
        
        true_ans = questions[index].true_option
    

        if stu_response == str(true_ans):
            is_ans_true = True
        else:
            is_ans_true = False

        question = questions[index]

        try:
            if stu_response != None:
                    attempt = Attemps_log.objects.get(stu_id = student , que_id = question)
                    attempt.stu_ans = stu_response
                    attempt.is_ans_true = is_ans_true
                    attempt.save()
                    print('attempted 2nd time' , attempt)
            else:
                print('none response')

        except:
            question = questions[index]
            attempt = Attemps_log.objects.create(stu_id = student , que_id = question , stu_ans = stu_response , is_ans_true = is_ans_true , attempted = attempted)
            print('response have been saved for this que' , attempt)


        if "previous" in request.POST:
            if index > 0:
                index = index - 1
        elif "next" in request.POST:
            if index < len(questions) - 1:
                index = index + 1


    else:
        index = 0


    if index < len(questions):
        question = questions[index]
    
    
    context = {'question' : question ,'stu_id':stu_id , 'exam_code': exam_code , 'index':index + 1 , 'attempt' : attempt } 
    return render(request , 'student_question.html' , context)

def student_result(request , stu_id , exam_code):
    student = Students.objects.get(id = stu_id)
    exam = Exams.objects.get(exam_code = exam_code)
    ques = Questions.objects.filter(exam_id = exam)
    print(ques)
    print(student)
    attempts = Attemps_log.objects.filter(stu_id = stu_id)
    student_preview = []
    for que in ques:
        preview_list = []
        preview_list.append(que)
        try:
            atmp = Attemps_log.objects.get(stu_id = student , que_id = que)
            preview_list.append(atmp.attempted)
            preview_list.append(atmp.stu_ans)
            preview_list.append(atmp.is_ans_true)
        except:
            preview_list.append(False)
            preview_list.append(None)
            preview_list.append(False)

        student_preview.append(preview_list) 
    
    print(student_preview)
    preview_lenght = len(student_preview)
    not_attempted = correct_answers = [preview[1] for preview in student_preview].count(False)
    correct_answers = [preview[3] for preview in student_preview].count(True)
    incorrect_answers = preview_lenght - correct_answers - not_attempted
    percentage = correct_answers/preview_lenght * 100
    print(percentage)
    

    context = {'student' : student , 'attempts' : attempts , 'questions' : ques , 'student_preview' : student_preview}
    return render(request , 'student_result.html' , context)

def htmlpage(request):
    logout(request)
    return render(request,'home.html')  


def dept_login(request):

    if request.user.is_authenticated:
        return redirect('department')

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # print(username , password)
        try:
            user = User.objects.get(username = username)
            # return redirect('department')
        except:
            pass

        user = authenticate(request , username = username , password = password)

        if user is not None:
            login(request ,user)
            messages.success(request , 'Login Successfully!')
            return redirect('department')
    
        else:
            messages.warning(request , 'Username or Password is Incorrect!')
        

    return render(request , 'dept_login_page.html')



def dept_logout(request):
    logout(request)
    messages.success(request , 'Logout Successfully!')
    return redirect('dept-login')



