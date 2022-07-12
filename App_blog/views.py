from django.shortcuts import get_object_or_404, render, redirect
from .models import Post

def posts(request):
    posts = Post.objects.all()[::-1]
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'post_detail.html', {'post': post})

def formulario(request):
    return render(request, 'formulario.html')

def publicar(request):
    if request.method == "POST":
        titulo = request.POST['txtTitulo']
        descripcion = request.POST['txtDescripcion']
        imagen = request.FILES['imagen']
        fecha = request.POST['txtFecha']
        publicacion = Post.objects.create(title=titulo,description=descripcion,image=imagen,date=fecha)
        return redirect('/')

def about(request):
    return render(request, 'about.html')