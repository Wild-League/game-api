from rest_framework import serializers
from .models import Deck, Card, Users


class CardSerializer(serializers.ModelSerializer):
	class Meta:
		model = Card
		fields = ['id', 'name', 'type', 'cooldown', 'damage', 'attack_range', 'speed', 'life', 'img_card', 'img_preview', 'img_attack', 'img_death', 'img_walk']


class DeckSerializer(serializers.ModelSerializer):
	class Meta:
		model = Deck
		fields = ['id', 'name', 'created_at', 'updated_at']


class DeckCardsSerializer(serializers.ModelSerializer):
	cards =	CardSerializer(many=True)

	class Meta:
		model = Deck
		fields = ['id', 'name', 'cards']


class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ['id', 'username', 'email', 'level']
