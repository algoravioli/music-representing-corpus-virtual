#include <random>
#include "waveform_gen.h"

namespace waveform_gen
{
Generator::Generator()
{
    std::random_device rd;
    auto gen = std::minstd_rand(rd());
    std::uniform_real_distribution<float> distro(-0.5f, 0.5f);
    urng = std::bind(distro, gen); // NOLINT
}

void Generator::load_model (std::ifstream&& json_stream)
{
    model = RTNeural::json_parser::parseJson<float> (json_stream);
    model_input.resize ((size_t) model->getInSize(), 0.0f);
}

void Generator::load_model (nlohmann::json&& model_json)
{
    model = RTNeural::json_parser::parseJson<float> (model_json);
    model_input.resize ((size_t) model->getInSize(), 0.0f);
}

void Generator::generate_signal (std::span<float> data)
{
    if (model == nullptr)
    {
        std::fill (data.begin(), data.end(), 0.0f);
        return;
    }

    for (auto& sample : data)
    {
        for (float& input_channel : model_input)
            input_channel = urng();
        sample = model->forward (model_input.data());
    }
}
}
