from django.urls import path
from . import views

app_name = "habit_tracker"
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new_habit_form, name='new'),
    path('publish/', views.publish, name='publish'),
    path('<int:id>/', views.detail, name="detail"),
]
