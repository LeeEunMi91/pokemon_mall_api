from rest_framework import serializers

from .models import Item, UserItem, Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'title']

class ItemSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    class Meta:

        model = Item
        fields = ['id', 'title', 'description', 'created', 'price', 'image', 'category']


class UserItemSerializer(serializers.ModelSerializer):
    item = ItemSerializer()

    class Meta:
        model = UserItem
        fields = ['item', 'user', 'count']
