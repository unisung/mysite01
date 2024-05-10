from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Question
from django.utils import timezone
from .forms import QuestionForm
from django.core.paginator import Paginator

def home(request):
    # question_list = Question.objects.all()
    # order_by('속성명'), order_by('-속성명')
    page = request.GET.get('page','1') #페이지
    print('page:',page, 'type:',type(page))
    question_list = Question.objects.order_by('-create_date')
    #
    paginator = Paginator(question_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)
    context = {'question_list': page_obj}
    #context = {'question_list': question_list}
    return render(request,
                  "pybo/question_list.html", context)

def detail(request, question_id):
    question= get_object_or_404(Question, pk=question_id)
    context={'question':question}
    return render(request,
                  'pybo/question_detail.html',context)

def answer_create(request, question_id):
    question=get_object_or_404(Question, pk=question_id)
    question.answer_set.create(content=request.POST.get('content'),
                               create_date=timezone.now())
    return redirect('pybo:details', question_id=question.id)


def question_create(request):
    if request.method=='POST':
        form=QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False) #임시저장
            question.create_date = timezone.now()
            question.save() #db에 저장
            return redirect('pybo:home')

    else:# 'GET'
        form = QuestionForm()
        context = {'form': form}
        return render(request,
                      'pybo/question_form.html',
                      context)
