from setuptools import setup, find_packages

setup(
    name='portfoliopackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Temitope-odeyemi?tab=repositories',
    author='Temitope Odeyemi',
    author_email='odeyemitemi23@gmail.com'
)