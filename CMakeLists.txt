cmake_minimum_required(VERSION 3.17)
cmake_policy(VERSION 3.9)
project(lg_implot)

include(lg_cmake_utils/lg_cmake_utils.cmake)

set(CMAKE_CXX_STANDARD 20)

add_subdirectory(external/pybind11)

####################################################
# Build implot Bound C++ library
####################################################
# Note: any sub shared library used by the bound C++ library should install its targets into the "lib/" subfolder
# 1. Build imgui (lib used by implot)
set(imgui_dir ${CMAKE_CURRENT_LIST_DIR}/external/imgui)
add_imgui_target(${imgui_dir}) # This will install its target into lib/
# 2. Build implot
set(implot_dir ${CMAKE_CURRENT_LIST_DIR}/external/implot)
file(GLOB implot_sources ${implot_dir}/*.cpp ${implot_dir}/*.h)
add_library(implot SHARED ${implot_sources})
target_link_libraries(implot PUBLIC imgui)
target_include_directories(implot PUBLIC ${implot_dir})
lg_target_force_include(implot ${CMAKE_CURRENT_LIST_DIR}/implot_config_dll_export.h)


#########################################################################
# Build python module that provides bindings to the library implot
#########################################################################
set(bound_library implot)                 # The library for which we are building bindings
set(python_native_module_name _lg_implot) # This is the native python module name (`_lg_implot`).
set(python_wrapper_module_name lg_implot) # This is the python wrapper around the native module
set(python_module_sources bindings/module.cpp bindings/pybind_mylib.cpp) # native python module sources

pybind11_add_module(${python_native_module_name} ${python_module_sources})
lg_setup_module(
    ${bound_library}
    ${python_native_module_name}
    ${python_wrapper_module_name}
)
