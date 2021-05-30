from setuptools import setup, find_packages

with open('README.md') as f:
    long_description = f.read()

setup(name='espydio',
      version='0.0.1',
      description='Command Line Utility for audio manipulations',
      long_description=long_description,
      long_description_content_type = 'text/markdown',
      url='',
      author='Naman Puri',
      author_email='namanpuri1712@gmail.com',
      license='MIT',
      include_package_data=True,
      entry_points ={
            'console_scripts': [
                'espydio = espydio.script_espydio:main'
            ]
        },
      packages=find_packages(),
      install_requires=['Flask==1.1.2','sox==1.4.1','requests==2.25.1'],
      classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: Windows',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
      ],
      zip_safe=False)