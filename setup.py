from setuptools import setup, find_packages
 
classifiers = [
  'Development Status :: 5 - Production/Stable',
  'Intended Audience :: Education',
  'Intended Audience :: Developers',
  'License :: OSI Approved :: MIT License',
  'Programming Language :: Python :: 3'
]
 
setup(
  name='rest_api_payload',
  version='0.0.6',
  description='A to-go-to production API payload with an easy format for building APIs with Python.',
  long_description_content_type="text/markdown",
  long_description=open('README.md').read(),
  url='https://github.com/israelabraham/API-Payload',  
  author='Abram',
  author_email='israelvictory87@gmail.com',
  license='MIT', 
  classifiers=classifiers,
  keywords=['api', 'payload', 'custom api payload'], 
  packages=find_packages()
)