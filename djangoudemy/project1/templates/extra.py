
                // <a href="/student/{{stu_id}}/{{exam_code}}/{{prev.id}}"><button class="btn btn-success btn-lg">Previous</button></a>
                
                // <a href="/student/{{stu_id}}/{{exam_code}}/{{nxt.id}}"><button class="btn btn-success btn-lg">Next</button></a>


                // window.location = `http://127.0.0.1:8000/student/${stu_id}/${exam_code}/${que_id}/`











                // onclick="next('{{question.id}}','{{stu_id}}','{{exam_code}}')"
                





index = 0
submit = False
def quiz(request, exam_id, part_id):
    participantObj = Participant.objects.get(id = part_id)
    examObj = Exam.objects.get(id = exam_id)
    questionObj_list = examObj.question.all()
    que_id_list = []
    global index, submit
    for que in questionObj_list:
        que_id_list.append(que.id)
    if request.method == "POST":
        try:
            value = request.POST['answer']
        except:
            value = ""
        questionObj = Question.objects.get(id = questionObj_list[index].id)
        true_answer = questionObj.answer
        if value == true_answer:
            mark = 1
        else:
            mark = 0
        try:
            outcome = Outcome.objects.get(participant = participantObj, question = questionObj)
            outcome.answer = value
            outcome.mark = mark
        except:
            outcome = Outcome.objects.create(participant = participantObj, question = questionObj, answer = value, mark = mark)
        if "previous" in request.POST:
            if index > 0:
                index = index - 1
        elif "next" in request.POST:
            if index < len(que_id_list) - 1:
                index = index + 1
                submit = False
                if index == len(que_id_list) - 1:
                    submit = True
        elif "submit" in request.POST:
            index = 0
            submit = False
            return redirect("result", part_id, exam_id)
    else:
        index = 0
    if index < len(que_id_list):
        question = questionObj_list[index]
    context = {'exam': examObj, 'participant': participantObj , 'que': index+1 , 'question': question, "submit": submit}
    return render(request, 'profile.html', context)













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
        attempt_form = Attempts_log_form()
        print(attempt_form)


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

        
        try:
            if stu_response != None:
                print('student response none is detected')
                question = questions[index]
                attempt = Attemps_log.objects.get(stu_id = student , que_id = question , attempted = True)
                attempt.stu_ans = stu_response
                attempt.is_ans_true = is_ans_true
            # pass

        except:
            question = questions[index]
            Attemps_log.objects.create(stu_id = student , que_id = question , stu_ans = stu_response , is_ans_true = is_ans_true , attempted = attempted)


        if "previous" in request.POST:
            if index > 0:
                index = index - 1
        elif "next" in request.POST:
            if index < len(questions) - 1:
                index = index + 1
                submit = False
                if index == len(questions) - 1:
                    submit = True
        elif "submit" in request.POST:
            index = 0
            submit = False
            # return redirect("result", stu, exam_id)

    else:
        index = 0


    if index < len(questions):
        question = questions[index]
    
    
    context = {'question' : question ,'stu_id':stu_id , 'exam_code': exam_code , 'index':index + 1 , 'attempt' : attempt } 
    return render(request , 'student_question.html' , context)
















if index < len(questions):
            stu_response = request.POST.get('options', None)
            if(stu_response != None):
                print(question)
                print(stu_response)
                print(question.true_option)
                
                ans_true = False
                if stu_response == question.true_option:
                    ans_true = True
                Attemps_log.objects.create(que_id = question , stu_id = student , stu_ans = stu_response , is_ans_true = ans_true )
    

        if "previous" in request.POST:
                if index > 0:
                    index = index - 1
        elif "next" in request.POST:
                if index < len(questions) - 1:
                    index = index + 1

        else:
            index = 0