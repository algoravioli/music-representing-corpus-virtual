#include "waveform_gen_plugin.h"

void WaveformGenPlugin::prepareToPlay (double sampleRate, int samplesPerBlock)
{
    juce::ignoreUnused (sampleRate, samplesPerBlock);
}

void WaveformGenPlugin::processAudioBlock (juce::AudioBuffer<float>& buffer)
{
    const juce::SpinLock::ScopedTryLockType try_lock { spin_mutex };
    if (! try_lock.isLocked())
    {
        buffer.clear();
        return;
    }

    generator.generate_signal (std::span { buffer.getWritePointer (0), (size_t) buffer.getNumSamples() });

    // split from mono!
    for (int ch = 1; ch < buffer.getNumChannels(); ++ch)
        buffer.copyFrom (ch, 0, buffer, 0, 0, buffer.getNumSamples());
}

juce::AudioProcessorEditor* WaveformGenPlugin::createEditor()
{
    struct Editor : juce::AudioProcessorEditor
    {
        explicit Editor (WaveformGenPlugin& p)
            : juce::AudioProcessorEditor (p),
              plugin (p)
        {
            setSize (300, 300);
        }

        void paint (juce::Graphics& g) override
        {
            g.fillAll (juce::Colours::black);
            g.setColour (juce::Colours::red);
            g.drawFittedText ("CLICK HERE!", getLocalBounds(), juce::Justification::centred, 1);
        }

        void mouseDown (const juce::MouseEvent&) override
        {
            static constexpr auto flags = juce::FileBrowserComponent::openMode | juce::FileBrowserComponent::canSelectFiles;
            file_chooser = std::make_shared<juce::FileChooser> ("Load Model", juce::File {}, "*.json", true, false, this);
            file_chooser->launchAsync (flags,
                                       [&] (const juce::FileChooser& fc)
                                       {
                                           if (fc.getResults().isEmpty())
                                               return;

                                           const auto file = fc.getResult();
                                           const juce::SpinLock::ScopedLockType lock { plugin.spin_mutex };
                                           try
                                           {
                                               plugin.generator.load_model (chowdsp::JSONUtils::fromFile (file));
                                           }
                                           catch (std::exception&)
                                           {
                                           }
                                       });
        }

        WaveformGenPlugin& plugin;
        std::shared_ptr<juce::FileChooser> file_chooser;
    };

    return new Editor { *this };
}

juce::AudioProcessor* createPluginFilter()
{
    return new WaveformGenPlugin;
}
