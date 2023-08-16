from rest_framework import serializers

from Todo.models import MyUser, task



#Custom Serializer

class UserSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = MyUser 
        fields = ["id","email","firstName","lastName","password","password2"]
        extra_kwrags = {
            'password':{'write_only':True}
        }

    def validate(self,attrs):
        password = attrs.get('password')
        password2 = attrs.get('password2')

        if password != password2:
            raise serializers.ValidationError("Password doesn't match ")
        
        return attrs
    
    def create(self, validate_data):
        return MyUser.objects.create_user(**validate_data)
    

#Task Serializer

class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = task
        fields = ["id","user","title","description","due_date","Completed"]
        
