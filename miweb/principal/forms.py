from django import forms

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Tu Nombre',
        'class': 'form-control'
    }))
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={
        'placeholder': 'tu.email@ejemplo.com',
        'class': 'form-control'
    }))
    asunto = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={
        'placeholder': 'Asunto del mensaje',
        'class': 'form-control'
    }))
    mensaje = forms.CharField(widget=forms.Textarea(attrs={
        'placeholder': 'Escribe tu mensaje aquí...',
        'class': 'form-control',
        'rows': 5
    }))