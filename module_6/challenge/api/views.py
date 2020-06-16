from rest_framework.response import Response
from rest_framework.decorators import api_view
from collections import Counter


@api_view(['POST'])
def lambda_function(request):
    question_list = request.data['question']
    result = [item for items, c in Counter(question_list).most_common()
              for item in [items] * c]

    return Response({'solution': result})
