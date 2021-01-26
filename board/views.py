from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from fcuser.models import Fcuser

from .forms import BoardForm
from .models import Board
from tag.models import Tag


# Create your views here.
def board_list(request):
    boards = Board.objects.all().order_by('id')  # -id: time 역순

    paginator = Paginator(boards, 3)  # 블로그  객체 3개를 한 페이지로 자르기
    page = request.GET.get('page')  # request 된 페이지가 뭔지를 알아낸다(request 페이지를 변수에 담는다)
    posts = paginator.get_page(page)  # request 된 페이지를 얻어온다

    return render(request, 'board/board_list.html', {'boards': boards, 'posts': posts})


def board_detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        raise Http404('Board does not exist.')

    return render(request, 'board/board_detail.html', {'board': board})


def board_write(request):
    if not request.session.get('user'):
        return redirect('/fcuser/login/')

    if request.method == 'POST':
        forms = BoardForm(request.POST)
        if forms.is_valid():  # board 생성
            user_id = request.session.get('user')
            fcuser = Fcuser.objects.get(pk=user_id)

            tags = forms.cleaned_data['tags'].split(',')

            board = Board()
            board.title = forms.cleaned_data['title']
            board.contents = forms.cleaned_data['contents']
            board.writer = fcuser
            board.save()  # save DB ->  먼저 저장해줘야 함

            for tag in tags:
                if not tag:
                    continue

                _tag, created = Tag.objects.get_or_create(name=tag)  # If the tag already exists, just import it. OR If the tag does not exist, create it.
                # _tag, _ = Tag.objects.get_or_create(name=tag, defaults={'writer': writer})  # _: not use
                # if created:
                board.tags.add(_tag)

            return redirect('/board/list/')  # url
    else:
        forms = BoardForm()

    return render(request, 'board/board_write.html', {'forms': forms})
