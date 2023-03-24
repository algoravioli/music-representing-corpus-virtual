CPMAddPackage("gh:fmtlib/fmt#9.1.0")
CPMAddPackage("gh:adishavit/argh#v1.3.2")
CPMAddPackage(
    NAME libsndfile
    GIT_REPOSITORY https://github.com/libsndfile/libsndfile
    GIT_TAG v1.0.30
    OPTIONS
    "BUILD_PROGRAMS OFF"
    "BUILD_EXAMPLES OFF"
    "BUILD_TESTING OFF"
)

add_executable(waveform_gen_cli waveform_gen_cli.cpp)
target_link_libraries(waveform_gen_cli
    PRIVATE
        waveform_gen
        fmt::fmt
        argh
        sndfile
        Threads::Threads
)
