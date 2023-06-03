from .models import Link

def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.Key] = link.url
    return ctx
    #Esto extiende el contexto global
    #Diccionario paea redes sociales 
    #Cuidar el como es que se escribe y se mandan aa traer los campos de los models
    
