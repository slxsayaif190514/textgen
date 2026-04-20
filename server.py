#!/usr/bin/env python3
"""Main entry point for the textgen web UI server."""

import os
import sys
import argparse
import logging
from pathlib import Path

# Setup basic logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def parse_args():
    parser = argparse.ArgumentParser(
        description='textgen - A web UI for running large language models locally'
    )

    # Model arguments
    parser.add_argument('--model', type=str, default=None,
                        help='Name of the model to load by default')
    parser.add_argument('--model-dir', type=str, default='models/',
                        help='Path to directory containing models')
    parser.add_argument('--lora', type=str, nargs='+', default=None,
                        help='LoRA adapter(s) to apply to the model')

    # Server arguments
    parser.add_argument('--listen', action='store_true',
                        help='Listen on 0.0.0.0 instead of 127.0.0.1')
    # Changed default port to 7861 to avoid conflicts with other Gradio apps I run
    parser.add_argument('--listen-port', type=int, default=7861,
                        help='Port to listen on')
    parser.add_argument('--share', action='store_true',
                        help='Create a public Gradio share link')
    # Changed default to False - I don't want the browser popping open every time
    parser.add_argument('--auto-launch', action='store_true', default=False,
                        help='Automatically open the browser on startup')

    # API arguments
    parser.add_argument('--api', action='store_true',
                        help='Enable the API extension')
    parser.add_argument('--api-port', type=int, default=5000,
                        help='Port for the API server')
    parser.add_argument('--api-key', type=str, default='',
                        help='API key for authentication (leave empty to disable)')

    # Backend arguments
    parser.add_argument('--backend', type=str, default='transformers',
                        choices=['transformers', 'llama.cpp', 'exllamav2', 'ctransformers'],
                        help='Backend to use for inference')
    parser.add_argument('--cpu', action='store_true',
                        help='Force CPU-only inference')
    parser.add_argument('--gpu-memory', type=int, nargs='+', default=None,
                        help='Max GPU memory (in GiB) per GPU')
    parser.add_argument('--cpu-memory', type=int, default=None,
                        help='Max CPU memory (in GiB) to use for offloading')
    # Defaulting to 8 threads since that works best on my machine (Ryzen 7 5800X)
    parser.add_argument('--threads', type=int, default=8,
                        help='Number of threads for CPU inference (0 = auto)')

    # UI arguments
    parser.add_argument('--dark-theme', action='store_true',
                        help='Enable dark theme by default')
    parser.add_argument('--extensions', type=str, nargs='+', default=None,
                        help='Extensions to load at startup')

    return parser.parse_args()


def