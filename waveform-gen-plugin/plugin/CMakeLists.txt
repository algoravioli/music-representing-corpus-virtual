CPMAddPackage("gh:juce-framework/JUCE#7.0.5")
CPMAddPackage("gh:Chowdhury-DSP/chowdsp_utils#v2.1.0")
CPMAddPackage("gh:free-audio/clap-juce-extensions#main")

juce_add_plugin(waveform_gen_plugin
    COMPANY_NAME chowdsp
    PLUGIN_MANUFACTURER_CODE Chow
    PLUGIN_CODE Wg54
    FORMATS AU VST3 Standalone
    ProductName "Chris's Waveform Gen Plugin"
    )

target_compile_definitions(waveform_gen_plugin
    PUBLIC
    JUCE_DISPLAY_SPLASH_SCREEN=0
    JUCE_REPORT_APP_USAGE=0
    JUCE_WEB_BROWSER=0
    JUCE_USE_CURL=0
    JUCE_VST3_CAN_REPLACE_VST2=0
    )
target_link_libraries(waveform_gen_plugin
    PRIVATE
        juce::juce_audio_utils
        chowdsp::chowdsp_plugin_base
        chowdsp::chowdsp_plugin_state
        waveform_gen
    PUBLIC
        juce::juce_recommended_config_flags
        juce::juce_recommended_lto_flags
        juce::juce_recommended_warning_flags
)

clap_juce_extensions_plugin(
    TARGET waveform_gen_plugin
    CLAP_ID "org.chowdsp.waveform_gen_plugin"
    CLAP_FEATURES audio-effect
    CLAP_PROCESS_EVENTS_RESOLUTION_SAMPLES 64
    CLAP_USE_JUCE_PARAMETER_RANGES DISCRETE
)

target_sources(waveform_gen_plugin PRIVATE waveform_gen_plugin.cpp)
