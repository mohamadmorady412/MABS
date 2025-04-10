import os
import importlib

def import_modules_from_folder(folder_name, package_name):
    folder_path = os.path.join(os.path.dirname(__file__), "..", folder_name)
    for filename in os.listdir(folder_path):
        if filename.endswith(".py") and not filename.startswith("__"):
            module_name = filename[:-3]
            importlib.import_module(f"{package_name}.{module_name}")
