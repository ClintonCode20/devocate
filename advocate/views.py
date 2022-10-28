from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from .serializers import AdvocateSerializer, CompanySerializer, LinkSerializer, AllCompanySerializer
from .models import Advocate, Company, Link
from advocate import serializers
# Create your views here.


def index(request):
    return render(request, "index.html")

class AdvocateList(ListCreateAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    filter_backends = [SearchFilter]
    search_fields = ["username", ]
    pagination_class = PageNumberPagination
    

class AdvocateDetail(RetrieveUpdateDestroyAPIView):
    queryset = Advocate.objects.all()
    serializer_class = AdvocateSerializer
    lookup_field = "username"

class CompanyList(ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = AllCompanySerializer
    
class CompanyDetail(RetrieveUpdateDestroyAPIView):
    queryset = Company.objects.all()
    serializer_class = AllCompanySerializer

    









@api_view()
def advocate_list(request):
    advocates  = Advocate.objects.all()
    serializer = AdvocateSerializer(advocates, many=True)
    filter_backends = [SearchFilter]
    search_fields = ["username"]
    return Response(serializer.data)


@api_view()
def advocate_detail(request, pk):
    advocate = get_object_or_404(Advocate, id=pk)
    serializer = AdvocateSerializer(advocate, many=False)
    return Response(serializer.data)


@api_view()
def company_list(request):
    companies = Company.objects.all()
    serializer = AllCompanySerializer(companies, many=True)
    return Response(serializer.data)

@api_view()
def company_detail(request, pk):
    company = get_object_or_404(Company, id=pk)
    serializer = AllCompanySerializer(company, many=False)
    return Response(serializer.data)