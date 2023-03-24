#pragma once

#include <span>
#include <RTNeural/RTNeural.h>

namespace waveform_gen
{
struct Generator
{
    Generator();

    void load_model (nlohmann::json&& model_json);
    void load_model (std::ifstream&& json_stream);

    void generate_signal (std::span<float> data);

    std::unique_ptr<RTNeural::Model<float>> model;
    std::vector<float, xsimd::aligned_allocator<float>> model_input;
    std::function<float()> urng;
};
}
