"""Shared state and configuration for the text generation server."""

import argparse
from pathlib import Path

# Global args namespace, populated by server.py
args = argparse.Namespace()

# Model state
model = None
tokenizer = None
model_name = "None"
model_type = None
loaded_preset = None

# Generation settings
stop_everything = False
generate_params = {}

# Paths
base_dir = Path(__file__).resolve().parent.parent
models_dir = base_dir / "models"
loras_dir = base_dir / "loras"
prompts_dir = base_dir / "prompts"
presets_dir = base_dir / "presets"
characters_dir = base_dir / "characters"
extensions_dir = base_dir / "extensions"
logs_dir = base_dir / "logs"

# Ensure core directories exist
for _dir in [models_dir, loras_dir, prompts_dir, presets_dir, characters_dir, logs_dir]:
    _dir.mkdir(parents=True, exist_ok=True)

# Extension state
enabled_extensions = []
extension_state = {}

# UI / server settings
gradio_auth = None
server_url = ""

# Default generation parameters
default_settings = {
    "temperature": 1.0,
    "top_p": 1.0,
    "top_k": 0,
    "repetition_penalty": 1.0,
    "max_new_tokens": 200,
    "seed": -1,
    "do_sample": True,
    "typical_p": 1.0,
    "epsilon_cutoff": 0,
    "eta_cutoff": 0,
    "tfs": 1.0,
    "top_a": 0.0,
    "min_length": 0,
    "no_repeat_ngram_size": 0,
    "num_beams": 1,
    "penalty_alpha": 0.0,
    "length_penalty": 1.0,
    "early_stopping": False,
    "mirostat_mode": 0,
    "mirostat_tau": 5.0,
    "mirostat_eta": 0.1,
    "guidance_scale": 1.0,
    "negative_prompt": "",
    "ban_eos_token": False,
    "add_bos_token": True,
    "skip_special_tokens": True,
    "truncation_length": 2048,
    "custom_stopping_strings": "",
}


def is_model_loaded() -> bool:
    """Return True if a model is currently loaded."""
    return model is not None


def get_model_name() -> str:
    """Return the name of the currently loaded model."""
    return model_name


def list_model_names() -> list[str]:
    """Scan the models directory and return a sorted list of model folder names."""
    if not models_dir.exists():
        return []
    names = [
        p.name
        for p in sorted(models_dir.iterdir())
        if p.is_dir() and not p.name.startswith(".")
    ]
    return names


def list_preset_names() -> list[str]:
    """Return a sorted list of preset file stems (without extension)."""
    if not presets_dir.exists():
        return []
    return sorted(
        p.stem for p in presets_dir.glob("*.yaml")
    ) + sorted(
        p.stem for p in presets_dir.glob("*.json")
    )
