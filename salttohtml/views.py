from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context, RequestContext
from django.http import HttpResponse
from .forms import SaltCodeForm
from .controller import doConvert
from .mapper import toConverterPayload


def convert_page(request):
	result1 = []
	result2 = []
	formSaltCode = SaltCodeForm(request.POST or None)
	if formSaltCode.is_valid():
		payload = toConverterPayload(formSaltCode.cleaned_data['salt_code'])
		result1, result2 = doConvert(payload)
	else:
		formSaltCode = SaltCodeForm()
	context = {
		"formSaltCode" : formSaltCode,
		"converterResult1" : result1,
		"converterResult2" : result2,
	}
	return render(request, "./pages/page_convert.html", context)


def home_page(request):
	context = RequestContext(request).flatten()
	return render(request, "./pages/page_home.html", context)


def guides_page(request):
	context = RequestContext(request).flatten()
	return render(request, "./pages/page_guides.html", context)

def preview_page1(request):
	if request.method == "POST":
		result = request.POST.get("converterResult")
		context = {
			"converterResult" : result,
		}
		return render(request, "./pages/page_preview.html", context)


def preview_page2(request):
	if request.method == "POST":
		result = request.POST.get("converterResult")
		context = {
			"converterResult" : result,
		}
		return render(request, "./pages/page_preview.html", context)