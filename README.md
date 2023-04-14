# Music Representing Corpus Virtual (MRCV)
At the same time that MRCV is the title of the musical work, it is the name of the code repository that accompanies said musical work. The main purpose of this work is to introduce the non-technical &| non-machine-learning-ai people to AI/ML (artificial intelligence/machine learning [used interchangeably in this case]). 

We present a number of use cases that is encompassed within the scope/remit of this codebase. As a first-pass, we will describe the use-cases before going in depth in further sections.

- Music Generation
   - Done through MIDI (currently, MUSIC-TO-SCORE is still underconstruction)
- Sampler Instrument Procedural Generation (Sound Design)
   - Two choices here, the first being the ability to generate 127 different sounds to fill up the sampler instrument.
   - The second choice is to fill up the sampler instrument by pitch-shifting one sound in order to get 127 different notes.
   - The sampler instrument generated is a [Decent Sampler Instrument](https://www.decentsamples.com/product/decent-sampler-plugin/).
- Realtime Audio-to-Audio Generation (VST/AU plugin)
  - In this case, the user is able to train a REALTIME-CAPABLE (audio rate inferencing) to be used in a plugin. (cf. `waveform-gen-plugin`)
- Neural Wavetable Generation through frequency features.
  - We generate a wavetable using frequency information.
  - This is then used as a wavetable/granular synthesiser and pitchshifted to fit 127 notes.
- Score Generation 
  - This is done through the `./genere/` part of the codebase.
