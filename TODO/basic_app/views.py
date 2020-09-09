from django.shortcuts import render,redirect
from .forms import Taskform
# Create your views here.
from .models import Task
from django.views.generic import TemplateView,DeleteView
from django.http import HttpResponse
from django.views import View
from django.urls import reverse_lazy


class TaskView(View):
    form_class=Taskform
    print(form_class)

    def get(self,request):
        form = self.form_class()
        task_list=Task.objects.all()
        context={
            "task_list":task_list,
            "form": form
        }
        return render(request,"basic_app/task_create.html",context)

    def post(self, request, *args, **kwargs):
        reg=False
        form = self.form_class(data=request.POST)
        if form.is_valid():
            form.save()
            # form=self.form_class()
            reg =True   
            return redirect("task")
        return HttpResponse("form is not valid")
    
            
    

class IndexView(TemplateView):
    template_name="basic_app/basic.html"
        
   

# class TaskDelelte(DeleteView):
#     model=Task
#     success_url=reverse_lazy("task")
    
def Task_delete(request,pk):
    task_obj=Task.objects.get(id=pk)
    task_obj.delete()
    return redirect("task")

    