from django.shortcuts import render
from django.http import HttpResponse
from . import my_code
from .models import SavedData
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import cm
from reportlab.lib.enums import TA_JUSTIFY

def home(request):
    # return HttpResponse('<h1>Sommaire Home</h1>')
    return render(request,'summarizer/home3.html')

# def home(request):
#     # return HttpResponse('<h1>Sommaire Home</h1>')
#     return render(request,'summarizer/home3_2.html')

def about(request):
    # return HttpResponse('<h1>Sommaire About Page</h1>')
    return render(request,'summarizer/about.html')

# def output(request):
#     if request.is_ajax():
#         py_obj = my_code.test_code(10)
#         return render(request, 'summarizer/output.html', {'output': py_obj})

# Create your views here.
# def output(request):
#     if request.method == 'GET':
#         txtInput = request.GET.get('txtInput')
#         # inputVal = request.POST['inputVal']
#         from simplet5 import SimpleT5
#         model = SimpleT5()        
#         model.load_model("t5","summarizer/T5/T5")
#         summaryContent = model.predict(txtInput)
#         context = {'summaryContent' : summaryContent[0], 'originalText' : txtInput}
#         #summaryContent = summaryContent
#         return render(request,'summarizer/home3.html',context)
summaryValue =None
def output(request):    
    if request.method == 'GET' and request.GET.get('txtInput')!=None:
        global summaryValue
        txtInput = request.GET.get('txtInput')
        # inputVal = request.POST['inputVal']
        from simplet5 import SimpleT5
        model = SimpleT5()        
        model.load_model("t5","summarizer/T5/T5")
        summaryContent = model.predict(txtInput)
        # summaryValue = "Hello World"
        summaryValue = summaryContent[0]
        context = {'summaryContent' : summaryValue, 'originalText' : txtInput}
        # generate_pdf(request,summaryValue)
        #summaryContent = summaryContent
        return render(request,'summarizer/home3.html',context)
    # elif request.method == 'POST':
    #     buffer = io.BytesIO()
    #     p = canvas.Canvas(buffer)
    #     p.drawString(100, 100, summaryValue)
    #     p.showPage()
    #     p.save()
    #     buffer.seek(0)
    #     return FileResponse(buffer, as_attachment=True, filename='hello.pdf')
        
    # if request.method == 'POST':

def generate_pdf(request):
    global summaryValue    
    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)
    textobject = p.beginText(2*cm, 29.7 * cm - 2 * cm)
    for line in summaryValue.splitlines(False):
        textobject.textLine(line.rstrip())
    p.drawText(textobject)
    p.showPage()
    p.save()
    buffer.seek(0)
    return FileResponse(buffer, as_attachment=True, filename='Summary.pdf')



    
        
