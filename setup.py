from setuptools import setup, find_packages

setup(
    name='gmao',
    version='0.0.1',
    description='Application GMAO pour ERPNext',
    author='Amine Hammouda',
    author_email='amine.hammoud51@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['frappe'],
)
