from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..serializers import CardSerializer
from ..models import Card

class CardModelViewSet(viewsets.ModelViewSet):
	queryset = Card.objects.all()
	serializer_class = CardSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

	def list(self, request):
		limit = self.request.query_params.get('limit', None)

		if limit:
			limit = int(limit)

		queryset = Card.objects.all().order_by('id')[:limit]
		serializer = CardSerializer(queryset, many=True)

		return Response(serializer.data)
