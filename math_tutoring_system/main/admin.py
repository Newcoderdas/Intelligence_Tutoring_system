from django.contrib import admin
from .models import Course, Lecture, Exercise, Submission

class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)

class LectureAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'video_url')
    search_fields = ('title',)
    list_filter = ('course',)

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('lecture', 'question_text')
    search_fields = ('question_text',)
    list_filter = ('lecture',)

class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise', 'marks_obtained', 'feedback')
    search_fields = ('user__username', 'exercise__question_text')
    list_filter = ('exercise', 'marks_obtained')
admin.site.register(Course)
admin.site.register(Lecture)
admin.site.register(Exercise)
admin.site.register(Submission)
