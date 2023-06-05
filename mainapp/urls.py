from django.urls import path
from rest_framework.routers import SimpleRouter
from mainapp import views
from mainapp.views import CategoryView, TypeWorkView

router = SimpleRouter()
router.register('api/categories', CategoryView)
router.register('api/works', TypeWorkView)

app_name = "mainapp"
urlpatterns = [
    path('', views.render_app, name='calculation'),
    path('api/user_and_user_choice', views.render_dexin)
]

urlpatterns += router.urls
