from django.urls import path
from .import views


urlpatterns = [
    
    # path("advocates", views.advocate_list),
    # path("companies", views.company_list),
    # path("advocates/<str:pk>", views.advocate_detail),
    # path("companies/<str:pk>", views.company_detail)
    
    path("advocates", views.AdvocateList.as_view()),
    path("advocates/<str:username>", views.AdvocateDetail.as_view()),
    path("companies", views.CompanyList.as_view()),
    path("companies/<str:pk>", views.CompanyDetail.as_view()),
    
    path("", views.index)
    
]