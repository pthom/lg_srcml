from skbuild import setup  # This line replaces 'from setuptools import setup'

setup(
    name="srcml",
    version="0.1.0",
    author="Pascal Thomet",
    author_email="pthomet@gmail.com",
    description="srcml, template bindings for litgen",
    url="https://github.com/pthom/litgen",
    packages=(["srcml"]),
    package_dir={"": "bindings"},
    cmake_install_dir="bindings/srcml",
    include_package_data=True,
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
    package_data={"srcml": ["py.typed", "*.pyi"]},
    install_requires=[],
)
