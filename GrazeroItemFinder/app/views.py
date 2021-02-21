"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from GrazeroItemFinder import finderMain

# トップページ
def top(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/top.html',
        {
            'title':'トップページ',
            'message':'メッセージ',
            'year':datetime.now().year,
        }
    )

# 工事中
def construction(request):
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/construction.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

# 更新ボタン
def updata_button(request):
    if request.method == 'POST':
        finderMain.finderMain()
