from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage

from django.conf import settings
import os
# Create your views here.
from django.shortcuts import redirect
from django.contrib import messages

@csrf_exempt
def search(request):
    
    #Cl=Cl_services.objects.all()
    #context={ 'Cl_services': Cl }
    print ("aaaaaaaaaaaaaaaaaaa")

    if request.method== "POST" and not request.FILES:
        text1=request.POST["text_zone"]
        print(text1)
        #return render(request, 'app/index.html',{'text':text1})
        messages.add_message(request, messages.INFO, text1)
        return redirect('/search/#result')


    if request.method == "POST"  and request.FILES['f1']:
        print("POST")
        # text=request.POST['f1']
        f1=request.FILES['f1']
        #print(text)
        print(f1)
        fs = FileSystemStorage()
        filename = fs.save(f1.name, f1)
        print(filename)
        uploaded_file_url = fs.url(filename)
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        uu=BASE_DIR+uploaded_file_url   
        text=open(uu)
        text1=""
        for line in text:
            text1+=line
        print("bbbb",text)
        print(text1)
        
    context={}
    return render(request, 'app/index.html',context)








# def my_services(request):
#     """Tables page.
#     """
#     if not request.user.is_authenticated():
#       return render(request,"django_sb_admin/login.html")
#     else: ###
#       if request.method == "POST":
#         user1=request.user
#         bag_label1 = request.POST['bag_label']
#         bag_of_words1 = request.POST['bag_of_words']
#         Bag_of_words_user.objects.all().delete()

#         bg=Bag_of_words_user(user=user1,bag_label=bag_label1,bag_words=bag_of_words1)
#         bg.save()
#         User_classes.objects.filter(user=user1).delete()
#         #save Personal services
#         Personal_services.objects.filter(user=request.user).delete()
#         res=search(bag_of_words1)
#         print('aaa',res)
#         for s in res :

#           print(s['service_name'])
#           pr=Personal_services(user=request.user,name=s['service_name'],description=s['description'],url=s['link'],provider=s['provider'])
#           pr.save()

#         # if cheched 
#         for a in request.POST.keys():
#           if(request.POST[a]=="1"):  # delete alll classes from favorite user classe and add the new favorite 
            

            
#             c=Class_Unify.objects.get(id=a)
#             classe_user=User_classes(user=request.user,classe=c)
#             classe_user.is_favorite=True
#             classe_user.save()


#         Cl1=User_classes.objects.all()
# ##
#       bag=Bag_of_words_user.objects.get(user=request.user)
#       Services=Personal_services.objects.all()

#       page = request.GET.get('page', 1)
#       paginator = Paginator(Services, 10)
#       try:
#         sr = paginator.page(page)
#       except PageNotAnInteger:
#         sr = paginator.page(1)
#       except EmptyPage:
#         sr = paginator.page(paginator.num_pages)
#       Cl=Class_Unify.objects.all()
#       up=Update.objects.all()


#       return render(request, "django_sb_admin/my_services.html",
#                   {"nav_active":"my_services","Services": sr ,"Bag":bag,'updates':up})





