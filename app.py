import os
import shutil

# Obter o caminho atual (diretório onde o script está rodando)
cwd = os.getcwd()

# Retornar todos os arquivos do diretório atual
lista = os.listdir(cwd)

# Loop para cada item na lista
for i in lista:
    # Pegar a extensão do arquivo (ex: 'txt', 'jpg')
    tipo_arquivo = i.split('.')[-1]
    
    # Verificar se já existe uma pasta com o nome da extensão
    verificar_pasta = os.path.exists(tipo_arquivo)
    
    # Checar se é um arquivo (e não uma pasta)
    if os.path.isfile(i):
        # Se não for um arquivo .py
        if not '.py' in i:
            
            # Se a pasta correspondente à extensão não existe, cria ela
            if not verificar_pasta:
                os.mkdir(tipo_arquivo)
            
            # Mover o arquivo para a pasta da extensão
            shutil.move(i, tipo_arquivo + '/' + i)
        else:
            # Arquivo Python não será movido
            pass
