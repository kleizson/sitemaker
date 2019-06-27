from def_html import *
print('Bem vindo ao Site Maker:\n  \nGaleria de fotos (1)          Blog (2) \nSite de Divulgação de eventos (3)       Editar um arquivo HTML (4)\n')
menu = int(input('Digite o número da opção desejada: '))
if menu == 1:
    site_gallery()
elif menu == 2:
    site_blog()
elif menu == 3:
    site_event()
elif menu == 4:
    print('\nAdicionar novas fotos a Galeria de fotos (1)\nAdicionar um novo post ao Blog (2)\n')
    edit_option = int(input('Digite a opção desejada: '))
    if edit_option == 1:
        edit_gallery()
    elif edit_option == 2:
        edit_blog()
    else:
        print('Opção Invalida!')
else:
    print('Opção Invalida!')
        


