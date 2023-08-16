from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import APIView,api_view
from Todo.serializers import TaskSerializer, UserSerializer
from rest_framework import status
from .models import MyUser, task
# Create your views here.
class UserProfileView(APIView):
    def get(self,request):
        details = MyUser.objects.all()
        serializer = UserSerializer(details, many=True)
        return Response(serializer.data , status=status.HTTP_200_OK)
    
    def post(self,request):
        serializer = UserSerializer(data= request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response(serializer.data, status = status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class UserProfileEditView(APIView):
    def get(self, request, id):
        try:
            detail = MyUser.objects.get(id =id)
        except MyUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

        serializer = UserSerializer(detail)
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    def put(self,request,id):
        try:
            detail = MyUser.objects.get(id =id)
        except MyUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSerializer(detail,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        try:
            detail = MyUser.objects.get(id =id)
        except MyUser.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        # serializer = UserSerializer(detail)
        detail.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        

            



class TaskView(APIView):
    def get(self,request):
        Task = task.objects.all()
        serializer = TaskSerializer(Task,many=True)
        return Response(serializer.data ,status=status.HTTP_302_FOUND)
    
    def post(self,request):
        Task = task.objects.all()
        serializer = TaskSerializer(Task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class TaskDetails(APIView):
    def get(self,request,id):
        try:
            Task = task.objects.get(id=id)
        except task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(Task)
        return Response(serializer.data, status=status.HTTP_302_FOUND)
    
    def put(self,request,id):
        try:
            Task = task.objects.get(id =id)
        except task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = TaskSerializer(Task,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, id):
        try: 
            Task = task.objects.get(id=id)
        except task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        Task.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)