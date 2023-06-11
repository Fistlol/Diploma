from datetime import datetime, timedelta

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework import viewsets

from . import models
from . import serializers

class UserModelViewSet(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer


class UserPlanModelViewSet(viewsets.ModelViewSet):
    queryset = models.UserPlan.objects.all()
    serializer_class = serializers.UserPlanSerializer


class CompanyModelViewSet(viewsets.ModelViewSet):
    queryset = models.Company.objects.all()
    serializer_class = serializers.CompanySerializer


class DietModelViewSet(viewsets.ModelViewSet):
    queryset = models.Diet.objects.all()
    serializer_class = serializers.DietSerializer


class FoodModelViewSet(viewsets.ModelViewSet):
    queryset = models.Food.objects.all()
    serializer_class = serializers.FoodSerializer


class PlanModelViewSet(viewsets.ModelViewSet):
    queryset = models.Plan.objects.all()
    serializer_class = serializers.PlanSerializer


def login_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)

                return redirect('/')
            else:
                messages.info(request, 'Логин или пароль введен неверно')

        return render(request, 'login/login.html', {})


def logout_user(request):
    logout(request)

    return redirect('/login')


@login_required(login_url='login/')
def catalog(request):
    companies = CompanyModelViewSet.queryset.all()

    return render(request, 'main/catalog/catalog.html', {'companies': companies})


@login_required(login_url='login/')
def company(request, pk):
    company_object = CompanyModelViewSet.queryset.get(pk=pk)
    company_objects = CompanyModelViewSet.queryset.all()
    food_objects = FoodModelViewSet.queryset.all().filter(company_id=pk)
    plan_objects = PlanModelViewSet.queryset.all().filter(company_id=pk)
    diet_objects = DietModelViewSet.queryset.all().filter(company_id=pk)

    return render(request, 'main/catalog/company.html', {
        'company_object': company_object,
        'company_objects': company_objects,
        'food_objects': food_objects,
        'plan_objects': plan_objects,
        'diet_objects': diet_objects,
    })


@login_required(login_url='login/')
def order(request, pk):
    plan_object = PlanModelViewSet.queryset.get(pk=pk)

    return render(request, 'main/catalog/order.html', {
        'plan_object': plan_object,
    })


@login_required(login_url='login/')
def success(request, pk):
    days = PlanModelViewSet.queryset.get(pk=pk).days

    models.UserPlan.objects.create(
        user_id=request.user.id,
        plan_id=pk,
        is_paid=False,
        created_at=datetime.today(),
        start_at=datetime.today() + timedelta(days=1),
        end_at=datetime.today() + timedelta(days=days+1),
    )

    return render(request, 'main/catalog/success.html')


@login_required(login_url='login/')
def my_plans(request, pk):
    user_plan = UserPlanModelViewSet.queryset.get(user_id=pk)
    food_times = ['7:30', '10:00', '13:30', '17:00', '19:00']
    food_types = ['Breakfast', 'Snack 1', 'Lunch', 'Snack 2', 'Dinner']
    food_objects = user_plan.plan.diet.foods.all()
    context = zip(food_times, food_types, food_objects)

    return render(
        request,
        'main/my_plans/my_plans.html',
        {
            'user_plan': user_plan,
            'context': context,
        })


@login_required(login_url='login/')
def checklist(request):
    return render(request, 'main/checklist/checklist.html')


@login_required(login_url='login/')
def your_information(request):
    return render(request, 'main/settings/your_information.html')


@login_required(login_url='login/')
def order_history(request):
    return render(request, 'main/settings/order_history.html')


@login_required(login_url='login/')
def promo_codes(request):
    return render(request, 'main/settings/promo_codes.html')


@login_required(login_url='login/')
def logout_page(request):
    return render(request, 'main/settings/logout.html')



