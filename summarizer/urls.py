from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='summarizer-home'),
    path('output/', views.output, name='summarizer-home-summary'),
    path('about/',views.about, name='summarizer-about'),
    path('save_pdf/',views.generate_pdf, name='summarizer-generate-pdf')
]