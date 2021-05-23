from django.urls import path
from .views import static_views, customer_views, document_views

app_name = "forms"
urlpatterns = [
    path("", static_views.index, name="index"),
    # Customer
    path("register/", customer_views.CustomerCreate.as_view(), name="register"),
    path("update/<str:pk>", customer_views.UpdateCustomer.as_view(), name="cust-update"),
    path("delete/<str:pk>", customer_views.DeleteCustomer.as_view(), name="cust-del"),
    path("cust-id/", customer_views.CustomerId.as_view(), name="cust-id"),
    path("thankyou/", static_views.thank_you, name="thank_you"),
    # Staff
    path("home/", static_views.user_home, name="user-home"),
    path("download/", document_views.DownloadDocument.as_view(), name="download"),
    path("upload/", document_views.CreateDocument.as_view(), name="upload"),
]
