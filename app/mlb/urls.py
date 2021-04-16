from django.urls import include, path
from rest_framework import routers
from accounts import views as account
from players import views as player
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register(r'users', account.UserViewSet)
router.register(r'groups', account.GroupViewSet)
router.register(r'players', player.PlayerViewSet)
router.register(r'teams', player.TeamViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-token-auth/', views.obtain_auth_token, name='api-token-auth'),
]