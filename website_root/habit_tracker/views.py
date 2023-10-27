from django.shortcuts import render, redirect
from django.http import HttpResponse
from datetime import datetime
from .models import Habit
from django.contrib.auth.models import User

from .forms import HabitForm

# Create your views here.
def index(request):
    habits = Habit.objects.filter(active=True)
    context = {
        'current_date': datetime.now(),
        'habits': habits
    }
    return render(request, 'habit_tracker/index.html', context=context)

def new_habit_form(request):
    form = HabitForm()
    context = {
        'form': form,
    }
    return render(request, 'habit_tracker/new_habit.html', context=context)

def publish(request):
    if request.method == "POST":
        form = HabitForm(request.POST)
        if form.is_valid():
            habit = Habit(
                name=form.cleaned_data["name"],
                sunday=form.cleaned_data["sunday"],
                monday=form.cleaned_data["monday"],
                tuesday=form.cleaned_data["tuesday"],
                wednesday=form.cleaned_data["wednesday"],
                thursday=form.cleaned_data["thursday"],
                friday=form.cleaned_data["friday"],
                saturday=form.cleaned_data["saturday"],
                start_at=datetime.now(),
                user=User.objects.get(pk=1)
            )
            habit.save()
            return redirect('habit_tracker:index')
    else:
        form = HabitForm()
    return render(request, 'habit_tracker/new_habit.html', {'form': form})

def detail(request, id):
    habit = Habit.objects.get(pk=id)
    context = {
        'habit': habit
    }
    return render(request, 'habit_tracker/habit_detail.html', context)