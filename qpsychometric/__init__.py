import pkgutil
import importlib

__all__ = []  # Start with an empty export list


# Relative imports for intra-package imports, adjust as necessary
package_name = __name__

# Dynamically import all subpackages and modules
for loader, module_name, is_pkg in pkgutil.walk_packages(__path__, package_name + '.'):
    # Import the module
    module = importlib.import_module(module_name)

    # Add all names defined in the module's __all__ to the current module's __all__
    if hasattr(module, '__all__'):
        __all__.extend(module.__all__)  # Import specific names to be exposed

        # Dynamically add imported names to globals() for 'from package import *' behavior
        for name in module.__all__:
            module_questions = getattr(module, name)
            globals()[name] = module_questions
