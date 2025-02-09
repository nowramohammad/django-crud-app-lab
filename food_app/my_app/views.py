from django.shortcuts import render, get_object_or_404, redirect
from .models import Food
from .forms import FoodForm
from django.contrib.auth import login
from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})
def home(request):
    return render(request, 'my_app/home.html')

def food_list(request):
    foods = Food.objects.all()
    return render(request, 'my_app/food_list.html', {'foods': foods})

def food_detail(request, pk):
    food = get_object_or_404(Food, pk=pk)
    return render(request, 'my_app/food_detail.html', {'food': food})

def food_create(request):
    if request.method == "POST":
        form = FoodForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm()
    return render(request, 'my_app/food_form.html', {'form': form})

def food_update(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        form = FoodForm(request.POST, instance=food)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodForm(instance=food)
    return render(request, 'my_app/food_form.html', {'form': form})

def food_delete(request, pk):
    food = get_object_or_404(Food, pk=pk)
    if request.method == "POST":
        food.delete()
        return redirect('food_list')
    return render(request, 'my_app/food_confirm_delete.html', {'food': food})

