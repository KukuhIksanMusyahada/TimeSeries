import os


def GetThisDir():
    return os.path.dirname(os.path.abspath(__file__))

def GetDataSource():
    return os.path.abspath(
        os.path.join(GetThisDir(), os.pardir, 'DataSource')
    )
