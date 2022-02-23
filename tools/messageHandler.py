# LK#9609: o rafao é feio demais <@!268198611941195776>
# LK#9609: o lucas é lindo <@!270928429925269518>
# SUBSTRING, SPLIT, REGEX, REPLACE
# Extrai o ID e buscar o nome na API   await fetch_user(user_id)¶


def main():
    texto = ['LK#9609: o lucas é lindo <@!270928429925269518> o rafao é feio demais <@!268198611941195776>',
             'o rafao é feio demais <@!268198611941195776>']  # 270928429925269518
    # verifyUser(texto[0])

# CRIAR UM METODO PARA VERIFICAR SE EXISTE UM ID DE USUARIO NA MENSAGEM


def idToUser(id):
    id = removeUserID()
    return print(id)


def hasUserID(texto):
    return '<@!' in texto


def removeUserID(texto):
    if hasUserID(texto):
        # Metodo que tira o ID
        nome_lista = [('270928429925269518', 'LK'), ('268198611941195776', 'Rafão'),
                      ('107332797332508672', 'Dashtail'), ('109427358162817024', 'Pseudão')]

        a = texto.split('<@!')
        b = a[1].split('>')
        id = b[0]
        dicio = dict(nome_lista)
        search = dicio.get(id, 'Não encontrado')
        if search != 'Não encontrado':
            result = a[0] + '@'+search + b[1]
        return removeUserID(result)
    else:
        return texto


def verifyUser(texto):
    if hasUserID(texto):
        print('Contém ID')
        removeUserID(texto)
    else:
        print('Não contém ID')
        return texto


if __name__ == "__main__":
    main()
