from setuptools import setup

setup(name='AutoSleepScorer',
      version='0.2',
      description='An Automatic Sleep Stage Classification Package',
      url='http://github.com/skjerns/AutoSleepScorer',
      author='skjerns',
      author_email='sikern@uos.de',
      license='See Github',
      packages=['sdill'],
      install_requires=['keras','tensorflow','mne', 'tqdm', 'sklearn', 'matplotlib'],
      zip_safe=False)