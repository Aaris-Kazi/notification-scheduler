from django.urls import path

from healthApp import views

urlpatterns = [
    path('health/', view=views.healthView),
]