from django import forms

IMAGE_SIZES = [
    "256x256",
    "512x512",
    "1024x1024",
]


class ImageGeneratorForm(forms.Form):
    prompt = forms.CharField(widget=forms.Textarea())
    size = forms.ChoiceField(choices={i: i for i in IMAGE_SIZES})
