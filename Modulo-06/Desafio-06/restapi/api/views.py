from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

class QuestionSerializer(serializers.Serializer):
    question = serializers.ListField()

@api_view(['POST'])
def lambda_function(request):
    serializer = QuestionSerializer(data=request.data)
    if serializer.is_valid():
        n_list = serializer.data.get('question')
        freq = {k: n_list.count(k) for k in n_list}
        freq_sorted = {k: v for k, v in sorted(freq.items(), key=lambda item: item[1], reverse=True)}
        return Response({'solution': [k for k in freq_sorted for v in range(freq_sorted[k])]})

    return Response(serializer.errors)
