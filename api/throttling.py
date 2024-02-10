from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
from rest_framework.views import APIView



class Five_by_h(UserRateThrottle):
    scope = 'five'

