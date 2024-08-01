from setuptools import find_packages,setup
from typing import List

e_dot='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]

        if e_dot in requirements:
            requirements.remove(e_dot)
setup(
    name='ML Project',
    version='0.0.1',
    author='Kamalakannan-K',
    author_email='kkamalakannanlearn@gmail.com',
    packages=find_packages(),
    install_requires= get_requirements('requirements.txt')      #['pandas','numpy','seaborn']
)

