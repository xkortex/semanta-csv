from setuptools import setup, find_packages

# https://python-packaging.readthedocs.org/en/latest/dependencies.html
# https://gehrcke.de/2014/02/distributing-a-python-command-line-application/
# python setup.py install develop

setup(name='semantacsv',
      version='0.1.0',
      description='Parsing and processing for Semanta CSV files',
      url='https://github.com/xkortex/semanta-csv',
      author='Michael McDermott',
      author_email='mikemcdermott23@gmail.com',
      license='Apache 2.0',
      packages=find_packages(exclude=["*.testing", "testing.*", "testing", "*.tests", "*.tests.*", "tests.*", "tests"]),
      install_requires=[
          'pandas==0.20.3',
      ],
      zip_safe=False)
