from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_essay, name='submit_essay'),
    path('history/', views.essay_history, name='essay_history'),
]
