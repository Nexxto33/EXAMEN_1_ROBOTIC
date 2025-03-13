from setuptools import find_packages, setup

package_name = 'sensor_package'

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
    description='TODO: Package description',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sensor1_node = sensor_package.sensor1_node:main',
            'sensor2_node = sensor_package.sensor2_node:main',
            'sensor3_node = sensor_package.sensor3_node:main',
            'filter_node = sensor_package.filter_node:main',
            'display_node = sensor_package.display_node:main',
        ],
    },
)
