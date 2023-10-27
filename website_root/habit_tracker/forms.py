from django import forms

class HabitForm(forms.Form):
    name = forms.CharField(label="Habit name", max_length=100, required=True)

    sunday = forms.BooleanField(label="Sunday", required=False)
    monday = forms.BooleanField(label="Monday", required=False)
    tuesday = forms.BooleanField(label="Tuesday", required=False)
    wednesday = forms.BooleanField(label="Wednesday", required=False)
    thursday = forms.BooleanField(label="Thursday", required=False)
    friday = forms.BooleanField(label="Friday", required=False)
    saturday = forms.BooleanField(label="Saturday", required=False)