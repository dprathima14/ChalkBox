from django.conf.urls import url
from .views import submission_list, submit_assignment

urlpatterns = [
    url(r'^(?P<aid>\d+)$', submission_list, name="submission_list"),
    url(r'^(?P<aid>\d+)/submit/$', submit_assignment, name="submit_assignment"),
] 