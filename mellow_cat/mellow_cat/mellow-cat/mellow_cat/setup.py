from setuptools import setup, find_packages

setup(
    name='mellow-cat',
    version='0.1',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mellow-cat = mellow_cat.mellow_cat:main',
        ],
    },
    description='A command-line tool for viewing server logs with additional useful information for system administrators.',
    author='Your Name',
    author_email='your_email@example.com',
    url='https://github.com/yourusername/mellow-cat',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
