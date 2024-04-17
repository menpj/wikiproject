from django.shortcuts import render

from . import util

from django.http import HttpResponseRedirect
from django.urls import reverse
from django import forms
from string import Template

import markdown2

import re

def writetofile(name,entryBody):
    file1 = open(f"encyclopedia/templates/wiki/{name}.html","w")
    file1.write('{% extends "encyclopedia/layout.html" %}\n')
    file1.write('{% block body %}\n')
    file1.write(entryBody)
    #editLink=f"<a href=\"{% url 'encyclopedia:editPage',{"name":{name}} %}\">Edit Page</a>"
    #editLink=f"<a href=\"{% url 'encyclopedia:editPage' name=name %}\">Edit Page</a>"
    #editLink=f"<a href=\"{% url 'encyclopedia:editPage' name='{name}' %}\">Edit Page</a>"
    #editLink="<a href=\"{% url 'encyclopedia:editPage' name='{}' %}\">Edit Page</a>".format(name)
    #editLink="<a href=\"{\% url 'encyclopedia:editPage',{'name': %s} \%}\">Edit Page</a>".format(name)
    #editLink = Template("<a href=\"{% url 'encyclopedia:editPage' , {name:'$name' }} %}\">Edit Page</a>")
    editLink = Template("<a href=\"{% url 'encyclopedia:editPage' name='$name'  %}\">Edit Page</a>")
    editLink=editLink.substitute(name=name)
    print(editLink)
    file1.write(editLink)
    file1.write('\n{% endblock %}')

    file1.close()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def newPageError(request):
    return render(request, "encyclopedia/newpageerror.html")

#def content(request):
def wiki(request,name):
    #name=request.GET.get('name')
    entryBody=util.get_entry(name)


    if entryBody:
        entryBody= markdown2.markdown(entryBody)
        writetofile(name,entryBody)
        #file1 = open(f"encyclopedia/templates/wiki/{name}.html","w")
        #file1.write('{% extends "encyclopedia/layout.html" %}\n')
        #file1.write('{% block body %}\n')
        #file1.write(entryBody)
        #file1.write('\n{% endblock %}')

        #file1.close()
        return render(request, f"wiki/{name}.html")
    else:
        return render(request, "encyclopedia/content.html", {
            "content": None
        })
    

def wikiSearch(request):

    if request.method=="POST":
        name=request.POST['q']
        entryBody=util.get_entry(name)
        if entryBody:
            entryBody= markdown2.markdown(entryBody)
            writetofile(name,entryBody)
            #file1 = open(f"encyclopedia/templates/wiki/{name}.html","w")
            #file1.write('{% extends "encyclopedia/layout.html" %}\n')
            #file1.write('{% block body %}\n')
            #file1.write(entryBody)
            #file1.write('\n{% endblock %}')
            #file1.close()
            #return render(request, f"wiki/{name}.html")
            return HttpResponseRedirect(f"wiki/{name}")
        else:
            entryList=util.list_entries()
            matchEntryList = []
            for entry in entryList:
                match= re.search(name,entry,re.I)
                if match:
                    matchEntryList.append(entry)
                else:
                    pass
                    #matchEntryList.append(entry)

            #print(matchEntryList)
            if matchEntryList:
                return render(request, "encyclopedia/search.html", {
                    "entries": matchEntryList
                })
            else:

                return render(request, "encyclopedia/content.html", {
                    "content": None
            })    
    

class NewTaskForm(forms.Form):
    title=forms.CharField(label="New Page Title",empty_value="Page Title",max_length=100)
    body=forms.CharField(label="Page Body",widget=forms.Textarea)
    #priority = forms.IntegerField(label="Priority",min_value=1,max_value=10)

def newPage(request):
    if request.method=="POST":
        form=NewTaskForm(request.POST)
        if form.is_valid():
            title=form.cleaned_data["title"]
            body=form.cleaned_data["body"]
            print(title)
            print(body)
            entryBody=util.get_entry(title)
            if entryBody:
                return HttpResponseRedirect(reverse("encyclopedia:newPageError"))
            else:
                newfile= open(f"entries/{title}.md","w")
                newfile.write(body)
                newfile.close()

                entryBody=util.get_entry(title)
                entryBody= markdown2.markdown(entryBody)
                #file1 = open(f"encyclopedia/templates/wiki/{title}.html","w")
                #file1.write('{% extends "encyclopedia/layout.html" %}\n')
                #file1.write('{% block body %}\n')
                #file1.write(entryBody)
                #file1.write('\n{% endblock %}')
                #file1.close()
                writetofile(title,entryBody)
                #return render(request, f"wiki/{title}.html")
                return HttpResponseRedirect(f"wiki/{title}")

        else:
            return render(request,"encyclopedia/newpage.html",{
                "form":form
            })
    return render(request, "encyclopedia/newpage.html",{"form": NewTaskForm()}) 

class EditForm(forms.Form):

    #def initial(self,name):
    #    self.titleName==name
    #def __init__(name):
    def __init__(self,name):
        super().__init__()
        print("test")
        self.titleName=name
        print("test 2")
        self.fields['title'].initial=name
        print("test 4")
        entryBody=util.get_entry(name)
        print("test 5")
        self.fields['body'].initial= entryBody
        
        #self.title=forms.CharField(label="Page Title",initial="test"   ,max_length=100)
        #self.body=forms.CharField(label="Page Body",widget=forms.Textarea,initial="sample body")
    title=forms.CharField(label="Page Title" ,max_length=100)
    body=forms.CharField(label="Page Body",widget=forms.Textarea)
    print("test 3")
    

def editPage(request,name):
    

    if request.method=="POST":
        print("post test 1")
        form = EditForm(request.POST)
        print("post test 2")
        if form.is_valid():
            title=form.cleaned_data["title"]
            body=form.cleaned_data["body"]
            print(title)
            print(body)
            return HttpResponseRedirect(f"wiki/{title}")
        else:
            return render(request,"encyclopedia/editpage.html",{
                "form":form
            })
            


    
    return render(request,"encyclopedia/editpage.html",{"name": name,"form": EditForm(name)})
    