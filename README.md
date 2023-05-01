# Music Representing Corpus Virtual (MRCV)
At the same time that MRCV is the title of the musical work, it is the name of the code repository that accompanies said musical work. The main purpose of this work is to introduce the non-technical &| non-machine-learning-ai people to AI/ML (artificial intelligence/machine learning [used interchangeably in this case]). 

We present a number of use cases that is encompassed within the scope/remit of this codebase. As a first-pass, we will describe the use-cases before going in depth in further sections.

- **Music Generation**
   - Done through MIDI (currently, MUSIC-TO-SCORE is still underconstruction)
- **Sampler Instrument Procedural Generation (Sound Design)**
   - Two choices here, the first being the ability to generate 128 different sounds to fill up the sampler instrument.
   - The second choice is to fill up the sampler instrument by pitch-shifting one sound in order to get 127 different notes.
   - The sampler instrument generated is a [Decent Sampler Instrument](https://www.decentsamples.com/product/decent-sampler-plugin/).
- **Realtime Audio-to-Audio Generation (VST/AU plugin)**
  - In this case, the user is able to train a REALTIME-CAPABLE (audio rate inferencing) to be used in a plugin. (cf. `waveform-gen-plugin`)
- **Neural Wavetable Generation through frequency features**
  - We generate a wavetable using frequency information.
  - This is then used as a wavetable/granular synthesiser and pitchshifted to fit 127 notes.
- **Procedural Score Generation**
  - This is done through the `./genere/` part of the codebase.

## Table of Contents
* **[Starting from Absolute Zero](#starting-from-absolute-zero)**
  * **[Mac OS](#mac-os)**
  * **[Post VSCode Install](#post-vscode-install)**
  * **[Verify Pyenv Install](#verify-pyenv-install)**
  * **[After Installing Pyenv](#after-installing-pyenv)**
  * **[Post Python Install](#post-python-install)**
  * **[Time to Set Up VSCODE](#time-to-set-up-vscode)**
* **[Dependencies](#dependencies)**
* **[Building the Audio Plugin](#building-the-audio-plugin-to-run-json-neural-network-files)**
* **[Using a Virtual Environment](#using-a-virtual-environment)**

## Starting from Absolute Zero
### Mac OS
This project is made under the full understanding that people will not have had any programming experience whatsoever. This section of the `README.md` will serve as a guide for setting everything up. We recommend using [VSCode](https://code.visualstudio.com/) as the code executor. 
##### Post VSCode Install
After installing VSCode, download [Homebrew](https://brew.sh/) in order to manage certain packages you will need to maintain some neatness in your computer. We recommend pyenv and graphviz.

First, install Homebrew, open the Terminal application (under Applications >> Terminal) and type these commands:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
After installing Homebrew, you will be able to install packages from your Terminal application, for example:
```bash
brew install <package-name>
```
Next, install pyenv and graphviz (for intel Macs, there seems to be a problem which can be easily fixed by installing xz)
```bash
brew install pyenv
brew install graphviz
brew install xz (if needed)
```
After this, you will need to type a few simple commands into the terminal. Type this command to see which shell you are running. Usually it will be bash or zsh.
```bash 
echo $SHELL
```
Follow the steps below for the necessary shell (bash or zsh).
##### bash (taken from the pyenv github README.md)
For **bash**, type these commands:
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc
```
Then, if you have `~/.profile`, `~/.bash_profile` or `~/.bash_login`, add the commands there as well.
If you have none of these, add them to `~/.profile`.

to add to `~/.profile`:
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init -)"' >> ~/.profile
```

to add to `~/.bash_profile`:
```bash
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
```

Restart your terminal after typing these commands.
##### zsh (taken from the pyenv github README.md)
For **zsh**, type these commands:
```zsh
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc
```
Restart your terminal after typing these commands.
##### Verify pyenv install
Type this line to check if you have done everything right:
```bash
pyenv --version
```
If correct, it should output something like:
```bash
pyenv 2.3.7
```
Your numbers may vary a little but in general it should not say pyenv can not be found or something along those lines.

##### After installing pyenv
Next, we will want to set up the proper python versions for your system. Python versions can be installed with pyenv using this command. This command installs python version 3.10.10, which is the most stable version for this library. However, we have tested it on 3.10.8 and it works as well.
```bash
pyenv install 3.10.10 
```
If you run into an error such as this:
```bash
python-build: definition not found
See all available versions with `pyenv install --list`.
...
```
Try to install versions by reducing the last number (first attempt from 3.10.10 to 3.10.9) until it allows you to install:
```bash
pyenv install 3.10.9
...

pyenv install 3.10.8
... (you get the idea)
```
##### Post-python install
Change our global version of python to the one we installed (the following command assumes 3.10.10, but yours might differ, it could be 3.10.8):
```bash
pyenv global 3.10.10
```
Restart your terminal application.
After restarting, you should be able to type in `python -V` and see that your current version is 3.10.10.
##### Time to set up VSCode
- Once you have installed the correct pyenv version, open VSCode and install the relevant python extensions by searching "Python" under the extensions (4 square logo with one square slightly lifted off).

- After clicking the small "Install" button next to it, it should install a couple of other extensions for you like Pylance etc. Wait for that to complete. Once that is complete, it should ask you to do a few things, ignore that and click on "Mark Done" for everything.

- When that is done, open a new file File >> New File ..., and call it something like test.py. Open that file.
- Once that file is open, there should be a small button on the bottom right corner of the screen that says something along the lines of "Select Python Interpreter", or "3.10.10 64-bit ...". If it says something like "... ('3.10.10':pyenv)", you are in luck and will not need the next step however, if it says anything else, click on it and choose the option that has pyenv in the name.
- If there are no options with pyenv in the name, select the option to type in the path, and type in `~/.pyenv/versions/3.10.10/bin/python`, replacing 3.10.10 with whichever version you installed.
## Dependencies
Because this project is not currently in production yet (version no. < 0.0.0), the some dependencies will need to be installed separately from the `requirements.txt` file. First we install `requirements.txt`:
```bash
pip install --upgrade pip
pip install -r requirements.txt
```
After this, depending on which OS:
##### Windows/Intel Macs/Linux
```bash
pip install tensorflow
```
##### M1 Macs
```bash
pip install tensorflow-macos tensorflow-metal
```

## Building the Audio Plugin to run `.json` neural network files
### Configuring
```bash
cd waveform-gen-plugin
```
```bash
cmake -Bbuild -DCMAKE_BUILD_TYPE=Release
```

<!-- cmake -Bbuild-xcode -GXcode -D"CMAKE_OSX_ARCHITECTURES=arm64;x86_64" -->

### Building Plugin
<!-- ### If you want VST3, change AU to VST3 -->
##### AU
```bash
cmake --build build --config Release --target waveform_gen_plugin_AU --parallel
```
##### VST3
```bash
cmake --build build --config Release --target waveform_gen_plugin_VST3 --parallel
```

The plugin will be located in build/plugin/waveform_gen_plugin_artefacts.

### Building CLI Tool

```bash
cmake --build build --config Release --target waveform_gen_cli --parallel
```

Then you can run the CLI tool like:
```bash
./build/cli/Debug/waveform_gen_cli --model-file="/Users/jatin/ChowDSP/Research/RTNeural/RTNeural/models/dense.json" --out-file=test.wav --samples=100000
```

## Using a virtual environment
You may choose to run the library from a virtual environment. Should you wish to do so, this is an example using virtualenv `pip install virtualenv`.
```bash
virtualenv --python=python3.10.10 env
```
```bash
pip install --upgrade pip
```
```bash
source env/bin/activate
```
```bash
pip install -r requirements.txt
```
After doing what you need to do:
```bash
deactivate
```
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
