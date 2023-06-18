from setuptools import setup, find_packages

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='django-event-calendar',
    version='1.0.0',
    include_package_data=True,
    license='MIT',
    description='Event Calendar for Django',
    long_description=open('README.md').read(),
    packages=[
        "eventcalendar",
        "calendarapp"
    ],
    install_requires=requirements,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
)
