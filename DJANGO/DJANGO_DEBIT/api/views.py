from rest_framework.response import Response
from rest_framework.decorators import api_view
# Create your views here.


@api_view(['POST'])
def debit(request):
    incoming_data = request.data
    if not incoming_data:
        return Response({'error': 'Invalid JSON in request body'}, 400)
    incoming_data["tx_debit"] = "passed"
    return Response(incoming_data)
