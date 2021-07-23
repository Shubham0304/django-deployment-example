from django.urls import path
from Basic_App import views

#template tagging
app_name="Basic_App"



urlpatterns=[
path("",views.relative,name="relative"),
path("others/",views.other,name="other"),

]
