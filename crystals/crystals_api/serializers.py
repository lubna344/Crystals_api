from rest_framework import serializers
from .models import Customer, Types


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'id']

class TypesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Types
        fields = ['crystal_type_one', 'crystal_type_two', 'id']