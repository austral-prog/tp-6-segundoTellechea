def remove_elements(list_to_remove_elements):
    remove = list_to_remove_elements[:]

    if len(remove) > 5:
        del remove[5]
    if len(remove) > 4:
        del remove[4]
    if len(remove) > 0:
        del remove[0]

    return remove

def add_elements(list_to_add_elements):
    add = list_to_add_elements[:]

    add.insert(0, 'Pink')                 
    add.append('Yellow')       

    return add

def is_empty(list_to_check):
    if len(list_to_check) == 0:
        return True
    else:
        return False

def check_lists(list_to_compare1, list_to_compare2):
    lista1 = list_to_compare1[:] 
    lista2 = list_to_compare2[:] 

    if len(lista1) >= 3 and len(lista2) >= 3:
        if lista1[2] == lista2[2]:
            return True
        else:
            return False
    else:
        return False

def list_of_lists(listas):
    nueva = listas[:]  
    nueva[0] = nueva[0][:2]
    nueva[1] = nueva[1][1:4]
    nueva[2] = nueva[2][-2:]

    return nueva
