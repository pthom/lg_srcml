cmake_minimum_required(VERSION 3.17)
cmake_policy(VERSION 3.9)
project(lg_implot)

include(lg_cmake_utils/lg_cmake_utils.cmake)

set(CMAKE_CXX_STANDARD 20)

add_subdirectory(external/pybind11)

####################################################
# Build mylib Bound C++ library
####################################################
set(mylib_dir external/mylib)
# The library shall be built as a shared library
add_library(mylib SHARED ${mylib_dir}/mylib.cpp ${mylib_dir}/mylib.h)
target_include_directories(mylib PUBLIC ${mylib_dir})
# The library shall install itself into lib/
# Note: any sub shared library used by the bound C++ library should install its targets into the "lib/" subfolder
install(TARGETS mylib DESTINATION ./lib/)
# Under windows, auto __declspec(dllexport)
if (WIN32)
    set_target_properties(mylib PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()


#########################################################################
# Build python module that provides bindings to the library implot
#########################################################################
set(bound_library mylib)                 # The library for which we are building bindings
set(python_native_module_name _mylib) # This is the native python module name
set(python_wrapper_module_name mylib) # This is the python wrapper around the native module
set(python_module_sources bindings/module.cpp bindings/pybind_${bound_library}.cpp) # native python module sources

pybind11_add_module(${python_native_module_name} ${python_module_sources})
lg_setup_module(
    ${bound_library}
    ${python_native_module_name}
    ${python_wrapper_module_name}
)
