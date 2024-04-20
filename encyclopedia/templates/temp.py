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