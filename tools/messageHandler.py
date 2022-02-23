# LK#9609: o rafao é feio demais <@!268198611941195776>
# LK#9609: o lucas é lindo <@!270928429925269518>
# SUBSTRING, SPLIT, REGEX, REPLACE
# Extrai o ID e buscar o nome na API   await fetch_user(user_id)¶


def main():
    texto = ['LK#9609: o lucas é lindo <@!270928429925269518> o rafao é feio demais <@!268198611941195776>',
             'o rafao é feio demais <@!268198611941195776>']  # 270928429925269518
    verifyUser(texto[0])

# CRIAR UM METODO PARA VERIFICAR SE EXISTE UM ID DE USUARIO NA MENSAGEM


def idToUser(id):
    id = removeUserID()
    return print(id)


def hasUserID(texto):
    return '<@!' in texto


def removeUserID(texto):
    if hasUserID(texto):
        # Metodo que tira o ID
        a = texto.split('<@!')
        b = a[1].split('>')
        id = b[0]
        result = a[0] + '@'+id + b[1]
        removeUserID(result)
    else:
        return texto


def verifyUser(texto):
    if hasUserID(texto):
        print('Contém ID')
        removeUserID(texto)
    else:
        print('Não contém ID')


if __name__ == "__main__":
    main()
