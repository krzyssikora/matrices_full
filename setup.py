from setuptools import setup

setup(
    name='matrices',
    packages=['matrices'],
    include_package_data=True,
    install_requires=[
        'flask',
    ],
    devtool='inline-source-map',
)
