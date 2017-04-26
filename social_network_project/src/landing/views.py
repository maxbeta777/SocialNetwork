from django.shortcuts import render
from .forms import GuestForm


def landing(request):

    form = GuestForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        print(request.POST)
        print(form.cleaned_data)
        data = form.cleaned_data  # функция для считывания из формы
        print(data["name"])

        new_form = form.save()

    return render(request, 'landing/landing.html', locals())
