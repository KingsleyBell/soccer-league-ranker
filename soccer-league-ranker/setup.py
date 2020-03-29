from setuptools import setup, find_packages


setup(
    name='soccer-league-ranker',
    version='0.1.0',
    description='Simple python utility for calculating soccer ranking tables',
    maintainer='https://github.com/Kingsleybell',
    license='MIT',
    url='https://github.com/Kingsleybell/soccer-league-ranker',
    package_dir={'': 'src'},
    include_package_data=True,
    packages=find_packages('src'),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'ranker=ranker.main:run'
        ]
    }
)
