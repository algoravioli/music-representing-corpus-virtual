cmake_minimum_required (VERSION 3.14 FATAL_ERROR)
project(waveform_gen VERSION 0.0.0 LANGUAGES C CXX)
set(CMAKE_CXX_STANDARD 20)

set(THREADS_PREFER_PTHREAD_FLAG ON)
find_package(Threads REQUIRED)

include(cmake/get_cpm.cmake)
CPMAddPackage(
    NAME RTNeural
    GIT_TAG main
    GITHUB_REPOSITORY jatinchowdhury18/RTNeural
    OPTIONS
    "RTNEURAL_XSIMD ON"
)

add_library(waveform_gen STATIC src/waveform_gen.cpp)
target_link_libraries(waveform_gen PUBLIC RTNeural)

add_subdirectory(plugin)
add_subdirectory(cli)
