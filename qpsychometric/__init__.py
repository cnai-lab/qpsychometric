import os
import importlib

__all__ = ["all_psychometrics"]

all_psychometrics={}

package_directory = os.path.dirname(__file__)  # Get the directory of the current package
package_name = __name__

# List only the top-level directories (modules) directly under the package directory
for entry in os.listdir(package_directory):
    if os.path.isdir(os.path.join(package_directory, entry)) and not entry.startswith('_'):
        # Construct the module name
        module_name = f"{package_name}.{entry}"
        # Import the module
        module = importlib.import_module(module_name)
        if hasattr(module, '__all__'):
            questionnaire_metric = module.__all__[0]
            all_psychometrics[questionnaire_metric]=getattr(module, questionnaire_metric)

