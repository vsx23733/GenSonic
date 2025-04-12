# Level Auto-Encoder for 2D Platformers

This project presents a specialized auto-encoder designed to process and reconstruct 2D platformer levels, with a focus on *Sonic the Hedgehog*. The tool facilitates the transformation of level images into structured data representations and vice versa, enabling advanced level analysis, generation, and AI-based testing.

## 🔍 Overview

The auto-encoder operates by:

- **Encoding**: Converting level images into a structured format using sprite tokenization.
- **Decoding**: Reconstructing level images from the structured data.
- **Analysis**: Providing tools for comparing original and reconstructed levels to assess fidelity.

This framework is adaptable to various 2D platformers, provided the necessary sprite data is available.

## 📁 Repository Structure

- **`auto-encoder.py`**: Core script for encoding and decoding level images.
- **`color_matching_engine.py`**: Handles color-based sprite matching.
- **`image_comparison.py`**: Tools for comparing original and reconstructed images.
- **`image_matching_engine.ipynb`**: Jupyter notebook demonstrating image matching processes.
- **`json_modifier_scripts.py`**: Scripts for modifying JSON representations of levels.
- **`matching.ipynb`**: Notebook showcasing matching algorithms and results.
- **`encoder_output/`**: Contains outputs from the encoding process.
- **`mappers/`**: Mapping configurations between sprites and tokens.
- **`mapsheet data/`**: Data related to level mapsheets.
- **`sprite_data_token_scripts/`**: Scripts for handling sprite data and tokenization.
- **`sprite_pool_level_1/`**: Sprite assets specific to Level 1.
- **`sprites_data/`**: General sprite data used across levels.
- **`sprites_token/`**: Token representations of sprites.
- **`Sonic1_MD_Map_Ghz1.png`**: Original map image of Green Hill Zone Act 1.
- **`ascii_commercial_level.txt`**: ASCII representation of a commercial level.
- **`reassembled_commercial_level.png`**: Reconstructed image from encoded data.

## 🛠️ Getting Started

### Prerequisites

- Python 3.x
- Recommended: Create a virtual environment

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vsx23733/level-auto-encoder.git
   cd level-auto-encoder
