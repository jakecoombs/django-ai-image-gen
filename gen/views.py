from django.http import HttpResponse
from django.shortcuts import render

from gen.forms import ImageGeneratorForm


def index(request):
    return HttpResponse("Create an image")


def generate_image(request):
    if request.method == "POST":
        form = ImageGeneratorForm(request.POST)
        if form.is_valid():
            # Generate Image
            print("done")

    else:
        form = ImageGeneratorForm()

    return render(request, "gen/generate_image.html", {"form": form})
