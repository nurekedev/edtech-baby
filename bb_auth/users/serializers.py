from rest_framework.serializers import ModelSerializer

from users.models import bProfile, bUser

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = bProfile
        fields = '__all__'