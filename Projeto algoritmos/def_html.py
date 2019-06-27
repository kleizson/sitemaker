#função para criar um arquivo html

def open_doc(code,name_html):
    Doc_html = open(f'{name_html}.html','w')
    Doc_html.write(code)
    Doc_html.close()

#Função para criação da galeria de fotos

def site_gallery():
    Gallery = 'div.gallery {margin: 5px;border: 1px solid #ccc;float: left;width: 180px;box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);background-color:white;margin-top: 10%;}div.gallery:hover {border: 1px solid #777; }div.gallery img {width: 100%;height: 125px;}div.desc {padding: 15px;text-align: center;}'
    name_html = input('Digite o nome do Arquivo HTML que será criado: ')
    title_page = input('Digite o titulo na página: ')
    title_site = input('Digite o nome do seu site: ')
    background_color = input('Digite a cor que deseja(em hexadecimal ou em inglês): ')
    background = 'body {background-color:' f'{background_color}' ';-webkit-animation-name: example; /* Safari 4.0 - 8.0 */-webkit-animation-duration: 10s; /* Safari 4.0 - 8.0 */animation-name: example;animation-duration: 10s;}/* Safari 4.0 - 8.0 */@-webkit-keyframes example {from {background-color: #53917E;}to {background-color:'f'{background_color}' ';}}/* Standard syntax */@keyframes example {from {background-color: #53917E;}to {background-color: 'f'{background_color}'';}}.titulo_site{font-size:100px;text-align: center; margin-bottom:-50%; margin-top:0%;font-family:Calibri;color:white;-webkit-text-stroke-width: 2px; /* largura da borda */-webkit-text-stroke-color: #000; /* cor da borda */}'
    num_image = int(input('Digite quantas fotos você quer adicionar: '))
    if num_image == 1:
        link_image = input('Digite o link da sua imagem: ')
        description_image = input('Digite a descrição da sua imagem: ')
        code = f'<!DOCTYPE html><html lang="pt-br"><head><meta charset="iso-8859-1"><title>{title_page}</title><style>{Gallery}{background}</style></head><body><h1 class="titulo_site">{title_site}</h1><div class="gallery"><a target="_blank" href="{link_image}"><img src={link_image} width="600" height="400"></a><div class="desc">{description_image}</div></div><!--newgallery--></body></html>'
        open_doc(code,name_html)
        print('Site criado com sucesso!')
    elif num_image > 1:
        div_list = []
        background = 'body {background-color:'f'{background_color}'';-webkit-animation-name: example; /* Safari 4.0 - 8.0 */-webkit-animation-duration: 10s; /* Safari 4.0 - 8.0 */animation-name: example;animation-duration: 10s;}/* Safari 4.0 - 8.0 */@-webkit-keyframes example {from {background-color: #53917E;}to {background-color:'f'{background_color}'';}}/* Standard syntax */@keyframes example {from {background-color: #53917E;}to {background-color: 'f'{background_color}'';}}.titulo_site{font-size:100px;text-align: center; margin-bottom:-50%; margin-top:0%;font-family:Calibri;color:white;-webkit-text-stroke-width: 2px; /* largura da borda */-webkit-text-stroke-color: #000; /* cor da borda */}'
        for i in range(num_image):
            link_image = input('Digite o link da sua imagem: ')
            description_image = input('Digite a descrição da sua imagem: ')
            div_Gallery = f'<div class="gallery"><a target="_blank" href="{link_image}"><img src={link_image} width="600" height="400"></a><div class="desc">{description_image}</div></div>'
            div_list.append(div_Gallery)
        div_list.append('<!--newgallery-->')
        string_div = ''.join(map(str, div_list))
        code = f'<!DOCTYPE html><html lang="pt-br"><head><meta charset="iso-8859-1"><title>{title_page}</title><style>{Gallery}{background}</style></head><body><h1 class="titulo_site">{title_site}</h1>{string_div}</body></html>'
        open_doc(code,name_html)
        print('Site criado com sucesso!')

#Função para criação do blog

def site_blog():
    name_html = input('Digite o nome do Arquivo HTML que será criado: ')
    title_page = input('Digite o titulo na página: ')
    name_blog = input('Digite o nome do seu blog: ')
    about_me = input('Digite sobre você: ')
    img_perfil = input('Digite o link da sua imagem de perfil: ')
    first_post = input('Deseja fazer um primeiro post agora?(coloque sim ou não): ')
    post_mini = first_post.lower()
    if post_mini == 'sim':
        img_post = input('Digite o link da imagem do post: ')
        post = input('Digite a legenda do post: ')
        code = f'<!DOCTYPE html><html lang="pt-br"><head><meta charset="iso-8859-1"><title>{title_page}</title></head><body style="background:black;"><div style="z-index:1;background: black;width:102%;margin-left:-20px;margin-right:2px;margin-top:-10px;z-index: 0;" ><span><img style="border-radius: 100%;height: 200px;object-fit: cover;width: 200px;margin-right:30%;margin-left:43%;margin-top: 5%;" src="{img_perfil}"></span><h1 style="color:white;text-align:center;">{name_blog}</h1><p style="text-align:center;color:white;font-size:20px;">{about_me}</p><hr style="background-color:black; border:none;"><div><div style="text-align:center;background:white; width:300px;margin-left: auto;margin-right: auto;  "></div><div style="border: 1px solid #777;width:700px;margin-left: auto;margin-right: auto; background-color:white;  "><img style="width: 700px;display: block;" src="{img_post}"><hr style="height:2px;color: black;background-color: black;border: none; "><p style="margin-top:-2px;font-style: italic;margin-left:5px;color:#084d6e;font-size:20px; "><strong>{name_blog}</strong></p><p style="text-align:left;margin-left:5px;margin-top:-15px;font-family: Times New Roman;font-size:15px;color:black;">{post}</p></div><hr style="height:3px;color: black;background-color:#1F2041;border: none;width:700px;"></div><!--newpost--></body></html>'
        open_doc(code, name_html)
        print('Site criado com sucesso!')
    elif post_mini == 'não':
        code = f'<!DOCTYPE html><html lang="pt-br"><head><meta charset="iso-8859-1"><title>{title_page}</title></head><body style="background:black;"><div style="z-index:1;background: black;width:102%;margin-left:-20px;margin-right:2px;margin-top:-10px;z-index: 0;" ><span><img style="border-radius: 100%;height: 200px;object-fit: cover;width: 200px;margin-right:30%;margin-left:43%;margin-top: 5%;" src="{img_perfil}"></span><h1 style="color:white;text-align:center;">{name_blog}</h1><p style="text-align:center;color:white;font-size:20px;">{about_me}</p><hr style="background-color:black; border:none;"><!--newpost--></body></html>'
        open_doc(code,name_html)
        print('Site criado com sucesso!')
    else:
        print('Opção invalida!')

#Função para criar o site de divulgação de eventos

def site_event():
    name_html = input('Digite o nome do Arquivo HTML que será criado: ')
    name_event = input('Digite o nome do Evento a ser divulgado: ')
    image_event = input('Digite o link do Banner do Evento: ')
    local = input('Digite o endereço do Evento: ')
    hour_event = input('Digite data e a hora do Evento: ')
    about_event = input('Digite sobre o que é o evento: ')
    code = f'<!DOCTYPE html><html><head></head><body ><div style="text-align: center; margin-top:-21px; width:102%; margin-left:-20px;    background:black; height:50px; color:white;  "><h1>{name_event}</h1></div><div style="background-image: -webkit-linear-gradient(270deg,rgba(0,0,0,.2),rgba(0,0,0,.2)) , url({image_event}); background-image: linear-gradient(180deg,rgba(0,0,0,.2),rgba(0,0,0,.2)) , url({image_event});position: absolute;width: 100%;height: 50%;background-size: auto, cover;background-repeat: repeat, no-repeat; margin-left:-8px;-webkit-filter: blur(4px);filter: blur(4px);  ">	</div><div><img style="width:52%;height:52%;border-radius:10%;display: block;margin-left: auto;margin-right: auto; margin-top:-7px;box-shadow: 0 10px 8px 0 rgba(0, 0, 0, 0.2), 0 6px 20px 0 rgba(0, 0, 0, 0.19);-webkit-filter: blur(4px);filter: blur(0px);" src="{image_event}"></div><div><h1 style="font-size: 30px;line-height: 100%;font-weight: 900;letter-spacing: 0.2px;color:#111111; margin-top:30px;  margin-left:350px;font-family:calibri;">{name_event}</h1><span><img style="display: inline; width:16px; height:16px;margin-left:350px; " align="left" src="https://images.vexels.com/media/users/3/154655/isolated/preview/71dccbb077597dea55dfc5b7a7af52c4---cone-de-contato-do-pino-de-localiza----o-by-vexels.png"><p style="margin-left:350px;">{local}</p></span><span><img style="display: inline; width:16px; height:16px;margin-left:350px;"align="left" src="http://www.naturezaevida.com.br/lojas/icones/horario.png"><p style="margin-left:368px;">{hour_event}</p></span><h1 style="font-size: 20px;line-height: 100%;font-weight: 900;letter-spacing: 0.2px;color:#111111;font-family:calibri;  margin-left:350px;">Sobre o Evento:</h1><p style="margin-left:350px;font-size: 18px;line-height: 100%;">{about_event}</p></div></body></html>'
    open_doc(code,name_html)
    print('Site criado com sucesso!')

#Função para editar a galeria de fotos

def edit_gallery():
    name_html = input('Digite o nome do seu arquivo HTML (coloque somente o nome): ')
    num_image = int(input('Digite quantas fotos você deseja adicionar: '))
    div_list = []
    for i in range(num_image):
        link_image = input('Digite o link da sua imagem: ')
        description_image = input('Digite a descrição da sua imagem: ')
        div_Gallery = f'<div class="gallery"><a target="_blank" href="{link_image}"><img src={link_image} width="600" height="400"></a><div class="desc">{description_image}</div></div>'
        div_list.append(div_Gallery)
    div_list.append('<!--newgallery-->')
    string_div = ''.join(map(str, div_list))
    Doc_html = open(f'{name_html}.html', 'r')
    for line in Doc_html:
        if line.find('<!--newgallery-->'):
            Doc_htm = open(f'{name_html}.html', 'w')
            new_div = line.replace('<!--newgallery-->', string_div)
            Doc_htm.write(new_div)
    Doc_htm.close()
    print('Site editado com sucesso!')

#Função para editar o blog

def edit_blog():
    name_html = input('Digite o nome do seu arquivo HTML (coloque somente o nome): ')
    name_user = input('Digite o nome do usúario que irá postar: ')
    img_post = input('Digite o link da imagem do post: ')
    post = input('Digite a legenda do post: ')
    add_post = f'<div><div style="text-align:center;background:white; width:300px;margin-left: auto;margin-right: auto;  "></div><div style="border: 1px solid #777;width:700px;margin-left: auto;margin-right: auto; background-color:white;  "><img style="width: 700px;display: block;" src="{img_post}"><hr style="height:2px;color: black;background-color: black;border: none; "><p style="margin-top:-2px;font-style: italic;margin-left:5px;color:#084d6e;font-size:20px; "><strong>{name_user}</strong></p><p style="text-align:left;margin-left:5px;margin-top:-15px;font-family: Times New Roman;font-size:15px;color:black;">{post}</p></div><hr style="height:3px;color: black;background-color:#1F2041;border: none;width:700px;"></div>'
    list_post = [add_post,'<!--newpost-->']
    string_post = ''.join(map(str, list_post))
    Doc_html = open(f'{name_html}.html', 'r')
    for line in Doc_html:
        if line.find('<!--newpost-->'):
            Doc_htm = open(f'{name_html}.html', 'w')
            new_post = line.replace('<!--newpost-->',string_post)
            Doc_htm.write(new_post)
    Doc_htm.close()
    print('Site editado com sucesso!')




