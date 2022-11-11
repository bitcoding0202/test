from rest_framework import serializers
from .models import Input



class InputSerializer(serializers.ModelSerializer):
    class Meta:
        model= Input
        fields='__all__' 
        

        
        
    def validate(self,data): 
        if data.get('password') != data.get('confirm_password'):
            raise serializers.ValidationError("Password Does Not Match")  
        return data
    
    def validate_mob_no(self, value):
        if Input.objects.filter(mob_no=value).exists():
            return serializers.ValidationError("Mobno of Above Details Already Exists")
        return value
    
    def validate_user_name(self,value):
        if Input.objects.filter(user_name=value).exists():
            return serializers.ValidationError("Username of Above Details Already Exists")
        return value
    
    def validate_email(self,value):
        if Input.objects.filter(email=value).exists():
            return serializers.ValidationError("Email of Above Details Already Exists")
        return value
    
    
    def create(self, validated_data):
        return Input.objects.create(**validated_data)        
       
                