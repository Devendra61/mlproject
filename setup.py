from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT ="-e ."
def get_requirements(file_path:str)->List[str]:
    '''
    this function will returns list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
            requirements=file_obj.readlines()
            requirements =[req.replace("\n","") for req in requirements]	
            if HYPHEN_E_DOT in requirements:
              requirements.remove(HYPHEN_E_DOT)

#metadata of entire project
setup(
name='mlproject',
version='0.0.1',
author='Devendra',
author_email="devbarahen@gmail.com",
packages = find_packages(),
install_requirements= get_requirements('requirements.txt'))
#specify all packages in requirements.py  