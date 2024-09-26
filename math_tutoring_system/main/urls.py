from django.urls import path,include
from . import views
urlpatterns = [
    path("",views.register,name='register'),
    # path("lectures/",views.lectures,name="lectures"),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('about/',views.about,name="about"),
    # path('quiz/',views.quiz,name='quiz'),
    # path('chatbot/',views.chatbot,name="chatbot"),
    # path('submit_exercise/<int:exercise_id>/', views.submit_exercise, name='submit_exercise'),
    path('courses/', views.course_list, name='course_list'),
    path('course/<int:course_id>/lectures/', views.lecture_list, name='lecture_list'),
    path('lecture/<int:lecture_id>/', views.lecture_detail, name='lecture_detail'),
    path('exercise/<int:exercise_id>/submit/', views.submit_exercise, name='submit_exercise'),
    path('marks/', views.marks_view, name='marks'),
    path('dashboard/',views.dashboard,name="dashboard"),
    path('lecture_list/',views.lecture_list,name='lecture_list'),
    # path('marks/', views.marks_page, name='marks'),
    # path('courses/', views.course_list, name='course'),
    path("__reload__/", include("django_browser_reload.urls")),
]
