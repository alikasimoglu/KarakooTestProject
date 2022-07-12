from django.urls import path
from mainsite.views import IndexView, CompanyCreateView, CompanyDetailView, CompanyUpdateView, CompanyListView, \
    CompanyDeleteView

app_name = 'mainsite'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create-company/', CompanyCreateView.as_view(), name='create_company'),
    path('company-details/<int:pk>/', CompanyDetailView.as_view(), name='company_details'),
    path('company-update/<int:pk>/', CompanyUpdateView.as_view(), name='company_update'),
    path('company-delete/<int:pk>/', CompanyDeleteView.as_view(), name='company_delete'),
    path('company-list/', CompanyListView.as_view(), name='company_list'),
]
