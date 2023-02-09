from django.urls import path
from zxt_test_app import views

app_name = 'zxt_test_app'

urlpatterns = [
	path('', biews.index, name = 'index'),
	]
	