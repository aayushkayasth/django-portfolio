from django.shortcuts import render
from .models import SkillCategory, Project, Experience

def home(request):
    # Fetch skill categories and map to template structure
    skill_categories = SkillCategory.objects.prefetch_related('skills').all()
    skills = []
    for cat in skill_categories:
        skills.append({
            "category": cat.name,
            "items": [skill.name for skill in cat.skills.all()]
        })

    # Fetch projects and map to template structure
    project_objs = Project.objects.prefetch_related('technologies').all()
    projects = []
    for p in project_objs:
        projects.append({
            "title": p.title,
            "description": p.description,
            "link": p.link,
            "technologies": [t.name for t in p.technologies.all()]
        })

    # Fetch experience
    exp_objs = Experience.objects.all()
    experience = []
    for e in exp_objs:
        experience.append({
            "role": e.role,
            "company": e.company,
            "duration": e.duration,
            "description": e.description
        })

    context = {
        "skills": skills,
        "projects": projects,
        "experience": experience,
    }
    return render(request, 'index.html', context)
