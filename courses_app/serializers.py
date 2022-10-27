from rest_framework import serializers
from .models import Category, Course, Contact, Branch


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['name', 'imgpath']


class BranchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['latitude', 'longitude', 'address']


class ContactSerializer(serializers.ModelSerializer):
    type = serializers.CharField(source='get_type_string', read_only=True)

    class Meta:
        model = Contact
        fields = ['type', 'value']


class CourseSerializer(serializers.ModelSerializer):
    branches = BranchSerializer(many=True, read_only=True)
    contacts = ContactSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)

    class Meta:
        model = Course
        fields = ['name', 'description', 'logo', 'branches', 'contacts', 'category']
