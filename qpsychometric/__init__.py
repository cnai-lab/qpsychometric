import os
import importlib
import pandas as pd
from .utils import QuestionnaireData

# __all__ = ["all_psychometrics"]

# all_psychometrics={}

# package_directory = os.path.dirname(__file__)  # Get the directory of the current package
# package_name = __name__

# # List only the top-level directories (modules) directly under the package directory
# for entry in os.listdir(package_directory):
#     if os.path.isdir(os.path.join(package_directory, entry)) and not entry.startswith('_') and not entry.startswith('.'):
#         # Construct the module name
#         module_name = f"{package_name}.{entry}"
#         # Import the module
#         module = importlib.import_module(module_name)
#         if hasattr(module, '__all__'):
#             questionnaire_metric = module.__all__[0]
#             all_psychometrics[questionnaire_metric]=getattr(module, questionnaire_metric)


__all__ = ["all_psychometrics"]

all_psychometrics = social_biases_questionnaires = pd.DataFrame([], columns=['category_name', 'questionnaire_name', 'questionnaire_task', 'question'])


package_directory = os.path.dirname(__file__)  # Get the directory of the current package
package_name = __name__

# List only the top-level directories (modules) directly under the package directory
for entry in os.listdir(package_directory):
    if os.path.isdir(os.path.join(package_directory, entry)) and not entry.startswith('_') and not entry.startswith('.'):
        # Construct the module name
        module_name = f"{package_name}.{entry}"
        # Import the module
        module = importlib.import_module(module_name)
        if hasattr(module, '__all__'):
            questionnaire_metric = module.__all__[0]
            wrapped_package_questions = getattr(module, questionnaire_metric)
            all_psychometrics = pd.concat([all_psychometrics, wrapped_package_questions.df], ignore_index=True)

        
        
all_psychometrics = QuestionnaireData(all_psychometrics)

# # Filter by category
# mental_health_questions = all_psychometrics.filter_by(category_name='mental_health_questionnaires')


# mental_health_questions.get_questions()
