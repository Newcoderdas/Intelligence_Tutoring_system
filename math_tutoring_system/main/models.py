from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

class Lecture(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    video_url = models.URLField()
    course = models.ForeignKey(Course, related_name='lectures', on_delete=models.CASCADE)


class Exercise(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE)
    question_text = models.TextField()
    correct_solution = models.TextField()
    lecture = models.ForeignKey(Lecture, related_name='exercises', on_delete=models.CASCADE)

class Submission(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    answer_text = models.TextField(blank=True)
    answer_image = models.ImageField(upload_to='submissions/', blank=True)
    feedback = models.TextField(blank=True)
    marks_obtained = models.IntegerField(default=0)
