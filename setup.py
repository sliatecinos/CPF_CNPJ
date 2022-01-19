from setuptools import setup

with open('README.rst') as _readme_file:
    readme = _readme_file.read()

setup(
    name='CPF_CNPJ',
    url='https://github.com/sliatecinos/CPF_CNPJ',
    version='0.0.1',
    author='Sliatecinos',
    author_email='sliatecinos@hotmail.com',
    maintainer='',
    license='MIT',
    description=(
        "A simple Python library containing functions that check Brazilian documents values"
    ),
    long_description=readme,
    classifiers=[
		'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
		'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.9',
)
