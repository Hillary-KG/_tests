from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('calculate-distance', ClosestPairView.as_view(), name='get_closest_pair'),
    # path('get-pair', ClosestPairDetail.as_view(), name='get_stored_pair'),
    # path('delete-pair/<str:input_str>', ClosestPairDetail.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
