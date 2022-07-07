import os

import litgen
from litgen.litgen_options_implot import litgen_options_implot


THIS_DIR = os.path.dirname(__file__)
print(f"{THIS_DIR=}")
CPP_HEADERS_DIR = THIS_DIR + "/external/implot"
CPP_GENERATED_PYBIND_DIR = THIS_DIR + "/bindings"
assert os.path.isdir(CPP_HEADERS_DIR)
assert os.path.isdir(CPP_GENERATED_PYBIND_DIR)


def autogenerate():
    input_cpp_header = CPP_HEADERS_DIR + "/implot.h"
    output_cpp_pydef_file = CPP_GENERATED_PYBIND_DIR + "/pybind_lg_implot.cpp"
    output_stub_pyi_file = CPP_GENERATED_PYBIND_DIR + "/lg_implot/__init__.pyi"

    # Configure options
    options = litgen_options_implot()
    generated_code = litgen.generate_code(options, filename=input_cpp_header)

    litgen.write_generated_code(
        generated_code,
        output_cpp_pydef_file=output_cpp_pydef_file,
        output_stub_pyi_file=output_stub_pyi_file,
    )


if __name__ == "__main__":
    print("autogenerate_hello_implot")
    autogenerate()
