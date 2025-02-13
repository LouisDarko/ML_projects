from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."
def get_requirements(file_path : str) -> List[str]: 
    
    '''
    this function will return the list of requirements
    '''
    
    requirements = []
    with open(file_path) as file_obj :
        requirements = file_obj.readlines()
        requirements = [req.replace("\n", "") for req in requirements]
        
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

setup(
    name = "ML_PROJECT",
    version = "0.01",
    author = "Louis Darko",
    author_email = "louisdarko20@gmail.com",
    packages = find_packages(),
    install_requirements = get_requirements("requirements.txt")
)