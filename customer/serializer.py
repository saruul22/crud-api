from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from .models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'date_joined', 'password']
        # extra_kwargs = {
        #     'password': {'written_only': True}
        # }

    def create(self, validated_data):
        print('validated_data', validated_data)
        validated_data['password'] = make_password(validated_data.get('password'))
        print(validated_data)
        return super().create(validated_data)
    
    def update(self, instance, validated_data):
        if 'password' in validated_data:
            validated_data['password'] = make_password(validated_data.get('password'))
        return super().update(instance, validated_data)