from skbuild import setup  # This line replaces 'from setuptools import setup'

setup(
    name="mylib",
    version="0.1.0",
    author="Pascal Thomet",
    author_email="pthomet@gmail.com",
    description="mylib, template bindings for litgen",
    url="https://github.com/pthom/litgen",
    packages=(["mylib"]),
    package_dir={"": "bindings"},
    cmake_install_dir="bindings/mylib",
    include_package_data=True,
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
    package_data={"mylib": ["py.typed", "*.pyi"]},
    install_requires=[],
)
