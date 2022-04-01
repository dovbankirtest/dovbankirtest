import os

ver2 = os.getenv('PTESTVERSION_GA', 'noo2')


def test1():
    print(' =+=' + ver2)
    assert ver2 == '6.2.5'
