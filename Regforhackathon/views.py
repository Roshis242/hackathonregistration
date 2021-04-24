from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from regapp.models import Team
# Create your views here.
def home(request):
    if request.method == 'POST' and request.FILES['proof']:
        collegename = request.POST.get('cname', '')
        teamname = request.POST.get('tname', '')
        pname1 = request.POST.get('name1','')
        pname2 = request.POST.get('name2','')
        pname3 = request.POST.get('name3','')
        pemail1 = request.POST.get('email1', '')
        pemail2 = request.POST.get('email2', '')
        pemail3 = request.POST.get('email3', '')
        pphone1 = request.POST.get('phone1', '')
        pphone2 = request.POST.get('phone2', '')
        pphone3 = request.POST.get('phone3', '')
        proof_pic=request.FILES['proof']
        fs=FileSystemStorage()
        filename=fs.save(proof_pic.name,proof_pic)
        proof_pic_url=fs.url(filename)
        team = Team(collegename=collegename, teamname=teamname, name1=pname1, name2=pname2, name3=pname3, email1=pemail1, email2=pemail2, email3=pemail3, phnumber1=pphone1, phnumber2=pphone2, phnumber3=pphone3, proof_pic=proof_pic_url)
        team.save()
        return render(request, 'thankyou.html')
    else:
        return render(request, 'registrationhome.html')

def thankyou(request):
    return render(request, 'thankyou.html')

def hackathoninfo(request):
    return render(request, 'hackathoninfo.html')

def teamdetails(request):
    team = Team.objects.all()
    return render(request, 'team-details.html', {'team': team})