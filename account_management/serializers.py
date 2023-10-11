from rest_framework import serializers

from .models import Account

class AccountRegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = Account
        fields = ['email', 'password', 'full_name']

    def create(self, validated_data):
        return Account.objects.create_user(**validated_data)

class AccountSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = Account
        fields = ('email', 'full_name', 'password',)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        for (key, value) in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
