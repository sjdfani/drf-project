from blog.models import article
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView, RetrieveUpdateDestroyAPIView
from .serializer import AppApiSerializer, UserSerializer
from rest_framework.permissions import IsAdminUser
from .permissions import isSuperUser, IsAuthorOrReadOnly, IsStaffOrReadOnly, IsSuperuserOrStaffReadOnly


class ArticaleCreate(CreateAPIView):
    queryset = article.objects.all()
    serializer_class = AppApiSerializer
    permission_classes = (isSuperUser, IsStaffOrReadOnly)


class ArticaleList(ListAPIView):
    queryset = article.objects.all()
    serializer_class = AppApiSerializer


class ArticaleDetail(RetrieveAPIView):
    queryset = article.objects.all()
    serializer_class = AppApiSerializer
    # lockup_field = 'pk'  <default>
    # lookup_field = 'slug'


class ArticaleUpdate(UpdateAPIView):
    queryset = article.objects.all()
    serializer_class = AppApiSerializer
    lockup_field = 'pk'
    permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)


class ArticaleDelete(DestroyAPIView):
    queryset = article.objects.all()
    serializer_class = AppApiSerializer
    lockup_field = 'pk'
    permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)


class ArticaleAll(RetrieveUpdateDestroyAPIView):
    queryset = article.objects.all()
    serializer_class = AppApiSerializer
    lockup_field = 'pk'
    permission_classes = (IsAuthorOrReadOnly, IsStaffOrReadOnly)

# ============================================


class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrStaffReadOnly,)
    # permission_classes = (isSuperUser,)


class UserDetail(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsSuperuserOrStaffReadOnly,)
    # permission_classes = (isSuperUser,)
