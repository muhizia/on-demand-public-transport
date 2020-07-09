from django.urls import path
from WeGo.api.view import (

	api_detail_passenger,
	api_update_passenger,
	api_delete_passenger,
	api_create_passenger,
	api_all_passengers,
	)


app_name = 'WeGo'

urlpatterns = [
    path('<name>/', api_detail_passenger , name="detail"),
    path('<name>/update', api_update_passenger , name="update"),
    path('<name>/delete', api_delete_passenger , name="delete"),
    path('create', api_create_passenger , name="create"),
    path('', api_all_passengers , name="veiwAll"),
]