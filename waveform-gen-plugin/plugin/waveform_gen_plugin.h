#pragma once

#include "chowdsp_plugin_base/chowdsp_plugin_base.h"

JUCE_BEGIN_IGNORE_WARNINGS_GCC_LIKE ("-Wshadow-field-in-constructor",
                                     "-Wzero-as-null-pointer-constant",
                                     "-Wsign-conversion",
                                     "-Wunused-parameter")
#include "../src/waveform_gen.h"
JUCE_END_IGNORE_WARNINGS_GCC_LIKE

struct Params : chowdsp::ParamHolder {};

using State = chowdsp::PluginStateImpl<Params>;
struct WaveformGenPlugin : public chowdsp::PluginBase<State>
{
    WaveformGenPlugin() = default;

    void prepareToPlay (double sampleRate, int samplesPerBlock) override;
    void releaseResources() override {}
    void processAudioBlock (juce::AudioBuffer<float>& buffer) override;

    juce::AudioProcessorEditor* createEditor() override;

    juce::SpinLock spin_mutex;
    waveform_gen::Generator generator;
};
