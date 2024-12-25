import os
import importlib

__all__ = ['social_biases_questionnaires']  # Start with an empty export list
social_biases_questionnaires={}

package_directory = os.path.dirname(__file__)  # Get the directory of the current package
package_name = __name__

# List only the top-level directories (modules) directly under the package directory
for entry in os.listdir(package_directory):
    if os.path.isdir(os.path.join(package_directory, entry)) and not entry.startswith('_'):
        # Construct the module name
        module_name = f"{package_name}.{entry}"
        # Import the module
        module = importlib.import_module(module_name)
        # Some modules don't have the __all__ global var, only packages.
        if hasattr(module, "__all__"):
            # Get the module global variable defined in `__all__`
            module_wild_card_var = module.__all__[0]
            module_questions = getattr(module, module_wild_card_var)
            # Get the questionnaire name
            questionnaire_name = module_questions['QMNLI'][0]()._descriptor['Questionnair']
            # Set the questionnaire as key and its global variables as the value.
            social_biases_questionnaires[questionnaire_name] = module_questions
            
            
