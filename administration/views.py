from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from administration.forms import RegisterForm, LoginForm
from rest_framework.views import APIView
from administration.serializers import DepartmentSerializer, CourseSerializer, SubjectSerializer, NoticeSerializer, ExamSerializer
from administration.models import Department, Course, Subject, Notice, Exam
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.contrib.auth import get_user_model
from administration.permissions import IsAdmin, IsTeacherorAdmin
from rest_framework.permissions import IsAuthenticated


User=get_user_model()


class RegisterView(View):
    def get(self, request):
        form=RegisterForm()
        return render(request, 'register.html', { 'form':form })
    
    def post(self, request):
        form_input=RegisterForm(request.POST)
        if form_input.is_valid():
            fname=form_input.cleaned_data['first_name']
            lname=form_input.cleaned_data['last_name']
            name=form_input.cleaned_data['username']
            email=form_input.cleaned_data['email']
            role=form_input.cleaned_data['role']
            password1=form_input.cleaned_data['password']
            password2=form_input.cleaned_data['rep_password']

            if password1==password2:
                if User.objects.filter(username=name).exists():
                    return render(request, 'register.html', { 'user_err':'user already exists' })
                
                else:
                    User.objects.create_user(first_name=fname, last_name=lname, username=name, email=email, role=role, password=password1)
                    return redirect('register')
            else:
                return render(request, 'register.html', { 'pass_err':'enter the same password in both the blocks' })
            



class DepartmentAPI(APIView):
    def get_permissions(self):

        if self.request.method == "GET":
            return [IsAuthenticated()]

        return [IsAdmin()]
    def get(self, request):
        data=Department.objects.all()
        serial=DepartmentSerializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=DepartmentSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response({ 'message':'invalid input' })


class DepartmentAPI_individual(APIView):
    def get_permissions(self):

        if self.request.method == "GET":
            return [IsAuthenticated()]

        return [IsAdmin()]
    def get(self, request, pk):
        data=get_object_or_404(Department, id=pk)
        serial=DepartmentSerializer(data)
        return Response(serial.data)
    
    def put(self, request, pk):
        instance=get_object_or_404(Department, id=pk)
        serial=DepartmentSerializer(instance, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response({ 'message':'invalid input' })
    
    def delete(self, request, pk):
        data=get_object_or_404(Department, id=pk)
        data.delete()
        return Response({"message": "Deleted successfully"})



class CourseAPI(APIView):
    def get_permissions(self):

        if self.request.method == "GET":
            return [IsAuthenticated()]

        return [IsAdmin()]
    def get(self, request):
        data=Course.objects.all()
        serial=CourseSerializer(data, many=True)
        return Response(serial.data)

    def post(self, request):
        serial=CourseSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response({ 'message':'invalid input' })
        
class CourseAPI_individual(APIView):
    def get_permissions(self):

        if self.request.method == "GET":
            return [IsAuthenticated()]

        return [IsAdmin()]
    def get(self, request, pk):
        instance=get_object_or_404(Course, id=pk)
        serial=CourseSerializer(instance)
        return Response(serial.data)
    
    def put(self, request, pk):
        instance=get_object_or_404(Course, id=pk)
        serial=CourseSerializer(instance, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response({ 'message':'invalid input' })
        
    def delete(self, request, pk):
        data=get_object_or_404(Course, id=pk)
        data.delete()
        return Response({"message": "Deleted successfully"})


class SubjectAPI(APIView):
    def get_permissions(self):

        if self.request.method == "GET":
            return [IsAuthenticated()]

        return [IsTeacherorAdmin()]
    def get(self, request):
        data=Subject.objects.all()
        serial=SubjectSerializer(data, many=True)
        return Response(serial.data)
    
    def post(self, request):
        serial=SubjectSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response({ 'message':'invalid input' })
        
class SubjectAPI_individual(APIView):
    def get_permissions(self):

        if self.request.method == "GET":
            return [IsAuthenticated()]

        return [IsTeacherorAdmin()]
    def get(self, request, pk):
        data=get_object_or_404(Subject, id=pk)
        serial=SubjectSerializer(data)
        return Response(serial.data)
    
    def put(self, request, pk):
        instance=get_object_or_404(Subject, id=pk)
        serial=SubjectSerializer(instance, data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response({ 'message':'invalid input' })
        
    def delete(self, request, pk):
        data=get_object_or_404(Subject, id=pk)
        data.delete()
        return Response({"message": "Deleted successfully"})
    

class NoticeAPI(ListCreateAPIView):
    def get_permissions(self):

        if self.request.method == "GET":
            return [IsAuthenticated()]

        return [IsTeacherorAdmin()]
    queryset=Notice.objects.all()
    serializer_class=NoticeSerializer

class NoticeAPI_individual(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):

        if self.request.method == "GET":
            return [IsAuthenticated()]

        return [IsTeacherorAdmin()]
    queryset=Notice.objects.all()
    serializer_class=NoticeSerializer

class ExamAPI(ListCreateAPIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return [IsTeacherorAdmin()]

    queryset=Exam.objects.all()
    serializer_class=ExamSerializer

class ExamAPI_individual(RetrieveUpdateDestroyAPIView):
    def get_permissions(self):
        if self.request.method == "GET":
            return [IsAuthenticated()]
        return [IsTeacherorAdmin()]

    queryset=Exam.objects.all()
    serializer_class=ExamSerializer
