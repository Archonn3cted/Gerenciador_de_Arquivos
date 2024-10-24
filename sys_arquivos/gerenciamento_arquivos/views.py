from django.shortcuts import render, get_object_or_404, redirect
from .models import Arquivo, Bloco

def criar_arquivo(request):
    if Bloco.objects.count() == 0:
        criar_blocos_iniciais()

    if request.method == 'POST':
        nome = request.POST.get('nome')
        conteudo = request.POST.get('conteudo')
        tamanho = len(conteudo)
        
        blocos_livres = Bloco.objects.filter(ponteiro__isnull=True, conteudo='')[:tamanho]
        if len(blocos_livres) < tamanho:
            return render(request, 'app_arquivos/criar_arquivo.html', {'erro': f'Memória insuficiente: {len(blocos_livres)} blocos livres disponiveis, {tamanho} necessários'})

        primeiro_bloco = blocos_livres[0]
        arquivo = Arquivo.objects.create(nome=nome, tamanho=tamanho, endereco_inicial=primeiro_bloco)

        for i, char in enumerate(conteudo):
            bloco_atual = blocos_livres[i]
            bloco_atual.conteudo = char
            bloco_atual.ponteiro = blocos_livres[i + 1].id if i < tamanho - 1 else None
            bloco_atual.save()
        
        return redirect('ler_arquivo', nome=nome)
    
    return render(request, 'app_arquivos/criar_arquivo.html')

def criar_blocos_iniciais():
    total_blocos = 32
    for _ in range(total_blocos):
        Bloco.objects.create(conteudo='', ponteiro=None)

def ler_arquivo(request, nome):
    arquivo = get_object_or_404(Arquivo, nome=nome)
    bloco_atual = arquivo.endereco_inicial
    conteudo = []
    
    while bloco_atual:
        conteudo.append(bloco_atual.conteudo)
        bloco_atual = Bloco.objects.filter(id=bloco_atual.ponteiro).first()
    
    return render(request, 'app_arquivos/ler_arquivo.html', {'arquivo': arquivo, 'conteudo': ''.join(conteudo)})

def deletar_arquivo(request, nome):
    arquivo = get_object_or_404(Arquivo, nome=nome)
    bloco_atual = arquivo.endereco_inicial
    
    while bloco_atual:
        proximo_bloco = Bloco.objects.filter(id=bloco_atual.ponteiro).first()
        bloco_atual.conteudo = ''
        bloco_atual.ponteiro = None
        bloco_atual.save()
        bloco_atual = proximo_bloco
    
    arquivo.delete()
    return redirect('lista_blocos')

def lista_arquivos(request):
    if request.method == 'POST' and 'delete_all' in request.POST:
        Arquivo.objects.all().delete()
        Bloco.objects.all().update(conteudo='', ponteiro=None)
    blocos = Bloco.objects.all()
    arquivos = Arquivo.objects.all()
    blocos_info = []
    for bloco in blocos:
        arquivo_relacionado = Arquivo.objects.filter(endereco_inicial=bloco).first()
        if bloco.conteudo:
            blocos_info.append({
                'bloco': bloco,
                'ocupado': True,
                'arquivo': arquivo_relacionado.nome if arquivo_relacionado else 'Desconhecido'
            })
        else:
            blocos_info.append({
                'bloco': bloco,
                'ocupado': False,
                'arquivo': None
            })

    return render(request, 'app_arquivos/lista_blocos.html', {'blocos_info': blocos_info, 'arquivos': arquivos})
