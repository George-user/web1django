from django.shortcuts import render
from .models import Bb,Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy


# Create your views here.

def index(request):
    bbs=Bb.objects.order_by('-published')
    rubrics = Rubric.objects.all()
    return render(request,'bboard/index.html',{'bbs':bbs,'rubrics':rubrics})

def by_rubric(request,rubric_id):
    bbs=Bb.objects.filter(rubric=rubric_id)
    rubrics=Rubric.objects.all()
    curent_rubric=Rubric.objects.get(pk=rubric_id)
    context={'bbs':bbs,'rubrics':rubrics,'current_rubric':curent_rubric}
    return render(request,'bboard/by_rubric.html',context)
class BbCreateView(CreateView):
    template_name = 'bboard/create.html'
    form_class = BbForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context=super().get_context_data(**kwargs)
        context['rubrics']=Rubric.objects.all()
        return context