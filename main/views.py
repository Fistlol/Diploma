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
    companies = CompanyModelViewSet.queryset
    # company = [x for x in CompanyModelViewSet.queryset.values_list('name')[0]]
    # print(type(company))

    return render(request, 'main/catalog/catalog.html', {'companies': companies})


@login_required(login_url='login/')
def my_plans(request):
    username = UserModelViewSet.queryset.values_list('username')[3][0]
    authenticated_user = str(request.user)

    return render(request, 'main/my_plans/my_plans.html', {'username': username,
                                                           'authenticated_user': authenticated_user})


@login_required(login_url='login/')
def checklist(request):
    return render(request, 'main/checklist/checklist.html')


@login_required(login_url='login/')
def settings(request):
    return render(request, 'main/settings/settings.html')


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



