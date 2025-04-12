#  GenSonic: The ASCII Level Auto-Encoder for 2D Platformers

This project presents a specialized auto-encoder designed to process and reconstruct 2D platformer levels but in ascii, with a focus on *Sonic the Hedgehog*. The tool facilitates the transformation of level images into structured data representations and vice versa, enabling advanced level analysis, generation, and AI-based testing.

## Overview

The auto-encoder operates by:

- **Encoding**: Converting level images into a structured format using sprite tokenization.
- **Decoding**: Reconstructing level images from the structured data.
- **Analysis**: Providing tools for comparing original and reconstructed levels to assess fidelity.

This framework is adaptable to various 2D platformers, provided the necessary sprite data is available.

## Repository Structure

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

## How does it work 

GenSonic take as input the image to encode and split it into 256x256 image block first because all level images can be descontruct into smaller blocks and this phase is called the 256-split. And each 256 image is split again into 64x64 image block. The 64-split. Now, we use a dictionary architecture a first one mapping each sprite data (array image) to its name, another one mapping each image name to the corresponding ascii character and finally the sprite pool which is the database of the sprite that we will be using to reconstruct the level. Each data structure communicate with each other to take a 64-image (of the original level), find the closest match in the sprite pool (using AI), retrieve its corresponding ascii character construct the matrix of ascii character for each 256 block.
Then we use those ascii matrixes to reconstruct the big level ascii matrix and save it as a text file. 

Thus, we can have results like this:

From this input image:

![Original Commercial Level](Sonic1_MD_Map_Ghz1.png)

to this ascii file:
![Encoded commercial Level](ascii_commercial_level.png)


### Prerequisites

- Python 3.x
- Recommended: Create a virtual environment

GenSonic can work with any platformer game where the level can be represented as an image. To adapt it to your game, you need to construct first the sprite pool for your game, then the dictionnaries which maps images to their names and then their names to their ascii character. Then give the path of all those files to the script and let the magic operates. 


### Installation

1. **Clone the repository:**
   ```
   git clone https://github.com/vsx23733/level-auto-encoder.git
   cd level-auto-encoder
   ```

2. **Create your own databases**
Create the dictionary mapping the images (arrays) to their names, and their names to the ascii character and the folder containing all the sprites used by your game or your specific level.

3. **Adjust the path**
Adjust the path to the datas in the scripts ("Litteraly just copy paste the paths")

4. **Run the python file**
```
python auto-encoder.py
```

## Future improvements

For this project as it's the v0.0 of GenSonic, then these are the future adjustment:

- Dynamic ascii character mapping (to reduce the manual work the user still have to do)
- Encoder Optimization (optimize the code to speed up the encoding process)
- Encoder improvement (add the color mathing engine to the encoder to make it more accurate)
- UI or bash commands (to simplify the use of the program)

## Contributors

This program was created with [Florian HOUNKPATIN](https://github.com/Kingflow-23)

### Contributions

Any bug ? Issue ? Idea for improvement ? Feel free to create and issue, submit a pull request or simply contact me via email or linkedIn


## LISCENCE

This project is under the MIT Liscence (check the liscence file)
Sega is the only owner of all sprites and assets used in this project. 
Sega don't own any intellectual property on the method used for this project. 
