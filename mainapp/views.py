from django.shortcuts import render
from django.views import View
from rest_framework.viewsets import ModelViewSet
from .models import *
from .serializers import CategorySerializer, TypeWorkSerializer


class CategoryView(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class TypeWorkView(ModelViewSet):
    queryset = TypeWork.objects.all()
    serializer_class = TypeWorkSerializer


def render_app(request):
    return render(request, 'calculation.html')

def render_dexin(request):
    return render(request, 'thanks.html')
