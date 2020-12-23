from django.core.files.storage import default_storage
from django.db.models import Q
from rest_framework import viewsets, status, pagination
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from .models import Post
from .serializers import PostSerializer, UploadSerializer


class Pagination(pagination.PageNumberPagination):
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'totalPageNumber': self.page.paginator.num_pages,
            'currentPageNumber': self.page.number,
            'results': data,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
        })


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = Pagination
    lookup_field = 'slug'

    def get_queryset(self):
        queryset = super().get_queryset()
        params = self.request.query_params
        keyword = params.get('keyword', None)
        if keyword:
            # django python のような、スペース区切りの複数キーワードに対応
            for k in keyword.split():
                queryset = queryset.filter(
                    Q(title__icontains=k) |
                    Q(description__icontains=k) |
                    Q(text__icontains=k) |
                    Q(slug__icontains=k)
                )
        return queryset

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def upload(request):
    serializer = UploadSerializer(data=request.data)
    if serializer.is_valid():
        upload_file = serializer.validated_data['image']
        file_name = default_storage.save(upload_file.name, upload_file)
        url = default_storage.url(file_name)
        return Response({'url': url}, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
