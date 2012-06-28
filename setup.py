from setuptools import setup

setup(
    name='sentry-cardinal',
    version='0.1.0-1',
    packages=['sentry_cardinal'],
    include_package_data=True,
    license='MIT',
    author='Noah Silas',
    author_email='noah.silas@causes.com',
    url='https://github.com/causes/sentry_cardinal',
    description="Added niceness for railsy tracebacks in Sentry",
    zip_safe=False,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'License :: OSI Approved :: BSD License',
        'Development Status :: 3 - Alpha',
    ],
)
