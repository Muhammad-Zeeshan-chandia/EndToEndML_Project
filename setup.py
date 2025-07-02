from setuptools import find_packages, setup

def get_requirements(path):
    with open(path) as file:
        return [
            line.strip() for line in file.readlines()
            if line.strip() and not line.startswith("-e")
        ]

setup(
    name='MLProject',
    version='0.0.1',
    author='Zeeshan',
    author_email='m.zeeshanchandia1@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)
