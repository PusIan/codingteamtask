from rest_framework import viewsets
from .serializers import FoodListSerializer
from .models import FoodCategory


# Create your views here.
class FoodsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = FoodCategory.objects.all()
    serializer_class = FoodListSerializer
