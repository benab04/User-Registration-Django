from rest_framework import serializers
from .models import User
import random
import string
class LoginSerializer(serializers.Serializer):
    username=serializers.CharField()
    password=serializers.CharField()
    
class UserSerializer(serializers.ModelSerializer):
    
    
    
    class Meta:
        model=User
        fields=['first_name', 'last_name','email', 'password','username', 'is_kgp', 'custom_id']
        extra_kwargs = {'password': {'write_only': True}} 
    def create(self, validated_data):
        def generate_custom_id(is_kgp):
            prefix = 'KG' if is_kgp else 'ID'
            prefix_length = len(prefix)
            
            # Generate 8 random digits
            digits = ''.join(random.choices(string.digits, k=8))
            
            # Concatenate prefix and digits
            custom_id = prefix + digits
            
            return custom_id
        
        print(validated_data)
        username = validated_data.pop('username', None)  # Extract username
        password = validated_data.pop('password', None) 
        is_kgp=validated_data.pop('is_kgp', None) 
        print(is_kgp)
        # Extract password
        # Check if both username and password are provided
        if username is not None and password is not None:
            user=User.objects.filter(username=username).first()
            if user is None:
                return  User.objects.create_user(username=username, password=password, custom_id=generate_custom_id(is_kgp),is_kgp=is_kgp,**validated_data)
            
        else:
            # Handle missing username or password gracefully
            raise serializers.ValidationError("Username and password are required.")
        