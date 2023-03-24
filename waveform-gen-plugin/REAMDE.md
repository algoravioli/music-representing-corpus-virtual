## Configuring

```bash
$ cmake -Bbuild -DCMAKE_BUILD_TYPE=Release
```

## Building Plugin

```bash
$ cmake --build build --config Release --target waveform_gen_plugin_VST3 --parallel
```

The plugin will be located in build/plugin/waveform_gen_plugin_artefacts.

## Building CLI Tool

```bash
$ cmake --build build --config Release --target waveform_gen_cli --parallel
```

Then you can run the CLI tool like:
```bash
./build/cli/Debug/waveform_gen_cli --model-file="/Users/jatin/ChowDSP/Research/RTNeural/RTNeural/models/dense.json" --out-file=test.wav --samples=100000
```
