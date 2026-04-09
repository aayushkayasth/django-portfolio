import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portfolio_project.settings")
django.setup()

from core.models import SkillCategory, Skill, Technology, Project, Experience

def seed():
    # Experience
    if not Experience.objects.exists():
        Experience.objects.create(
            role="AI/ML Developer & Data Analyst",
            company="Freelance/Projects",
            duration="2023 - Present",
            description="Building and deploying machine learning models, creating data pipelines, and analyzing business data.",
            order=1
        )
        print("Seeded Experience")

    # Skills
    if not SkillCategory.objects.exists():
        skills_data = [
            {"category": "Machine Learning", "items": ["TensorFlow", "PyTorch", "Scikit-Learn", "Keras", "Pandas", "NumPy"]},
            {"category": "Data Analysis", "items": ["Python", "SQL", "Matplotlib", "Seaborn", "Tableau", "Power BI"]},
            {"category": "Software Dev", "items": ["Django", "Flask", "FastAPI", "HTML/CSS", "JavaScript"]},
            {"category": "Tools", "items": ["Git", "Docker", "Jupyter", "AWS", "Linux"]}
        ]
        
        for idx, group in enumerate(skills_data):
            cat = SkillCategory.objects.create(name=group["category"], order=idx)
            for item in group["items"]:
                Skill.objects.create(category=cat, name=item)
        print("Seeded Skills")

    # Projects
    if not Project.objects.exists():
        projects_data = [
            {
                "title": "AI Image Recognizer",
                "description": "Deep learning model for real-time image classification.",
                "technologies": ["Python", "PyTorch", "OpenCV"],
                "link": "https://github.com/aayushkayasth"
            },
            {
                "title": "Sales Prediction Engine",
                "description": "Predictive modeling and interactive dashboard for sales forecasting.",
                "technologies": ["Python", "Scikit-Learn", "Pandas"],
                "link": "https://github.com/aayushkayasth"
            },
            {
                "title": "Django Backend API",
                "description": "Robust REST API serving machine learning model predictions.",
                "technologies": ["Python", "Django", "Django REST Framework"],
                "link": "https://github.com/aayushkayasth"
            }
        ]
        
        for p_idx, p_data in enumerate(projects_data):
            proj = Project.objects.create(
                title=p_data["title"],
                description=p_data["description"],
                link=p_data["link"],
                order=p_idx
            )
            for tech_name in p_data["technologies"]:
                tech, created = Technology.objects.get_or_create(name=tech_name)
                proj.technologies.add(tech)
        print("Seeded Projects")

if __name__ == "__main__":
    seed()
