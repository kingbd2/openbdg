from django.urls import path
from . import views

app_name = 'glossary'
urlpatterns = [
    path('', views.glossary, name='glossary'),
    path('<element_name>/', views.element_detail, name='element_detail'),
    ]
