# 🌐 Personal Portfolio Website

A fully responsive personal portfolio website built with **Python** and **Django** to showcase my projects, skills, and experience.

## 🛠️ Tech Stack
- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite3
- **Other:** Django ORM, Django Templating Engine

## ✨ Features
- Home, About, Projects, and Contact sections
- Dynamic content management via Django Admin
- Contact form with Django form handling
- Responsive design for all screen sizes
- Static file management using Django staticfiles

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/aayushkayasth/django-portfolio.git

# Go into the project folder
cd django-portfolio

# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Start the server
python manage.py runserver
```

Open your browser and go to: `http://127.0.0.1:8000/`

## 📁 Project Structure
├── core/               # Main Django app
├── portfolio_project/  # Project settings
├── static/             # CSS, JS, Images
├── templates/          # HTML Templates
├── manage.py
└── requirements.txt

## 👤 Author
**Aayush Kayasth**  
[GitHub](https://github.com/aayushkayasth)
