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
```

## Docker

```bash
docker compose up
```

## Contributing

Pull requests are welcome. Please check the existing issues before opening a new one.

## License

AGPL-3.0
