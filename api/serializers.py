from typing import Tuple
from rest_framework import serializers
from .models import Bucketlist


class BucketlistSerializer(serializers.ModelSerializer):
    """
    Serializer to map the Model instance into JSON format.
    """

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        """
        Meta class to map serializer's fields with model fields
        """
        model: Bucketlist = Bucketlist
        fields: Tuple[str] = ('id', 'name', 'owner', 'date_created', 'date_modified')
        read_only_fields: Tuple[str] = ('date_created', 'date_modified')
