from django.db.models.base import Model as Model
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from Recipe_App.models import Recipe
from Recipe_App.form import SignupForm, LoginForm
from django.views.generic.edit import FormView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.

def home(request):
    recipes = Recipe.objects.filter()
    recipeSort = set()
    for i in recipes:
        recipeSort.add(i.category)
    context = {'recipes' : recipes, 'recipeSort': recipeSort}
    return render(request, 'home.html', context)

def Search(request):
    if request.method == 'POST':
        search_query = request.POST.get('search')
        recipes = Recipe.objects.filter(Q(recipe_name__icontains=search_query) | Q(description__icontains=search_query))
        context = {'recipes': recipes, 'search_query': search_query}
        return render(request, 'home.html', context)
    else:
        recipes = Recipe.objects.all()
        context = {'recipes': recipes}
        return render(request, 'home.html', context)
    
def Category(request, cat):
    recipes = Recipe.objects.all()
    recipeSort = set()
    for i in recipes:
        recipeSort.add(i.category)
    
    filterd_recipe = Recipe.objects.filter(category=cat)
    context = {'recipes' : filterd_recipe
    , 'recipeSort': recipeSort}
    return render(request, 'home.html', context)

# Auth/User------------------------------------------------------------------------
class Signup(FormView):
    template_name = 'signup.html'
    form_class = SignupForm
    success_url = '/login'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
    

from django.contrib.auth import authenticate, login
from django.views.generic import FormView

class Login(FormView):
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'
    
    def form_valid(self, form):
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            self.request.session['uid'] = user.id 
            return super().form_valid(form)
        else:
            form.add_error(None, 'Invalid username or password')
            return self.form_invalid(form)
    
def Signout(request):
    logout(request)
    return redirect('/')

#Recipe------------------------------------------------------------------------------

from Recipe_App.form import RecipeForm

def addrecipe(request):
    if not request.user.is_authenticated:
        return redirect('login') 

    if request.method == 'POST':
        uid = request.user.id  
        recipe_name = request.POST.get('recipe_name')
        recipe_img = request.FILES.get('recipe_img')
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        instructions = request.POST.get('instructions')
        category = request.POST.get('category')
        
        recipe = Recipe()
        recipe.recipe_name = recipe_name
        recipe.recipe_img = recipe_img
        recipe.description = description
        recipe.ingredients = ingredients
        recipe.instructions = instructions
        recipe.category = category
        recipe.user = User.objects.get(id=uid) 
        recipe.save()
        return redirect('/')
    else:
        f = RecipeForm()
        context = {'form': f}
        return render(request, 'recipe.html', context)


#ViewRecipe---------------------------------------------------------------------------

def viewpage(request, rid):
    recipes = get_object_or_404(Recipe, id = rid)
    context = {'recipes' : recipes}
    return render(request, 'viewpage.html', context)


#Myrecipe------------------------------------------------------------------------------

def recipelist(request):
    uid = request.session.get('uid')
    print(f"UID from session: {uid}")
    if uid:
        rlist = Recipe.objects.filter(user=uid)
        context = {'recipelist': rlist}
        return render(request, 'myrecipe.html', context)
    else:
        return redirect('/login') 
    
def editRecipe(request, id):
    recipe = Recipe.objects.get(id=id)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            print(form.errors) 
            return HttpResponse("Form is not valid")

    else:
        form = RecipeForm(instance=recipe)
    
    context = {'form':form}
    return render(request, 'edit_recipe.html',context)

def deleteRecipe(request, id):
    recipe = Recipe.objects.get(id = id)
    recipe.delete()
    return redirect('/myrecipe')