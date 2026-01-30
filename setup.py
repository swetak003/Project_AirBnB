from setuptools import setup, find_packages
from typing import List
def get_requirements(file_path: str) -> List[str]:
    '''
    Docs for retreiving the requirements from requirements.txt file
    1. Open the requirements.txt file 
    2. Read each line and strip whitespace
    3. Return a list of requirements
    4. Ignore empty lines and comments
    5. Return the list of requirements  
    
    '''
    with open(file_path, 'r') as file:
        requirements = file.readlines()
    return [req.strip() for req in requirements if req.strip() and not req.startswith('#')]

setup(
    name='my_package',
    version='0.1.0',
    author='Sweta Kumari',
    author_email="swetakumari071188@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirement.txt'),
    description='A sample Python package'
)