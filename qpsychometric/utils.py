from pathlib import Path
import importlib
import os
import importlib.util

def load_questions(pattern='_qmnli.py'):
    base_path = Path('')
    questions = []
    for questionnaire_path in list(base_path.glob(f'**/*{pattern}')):
        # questionnaire_path = questionnaire_path.relative_to(base_path.__path__[0])
        name = questionnaire_path.name.replace(".py", "")
        file = questionnaire_path
        module_path = str(questionnaire_path.parent).replace('/', '.') + f'.{name}'
        module = importlib.import_module(module_path)
        if hasattr(module, name):
            print('load:', name)
            questions += getattr(module, name)
            
    return questions


def extract_all_questions(root_dir):
    all_questions = []

    # Walk through the directory structure
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith('_qmnli.py'):
                # Construct the file path
                file_path = os.path.join(dirpath, filename)

                # Dynamically import the file as a module
                module_name = filename.replace('.py', '')
                spec = importlib.util.spec_from_file_location(module_name, file_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)

                # Access the global variable 'all_questions' if it exists
                if hasattr(module, 'all_questions'):
                    all_questions.extend(module.all_questions)

    return all_questions

    