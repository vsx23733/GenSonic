import os
import cv2
import random
import numpy as np
import pandas as pd
import tensorflow as tf
import matplotlib.pyplot as plt
import gc
from PIL import Image
import cv2
from skimage.metrics import structural_similarity as ssim
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.utils import to_categorical, Sequence
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
import torch
import torchvision.models as models
import torchvision.transforms as transforms
import torch.nn.functional as F
import json

def clean_ascii_spaces(input_file: str, output_file: str, max_empty_lines=0):
    """
    Cleans excessive blank lines from an ASCII file.

    Parameters:
        input_file (str): Path to the original ASCII file.
        output_file (str): Path to save the cleaned ASCII file.
        max_empty_lines (int): Maximum consecutive empty lines allowed.
    """
    with open(input_file, "r") as f:
        lines = f.readlines()

    cleaned_lines = []
    empty_count = 0

    for line in lines:
        if line.strip() == "":
            empty_count += 1
        else:
            empty_count = 0  
        
        if empty_count <= max_empty_lines:
            cleaned_lines.append(line)

    with open(output_file, "w") as f:
        f.writelines(cleaned_lines)


# Slice input level to 256x256 block
def level_image_slicer(level_image_path, patch_size=256) -> list[Image.Image]:
    """
    This function takes as input the image of a commercial level  and will return sliced images of 256x256 pixels
    """
    level_image = Image.open(level_image_path).convert('RGB')
    level_image_array = np.array(level_image)

    h, w, _ = level_image_array.shape

    patches = []
    for i in range(0, h, patch_size):
        for j in range(0, w, patch_size):
            patch = level_image_array[i:i+patch_size, j:j+patch_size, :]
            patch_image = Image.fromarray(patch)
            patches.append(patch_image)

    return patches


# Slice 256x256 into slice 64x64
def mid_block_slicer(mid_block_image, patch_size=64) -> list[Image.Image]:
    """
    This function takes as input an image of 256x256 and will return sliced images of 16x16 pixels
    """
    # mid_block_image = Image.open(mid_block_image_path).convert('RGB')
    mid_block_image_array = np.array(mid_block_image, dtype=np.uint8)

    h, w, _ = mid_block_image_array.shape

    patches = []
    for i in range(0, h, patch_size):
        for j in range(0, w, patch_size):
            patch = mid_block_image_array[i:i+patch_size, j:j+patch_size, :]
            patch_image = Image.fromarray(patch)
            patches.append(patch_image)

    return patches


# Assemble image using slices
def assemble_image(sub_images, image_size, sub_image_size):
    """Assembles a list of image slices into a full image"""

    grid_size = image_size // sub_image_size  # Number of slices per row/column

    sub_images = [np.array(img) for img in sub_images]

    rows = [np.hstack(sub_images[i * grid_size: (i + 1) * grid_size]) for i in range(grid_size)]
    assembled_image = np.vstack(rows)

    assembled_image = Image.fromarray(assembled_image.astype(np.uint8))

    return assembled_image

def assemble_image_updated(sub_images, image_size, sub_image_size):
    """Assembles a list of sub-images into a full rectangular image."""
    h, w = image_size
    sub_h, sub_w = sub_image_size

    grid_rows = w // sub_w  # Number of rows
    grid_cols = h // sub_h  # Number of columns

    if len(sub_images) != grid_rows * grid_cols:
        raise ValueError(f"Expected {grid_rows * grid_cols} sub-images, but got {len(sub_images)}.")

    sub_images = [np.array(img) for img in sub_images]
    
    # Reshape sub-images into rows
    rows = [np.hstack(sub_images[i * grid_cols: (i + 1) * grid_cols]) for i in range(grid_rows)]
    assembled_image = np.vstack(rows)

    return Image.fromarray(assembled_image.astype(np.uint8))


# Model for features extraction
def create_model():
    """
    """

    model = models.resnet50(pretrained=True)
    model = torch.nn.Sequential(*list(model.children())[:-1])
    model = model.eval()

    return model 

# Function to process the images before the extractor
def transform_image(input_image: Image.Image) -> torch.Tensor:
    """
    """

    transform = transforms.Compose([
    transforms.Lambda(lambda img: img.convert("RGB")),
    transforms.Resize((224, 224)), 
    transforms.ToTensor(), 
    transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
    ])

    return transform(input_image).unsqueeze(0)

# Function for features extraction
def extract_features(image):
    """
    """

    image = transform_image(image)  

    model = create_model()


    with torch.no_grad():
        features = model(image)

    return features.view(2048)


# Function to build the sprite pool
def build_sprite_pool(sprite_pool_path: str) -> list:
    """
    """

    sprite_pool = []

    for sprite_path in os.listdir(sprite_pool_path):
        sprite_pool.append(Image.open(os.path.join(sprite_pool_path, sprite_path)))

    return sprite_pool


# Building database of emebdding (embedding  pool)
def build_embedding_database(sprite_pool : list):
    """
    """

    sprite_embeddings_dict = {}
    sprite_image_dict = {}

    for i, sprite_image in enumerate(sprite_pool): # mapper_image_to_name.values()
        sprite_embeddings_dict[i] = extract_features(sprite_image)
        sprite_image_dict[i] = sprite_image

    return sprite_image_dict, sprite_embeddings_dict



# Function to find the closest match of a slice in the sprite pool
def find_closest_match(input_image : Image.Image, embeddings_pool : dict, feature_extractor) -> tuple:
    """
    Takes as input an image and find the closest image in the provided image pool embedding
    The similarity function used here is the cosine similarity
    """

    if isinstance(input_image, Image.Image):
        input_features = extract_features(input_image)  
    elif not isinstance(input_image, torch.Tensor):
        raise TypeError(f"Unexpected input type {type(input_image)}")

    similarity_scores = []
    #input_features = feature_extractor(input_image)
    #input_features = input_features.view(-1)
        
    for sprite_feature in embeddings_pool.values():

        sprite_feature = sprite_feature.view(-1) 

        similarity_score = F.cosine_similarity(
                    sprite_feature.unsqueeze(0),  
                    input_features.unsqueeze(0)
            ).item()
        similarity_scores.append(similarity_score)
    

    best_score = max(similarity_scores)
    best_idx = similarity_scores.index(best_score)
    best_match = embeddings_pool[best_idx]
    return best_match, best_idx

# Load ascii representation of a file
def load_ascii_from_file(file_path: str) -> list:
    """Load ASCII art from a text file and return it as a list of strings (rows)."""
    with open(file_path, "r") as f:
        return f.read().splitlines()
    

# Get the file name based on array of input image (value)
def get_key_by_value(d: dict, value) -> str:
    for key, val in d.items():
        val = np.array(val)
        if np.allclose(val, value, rtol=1e-5, atol=1):
            return key
    print("⚠️ Warning: No exact match found, returning default block")
    return "default_block"  # Ensure "default_block.txt" exists

def load_mappers(mapper_image_to_name_path: str,
                 mapper_name_to_ascii_path: str
                 ) -> tuple[dict, dict]:
    
    with open(mapper_image_to_name_path, "r") as f:
        mapper_image_to_name = json.load(f)
        
    with open(mapper_name_to_ascii_path, "r") as f:
        mapper_name_to_ascii = json.load(f)
    
    return mapper_image_to_name, mapper_name_to_ascii



# Construct the ascii representation of a block 256x256
def image_to_ascii(input_block_image: Image.Image, sub_image_size: int, mapper_image_to_name: dict, mapper_name_to_ascii: dict, file_name: str, output_path: str):
    """
    Build the ascii equivalent of an image.

    Parameters:
        input_block_image : Input image block which will be encoded in ascii. Expecting 256x256 blocks or the image level or the commercial level.
        sub_image_size : The dimension by which the size of the input image block will be divided
        mapper_image_to_name : The dictionary mapping the slice (sub_image_size x sub_image_size) to their ID (name).
        mapper_name_to_ascii : The dictionary mapping the ID of the slice (name) to the corresponding ASCII character.
        file_name: The name of the output file.
    """

    input_block_image_array = np.array(input_block_image)
    # Resize the grayscale image
    input_block_image_array = cv2.resize(input_block_image_array, (128, 128), interpolation=cv2.INTER_LINEAR)

    # Now unpack the shape correctly
    h, w = input_block_image_array.shape

    file_height = int(h / sub_image_size)
    file_width = int(w / sub_image_size)

    ascii_image = []

    for i in range(file_height):
        row = []
        for j in range(file_width):
            sub_block_array = input_block_image_array[(i*sub_image_size):(i*sub_image_size)+sub_image_size, 
                                                      (j*sub_image_size):(j*sub_image_size)+sub_image_size]
            sub_block_name = ""

            # Compare sub-block to find the matching sprite in the dictionary
            for sprite_name, sprite in mapper_image_to_name.items():
                sprite = np.array(sprite, dtype=np.uint8)
                # Convert sprite to grayscale
                if len(sprite.shape) == 3:  
                    sprite = cv2.cvtColor(sprite, cv2.COLOR_RGB2GRAY)

                if len(sub_block_array.shape) == 3:
                    sub_block_array = cv2.cvtColor(sub_block_array, cv2.COLOR_RGB2GRAY)

                if np.allclose(sprite, sub_block_array, rtol=1e-5, atol=1):
                    #print(sprite_name)
                    sub_block_name = sprite_name
                    break

            #if sub_block_name == "":
            #    print("No block found !!")

            sub_block_ascii = mapper_name_to_ascii.get(sub_block_name, " ")  # Default to space if no match found
            row.append(sub_block_ascii)
        
        ascii_image.append(''.join(row))

    with open(os.path.join(output_path, file_name), "w") as f:
        for row in ascii_image:
            f.write(row + "\n")

    return ascii_image


# Create the ascii representation of the commercial level
def compose_ascii(large_image: Image.Image, block_size: int, slice_size: int,
                              ascii_folder: str, output_file: str, block_to_ascii: dict):
    """
    Create the ASCII equivalent of a large image using precomputed ASCII blocks.
    
    Parameters:
        large_image : PIL Image of the large image to be converted.
        block_size : The size of each block (assumes square blocks, e.g., 256x256).
        slice_size : The size of each slice of the block (32x32 or 64x64)
        ascii_folder : Folder containing the ASCII block text files.
        output_file : The file name to save the ASCII output.
        block_to_ascii : Maps each block to its ASCII representation. Key is file name and value the array of the block. 
        
    """
    # Convert the large image to a numpy array
    # gray_large_image = large_image.convert("L")
    large_image_array = np.array(large_image)
    h, w = large_image_array.shape
    assert h % block_size == 0 and w % block_size == 0, "Image dimensions must be multiples of block_size"
    
    ascii_blocks = {} # key: file_name, value: ascii
    for filename in os.listdir(ascii_folder):
        if filename.endswith(".txt"):
            block_name = filename.split(".")[0]  # Use filename as a key
            file_path = os.path.join(ascii_folder, filename)
            ascii_blocks[block_name] = load_ascii_from_file(file_path)
    
    ascii_representation = []
    
    # Process the large image in blocks
    for i in range(0, h, block_size):
        ascii_rows = ["" for _ in range(block_size)]  # Prepare rows to append ASCII text
        for j in range(0, w, block_size):
            block = large_image_array[i:i+block_size, j:j+block_size]
            block_name = get_key_by_value(
                d=block_to_ascii,
                value=block
            ) # Retrieve the filename based on the image block
            block_name = block_name.split(".")[0] # Retrieve the file name of the ascii based on array block
            
            matched_ascii = ascii_blocks.get(block_name, [" " * block_size] * block_size) # Retrieve the ascii corresponding
            
            for k in range(len(matched_ascii)):  # Use actual ASCII block length
                ascii_rows[k] += matched_ascii[k]
        
        # Append full ASCII block rows to final representation
        ascii_representation.extend(ascii_rows)
    
    # Save to file
    with open(output_file, "w") as f:
        for row in ascii_representation:
            f.write(row + "\n")
    
    return ascii_representation


# Clean the ascii file from empty lines
def clean_ascii_spaces(input_file: str, output_file: str, max_empty_lines=0):
    """
    Cleans excessive blank lines from an ASCII file.

    Parameters:
        input_file (str): Path to the original ASCII file.
        output_file (str): Path to save the cleaned ASCII file.
        max_empty_lines (int): Maximum consecutive empty lines allowed.
    """
    with open(input_file, "r") as f:
        lines = f.readlines()

    cleaned_lines = []
    empty_count = 0

    for line in lines:
        if line.strip() == "":
            empty_count += 1
        else:
            empty_count = 0  # Reset if a non-empty line appears
        
        if empty_count <= max_empty_lines:
            cleaned_lines.append(line)

    with open(output_file, "w") as f:
        f.writelines(cleaned_lines)


# The auto-encoder function
def auto_encoder(commercial_level_path: str,
                 sprite_pool_path: str, 
                 mapper_image_to_name_path: str,
                 mapper_name_to_ascii_path: str,
                 model):
    
    mapper_image_to_name, mapper_name_to_ascii = load_mappers(mapper_image_to_name_path, mapper_name_to_ascii_path)
    
    if not os.path.exists(sprite_pool_path) or not os.listdir(sprite_pool_path):
        raise ValueError(f"Sprite pool path {sprite_pool_path} is invalid or empty.")
    

    # Defining path of images and txt file 
    block_output_path = "commercial_block_folder" # To save the blocks 256x256
    block_slices_path = "block_slices_folder" # To save the slices 64x64
    reassembled_block_output_path = "reassembled_commercial_block_folder" # To save the reasselbled 256x256
    ascii_output_path = "ascii_block_folder" # To save the ascii of the 256x256 block 
    os.makedirs(block_output_path, exist_ok=True)
    os.makedirs(block_slices_path, exist_ok=True)
    os.makedirs(reassembled_block_output_path, exist_ok=True)
    os.makedirs(ascii_output_path, exist_ok=True)


    
    first_level_sprite_pool_path = sprite_pool_path  
    sprite_pool = [Image.open(os.path.join(first_level_sprite_pool_path, sprite_path)) 
                   for sprite_path in os.listdir(first_level_sprite_pool_path)]

    if len(sprite_pool) < 35:
        print(f"Warning: Sprite pool contains only {len(sprite_pool)} images.")

    sprite_pool = build_sprite_pool(sprite_pool_path)  # Limit to first 35 images
    # sprite_pool = sprite_pool[:35]
    
    # Create sprite embeddings pool
    sprite_image_dict, sprite_embeddings_dict = build_embedding_database(sprite_pool=sprite_pool)

    
    # Slice the commercial level image
    commercial_lvl_img_patch = level_image_slicer(
        level_image_path=commercial_level_path, 
        patch_size=256
    )

    # data
    
    block_to_ascii = {}  
    commercial_lvl_reassambled_block_L = []
    commercial_lvl_reassambled_block = []

    # Saving each sliced block
    for k, block in enumerate(commercial_lvl_img_patch):
        block_path = os.path.join(block_output_path, f"initial_block_{k+1}.png")
        block.save(block_path)
        #print(f"initial_block_{k+1}.png saved")

    for i, img_block in enumerate(commercial_lvl_img_patch):
        block_folder = os.path.join(block_slices_path, f"block_{i+1}")
        match_folder = os.path.join(block_folder, f"block_match_{i+1}")
        os.makedirs(block_folder, exist_ok=True)
        os.makedirs(match_folder, exist_ok=True) 
        
        # Slice each block of 256x256

        img_block_slices = mid_block_slicer(img_block, patch_size=64)
        img_block_slices_matches_L = []
        img_block_slices_matches = []
        
        # Find closest match of the slice and saving it

        for j, slice in enumerate(img_block_slices): 
            match_idx = find_closest_match(slice, sprite_embeddings_dict, model)[1]
            matched_sprite = sprite_image_dict[match_idx]
            # img_block_slices_matches.append(matched_sprite)
            img_block_slices_matches.append(matched_sprite)
            slice_path = os.path.join(block_folder, f"slice_{j+1}.png")
            slice_match_path = os.path.join(match_folder, f"slice_match_{j+1}.png")
            slice.save(slice_path)
            matched_sprite.save(slice_match_path)

        # Using saved matched to reassemble the 256x256 block and save reassembled block

        for slice_path in os.listdir(match_folder):
            slice_path = os.path.join(match_folder, slice_path)
            slice = Image.open(slice_path).convert("L")
            img_block_slices_matches_L.append(slice)
        
        img_block_reassembled = assemble_image_updated(
            sub_images=img_block_slices_matches,
            image_size=(128, 128),
            sub_image_size=(32, 32)
        ) # For ascii recontruction
        img_block_reassembled_L = assemble_image_updated(
            sub_images=img_block_slices_matches_L,
            image_size=(128, 128),
            sub_image_size=(32, 32)
        ) # To save the image

        img_block_reassembled_path = os.path.join(reassembled_block_output_path, f"reassembled_block_{i+1}.png")
        img_block_reassembled_L.save(img_block_reassembled_path)
        #print(f"Block reassembled {i+1} saved")

        
        reassembled_block = Image.open(img_block_reassembled_path) # L mode Image
        commercial_lvl_reassambled_block_L.append(reassembled_block) # L commercial image block
        commercial_lvl_reassambled_block.append(img_block_reassembled) # Normal commercial image block

        file_name = f"img_block_{i+1}.txt"
        image_to_ascii(
            input_block_image=img_block_reassembled,  
            sub_image_size=32,
            mapper_image_to_name=mapper_image_to_name,
            mapper_name_to_ascii=mapper_name_to_ascii,
            file_name=file_name,
            output_path=ascii_output_path
        )
        img_block_reassembled = img_block_reassembled.resize((256, 256))
        block_to_ascii[file_name] = np.array(img_block_reassembled).tolist()

    commercial_lvl_image = Image.open(commercial_level_path)
    h, w = commercial_lvl_image.size

    print(f"Number of sub-images: {len(commercial_lvl_reassambled_block_L)}")

    print(f"Original Image Size: {h}x{w}")
    print(f"Expected Grid: {h // 256} rows × {w // 256} cols = {(h // 256) * (w // 256)} sub-images")
    print(f"Actual Number of Sub-images: {len(commercial_lvl_reassambled_block_L)}")


    resized_commercial_lvl_reassambled_block_L = [img.resize((256, 256)) for img in commercial_lvl_reassambled_block_L]
    resized_commercial_lvl_reassambled_block = [img.resize((256, 256)) for img in commercial_lvl_reassambled_block]

    # Final reconstruction
    commercial_lvl_reassambled_L = assemble_image_updated(
        sub_images=resized_commercial_lvl_reassambled_block_L,
        image_size=(h, w),
        sub_image_size=(256, 256) 
    ) # For image saving
    
    
    commercial_lvl_reassambled = assemble_image_updated(
        sub_images=resized_commercial_lvl_reassambled_block,
        image_size=(h, w),
        sub_image_size=(256, 256)  
    ) # For image reconstruction

    print("Commercial level reassembled saved")
    commercial_lvl_reassambled_L.convert("L").save("reassembled_commercial_level.png")

    # Final ascii encoding
    ascii_folder = r"C:\Users\axelo\Documents\Projects\level-auto-encoder\ascii_block_folder"
    os.makedirs(ascii_folder, exist_ok=True)


    print("Constructing the ascii representation of the commercial level...")
    encoded_commercial_level = "ascii_commercial_level.txt"
    ascii_representation_lvl = compose_ascii(
        large_image=commercial_lvl_reassambled,
        block_size=256,
        slice_size=64,
        ascii_folder=ascii_folder,
        output_file=encoded_commercial_level,
        block_to_ascii=block_to_ascii
    )
    if ascii_representation_lvl:
        print(f"Encoded commercial level saved as {encoded_commercial_level}")
    else:
        print("Failed to encode commercial level")


def main():

    model = create_model()
    print("Encoding the level...")
    auto_encoder(
            commercial_level_path=r"C:\Users\axelo\Documents\COURS PGE 3\AI CLINIC\S1\level-auto-encoder\Sonic1_MD_Map_Ghz1.png", # Path to the level to encode
            sprite_pool_path=r"C:\Users\axelo\Documents\COURS PGE 3\AI CLINIC\S1\level-auto-encoder\sprite_pool_level_1", #  Path to the sprite database
            mapper_image_to_name_path=r"C:\Users\axelo\Documents\COURS PGE 3\AI CLINIC\S1\level-auto-encoder\sprites_data\level_1.json", # Path to 
            mapper_name_to_ascii_path=r"C:\Users\axelo\Documents\COURS PGE 3\AI CLINIC\S1\level-auto-encoder\sprites_token\lvl_1_token_mapping.json",
            model=model
        )
    print("Encoding finished !!")



if __name__ == "__main__":
    main()
    