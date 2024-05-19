import openai
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Essay
from .forms import EssayForm

openai.api_key = settings.OPENAI_API_KEY

@login_required
def submit_essay(request):
    if request.method == 'POST':
        form = EssayForm(request.POST)
        if form.is_valid():
            essay = form.save(commit=False)
            essay.user = request.user
            essay.feedback = get_feedback(essay.title, essay.body)
            essay.save()
            return redirect('essay_history')
    else:
        form = EssayForm()
    return render(request, 'evaluations/submit_essay.html', {'form': form})

@login_required
def essay_history(request):
    essays = Essay.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'evaluations/essay_history.html', {'essays': essays})

def get_feedback(title, body):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Evaluate the following essay with respect to spelling errors, relevance to the title '{title}', and provide a score out of 10:\n\n{body}\n",
        max_tokens=150
    )
    feedback = response['choices'][0]['text'].strip()
    # Process feedback to extract required information
    return feedback
