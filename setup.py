from setuptools import setup, find_packages

REQUIRED_PACKAGES = ['torch >= 1.13',
                     'numpy',
                     'scipy',
                     'torchvision>=0.8',
                     'dominate>=2.5.1',
                     'torchkbnufft >= 1.4.0',
                     'scipy>=1.6.0',
                     'PyWavelets>=1.1.0',
                     'h5py >= 3.2.1',
                     'pytorch_wavelets',
                     'einops',
                     'matplotlib',
                     'xitorch']

with open("README.md", "r") as h:
    long_description = h.read()

setup(
    name="mirtorch",
    version="0.0.2",
    author="Keyue Zhu, Neel Shah and Guanhua Wang",
    author_email="guanhuaw@umich.edu",
    description="a PyTorch-powered imaging reconstruction toolbox",
    license='BSD',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/guanhuaw/MIRTorch",
    packages=find_packages(),
    install_requires=REQUIRED_PACKAGES,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        'Development Status :: 2 - Pre-Alpha',
        'Topic :: Signal Processing'
    ],
    dependency_links=[
        # Make sure to include the `#egg` portion so the `install_requires` recognizes the package
        'git+https://github.com/fbcotter/pytorch_wavelets.git#egg=pytorch_wavelets'
    ],
    python_requires='>=3.6',
)
