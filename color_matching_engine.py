import os
import math
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image

def get_level_sprite_dict(level_sprite_dir):
    """
    Scans a directory for level sprite images and organizes them by level number.
    
    Parameters:
    - level_sprite_dir (str): Path to the directory containing sprite images.
    
    Returns:
    - dict: Dictionary mapping level numbers to a list of sprite filenames.
    """
    level_sprite_dict = {}
    
    for filename in os.listdir(level_sprite_dir):
        if filename.startswith("sprite_") and filename.endswith(".png"):
            try:
                _, i, j = filename.rstrip(".png").split("_")
                i = int(i)
                j = int(j)
            except ValueError:
                continue

            # Determines the level number based on row index
            level_number = i // 7

            if level_number not in level_sprite_dict:
                level_sprite_dict[level_number] = []

            level_sprite_dict[level_number].append(filename)
    
    return level_sprite_dict

def get_most_frequent_color(image):
    """
    Determines the most frequent color in an image.
    
    Parameters:
    - image (PIL.Image): Image to analyze.
    
    Returns:
    - tuple: The most frequent RGB color.
    """
    image = image.convert("RGB")
    pixels = list(image.getdata())

    color_count = {}
    for pixel in pixels:
        if pixel in color_count:
            color_count[pixel] += 1
        else:
            color_count[pixel] = 1

    # Find the color with the maximum count
    most_frequent_color = max(color_count, key=color_count.get)
    return most_frequent_color

def get_level_main_color(level_sprite_dict, basic_sprite_folder_path):
    """
    Computes the most frequent color for each level by analyzing all its sprites.
    
    Parameters:
    - level_sprite_dict (dict): Dictionary mapping level numbers to sprite filenames.
    - basic_sprite_folder_path (str): Path to the sprite directory.
    
    Returns:
    - dict: Dictionary mapping level numbers to their dominant color and sprites.
    """
    new_level_sprite_dict = {}
    
    for level, sprite_path in level_sprite_dict.items():
        color_counts = {}
        
        for sprite in sprite_path:
            image = Image.open(f"{basic_sprite_folder_path}/{sprite}")
            main_color = get_most_frequent_color(image)

            if main_color in color_counts:
                color_counts[main_color] += 1
            else:
                color_counts[main_color] = 1
                
        main_color = max(color_counts, key=color_counts.get)
        new_level_sprite_dict[level] = (main_color, sprite_path)

    return new_level_sprite_dict 

def show_color(rgb):
    """
    Displays a color as a square using Matplotlib.
    
    Parameters:
    - rgb (tuple): RGB color tuple.
    """
    color_array = np.zeros((100, 100, 3), dtype=np.uint8)
    color_array[:, :] = rgb  # Fill the array with the given color

    plt.imshow(color_array)
    plt.axis("off")  # Hide axis
    plt.show()
    
def calculate_color_distance(color1, color2):
    """
    Computes the Euclidean distance between two RGB colors.
    
    Parameters:
    - color1 (tuple): First RGB color.
    - color2 (tuple): Second RGB color.
    
    Returns:
    - float: Euclidean distance between the two colors.
    """
    return math.sqrt(sum((color1[i] - color2[i]) ** 2 for i in range(3)))

def find_closest_sprites(level_image, level_sprite_dict, level_sprite_dir):
    """
    Identifies the closest matching set of sprites based on color similarity.
    
    Parameters:
    - level_image (PIL.Image): Input level image.
    - level_sprite_dict (dict): Dictionary mapping level numbers to sprite filenames.
    - level_sprite_dir (str): Path to the sprite directory.
    
    Returns:
    - list: List of sprite filenames from the closest matching level.
    """
    input_main_color = get_most_frequent_color(level_image)
    
    # print("Main color of input level:")
    # show_color(input_main_color)
    
    # Compute the dominant color for each level sprites
    level_main_colors = get_level_main_color(level_sprite_dict, level_sprite_dir)

    closest_level = None
    min_distance = float("inf")

    # Find the level with the closest color match
    for level, level_info in level_main_colors.items():
        distance = calculate_color_distance(input_main_color, level_info[0])
        if distance < min_distance:
            min_distance = distance
            closest_level = level

    # print("Closest sprites color found:")
    # show_color(level_main_colors[closest_level][0])
    
    return level_sprite_dict.get(closest_level, []) 


if __name__ == "__main__":
    level_sprite_dir = "all_general_map_sprite"         # Directory containing sprites
    level_sprite_dict = get_level_sprite_dict(level_sprite_dir)
    
    level_path = "Sonic1_MD_Map_Ghz1.png"               # Path to input level image
    level_image = Image.open(level_path)
    find_closest_sprites(level_image, level_sprite_dict, level_sprite_dir)