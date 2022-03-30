import os

ver1 = os.getenv('VERRS', 'noo1')
ver2 = os.getenv('PTESTVERSION', 'noo2')

def test1():
    print(ver1 + '====' + ver2)
    assert ver1 == '6.2.5'
