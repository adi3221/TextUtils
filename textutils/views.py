# I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # params={'name':'Aditya', 'place':'Renukoot'}
    return render(request, "index.html")

# def ex1(request):
#     s = '''<h2>Navigation bar<br><h2>
#              <a href="https://wwww.facebook.com/">Facebook</a><br>
#              <a href="https://www.flipkart.com/">Flipkart</a><br>
#              <a href="https://www.hindustantimes.com/">News</a><br>
#              <a href="https://wwww.google.com/">Google</a>'''
#     return HttpResponse(s)


def analyze(request):
    djtext = request.POST.get('text', 'default')
    # check the checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # print(removepunc)
    # print(djtext)
    # check which checkbox is on
    if removepunc=='on':
        # analyzed = djtext
        punctuations='''!()-[];:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext=analyzed
        # return render(request, 'analyze.html', params )
    if fullcaps=="on":
        analyzed=""
        for char in djtext:
            analyzed += char.upper()
        params = {'purpose': 'Full UpperCase ', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if (newlineremover=="on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed += char
        params = {'purpose': 'New Line Remover ', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
        djtext = analyzed
    if (extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if djtext[index] == " " and djtext[index+1] ==" ":
                pass
            else:
                analyzed += char
        params = {'purpose': 'New Line Remover ', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)
    if (removepunc !='on' and fullcaps !="on" and newlineremover !="on" and extraspaceremover !="on"):
        return HttpResponse("Please select something and Try Again ")
    return render(request, 'analyze.html', params)
    # else:
    #     return HttpResponse("ERROR")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("remove new line")
#
# def spaceremove(request):
#     return HttpResponse("space remove <a href='/'>back</a> ")
#
# def charcount(request):
#     return HttpResponse("count the character")