from setuptools import setup, find_packages

setup(name='pylexo',
      version='0.3.0',
      packages=find_packages(),
      description='Pythonic Lex Object (PyLexO)',
      author='WavyCloud',
      author_email='',
      entry_points={
          'console_scripts': [
              'pylexo = pylexo.__main__:main'
          ]
      },
      url='https://github.com/wavycloud/pylexo',
      py_modules=['pylexo'],
      install_requires=['jsonobject==0.7.1'],
      license='MIT License',
      zip_safe=True,
      keywords='aws python lex lambda',
      classifiers=[])
