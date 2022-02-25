from tools.variaveis import changeUser


def hasUserID(texto):
    return '<@!' in texto


def removeUserID(texto):
    if hasUserID(texto):
        a = texto.split('<@!')
        b = a[1].split('>')
        id = b[0]
        search = changeUser(id)
        if search is not None:
            result = a[0] + '@'+search + b[1]
        else:
            result = a[0] + '@desconhecido' + b[1]

        return removeUserID(result)
    else:
        return texto


def verifyUser(texto):
    if hasUserID(texto):
        removeUserID(texto)
    else:
        return texto
