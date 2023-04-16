# Music Representing Corpus Virtual (MRCV)
At the same time that MRCV is the title of the musical work, it is the name of the code repository that accompanies said musical work. The main purpose of this work is to introduce the non-technical &| non-machine-learning-ai people to AI/ML (artificial intelligence/machine learning [used interchangeably in this case]). 

We present a number of use cases that is encompassed within the scope/remit of this codebase. As a first-pass, we will describe the use-cases before going in depth in further sections.

- **Music Generation**
   - Done through MIDI (currently, MUSIC-TO-SCORE is still underconstruction)
- **Sampler Instrument Procedural Generation (Sound Design)**
   - Two choices here, the first being the ability to generate 127 different sounds to fill up the sampler instrument.
   - The second choice is to fill up the sampler instrument by pitch-shifting one sound in order to get 127 different notes.
   - The sampler instrument generated is a [Decent Sampler Instrument](https://www.decentsamples.com/product/decent-sampler-plugin/).
- **Realtime Audio-to-Audio Generation (VST/AU plugin)**
  - In this case, the user is able to train a REALTIME-CAPABLE (audio rate inferencing) to be used in a plugin. (cf. `waveform-gen-plugin`)
- **Neural Wavetable Generation through frequency features**
  - We generate a wavetable using frequency information.
  - This is then used as a wavetable/granular synthesiser and pitchshifted to fit 127 notes.
- **Procedural Score Generation**
  - This is done through the `./genere/` part of the codebase.


# LICENSE
BSD 3-Clause License

Copyright (c) 2023, Christopher Johann Clarke

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its
   contributors may be used to endorse or promote products derived from
   this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
