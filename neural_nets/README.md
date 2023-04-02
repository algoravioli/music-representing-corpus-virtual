Neural Net 1: Realtime Generative Moddel (RGM) trained on the MAESTRO dataset.
Available at the link:
(https://storage.googleapis.com/magentadata/datasets/maestro/v3.0.0/maestro-v3.0.0.zip)
Curtis Hawthorne, Andriy Stasyuk, Adam Roberts, Ian Simon, Cheng-Zhi Anna Huang,
Sander Dieleman, Erich Elsen, Jesse Engel, and Douglas Eck. "Enabling
Factorized Piano Music Modeling and Generation with the MAESTRO Dataset."
In International Conference on Learning Representations, 2019.

This model is not trained to be a piano music generation model, rather, it uses the data as an input for continuous musical generation under some form on control parameters.

Neural Net 2: Sampler Instrument using Neural Generation based on Saxophone Multiphonics Data.
The data can be found under `./saxophone_audiodata/multiphonics`.
One can try varying the model sizes and training on this dataset to generate audio data through the waveform-gen-plugin.

Neural Net 3: Realtime Audio Waveform Generation from Ecological Saxophone Data

Neural Net 4: Neural Wavetables from Mel-Spectrograms to Sampler Instrument based on Audio Input