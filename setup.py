from setuptools import setup

setup(name='mention',
      version='0.1.0',
      description='Get share counts from a given URL easily.',
      url='https://github.com/thinkxl/mention',
      author='Juan Olvera',
      author_email='thinkxl@gmail.com',
      license='MIT',
      packages=['mention'],
      zip_safe=False,
      install_requires=[
        'requests>=2.5.1',
        'beautifulsoup4>=4.3.2'
      ]
)
