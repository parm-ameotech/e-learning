from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title','description','leval','cover_image','lectures','durations','course_video','course_docx']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)