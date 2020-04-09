#Encriptador e Desencriptador (Script)

def change_files(filename, cryptoFn, block_size = 16):

    whith open(filename, 'r+b') as _file: #Abriu arquivo no modo de leitura e escrita binária
        raw_value = _file.read(block_size)
        while raw_value:
            cipher_value = cryptoFn(raw_value)
            #Compara o tamanho do bloco cifrado e plano (plaintext)
            if len(raw_value) != len(cipher_value):
                raise ValueError("O valor cifrado {} tem um tamanho diferente do valor plano {}" .format(len(cipher_value), len(raw_value)))

            _file.seek(-len(raw_value), 1)
            _file.write(cipher_value)
            raw_value = _file.read(block_size)
