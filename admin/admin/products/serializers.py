from django.db.models import fields
from rest_framework import serializers
from .models import Products

class ProductSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'