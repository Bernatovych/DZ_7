from setuptools import setup, find_namespace_packages

setup(
    name='clean_folder',
    version='1.0.0',
    description='clian_folder',
    url='http://github.com/Bernatovych/clean_folder',
    author='Bernatovych',
    author_email='Bernatovych@example.com',
    license='MIT',
    packages=find_namespace_packages(),
    entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
)