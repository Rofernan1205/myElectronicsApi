from rest_framework.routers import DefaultRouter
from .views import UserViewSet, UserApiView
from django.urls import path, include  # Se agrega include

userRouter = DefaultRouter()
userRouter.register(prefix='users', basename='users', viewset=UserViewSet)

urlpatterns = [
    path('user/me/', UserApiView.as_view(), name='user'),
    path('', include(userRouter.urls)),  # Incluye las rutas del router correctamente
]
