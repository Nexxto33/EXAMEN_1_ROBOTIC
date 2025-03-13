from setuptools import setup

package_name = 'aibo_kinematics'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/srv', ['srv/Kinematics.srv']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='nelson',
    maintainer_email='nelson.ramirez@ucb.edu.bo',
    description='Cinemática directa de la pierna del robot AIBO ERS-7',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'kinematics_server = aibo_kinematics.kinematics_server:main',
            'kinematics_client = aibo_kinematics.kinematics_client:main',
        ],
    }
)

