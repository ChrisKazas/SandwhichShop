from django.urls import path, include

from sandwhichApp.views import SandwichView, IngredientsListView, SandwichGeneratorView

urlpatterns = [
    path('', SandwichView.as_view(), name='sandwich'),
    path('ingredients/<str:ingredient_type>', IngredientsListView.as_view(), name='ingredients_list'),
    path('random', SandwichGeneratorView.as_view(), name='sandwich_generator')
]
