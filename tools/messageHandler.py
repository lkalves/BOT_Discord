
def hasUserID(texto):
    return '<@!' in texto


def removeUserID(texto):
    if hasUserID(texto):
        nome_lista = [('270928429925269518', 'LK'), ('268198611941195776', 'Rafão'),
                      ('107332797332508672',
                       'Dashtail'), ('109427358162817024', 'Pseudão'),
                      ('112262967101255680',
                       'Luorhane'), ('115948020360675329', 'Itala'),
                      ('192460714512744448',
                       'Matiserguei'), ('112964615335321600', 'Peterola'),
                      ('114546184193835011',
                       'Paithias'), ('115948643722330119', 'Gijas'),
                      ('209833913336463362', 'Aloens')]

        a = texto.split('<@!')
        b = a[1].split('>')
        id = b[0]
        dicio = dict(nome_lista)
        search = dicio.get(id)

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
