"""
URL configuration for RecipeManagementSystem_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .import views as v

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', v.home, name='home'),
    path('recipe_search', v.Search, name='recipe_search'),
    path('category/<str:cat>', v.Category, name='category'),
    path('signup', v.Signup.as_view(), name='signup'),
    path('login', v.Login.as_view(), name='login'),
    path('signout', v.Signout, name='signout'),
    path('addrecipe', v.addrecipe, name='addrecipe'), 
    path('viewpage/<int:rid>', v.viewpage, name='viewpage'), 
    path('myrecipe', v.recipelist, name='myrecipe'),
    path('editpage/<int:id>/', v.editRecipe, name='editpage'), 
    path('deletepage/<int:id>/', v.deleteRecipe, name='deletepage'), 
]
