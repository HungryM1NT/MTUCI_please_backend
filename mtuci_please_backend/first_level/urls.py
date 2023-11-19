from django.urls import path
from . import views

urlpatterns = [
    path('persons', views.PersonsRandomize.as_view(), name='persons'),
]
