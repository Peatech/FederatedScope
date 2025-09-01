from __future__ import absolute_import, division, print_function

import setuptools

__name__ = 'federatedscope'
__version__ = '0.3.0'
URL = 'https://github.com/alibaba/FederatedScope'

minimal_requires = [
    'numpy', 'scikit-learn', 'scipy', 'pandas',
    'grpcio', 'grpcio-tools', 'pyyaml', 'fvcore', 'iopath',
    'wandb', 'tensorboard', 'tensorboardX', 'pympler', 'protobuf==3.19.4',
    'matplotlib'
]

test_requires = ['pytest', 'pytest-cov']

dev_requires = test_requires + ['pre-commit', 'networkx', 'matplotlib']

org_requires = ['paramiko', 'celery[redis]', 'cmd2']

app_requires = [
    'torch-geometric', 'nltk', 'transformers',
    'tokenizers', 'datasets', 'sentencepiece', 'textgrid', 'typeguard',
    'openml'
]

benchmark_hpo_requires = [
    'configspace', 'hpbandster', 'smac', 'optuna'
]

benchmark_htl_requires = ['learn2learn']

full_requires = org_requires + benchmark_hpo_requires + \
                benchmark_htl_requires + app_requires

with open("README.md", "r", encoding='UTF-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name=__name__,
    version=__version__,
    author="Alibaba Damo Academy",
    author_email="jones.wz@alibaba-inc.com",
    description="Federated learning package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=URL,
    download_url=f'{URL}/archive/{__version__}.tar.gz',
    keywords=['deep-learning', 'federated-learning', 'benchmark'],
    packages=[
        package for package in setuptools.find_packages()
        if package.startswith(__name__)
    ],
    install_requires=minimal_requires,
    extras_require={
        'test': test_requires,
        'app': app_requires,
        'org': org_requires,
        'dev': dev_requires,
        'hpo': benchmark_hpo_requires,
        'htl': benchmark_htl_requires,
        'full': full_requires
    },
    license="Apache License 2.0",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
)
