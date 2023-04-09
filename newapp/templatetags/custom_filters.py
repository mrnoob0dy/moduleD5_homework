from django import template



register = template.Library() 

@register.filter(name='censor') 
def censor(value, arg): 
    bList = ['идиот', 'хрен']
    vEdit = value
    result = ''

    for w in bList:
        vTemp = vEdit.lower().replace(w, arg * len(w))
        vEdit = vTemp

    for i in range(0, len(value)):
        if (value[i] != vEdit[i]):
            result += vEdit[i].upper()
        else:
            result += vEdit[i]

    return result