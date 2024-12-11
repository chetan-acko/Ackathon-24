from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import filters, generics, permissions, status, viewsets

from . import models


class BankData(APIView):
    def get(self,request):
        kk = models.ConfigurableDataTable.objects.get(id=1)
        return Response(kk.image.url, status=status.HTTP_200_OK)
