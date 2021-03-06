from setuptools import setup, find_packages

with open('README.rst', 'r') as f:
    readme = f.read()

setup(
    name='dbbackup',
    version='0.1.0',
    description='Database backups locally or the cloud.',
    author='Felipe Gusmao',
    author_email='fgmonad@gmail.com',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    install_requires=['boto3'],
    entry_points={
        'console_scripts': [
            'dbbackup=dbbackup.cli:main',
        ]
    }
)
