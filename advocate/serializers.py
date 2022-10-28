from dataclasses import field
from rest_framework import serializers
from .models import Advocate, Company, Link

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ["id", "youtube", "twitter", "github"]
        
        

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "logo", "summary"]


class AdvocateSerializer(serializers.ModelSerializer):
    
    company = CompanySerializer()
    links = LinkSerializer()
    
    class Meta:
        model = Advocate
        fields = ["id", "username", "name", "profile_pic", "bio", 
                  "years_of_experience", "company", "links"]
        
   
    
class SimpleAdvocateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advocate
        fields = ["id", "username", "profile_pic", "bio"]


class AllCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name", "logo", "summary", "advocates"]
        
    advocates = serializers.SerializerMethodField(method_name="company_advocates")
    
    
    def company_advocates(self, company:Company):
        c_advocates = Advocate.objects.filter(company_id=company.id)
        serializer = SimpleAdvocateSerializer(c_advocates, many=True)
        
        return serializer.data
        
    