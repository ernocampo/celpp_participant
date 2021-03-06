import setuptools

setuptools.setup(
    name="cp_docker",
    version="0.1.0",
    url="www.github.com/ernocampo/CatalysisPrediction",

    author="Ernesto Ocampo",
    author_email="ocampoernesto@gmail.com",

    description="My docker",
    long_description=open('README.rst').read(),

    packages=setuptools.find_packages(),

    install_requires=["d3r"],

    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],
     scripts = ['cp_docker/ernesto_dock.py',
                'cp_docker/ernesto_ligand_prep.py', 
                'cp_docker/ernesto_protein_prep.py']
)
