import inspect

available_functions = {}
available_constants = {}
module = __import__("math")
builtins = __import__("builtins")
available_functions_names_of_module = filter(lambda x: not x.startswith("_"), dir(module))

for avai_name in available_functions_names_of_module:
    obj = getattr(module, avai_name)
    if inspect.isfunction(obj) or inspect.isbuiltin(obj):
        available_functions.update({avai_name: obj})
    if isinstance(obj, int) or isinstance(obj, float):
        available_constants.update({avai_name: obj})

for avai_name in filter(lambda x: not x.startswith("_"), dir(builtins)):
    obj = getattr(builtins, avai_name)
    if inspect.isfunction(obj) or inspect.isbuiltin(obj):
        available_functions.update({avai_name: obj})
    if isinstance(obj, int) or isinstance(obj, float):
        available_constants.update({avai_name: obj})
