from django.urls import path
# from django.contrib import  admin

from . import views




urlpatterns = [
    # path('projects/' , views.projects , name = "projects"),
    # path('project/<str:id>/' , views.project , name = "project with id"),
    path('',views.htmlpage , name="htmlpage"),
    path('department/' , views.department , name="department"),
    path('student/' , views.student , name="student"),
    path('createNewDepartment/' , views.createNewDepartment , name="createNewDepartment"),
    path('department/update_department/<str:id>/' , views.update_department,name='update_department'),
    path('department/delete_department/<str:id>/' , views.delete_department,name='delete_department'),

    path('question/<str:que_id>/' , views.question,name='question'),
    path('department/show_exams/<str:dept_id>/show_questions/<str:exam_id>/update_question/<str:que_id>/' , views.update_question , name='update_question'),
    path('department/show_exams/<str:dept_id>/show_questions/<str:exam_id>/delete_question/<str:que_id>/' , views.delete_question , name='delete_question'),



    path('department/show_exams/<str:id>/' , views.show_Exams,name='show_Exams'),
    path('department/show_exams/<str:id>/newExamCreation/' , views.newExamCreation,name='newExamCreation'),
    path('department/show_exams/<str:dept_id>/delete_exam/<str:exam_id>/' , views.delete_exam,name='delete_Exams'),
    path('department/show_exams/<str:dept_id>/show_questions/<str:exam_id>/' , views.show_questions,name='show_questions'),
    path('department/show_exams/<str:dept_id>/show_questions/<str:exam_id>/createQuestion/' , views.createQuestion,name='createQuestion'),


    
]