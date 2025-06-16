from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from .forms import FormularioContacto


def cv(request):
    if request.method == 'POST':
        # Si el método es POST, procesamos el formulario
        form = FormularioContacto(request.POST)
        if form.is_valid():
            # Si el formulario es válido, procedemos a enviar el correo
            nombre = form.cleaned_data['nombre']
            email = form.cleaned_data['email']
            asunto = form.cleaned_data['asunto']
            mensaje_form = form.cleaned_data['mensaje']

            # Construimos el cuerpo del email
            mensaje_html = f"""
            <p>Has recibido un nuevo mensaje desde tu página de CV:</p>
            <ul>
                <li><strong>Nombre:</strong> {nombre}</li>
                <li><strong>Email del remitente:</strong> {email}</li>
                <li><strong>Asunto:</strong> {asunto}</li>
            </ul>
            <hr>
            <p><strong>Mensaje:</strong></p>
            <p>{mensaje_form}</p>
            """
            
            try:
                send_mail(
                    subject=f'Nuevo Contacto CV: {asunto}', # Asunto del email que recibirás
                    message='', # El mensaje de texto plano (opcional si usas html)
                    from_email=settings.EMAIL_HOST_USER, # El email que envía (configurado en settings)
                    recipient_list=[settings.EMAIL_HOST_USER], # A quién se le envía (¡a ti mismo!)
                    html_message=mensaje_html, # El mensaje en formato HTML
                    fail_silently=False,
                )
                # Mensaje de éxito para el usuario
                messages.success(request, '¡Tu mensaje ha sido enviado con éxito! Gracias por contactar.')
            except Exception as e:
                # Mensaje de error si algo falla
                messages.error(request, f'Hubo un error al enviar el mensaje: {e}')

            # Redirigimos a la misma página para evitar reenvíos del formulario
            return redirect('cv') 
    else:
        # Si el método es GET, simplemente mostramos un formulario vacío
        form = FormularioContacto()

    return render(request, 'cv.html', {'form': form})

def inicio(request):
    contexto = {'nombre': 'Usuario'}
    return render(request, 'index.html', contexto)

def saludo(request):
    return HttpResponse("¡Hola, desde mi vista de Django!")

def saludar_usuario(request, nombre):
    return HttpResponse(f"Hola, {nombre}!")

def edad(request, edad):
    return HttpResponse(f"Hola, tienes {edad} años!")
