from rest_framework.routers import DefaultRouter

import manager.views

# We define a router object. It will look at our viewsets, decide
# what URLs we need and create them automatically so we don't have to
router = DefaultRouter()
# Register the viewsets that the router must analyze
router.register(r'book', manager.views.BookViewSet, base_name='book')
router.register(r'author',manager.views.AuthorViewSet, base_name='author')


# The variable `urlpatterns` will simply receive the URLs computed by the router
# Lets open a shell, import the variable `router` and have a look at the URLs
# it produces
urlpatterns = router.urls