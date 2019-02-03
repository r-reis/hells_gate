import inspect

def get_class(module):
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            return obj

def get_classes(modules):
    classes = []
    
    for module in modules:
        for name, obj in inspect.getmembers(module):
            classes.append(get_class(obj))

    return classes

def get_modules(module):
    modules = []

    for name, obj in inspect.getmembers(module):
        if inspect.ismodule(obj):
            modules.append(obj)

    return modules
