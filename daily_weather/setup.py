from setuptools import setup

setup(
    name='daily_weather',
    packages=['daily_weather'],
    include_package_data=True,
    install_requires=[
        'flask',
        'pylint'
    ],
)
