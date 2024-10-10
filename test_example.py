from hack import suma, restar, lista, texto, texto_upper



def test_suma():
    assert 1 + 1  == 2


def test_restar():
    assert 2 - 1 == 1



#
def test_compare_sum():
    r = suma()
    token = False
    if r == 2:
        token = True
    assert token == True


def test_compare_subtract():
    r = restar()
    token = False
    if r == 1:
        token = True
    
    res = isinstance(r, int)
    assert(r, int, token) == (res, int, True)  


def test_compare_list():
    r = lista()
    token_ls = False
    token_len = False

    if r == ["foo","bar","charlie"]:
        token_ls = True
    
    if len(r) == 3:
        token_len = True

    assert(token_ls, token_len) == (True, True)


def test_compare_string():
    check = "hola"
    assert texto(check) == "hola"


def test_compare_upper():
    check = "hola"
    assert texto_upper(check) == "HOLA"

