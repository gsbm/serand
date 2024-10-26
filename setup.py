from setuptools import setup, find_packages

setup(
    name='serand',
    version='1.0.0',
    description='All-in-one library to generate cryptographically secure random numbers.',
    author='gsbm',
    url='https://github.com/gsbm/serand',  # Remplacez par l'URL de votre projet si applicable
    packages=find_packages(),
    install_requires=[],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
