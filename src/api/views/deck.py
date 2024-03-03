from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from ..serializers import DeckSerializer, DeckCardsSerializer
from ..models import Deck

class DeckModelViewSet(viewsets.ModelViewSet):
	queryset = Deck.objects.all()
	serializer_class = DeckSerializer
	permission_classes = [IsAuthenticatedOrReadOnly]

	def retrieve(self, request, pk):
		try:
			deck = Deck.objects.get(pk=pk)
		except Deck.DoesNotExist:
			return Response(status=status.HTTP_404_NOT_FOUND)

		serialized_deck = DeckCardsSerializer(deck).data
		return Response(data=serialized_deck, status=status.HTTP_200_OK)

