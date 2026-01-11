from rest_framework import viewsets, permissions, filters
from .models import Tone, Summary
from .serializers import ToneSerializer, SummarySerializer
from rest_framework.permissions import IsAuthenticated


class ToneViewSet(viewsets.ModelViewSet):
    """
    Public: List & Retrieve
    Authenticated: Create, Update, Delete
    """
    queryset = Tone.objects.all()
    serializer_class = ToneSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class SummaryViewSet(viewsets.ModelViewSet):
    """
    Authenticated users only.
    Users can see ONLY their summaries.
    """
    serializer_class = SummarySerializer
    permission_classes = [IsAuthenticated]

    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['tone__name']
    ordering_fields = ['created_at']

    def get_queryset(self):
        return Summary.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

