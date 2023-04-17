from django.urls import path
# from .views import HerbsList, HerbsDetail, UserList, UserDetail  # new

from rest_framework.routers import SimpleRouter

from .views import UserViewSet, HerbsViewSet


router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", HerbsViewSet, basename="herbs")

urlpatterns = router.urls

# urlpatterns = [
#     path("users/", UserList.as_view()), # new
#     path("users/<int:pk>/", UserDetail.as_view()),  # new
#     path("<int:pk>/", HerbsDetail.as_view(), name="herbs_detail"),
#     path("", HerbsList.as_view(), name="herbs_list"),
# ]