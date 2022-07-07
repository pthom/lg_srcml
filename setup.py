from skbuild import setup  # This line replaces 'from setuptools import setup'

setup(
    name="lg-implot",
    version="0.1.0",
    author="Pascal Thomet",
    author_email="pthomet@gmail.com",
    description="lg-implot, bindings for implot, using litgen",
    url="https://github.com/epezent/implot",
    packages=(["lg_implot"]),
    package_dir={"": "bindings"},
    cmake_install_dir="bindings/lg_implot",
    include_package_data=True,
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
    package_data={"lg_implot": ["*.pyi"]},
    install_requires=[
        "lg-imgui @ git+https://github.com/pthom/lg_imgui.git",
    ],
)
