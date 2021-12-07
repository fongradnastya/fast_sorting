from setuptools import setup, find_packages

setup(
      name='sorting_package',
      version='1.3',
      url='https://github.com/fongradnastya/fast_sorting',
      license='MIT',
      author='Fongrad Anastasia',
      author_email='fongradnastya@gmail.com',
      description='Fast sorting module',
      packages=find_packages(exclude=['tests']),
      long_description=open('README.md', encoding='UTF-8').read(),
      long_description_content_type='text/markdown',
      zip_safe=False,
      python_requires='>=3.6, <4',
      setup_requires=['click', 'pytest'],
      include_package_data=True,
      test_suite='test'
)
