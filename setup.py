import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

    setuptools.setup(
        name='pgdancer',
        version="0.1",
        description=(
            'common dynamic data visualization framework for python'
        ),
        long_description = long_description,
        long_description_content_type="text/markdown",
        author='zgmphoo',
        author_email='zgmphoo@gmail.com',
        license='BSD License',
        packages=setuptools.find_packages(),
        install_requires=['pandas>=0.20.1', 'pygame>=1.9.5'],
        url='https://github.com/zgmphoo/pgdancer',
        include_package_data = True,
        entry_points={
        'console_scripts': [
            'pgdancer=pgdancer.cmdline:main'
            ],
        },
        platforms=['any'],
        classifiers=[
            'Operating System :: OS Independent',
            'License :: OSI Approved :: BSD License',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
        ],
    )