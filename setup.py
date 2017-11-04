"""
Stream any media content using console
"""
from setuptools import setup

dependencies = ['click', 'beautifulsoup4', 'lxml']

setup(
    name='torstream',
    version='0.1.2',
    url='https://github.com/PandaWhoCodes/torstream',
    license='MIT',
    author='Thomas Ashish Cherian',
    author_email='ufoundashish@gmail.com',
    description='Stream any media content using console',
    long_description=__doc__,
    packages=['torstream'],
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    scripts=['torstream/streamer.py'],
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'torstream = torstream.streamer:argParser',
        ],
    },

    classifiers=[
        # As from http://pypi.python.org/pypi?%3Aaction=list_classifiers
        # 'Development Status :: 1 - Planning',
        # 'Development Status :: 2 - Pre-Alpha',
        # 'Development Status :: 3 - Alpha',
        'Development Status :: 4 - Beta',
        # 'Development Status :: 5 - Production/Stable',
        # 'Development Status :: 6 - Mature',
        # 'Development Status :: 7 - Inactive',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]
)
