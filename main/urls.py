from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.SimpleRouter()
router.register('user', views.UserModelViewSet),
router.register('user_plan', views.UserPlanModelViewSet),
router.register('company', views.CompanyModelViewSet),
router.register('diet', views.DietModelViewSet),
router.register('food', views.FoodModelViewSet),
router.register('plan', views.PlanModelViewSet),

app_name = 'main'
urlpatterns = [
    path('api/v1/', include(router.urls)),

    path('login/', views.login_page, name='login'),

    path('', views.catalog, name='catalog'),
    path('<int:pk>/', views.company, name='company'),
    path('order/<int:pk>/', views.order, name='order'),
    path('success/<int:pk>/', views.success, name='success'),

    path('my_plans/<int:pk>/', views.my_plans, name='my_plans'),

    path('checklist/', views.checklist, name='checklist'),

    path('settings/your_information/', views.your_information, name='settings'),
    path('settings/your_information/', views.your_information, name='your_information'),
    path('settings/order_history/', views.order_history, name='order_history'),
    path('settings/promo_codes/', views.promo_codes, name='promo_codes'),
    path('settings/logout_page/', views.logout_page, name='logout_page'),
    path('logout/', views.logout_user, name='logout_user'),
]
