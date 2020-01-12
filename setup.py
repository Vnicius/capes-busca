
from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='capesbusca',
    packages=find_packages(),
    version='0.1.1',
    license='MIT',
    description='Biblioteca para realizar busca de termos no catálogo de teses e dissertações da Capes',
    long_description=long_description,
    long_description_content_type="text/markdown",
    author='Vinícius Veríssimo',
    author_email='vinicius.matheus252@gmail.com',
    url='https://github.com/Vnicius/capes-busca',
    download_url='https://github.com/Vnicius/capes-busca/archive/v0.1.1.tar.gz',
    keywords=['data', 'api', 'capes', 'works'],
    install_requires=[
        'requests',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
