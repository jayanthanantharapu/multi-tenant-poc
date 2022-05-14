from rest_framework import serializers

from .models import Client, Domain


class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domain
        fields = ("domain",)


class ClientSerializer(serializers.ModelSerializer):
    def update(self, instance, validated_data):
        pass

    domain = serializers.CharField(required=True)

    class Meta:
        model = Client
        fields = "__all__"

    def create(self, validated_data):
        model_domain_data = validated_data.pop("domain")
        model_client_instance = Client.objects.create(**validated_data)
        model_domain_instance = Domain.objects.create(
            domain=model_domain_data, tenant=model_client_instance, is_primary=True
        )
        return model_domain_instance
