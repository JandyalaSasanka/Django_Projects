from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def homepage(requests):
    return render(requests,'wcount/homepage.html')
def about(requests):
    return render(requests,'wcount/about.html')
def count(requests):
    fulltext = requests.GET['text']
    word_count = len(fulltext.split())
    word_dict = {}
    for w  in fulltext.split():
        if w in word_dict:
            word_dict[w]+=1
        else:
            word_dict[w]=1
    
    word_list = [(c,word_dict[c]) for c in word_dict]
    #word_list = [(w,word_dict[w]) for w in list(word_dict.keys())]
    return render(requests,'wcount/count.html',{'counttext':fulltext,'word_count':word_count,'word_dict':word_dict,'list':word_list})

