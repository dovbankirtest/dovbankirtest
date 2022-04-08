import os

ver1 = os.getenv('PTESTVERSION', 'noo1')
ver2 = os.getenv('PTESTVERSION_GA', 'noo2')
ver3 = os.getenv('MYVAR', 'noo3')


def test1():
    print(' =+=' + ver1)
    print(' =+=' + ver2)
    print(' =+=' + ver3)
    assert ver2 == '6.2.5'
