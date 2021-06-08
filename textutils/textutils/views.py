#Created for practice

from django.http import HttpResponse
from django.shortcuts import render

#def index(request):
#  return HttpResponse('''<h1>Hi Bilal</h1> <a href="https://youtube.com">Youtube</a></br> <a href="https://linkedin.com">LinkedIn</a></br> <a href="https://facebook.com">Facebook</a></br> <a href="https://gmail.com">Gmail</a></br>''');

#def about(request):
#  return HttpResponse("About Us");

#def index(request):
#  params = {"name": "Bilal", "place": "Karachi"}
#  return render(request, 'index.html', params);

def index(request):
  return render(request, 'index.html');

def analyze(request):
      
  # Get the text
  djtext = request.POST.get("text", "default")
  
  # Get checkbox values
  removepunc = request.POST.get("removepunc", "off")
  fullcaps = request.POST.get("fullcaps", "off")
  charcount = request.POST.get("charcount", "off")
  newlineremover = request.POST.get("newlineremover", "off")
  extraspaceremove = request.POST.get("extraspaceremove", "off")
  
  # Check which of the checkboxes is on/ticked
  '''analyzed = djtext'''
  if (removepunc == "on"):
    punctuations = ''':;()-[]{}'"\/*?><$%^&#@'''
    analyzed=""
    for char in djtext:
          if char not in punctuations:
                analyzed = analyzed + char
    params = { "purpose": "Remove Punctuations", "analyzed_text": analyzed}
    djtext = analyzed
    # Analyze the text
    #return render(request, 'Analyzed.html', params);
  
  if (fullcaps == "on"):
    analyzed=""
    for char in djtext:
        analyzed = analyzed + char.upper()
    params = { "purpose": "Changed To Uppercase", "analyzed_text": analyzed}
    djtext = analyzed
    # Analyze the text
    #return render(request, 'Analyzed.html', params);
  
  if (newlineremover == "on"):
    analyzed=""
    for char in djtext:
      if char !="\n" and char !="\r":
        analyzed = analyzed + char
      else:
        print("no")
    print("pre", analyzed)
    params = { "purpose": "Remove New Lines", "analyzed_text": analyzed}
    djtext = analyzed
    # Analyze the text
    #return render(request, 'Analyzed.html', params);
  
  if (extraspaceremove == "on"):
    analyzed=""
    for index, char in enumerate(djtext):
      if not (djtext[index] == " " and djtext[index + 1] == "  "):
        analyzed = analyzed + char
    params = { "purpose": "Remove Extra Spaces", "analyzed_text": analyzed}
    djtext = analyzed
    # Analyze the text
    #return render(request, 'Analyzed.html', params);
  
  if (charcount == "on"):
    # Count string and convert the counted integer to string to print additional string
    analyzed = str(len(djtext)) + " characters"
    analyzed = djtext + '\n' + analyzed
    params = { "purpose": "Character Count", "analyzed_text": analyzed}
    # Analyze the text
    #return render(request, 'Analyzed.html', params);

  # Print error if no box is checked
  #else:
    #return HttpResponse("Error, You've not selected to do anything yet!")
  if (removepunc != "on" and fullcaps != "on" and newlineremover != "on" and extraspaceremove != "on" and charcount != "on"):
    return HttpResponse("No operation selected. Please try again!")
  return render(request, 'Analyzed.html', params);

#def capfirst(request):
#  return HttpResponse("capitalize first");

#def newlineremove(request):
#  return HttpResponse("new line remover");

#def spaceremove(request):
#  return HttpResponse("space remover");

#def charcount(request):
#  return HttpResponse("char counter");

#def newlineremove(request):
#  return HttpResponse("newlineremove");


def about(request):
  return render(request, 'about.html');

def contact(request):
  return render(request, 'contact.html');