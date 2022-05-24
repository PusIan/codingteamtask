import pytest
from hometask.models import Food, FoodCategory


@pytest.fixture
def food_category1():
    return FoodCategory.objects.create(name_ru='Напитки', order_id=10)


@pytest.fixture
def food_category2():
    return FoodCategory.objects.create(name_ru='Выпечки', order_id=20)


@pytest.fixture
def food1(food_category1):
    return Food.objects.create(category=food_category1,
                               code=1,
                               internal_code=100,
                               name_ru='Чай',
                               cost=123)


@pytest.fixture
def food2(food_category1):
    return Food.objects.create(category=food_category1,
                               code=2,
                               internal_code=200,
                               name_ru='Кола',
                               cost=123)


@pytest.fixture
def food3(food_category2):
    return Food.objects.create(category=food_category2,
                               code=3,
                               internal_code=300,
                               name_ru='Пирожок',
                               cost=123)
