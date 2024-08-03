# views.py

from PyPDF2 import PdfReader
from django.shortcuts import render
from django.http import HttpResponse
from .forms import JobResumeForm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def home(request):
    if request.method == 'POST':
        form = JobResumeForm(request.POST, request.FILES)
        if form.is_valid():
            job_description = form.cleaned_data['job_description']
            resume_file = request.FILES['resume_content']

            # Extract text from PDF
            pdf_reader = PdfReader(resume_file)
            resume_content = ""
            for page in pdf_reader.pages:
                resume_content += page.extract_text()

            vectorizer = TfidfVectorizer(stop_words='english')
            tfidf_matrix = vectorizer.fit_transform([job_description, resume_content])
            similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]

            return render(request, 'analysis.html', {'similarity': similarity})
    else:
        form = JobResumeForm()
    return render(request, 'home.html', {'form': form})
