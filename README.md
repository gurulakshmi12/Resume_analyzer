# Resume Analyzer

## Overview

The Resume Analyzer is a web-based application built using Django that analyzes resumes and job descriptions to provide insights and recommendations. It uses `TfidfVectorizer` and `cosine_similarity` from scikit-learn for natural language processing (NLP). The project includes a front end built with HTML, CSS, and JavaScript, and uses a local database for data storage.

## Features

- Upload and analyze resumes and job descriptions
- Provides insights and recommendations for improving resume matching
- User-friendly interface
- Responsive design

## Technologies Used

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite (local database)

## Installation

### Prerequisites

- Python 3.x
- Django

### Steps

1. **Clone the repository**
    ```sh
    git clone https://github.com/your-username/resume-analyzer.git
    cd resume-analyzer
    ```

2. **Create a virtual environment**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies**
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply the migrations**
    ```sh
    python manage.py migrate
    ```

5. **Run the development server**
    ```sh
    python manage.py runserver
    ```

6. **Open your browser**
    Navigate to `http://127.0.0.1:8000` to see the application in action.

## Project Structure


