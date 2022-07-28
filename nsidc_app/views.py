from datetime import datetime
from http.client import HTTPResponse
from django.forms import DateField
from django.http import HttpResponse
from django.shortcuts import render
from nsidc_app.models import about
from django.utils import timezone

from nsidc_app.models import informationResearch
from nsidc_app.models import researchScientist
from nsidc_app.models import researchGrant, myclass, archiveclass
from nsidc_app.models import scientificPublication, research_example_down_sp
from nsidc_app.models import scientificExpedition, research_example_down_scientists, research_example_down_resgran


# Create your views here.

def home(request):
    abouts = about.objects.all()
    research_example_down_resgr = research_example_down_resgran.objects.all()
    research_example_down_sps = research_example_down_sp.objects.all()
    # researchs_drops = research_drop.objects.all()
    informationResearchs = informationResearch.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    scientificPublications = scientificPublication.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    research_example_down_scientist = research_example_down_scientists.objects.all()
    context = {'abouts': abouts, 'informationResearchs': informationResearchs, 'researchScientists': researchScientists, 'researchGrants': researchGrants, 'scientificPublications': scientificPublications,
               'scientificExpeditions': scientificExpeditions, 'redsc': research_example_down_scientist, 'redrg': research_example_down_resgr, "down_publ": research_example_down_sps}
    return render(request, 'home.html', context)
# def about_jobs(request):
#     return HttpResponse("this is home page")
# def about_ncpor(request):
#     return HttpResponse("this is home page")
# def about_sponsors(request):
#     return HttpResponse("this is home page")
# def about_highlights(request):
#     return HttpResponse("this is home page")
# def about_copyright(request):
#     return HttpResponse("this is home page")
# def about_contact(request):
#     return HttpResponse("this is home page")
# def about_greendata(request):
#     return HttpResponse("this is home page")
# def about_home(request):
#     abouts = about.objects.all()
#     context = {'abouts':abouts}
#     return render(request,'about.html',context)


def about_example(request, slug):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    About = about.objects.filter(slug=slug).first()
    researchGrants = researchGrant.objects.all()
    scientificPublications = scientificPublication.objects.all()
    informationResearchs = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'about': About,
               'ab': abouts,
               'rs': researchScientists,
               'rsg': researchGrants,
               'sfpb': scientificPublications,
               'ifrsc': informationResearchs,
               'expd': scientificExpeditions
               }
    return render(request, 'about_example.html', context)


# Research
def research_scientists(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'research/r_scientists.html', context)


def research_grants(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'research/research_grants.html', context)


def research_publications(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'research/scientific_publications.html', context)


def research_information(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'research/InformationResearch.html', context)


def scientific_expeditions(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'research/ScientificExpeditions.html', context)


# def research_example(request,slug):
#     Researchs = research.objects.filter(slug=slug).first()
#     context = {'research':Researchs}
#     return render(request,'research_example.html',context)
def research_scientists_example(request, slug):
    abouts = about.objects.all()
    Researchs = researchScientist.objects.filter(slug=slug).first()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'research': Researchs,
               'ab': abouts,
               'rs': researchScientists,
               'rg': researchGrants,
               'rp': researchPublications,
               'ri': researchInformation,
               'se': scientificExpeditions
               }
    return render(request, 'research/research_scientist_example.html', context)


def research_grants_example(request, slug):
    abouts = about.objects.all()
    Researchs = researchGrant.objects.filter(slug=slug).first()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'research': Researchs,
               'ab': abouts,
               'rs': researchScientists,
               'rg': researchGrants,
               'rp': researchPublications,
               'ri': researchInformation,
               'se': scientificExpeditions
               }
    return render(request, 'research/research_grant_example.html', context)


def research_publications_example(request, slug):
    abouts = about.objects.all()
    Researchs = scientificPublication.objects.filter(slug=slug).first()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'research': Researchs,
               'ab': abouts,
               'rs': researchScientists,
               'rg': researchGrants,
               'rp': researchPublications,
               'ri': researchInformation,
               'se': scientificExpeditions
               }
    return render(request, 'research/research_publications_example.html', context)


def research_information_example(request, slug):
    abouts = about.objects.all()
    Researchs = informationResearch.objects.filter(slug=slug).first()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'research': Researchs,
               'ab': abouts,
               'rs': researchScientists,
               'rg': researchGrants,
               'rp': researchPublications,
               'ri': researchInformation,
               'se': scientificExpeditions
               }
    return render(request, 'research/research_IR_example.html', context)


def scientific_expeditions_example(request, slug):
    abouts = about.objects.all()
    Researchs = scientificExpedition.objects.filter(slug=slug).first()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {'research': Researchs,
               'ab': abouts,
               'rs': researchScientists,
               'rg': researchGrants,
               'rp': researchPublications,
               'ri': researchInformation,
               'se': scientificExpeditions
               }
    return render(request, 'research/research_scientific_example.html', context)


# image Dropdown
def research_exam_slug(request, slug):
    rsres = research_example_down_scientists.objects.filter(slug=slug).first()
    context = {'resrchesg': rsres}
    return render(request, 'research/research_example.html', context)


def research_exam_slug(request, slug):
    rsres = research_example_down_scientists.objects.filter(slug=slug).first()
    context = {'resrchesg': rsres}
    return render(request, 'research/research_example.html', context)


def research_exam_resgr(request, slug):
    resgr = research_example_down_resgran.objects.filter(slug=slug).first()
    context = {'grants': resgr}
    return render(request, 'research/down_res_grants.html', context)


def research_exam_public(request, slug):
    publica = research_example_down_sp.objects.filter(slug=slug).first()
    context = {'publct': publica}
    return render(request, 'research/down_publications.html', context)
    # return render(request,'research/research_scientific_example.html',context)
    # return HttpResponse("fbjfns")

# def research_drop_example(request,slug,slug_drop):
#     Researchs_Drops = research_drop.objects.filter(slug=slug,slug_drop=slug_drop).first()
#     context = {'research_drop':Researchs_Drops}
#     return render(request,'research_drop.html',context)(drop-dowm-->dropdowm through cms / made by priyanshi)

def tender(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, 'tender.html', context)
    # return HttpResponse("hello")


def tenderTable(request):
    c=myclass.objects.all()
    cd=c.exclude(closingdate__lte=datetime.today())
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'co':cd,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/tenderTable.html", context)

def CorrigendumTable(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/CorrigendumTable.html", context)
def ProcurementTable(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/ProcurementTable.html", context)
def PanelmentTable(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/PanelmentTable.html", context)
def EnquiryTable(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/EnquiryTable.html", context)
def GeMTable(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/GeMTable.html", context)

def tenderArchive(request):
    c=myclass.objects.filter(closingdate__lte=datetime.today())
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'co':c,
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "tender/tenderArchive.html", context)


# career
def careers(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "career.html", context)

def careerArchive(request):
    abouts = about.objects.all()
    researchScientists = researchScientist.objects.all()
    researchGrants = researchGrant.objects.all()
    researchPublications = scientificPublication.objects.all()
    researchInformation = informationResearch.objects.all()
    scientificExpeditions = scientificExpedition.objects.all()
    context = {
        'ab': abouts,
        'rs': researchScientists,
        'rg': researchGrants,
        'rp': researchPublications,
        'ri': researchInformation,
        'se': scientificExpeditions
    }
    return render(request, "careerArchive.html", context)

