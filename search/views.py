from rest_framework import viewsets, permissions
from .models import SearchIndex
from .serializers import SearchIndexSerializer
from django.conf import settings
from rest_framework.response import Response

class SearchIndexViewSet(viewsets.ModelViewSet):
    queryset = SearchIndex.objects.all()
    serializer_class = SearchIndexSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        query = request.GET.get('q')
        if query:
            index = settings.ALGOLIA_SEARCH_CLIENT.init_index(settings.ALGOLIA_INDEX_NAME)
            results = index.search(query)
            return Response(results['hits'])
        else:
            return Response([])
