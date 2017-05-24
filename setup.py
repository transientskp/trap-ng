from setuptools import setup, find_packages

__version__ = "0.1pre"


install_requires = [
    'bdsf',
    'astropy',
]

scripts = [
]

setup(
    name="trap-ng",
    version=__version__,
    packages=find_packages(),
    scripts=scripts,
    install_requires=install_requires,
    package_data={ },
    author="Gijs Molenaar",
    author_email="gijs@pythonic.nl",
    description="Radio astronomy Transient Detection Next Generation",
    license="mit",
    keywords="science radio astronomy",
    url="https://github.com/transientskp/trap-ng",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 2.7",
        "Topic :: Scientific/Engineering",
        ]
)
