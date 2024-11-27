
if __name__=='__main__':
    print('Hello World')
    import pkgutil
    import traceback

    try:
        print(pkgutil.ImpImporter)
    except AttributeError as e:
        print(e)
        traceback.print_stack()