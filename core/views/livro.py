from rest_framework.viewsets import ModelViewSet

from core.models import Autor, Categoria, Editora, Livro

from core.serializers import AutorSerializer, CategoriaSerializer, EditoraSerializer, LivroSerializer, LivroDetailSerializer


class LivroViewSet(ModelViewSet):
    queryset = Livro.objects.all()
    serializer_class = LivroSerializer

    def get_serializer_class(self):
        if self.action == "list":
            return LivroListSerializer
        elif self.action == "retrieve":
            return LivroDetailSerializer
        return LivroSerializer