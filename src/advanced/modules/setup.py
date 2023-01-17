from setuptools import setup, find_packages

setup(
    name='javacream',
    version='1.0.0',
    license='MIT',
    author="Javacream",
    author_email='training@rainer-sawitzki.de',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/Javacream/org.javacream.training.python',
    keywords='python training project',
    install_requires=[
      "Django >= 1.1.1",
    ]

)