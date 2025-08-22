from setuptools import setup, find_packages

setup(
    name="mkdocs-java-interpreter",
    version="1.0.0",
    description="Un plugin para MkDocs que añade un intérprete de Java online",
    author="Tu Nombre",
    author_email="tu@email.com",
    url="https://github.com/tu-usuario/mkdocs-java-interpreter",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'mkdocs>=1.0.0',
    ],
    entry_points={
        'mkdocs.plugins': [
            'java-interpreter = mkdocs_java_interpreter:JavaInterpreterPlugin',
        ]
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
)
