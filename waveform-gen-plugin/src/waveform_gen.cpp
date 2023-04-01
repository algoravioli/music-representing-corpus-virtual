#include <random>
#include "waveform_gen.h"

namespace waveform_gen
{
Generator::Generator() = default;

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

void Generator::generate_signal (std::span<const float> input, std::span<float> data)
{
    if (model == nullptr)
    {
        std::fill (data.begin(), data.end(), 0.0f);
        return;
    }

    for (size_t idx = 0; idx < data.size(); ++idx)
    {
        model_input[0] = input[idx];

        data[idx] = model->forward (model_input.data());

        // shift input signal history
        for (size_t hist_idx = model->getInSize() - 1; hist_idx > 0; --hist_idx)
            model_input[hist_idx] = model_input[hist_idx - 1];
    }
}
}
