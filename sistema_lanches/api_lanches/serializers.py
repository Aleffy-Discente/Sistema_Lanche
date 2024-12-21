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
    cliente_id = serializers.PrimaryKeyRelatedField(queryset=Cliente.objects.all(), source='cliente')
    produtos_ids = serializers.PrimaryKeyRelatedField(queryset=Produto.objects.all(), many=True, source='produtos')

    class Meta:
        model = Pedido
        fields = '__all__'

    def create(self, validated_data):
        produtos = validated_data.pop('produtos')  # Usa o `source='produtos'` do campo `produtos_ids`
        pedido = Pedido.objects.create(**validated_data)
        pedido.produtos.set(produtos)  # Define os produtos ManyToMany
        pedido.save()
        return pedido