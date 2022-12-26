from django.shortcuts import render, redirect
from .models import Food, Consume


# Create your views here.
def index(request):
    if request.method == 'POST':
        food_consumed = request.POST['food_consumed']
        consume = Food.objects.get(name=food_consumed)
        user = request.user
        consume = Consume(user=user, food=consume)
        consume.save()
        foods = Food.objects.all()

    else:
        foods = Food.objects.all()

    consumed_food = Consume.objects.filter(user=request.user)

    context = {
        'foods': foods,
        'consumed_food': consumed_food,
    }

    return render(request, 'index.html', context)


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect(index)
    
    context = {
        'consumed_food': consumed_food,
    }

    return render(request, 'delete.html', context)
