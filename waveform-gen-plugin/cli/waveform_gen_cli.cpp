#include <argh.h>
#include <fmt/core.h>
#include <sndfile.hh>

#include <filesystem>
namespace fs = std::filesystem;

#include "../src/waveform_gen.h"

constexpr double sample_rate = 48000.0;

void write_file (const fs::path& file_path, const std::vector<float>& data)
{
    fmt::print ("Writing output to file: {}\n", file_path.string());
    SndfileHandle file { file_path.c_str(), SFM_WRITE, SF_FORMAT_WAV | SF_FORMAT_PCM_16, 1, (int) sample_rate };
    file.write (data.data(), (sf_count_t) data.size());
}

int main (int, char* argv[])
{
    fmt::print ("Running waveform generator!\n");

    argh::parser cmdl (argv);

    fs::path output_file_path;
    if (! (cmdl ({ "--out-file" }) >> output_file_path))
    {
        fmt::print ("[ERROR] Must provide an output file!\n");
        return 1;
    }

    waveform_gen::Generator generator;
    if (fs::path model_file_path; cmdl ({ "--model-file" }) >> model_file_path)
    {
        generator.load_model (std::ifstream { model_file_path.c_str(), std::ifstream::binary });

        if (generator.model == nullptr)
        {
            fmt::print ("[ERROR] reading model file!\n");
            return 1;
        }
    }
    else
    {
        fmt::print ("[ERROR] Must provide a model file!\n");
        return 1;

    }

    std::vector<float> data;
    if (int in_size; cmdl ({ "--samples" }) >> in_size)
        data.resize ((size_t) in_size, 0.0f);
    else
        data.resize (10000, 0.0f);

    generator.generate_signal (data);

    write_file (output_file_path, data);

    system (fmt::format ("play {}", output_file_path.string()).c_str());

    return 0;
}
