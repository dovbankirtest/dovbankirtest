import os

ver000 = os.getenv('PTESTVERSION22', 'nooON22')
ver00 = os.getenv('PTESTVERSION11', 'noo1')
ver0 = os.getenv('PTESTVERSION33', 'noo1')
ver1 = os.getenv('PTESTVERSION', 'noo1')
ver2 = os.getenv('PTESTVERSION_GA', 'noo2')
ver3 = os.getenv('MYVAR', 'noo3')
ver4 = os.getenv('PTESTV', 'noo4')
ver5 = os.getenv('PTESTV2', 'noo5')



def test1():
    print(' =+=' + ver000)
    print(' =+=' + ver00)
    print(' =+=' + ver0)
    print(' =+=' + ver1)
    print(' =+=' + ver2)
    print(' =+=' + ver3)
    print(' =+=' + ver4)
    print(' =+=' + ver5)
    assert ver2 == '6.2.5'
