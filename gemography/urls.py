from django.urls import path

from gemography.githubtop import views

urlpatterns = [
    path('top-languages/', views.TopLanguages.as_view(), name='top_languages'),
]
