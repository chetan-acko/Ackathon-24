from rest_framework.response import Response
from rest_framework.views import APIView

from master.models import BasicFeature


class CreateBaseVariantView(APIView):

    def post(self, request):
        data = request.data
        filtered_data = {key: value for key, value in data.items() if value}
        budget = filtered_data.pop('budget', None)
        query = BasicFeature.objects.filter(**filtered_data)
        if budget:
            query = query.filter(variantcolor__price__lte=budget)

        return Response({"results": query.values()})
