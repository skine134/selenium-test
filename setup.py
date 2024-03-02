from setuptools import setup

setup(
    name='selenium_test',
    version='0.0.1',
    description='selnium_test pip test',
    author='skine134',
    author_email='skine134',
    license='bear',
    packages=['sele','spk'],
    zipa_safe=False,
    install_requires=[
        'selenium==4.18.1',
        'pyspark==3.5.1'
    ]
)