import os

from django.shortcuts import render
from openai import OpenAI
from openai.types import ImagesResponse

from gen.forms import ImageGeneratorForm

NUM_IMAGES = 1
SIZE = "256x256"
MODEL = "dall-e-2"

client = OpenAI(api_key=os.getenv("OPENAI_KEY"))


def get_images_from_openai(prompt: str) -> list[str]:
    response: ImagesResponse = client.images.generate(
        prompt=prompt, n=NUM_IMAGES, size=SIZE, model=MODEL
    )

    return [image.url for image in response.data]


def generate_image(request):
    if request.method == "POST":
        form = ImageGeneratorForm(request.POST)
        if form.is_valid():
            try:
                images: list[str] = get_images_from_openai(**form.cleaned_data)
                return render(
                    request, "gen/generate_image.html", {"form": form, "images": images}
                )
            except Exception as e:
                return render(
                    request,
                    "gen/generate_image.html",
                    {"form": form, "error_message": str(e)},
                )

    else:
        form = ImageGeneratorForm()

    return render(request, "gen/generate_image.html", {"form": form})
