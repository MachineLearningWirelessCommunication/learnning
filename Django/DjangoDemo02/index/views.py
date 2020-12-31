from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
# Create your views here.
"""
def temp(request):
    t = loader.get_template('01-temp.html')
    html = t.render()
    return HttpResponse(html)
"""

"""
def temp(request):
    dic_ = {
        'music':'《嚣张》',
        'author':'宝强',
        'singer':'羽凡',
    }
    return render(request,'01-temp.html',dic_)
"""
class TEST:
    name = None
    def test(self):
        return 'testing'
def temp(request):
    # music ='《嚣张》'
    # author='宝强'
    # singer='羽凡'
    lst = ['时来运转','好运连连']
    tup = ('时来运转','好运连连')
    dic_ = {
        'music':'《嚣张》',
        'author':'宝强',
        'singer':'羽凡',
    }
    test = TEST()
    return render(request,'01-temp.html',locals())