from rest_framework import serializers
from .models import Cliente, Produto, Pedido

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    cliente = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all())
    produtos = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), many=True)

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        produtos = validated_data.pop('produtos')
        pedido = Pedido.objects.create(**validated_data)
        pedido.produtos.set(produtos)
        pedido.save()
        return pedido