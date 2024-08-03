# forms.py

from django import forms

class JobResumeForm(forms.Form):
    job_description = forms.CharField(widget=forms.Textarea, label='Job Description')
    resume_content = forms.FileField(label='Upload Resume (PDF only)')
