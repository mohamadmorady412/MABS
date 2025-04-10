import os, importlib

def import_modules_from_folder(folder_path, package_name):
    for filename in os.listdir(folder_path):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            importlib.import_module(f"{package_name}.{module_name}")