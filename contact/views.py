from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import EmailMessage #Para crear la estructura de mensaje
from .forms import ContactForm


def contact(request):
    contact_form = ContactForm()

    if request.method == "POST":
        contact_form = ContactForm(data=request.POST)
        if contact_form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            number = request.POST.get('number', '')
            asunt = request.POST.get('asunt', '')
            content = request.POST.get('content', '')
            #Enviamos el correo y redireccionamos 
            email = EmailMessage(
                "Pixsoft: Nuevo mensaje de contacto",
                "De {} <{}>\n\nEscribió:\n\n{}".format(name, email, content),
                "no-contestar@inbox.mailtrap.io",
                ["alexsintec173@gmail.com"],# Validación de emails para que el email se envie
                ["faty.aome.rojas14@gmail.com"],
                reply_to=[email]
            )

            # Lo enviamos y redireccionamos 
            # esto es por si falla el envio del mensaje
            try:
                email.send()
                # Todo ha ido bien, redireccionamos a OK
                return redirect(reverse('contact')+"?ok")
            except:
                # Algo no ha ido bien, redireccionamos a FAIL
                return redirect(reverse('contact')+"?fail")

    return render(request, "contact/contact.html",{'form':contact_form})