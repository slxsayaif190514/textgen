# textgen

A fork of [oobabooga/text-generation-webui](https://github.com/oobabooga/text-generation-webui) with additional features and improvements.

## Features

- Web UI for running large language models
- Support for multiple backends (llama.cpp, ExLlamaV2, transformers, etc.)
- OpenAI-compatible API
- Character/persona support
- Extensions system

## Installation

### One-click installers

Download the latest release for your platform from the [Releases](../../releases) page.

| Platform | File |
|----------|------|
| Windows (CUDA) | `textgen-windows-cuda.zip` |
| Linux (CUDA) | `textgen-linux-cuda.tar.gz` |
| macOS | `textgen-macos.tar.gz` |

### Manual installation

```bash
git clone https://github.com/yourusername/textgen
cd textgen
pip install -r requirements.txt
python server.py
```

### With conda

```bash
conda create -n textgen python=3.11
conda activate textgen
pip install -r requirements.txt
python server.py
```

## Usage

```bash
# Start the web UI
python server.py

# Start with API enabled
python server.py --api

# Start on a specific port
python server.py --port 7860

# Load a model at startup
python server.py --model your-model-name

# My usual launch command (listen on all interfaces for local network access)
python server.py --api --listen --port 7860

# With a specific model and GPU memory limit (useful on my 8GB card)
python server.py --api --listen --port 7860 --model mistral-7b-instruct --gpu-memory 7

# Low VRAM mode - handy when running other stuff in the background
python server.py --api --listen --port 7860 --model mistral-7b-instruct --gpu-memory 5 --cpu-memory 8

# ExLlamaV2 loader tends to be faster for quantized models on my setup
python server.py --api --listen --port 7860 --model mistral-7b-instruct --loader exllamav2 --gpu-memory 7
```

## Docker

```bash
docker compose up
```

## Contributing

Pull requests are welcome. Please check the existing issues before opening a new one.

## License

AGPL-3.0
