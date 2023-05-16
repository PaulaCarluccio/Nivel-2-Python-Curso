def decorador(f):
    def f2():
        print("f2 ...")
        f()
    return f2

@decorador
def f1():
    print("f1 ...")

f1()