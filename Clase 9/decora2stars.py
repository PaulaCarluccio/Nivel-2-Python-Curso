def star(f):
    def wrapped():
        return '**' + f() + '**'
    return wrapped

def plus(f):
    def wrapped():
        return '++' + f() + '++'
    return wrapped

@star
@plus
def hello():
    return 'hello'

print(hello())