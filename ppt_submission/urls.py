from django.urls import path,include
from ppt_submission import views

urlpatterns = [
    path('',views.Topics,name="topic"),
    path('<int:id>',views.Index,name="index"),
    path('add_topic/',views.add_topic,name="add_topic"),
    path('<int:id>/add_student/',views.add_student,name="add_student"),
    path('<int:id>/add_file/',views.add_file,name="add_file"),
    path('<int:roll>/download/',views.download,name="download") 
]
