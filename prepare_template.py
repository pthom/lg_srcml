help_prepare = """

By default lg_template build a module named "examplelib"
This utility will make the modifications in order to use a new name.

Directories where to replace examplelib by the new module name:
    ./bindings
    ./bindings/examplelib
    ./external/examplelib
    .

Directories and files to rename:
    ./bindings/examplelib
    ./external/examplelib
    ./bindings/examplelib/examplelib.h
    ./bindings/examplelib/examplelib.cpp
    autogenerate_examplelib.py
    
    
"""

import os


_THIS_DIR = os.path.dirname(os.path.realpath(__file__))


def _replace_in_file(filename: str, new_module_name: str) -> None:
    print(f"_replace_in_file {filename}")

    with open(filename, "r") as input_file:
        content = input_file.read()
        content = content.replace("examplelib", new_module_name)

    with open(filename, "w") as outputfile:
        outputfile.write(content)


def replace_in_files(new_module_name: str) -> None:
    directories = [
        "./bindings",
        "./bindings/examplelib",
        "./external/examplelib",
        ".",
    ]

    for directory in directories:
        files = os.listdir(f"{_THIS_DIR}/{directory}")
        for file in files:
            file_fullpath = f"{_THIS_DIR}/{directory}/{file}"
            if os.path.isfile(file_fullpath) and file != "prepare_template.py":
                _replace_in_file(file_fullpath, new_module_name)


def rename_files(new_module_name:str) -> None:
    """
    Directories and files to rename:
    """
    dir_and_files_to_rename = [
        "./bindings/examplelib/",
        "./bindings/pybind_examplelib.cpp",

        "./external/examplelib/",

        "autogenerate_examplelib.py",
    ]

    for pathname in dir_and_files_to_rename:
        new_pathname = pathname.replace("examplelib", new_module_name)
        src = f"{_THIS_DIR}/{pathname}"
        dst = f"{_THIS_DIR}/{new_pathname}"
        print(f"os.rename({src}, {dst})")
        os.rename(src, dst)

    os.rename(
        f"{_THIS_DIR}/external/{new_module_name}/examplelib.h",
        f"{_THIS_DIR}/external/{new_module_name}/{new_module_name}.h")
    os.rename(
        f"{_THIS_DIR}/external/{new_module_name}/examplelib.cpp",
        f"{_THIS_DIR}/external/{new_module_name}/{new_module_name}.cpp")


def do_replace(new_module_name: str) -> None:
    replace_in_files(new_module_name)
    rename_files(new_module_name)


if __name__ == "__main__":
    print(help_prepare)
    new_module_name = input("Name of the new module: ")
    answer = input("Are you sure (this cannot be undone). Type 'yes' to confirm: ")
    if answer == "yes":
        do_replace(new_module_name)
    else:
        print("Cancelled!")
