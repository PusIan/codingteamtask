from rest_framework import viewsets
from .serializers import FoodListSerializer
from .models import FoodCategory, Food
from django.db.models import Prefetch, Case, When


# Create your views here.
class FoodsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FoodCategory.objects.prefetch_related(
        Prefetch(
            'food', queryset=Food.objects.filter(is_publish=True))).annotate(
                food_cnt=Case(When(food__is_publish=True, then=1))).filter(
                    food_cnt__gt=0).distinct()
    serializer_class = FoodListSerializer
