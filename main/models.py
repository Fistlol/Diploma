from django.db import models

from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    age = models.IntegerField(null=True)
    phone = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    REQUIRED_FIELDS = []


class UserPlan(models.Model):
    user = models.ForeignKey('main.User', related_name="user_plans", on_delete=models.CASCADE)
    is_paid = models.BooleanField()
    created_at = models.DateField()
    start_at = models.DateField()
    end_at = models.DateField()

    class Meta:
        verbose_name = 'User Plan'
        verbose_name_plural = 'User Plans'


class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    manager = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self) -> str:
        return self.name


class FoodCategories(models.TextChoices):
    BREAKFAST = "BREAKFAST", "breakfast"
    LUNCH = "LUNCH", "lunch"
    DINNER = "DINNER", "dinner"
    FIRST_SNACK = "FIRST_SNACK", "first_snack"
    SECOND_SNACK = "SECOND_SNACK", "second_snack"


class Food(models.Model):
    company = models.ForeignKey('main.Company', related_name="foods", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    category = models.CharField(
        "category",
        max_length=32,
        choices=FoodCategories.choices,
        default=FoodCategories.BREAKFAST,
    )
    calories = models.DecimalField(decimal_places=2, max_digits=10)
    photo = models.ImageField(upload_to='food/images/')

    class Meta:
        verbose_name = 'Food'
        verbose_name_plural = 'Foods'

    def __str__(self) -> str:
        return self.name


class Diet(models.Model):
    company = models.ForeignKey('main.Company', related_name="diets", on_delete=models.CASCADE)
    foods = models.ManyToManyField(Food)
    name = models.CharField(max_length=100)
    calories = models.DecimalField(decimal_places=2, max_digits=10)

    class Meta:
        verbose_name = 'Diet'
        verbose_name_plural = 'Diets'

    def __str__(self) -> str:
        return self.name


class Plan(models.Model):
    company = models.ForeignKey('main.Company', related_name="plans", on_delete=models.CASCADE)
    diet = models.ForeignKey('main.Diet', related_name="plans", on_delete=models.CASCADE)
    user_plan = models.ForeignKey('main.UserPlan', related_name="plans", on_delete=models.CASCADE)
    days = models.IntegerField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    benefit = models.IntegerField(null=True)

    class Meta:
        verbose_name = 'Plan'
        verbose_name_plural = 'Plans'
