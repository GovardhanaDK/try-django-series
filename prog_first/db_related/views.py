from django.shortcuts import render, get_object_or_404, redirect
from django.http import  Http404
from .forms import productform
from .models import db_project
from django.urls import  reverse
from django.views.generic import (ListView,DetailView,CreateView,UpdateView,DeleteView)
from django.views import View

# Create your views here.
def productview_db(request,my_id):
    # obj=db_project.objects.get(id=my_id)
    obj = get_object_or_404(db_project, id=my_id)
    # try:
    #     obj=db_project.objects.get(id=my_id)
    # except db_project.DoesNotExist:
    #     raise Http404
    queryset=db_project.objects.all()
    form = productform(request.POST or None,instance=obj)
    if form.is_valid():
        form.save()
        form=productform()


    context = {"object_list":queryset,'form': form}
    return render(request, 'project_db.html', context)

def product_detail(request,my_id):
    obj = get_object_or_404(db_project, id=my_id)
    context = {"object": obj}
    return render(request, 'product_detail.html', context)

def product_delete(request,my_id):
    obj = get_object_or_404(db_project, id=my_id)
    if request.method == "POST":
        obj.delete()
        return redirect("../..")
    context = {"object":obj}
    return render(request, 'product_delete.html', context)


# class Db_projectListView(ListView):
#     template_name= 'Db_project/Db_project_list.html'
#     queryset = db_project.objects.all()

class Db_projectDetailView(DetailView):
    template_name= 'Db_project/Db_project_details.html'
   # queryset = db_project.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(db_project,id= id_)

class Db_projectCreateView(CreateView):
    template_name = 'Db_project/Db_project_create.html'
    form_class = productform
    queryset = db_project.objects.all()

class Db_projectUpdateView(UpdateView):
    template_name = 'Db_project/Db_project_create.html'
    form_class = productform
    queryset = db_project.objects.all()

    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(db_project, id = id_)


class Db_projectDeleteView(DeleteView):
    template_name = 'Db_project/Db_project_delete.html'


    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(db_project, id=id_)

    def get_success_url(self):
        return  reverse('db_related:db_project_list')


class ProjectView(View):
    template_name="yo.html"
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})

class CourseView(View):
    template_name = 'Db_project/Db_project_details.html'
    def get(self, request, id=None, *args, **kwargs):
        context={}
        if id is not None:
            obj = get_object_or_404(db_project, id=id)
            context["object"] = obj
        return render(request, self.template_name, context)

class Db_projectListView(View):
    template_name = 'Db_project/Db_project_list.html'
    queryset = db_project.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, request, *args, **kwargs):
        self.queryset = db_project.objects.all()
        context = {'object_list' : self.get_queryset()}
        return render(request, self.template_name, context)

#This is to show the uses of class based view
#Inheritance
# class MyListView(Db_projectListView):
#     queryset = db_project.objects.filter(id=1)

class CourseCreateView(View):
    template_name = 'Db_project/Db_project_create.html'

    def get(self, request, *args, **kwargs):
        form = productform()
        context = {"form" : form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = productform(request.POST)
        if form.is_valid():
            print(form.is_valid())
            form.save()
            return redirect("../")
        context = {"form": form}
        return render(request, self.template_name, context)




