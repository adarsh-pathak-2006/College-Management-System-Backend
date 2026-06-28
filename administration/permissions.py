from rest_framework.permissions import BasePermission
from django.contrib.auth import get_user_model
from rest_framework.permissions import SAFE_METHODS


User=get_user_model()

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role==User.ADMIN)
    
class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role==User.TEACHER)
    
class IsStudent(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role==User.STUDENT)
    
class IsAccountant(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role==User.ACCOUNTANT)
    
class IsTeacherorAdmin(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in [User.ADMIN, User.TEACHER])
    
class IsStudentorAdmin(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in [User.STUDENT, User.ADMIN])

class IsAccountantorAdmin(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in [User.ACCOUNTANT, User.ADMIN])
    
class IsAdminStudentorTeacher(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in [User.TEACHER, User.ADMIN, User.STUDENT])
    
class IsAdminorAccountant(BasePermission):
    def has_permission(self, request, view):
        return (request.user.is_authenticated and request.user.role in [User.ACCOUNTANT, User.ADMIN])    


class IsStudentRelatedOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.ADMIN:
            return True
        if request.user.role == User.TEACHER:
            return True
        return getattr(obj, "user_id", None) == request.user.id


class IsTeacherOwnerOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.ADMIN:
            return True
        return getattr(obj, "user_id", None) == request.user.id


class IsFeePaymentOwnerAccountantOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role in [User.ADMIN, User.ACCOUNTANT]:
            return True
        student = getattr(obj, "student", None)
        return getattr(student, "user_id", None) == request.user.id


class IsResultParticipantTeacherOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.ADMIN:
            return True
        if request.user.role == User.TEACHER:
            return request.method in SAFE_METHODS or getattr(obj.teacher, "user_id", None) == request.user.id
        student = getattr(obj, "student", None)
        return request.method in SAFE_METHODS and getattr(student, "user_id", None) == request.user.id


class IsAttendanceParticipantTeacherOrAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.user.role == User.ADMIN:
            return True
        if request.user.role == User.TEACHER:
            return request.method in SAFE_METHODS or getattr(obj.teacher, "user_id", None) == request.user.id
        student = getattr(obj, "student", None)
        return request.method in SAFE_METHODS and getattr(student, "user_id", None) == request.user.id
