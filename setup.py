from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Operating System :: Linux :: MacOS :: Microsoft Windows',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='api_payload',
  version='0.0.1',
  description='Industry ready custom API payload with an easy format for building Python APIs (Django/Django Rest Framework)',
  long_description=open('README.md').read() + '\n\n' + open('CHANGELOG.txt').read(),
  url='https://github.com/israelabraham',  
  author='Abraham (Abram 🐼) Israel',
  author_email='israelvictory87@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['api', 'payload', 'custom api payload'], 
  packages='api_payload',
  install_requires=[''] 
)