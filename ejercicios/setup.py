from setuptools import find_packages, setup

package_name = 'ejercicios'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nelson',
    maintainer_email='nelson.ramirez@ucb.edu.bo',
    description='Publicador y suscriptor',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'pub_ej1 = ejercicios.pub_ej1:main',
            'sub_ej1 = ejercicios.sub_ej1:main',
        ],
    },
)
