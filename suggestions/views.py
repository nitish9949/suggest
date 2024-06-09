from django.shortcuts import render
from .models import College

def home(request):
    if request.method == 'POST':
        min_gpa = float(request.POST.get('min_gpa', 0))
        min_gre_score = int(request.POST.get('min_gre_score', 0))
        min_toefl_score = int(request.POST.get('min_toefl_score', 0))
        min_duolingo_score = int(request.POST.get('min_duolingo_score', 0))
        min_ielts_score = float(request.POST.get('min_ielts_score', 0))
        
        # Filter colleges based on user inputs
        suggested_colleges = College.objects.filter(
            min_gpa__gte=min_gpa,
            min_gre_score__gte=min_gre_score,
            min_toefl_score__gte=min_toefl_score,
            min_duolingo_score__gte=min_duolingo_score,
            min_ielts_score__gte=min_ielts_score
        )
        
        context = {
            'suggested_colleges': suggested_colleges
        }
        return render(request, 'suggestions/home.html', context)
    
    return render(request, 'suggestions/home.html')
