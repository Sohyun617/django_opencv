from django import forms
from .models import ImageUploadModel

class SimpleUploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    image = forms.ImageField()
    #imageField(): filefield의 속성및 기능들을 동일하게 갖음 + 이미지파일 검증,자동저장 등 유용

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageUploadModel
        fields = ('description','document', ) #des 는 이미지 제목, doc는 내용
#
# 1) Hard-coded HTML : form, input, label, button, ...
# 2) forms.Form: 양식(Form class) 안에 받아들일 Field 선언
# 3) forms.ModelForm : Model class 안에 받아들일 Field를 선언,해당 클래스를 당겨와 활동
