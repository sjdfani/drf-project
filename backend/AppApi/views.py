from blog.models import article
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializer import AppApiSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser
from .permissions import isSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperuserOrStaffReadOnly
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

# class ArticleCreate(CreateAPIView):
#     queryset = article.objects.all()
#     serializer_class = AppApiSerializer
#     permission_classes = (isSuperUser, IsStaffOrReadOnly)


# class ArticleList(ListAPIView):
#     queryset = article.objects.all()
#     serializer_class = AppApiSerializer


# class ArticleDetail(RetrieveAPIView):
#     queryset = article.objects.all()
#     serializer_class = AppApiSerializer
#     # lockup_field = 'pk'  <default>
#     # lookup_field = 'slug'


# class ArticleUpdate(UpdateAPIView):
#     queryset = article.objects.all()
#     serializer_class = AppApiSerializer
#     lockup_field = 'pk'
#     permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)


# class ArticleDelete(DestroyAPIView):
#     queryset = article.objects.all()
#     serializer_class = AppApiSerializer
#     lockup_field = 'pk'
#     permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)


# class ArticleAll(RetrieveUpdateDestroyAPIView):
#     queryset = article.objects.all()
#     serializer_class = AppApiSerializer
#     lockup_field = 'pk'
#     permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)

class ArticleViewSet(ModelViewSet):
    queryset = article.objects.all()
    serializer_class = AppApiSerializer
    # status filter won't work beacuse I change all() func in modal->manager to status=True
    filterset_fields = ['status', 'author__username']
    ordering_fields = ['status', 'publish']
    ordering = ['-publish']
    search_fields = [
        'title',
        'content',
        'author__username',
        'author__first_name',
        'author__last_name',
    ]

    # def get_queryset(self):
    #     queryset = article.objects.all()
    #     author = self.request.query_params.get('author')
    #     if author is not None:
    #         queryset = queryset.filter(author__username=author)
    #     status = self.request.query_params.get('status')
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #     return queryset

    def get_permissions(self):
        if self.action in ['list', 'create']:
            permission_classes = [IsStaffOrReadOnly]
        else:
            permission_classes = [IsAuthorOrReadOnly, IsStaffOrReadOnly]
        return [permission() for permission in permission_classes]


# ============================================


# class UserList(ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperuserOrStaffReadOnly,)
#     # permission_classes = (isSuperUser,)


# class UserDetail(RetrieveUpdateDestroyAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = (IsSuperuserOrStaffReadOnly,)
#     # permission_classes = (isSuperUser,)

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (isSuperUser,)
