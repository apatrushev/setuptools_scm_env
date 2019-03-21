import setuptools
from setuptools import setup


with open("README.rst") as fp:
    long_description = fp.read()


setup(
    name="setuptools_scm_env",
    description=("helper package to get scm version from env as fallback"),
    long_description=long_description,
    url="https://github.com/apatrushev/setuptools_scm_env/",
    license="MIT",
    author="Anton Patrushev",
    author_email="apatrushev@gmail.com",
    use_scm_version=True,
    setup_requires=["setuptools_scm"],
    packages=["setuptools_scm_env"],
    package_dir={"": "src"},
    entry_points="""
        [setuptools_scm.parse_scm_fallback]
        setup.py=setuptools_scm_env:main
    """,
    zip_safe=True,
    platforms="any",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Version Control",
        "Topic :: System :: Software Distribution",
        "Topic :: Utilities",
    ],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*",
)
