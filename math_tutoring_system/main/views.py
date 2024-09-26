from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

import os

from .models import Course, Lecture, Exercise, Submission

# Load environment variables



# Create your views here.

def register(request):
    if request.method == 'POST':
        uname = request.POST.get('fullname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        if password != confirm_password:
            return HttpResponse("Passwords do not match")
        
        User.objects.create_user(username=uname, email=email, password=password)
        return redirect('login')
    
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return HttpResponse("Invalid credentials")
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    # Initialize userid for both GET and POST requests
    userid = request.user.id

    if request.method == 'POST' and 'logout' in request.POST:
        return redirect('logout')

    # Pass the userid to the template context
    return render(request, 'dashboard.html', {'userid': userid})

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

# View for listing all lectures in a course
def lecture_list(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    lectures = Lecture.objects.filter(course=course).prefetch_related('exercises')  # Ensure exercises are prefetched

    return render(request, 'lecture_list.html', {'lectures': lectures, 'course': course})

# View for displaying a specific lecture and its associated exercises
def lecture_detail(request, lecture_id):
    lecture = get_object_or_404(Lecture, id=lecture_id)
    exercises = Exercise.objects.filter(lecture=lecture)
    return render(request, 'lecture_detail.html', {'lecture': lecture, 'exercises': exercises})
def check_solution(user_solution):
    # Example implementation: Check if the solution contains a specific keyword
    correct_keywords = ['correct', 'solution', 'valid']  # Modify based on your criteria
    feedback = []

    if any(keyword in user_solution.lower() for keyword in correct_keywords):
        feedback.append('Great job! Your solution is correct.')
    else:
        feedback.append('The solution is incorrect. Please try again.')

    return feedback

# View for submitting an answer to an exercise

@login_required
def submit_exercise(request, exercise_id):
    exercise = get_object_or_404(Exercise, id=exercise_id)
    feedback = None
    if request.method == "POST":
        user_solution = request.POST.get('solution')
        if user_solution:
            feedback = check_solution(user_solution)  # Your existing check_solution function
            Submission.objects.create(
                exercise=exercise,
                user=request.user,
                answer_text=user_solution,
                feedback=feedback,
                marks_obtained=feedback.count('great job') * 10  # Example logic for assigning marks
            )
            return redirect('marks')
    return render(request, 'submit_exercise.html', {'exercise': exercise, 'feedback': feedback})

# View for displaying the marks and feedback for the logged-in user
@login_required
def marks_view(request):
    submissions = Submission.objects.filter(user=request.user)
    return render(request, 'marks.html', {'submissions': submissions})

@login_required
def about(request):
    return render(request, 'about.html')


