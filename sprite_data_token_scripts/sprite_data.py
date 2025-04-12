import os
import re
import json
import numpy as np

from PIL import Image

sprites_path = r"C:\Users\axelo\Documents\Projects\level-auto-encoder\all_general_map_sprite"
sprites = os.listdir(sprites_path)

sprites = sorted(sprites, key=lambda f: tuple(map(int, re.findall(r"\d+", f))))

# -------------------------------------------- LEVEL 1

batch = 256

level_1_sprites = {
    # -- INCLINED / SLOPE PIECES --
    
    # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[0]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[1]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[2]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[3]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[4]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[5]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[6]}")
    ),
    
    # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[16]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[17]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[18]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[19]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[20]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[21]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[22]}")
    ),
    
    # -- LOOP & CORNER PIECES --

    # RIGHT SIDE
    "loop_bottom_middle_right": np.array(Image.open(f"{sprites_path}/{sprites[7]}")),
    "loop_bottom_right": np.array(Image.open(f"{sprites_path}/{sprites[8]}")),
    "loop_right_middle_bottom": np.array(Image.open(f"{sprites_path}/{sprites[9]}")),
    "loop_right_middle_top": np.array(Image.open(f"{sprites_path}/{sprites[10]}")),
    "loop_top_right": np.array(Image.open(f"{sprites_path}/{sprites[11]}")),
    "loop_top_middle_right": np.array(Image.open(f"{sprites_path}/{sprites[12]}")),
    
    # LEFT SIDE
    "loop_bottom_middle_left": np.array(Image.open(f"{sprites_path}/{sprites[23]}")),
    "loop_bottom_left": np.array(Image.open(f"{sprites_path}/{sprites[24]}")),
    "loop_left_middle_bottom": np.array(Image.open(f"{sprites_path}/{sprites[25]}")),
    "loop_left_middle_top": np.array(Image.open(f"{sprites_path}/{sprites[26]}")),
    "loop_top_left": np.array(Image.open(f"{sprites_path}/{sprites[27]}")),
    "loop_top_middle_left": np.array(Image.open(f"{sprites_path}/{sprites[28]}")),
    
    # -- GROUND / SAND GROUND / CHECKER TILES --
    
        # GROUND TILES
    
            # LOW
    "low_ground_v1": np.array(Image.open(f"{sprites_path}/{sprites[13]}")),
    "low_ground_v2": np.array(Image.open(f"{sprites_path}/{sprites[15]}")),
    "low_ground_v3": np.array(Image.open(f"{sprites_path}/{sprites[29]}")),
    "low_ground_v4": np.array(Image.open(f"{sprites_path}/{sprites[31]}")),
    
    "triangle_ground": np.array(Image.open(f"{sprites_path}/{sprites[30]}")),
    
            # HIGH
    "curved_ground": np.array(Image.open(f"{sprites_path}/{sprites[14]}")),
    
    "high_ground_v1": np.array(Image.open(f"{sprites_path}/{sprites[33]}")),
    "high_ground_v2": np.array(Image.open(f"{sprites_path}/{sprites[34]}")),
    "high_ground_v3": np.array(Image.open(f"{sprites_path}/{sprites[36]}")),
    "high_ground_v4": np.array(Image.open(f"{sprites_path}/{sprites[47]}")),
    
    "high_ground_top_left_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[37]}")
    ),
    "high_ground_top_left_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[39]}")
    ),
    "high_ground_top_left_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[41]}")
    ),
    "high_ground_top_left_grass_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[42]}")
    ),
    "high_ground_top_right_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[38]}")
    ),
    "high_ground_top_right_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[40]}")
    ),
    "high_ground_top_right_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[43]}")
    ),
    "high_ground_top_right_grass_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[44]}")
    ),
    
        # SAND GROUND TILES
    
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_sand_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[64]}")
    ),
    "inclined_sand_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[65]}")
    ),
    "inclined_sand_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[66]}")
    ),
    "inclined_sand_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[67]}")
    ),
    "inclined_sand_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[68]}")
    ),
    "inclined_sand_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[69]}")
    ),
    "inclined_sand_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[70]}")
    ),
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_sand_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[80]}")
    ),
    "inclined_sand_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[81]}")
    ),
    "inclined_sand_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[82]}")
    ),
    "inclined_sand_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[83]}")
    ),
    "inclined_sand_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[84]}")
    ),
    "inclined_sand_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[85]}")
    ),
    "inclined_sand_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[86]}")
    ),
    
            # LOW
    "low_sand_ground_v1": np.array(Image.open(f"{sprites_path}/{sprites[77]}")),
    "low_sand_ground_v2": np.array(Image.open(f"{sprites_path}/{sprites[79]}")),
    
    "low_sand_ground_waterfall_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[93]}")
    ),
    "low_sand_ground_waterfall_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[95]}")
    ),
    "triangle_sand_ground": np.array(Image.open(f"{sprites_path}/{sprites[94]}")),
    
            # HIGH
    "curved_sand_ground": np.array(Image.open(f"{sprites_path}/{sprites[78]}")),
    
    "high_sand_ground_v1": np.array(Image.open(f"{sprites_path}/{sprites[96]}")),
    "high_sand_ground_v2": np.array(Image.open(f"{sprites_path}/{sprites[97]}")),
    "high_sand_ground_v3": np.array(Image.open(f"{sprites_path}/{sprites[98]}")),
    "high_sand_ground_v4": np.array(Image.open(f"{sprites_path}/{sprites[99]}")),
    "high_sand_ground_v5": np.array(Image.open(f"{sprites_path}/{sprites[100]}")),
    "high_sand_ground_v6": np.array(Image.open(f"{sprites_path}/{sprites[101]}")),
    "high_sand_ground_v7": np.array(Image.open(f"{sprites_path}/{sprites[102]}")),
    "high_sand_ground_v8": np.array(Image.open(f"{sprites_path}/{sprites[103]}")),
    "high_sand_ground_v9": np.array(Image.open(f"{sprites_path}/{sprites[104]}")),
    "high_sand_ground_v10": np.array(Image.open(f"{sprites_path}/{sprites[105]}")),
    "high_sand_ground_v11": np.array(Image.open(f"{sprites_path}/{sprites[106]}")),
    "high_sand_ground_v12": np.array(Image.open(f"{sprites_path}/{sprites[107]}")),
    "high_sand_ground_v13": np.array(Image.open(f"{sprites_path}/{sprites[108]}")),
    "high_sand_ground_v14": np.array(Image.open(f"{sprites_path}/{sprites[109]}")),
    "high_sand_ground_v15": np.array(Image.open(f"{sprites_path}/{sprites[110]}")),
    "high_sand_ground_v16": np.array(Image.open(f"{sprites_path}/{sprites[111]}")),
    
        
        # CHECKER TILES
    
            # LOW
    "low_checker_v1": np.array(Image.open(f"{sprites_path}/{sprites[148]}")),
    "low_checker_v2": np.array(Image.open(f"{sprites_path}/{sprites[149]}")),
    
            # HIGH
    "high_checker_v1": np.array(Image.open(f"{sprites_path}/{sprites[32]}")),
    "high_checker_v2": np.array(Image.open(f"{sprites_path}/{sprites[35]}")),
    "high_checker_v3": np.array(Image.open(f"{sprites_path}/{sprites[45]}")),
    "high_checker_v4": np.array(Image.open(f"{sprites_path}/{sprites[46]}")),
    "high_checker_v5": np.array(Image.open(f"{sprites_path}/{sprites[135]}")),
    "high_checker_v6": np.array(Image.open(f"{sprites_path}/{sprites[150]}")),
    "high_checker_v7": np.array(Image.open(f"{sprites_path}/{sprites[151]}")),
    "high_checker_v8": np.array(Image.open(f"{sprites_path}/{sprites[152]}")),
    "high_checker_v9": np.array(Image.open(f"{sprites_path}/{sprites[153]}")),
    "high_checker_v10": np.array(Image.open(f"{sprites_path}/{sprites[154]}")),
    "high_checker_v11": np.array(Image.open(f"{sprites_path}/{sprites[155]}")),
    "high_checker_v12": np.array(Image.open(f"{sprites_path}/{sprites[156]}")),
    "high_checker_v13": np.array(Image.open(f"{sprites_path}/{sprites[157]}")),
    "high_checker_v14": np.array(Image.open(f"{sprites_path}/{sprites[251]}")),
    "high_checker_v15": np.array(Image.open(f"{sprites_path}/{sprites[252]}")),
    
    # -- BRIDGE PIECES --
    "bridge_piece_from_left": np.array(Image.open(f"{sprites_path}/{sprites[158]}")),
    "bridge_piece_from_right": np.array(Image.open(f"{sprites_path}/{sprites[159]}")),
    
    "bridge_support_top_right": np.array(Image.open(f"{sprites_path}/{sprites[237]}")),
    "bridge_support_top_left": np.array(Image.open(f"{sprites_path}/{sprites[238]}")),
    "bridge_two_top_supports": np.array(Image.open(f"{sprites_path}/{sprites[239]}")),
    
    # -- PALM TREES, BUSH & FLOWERS --
    "palm_tree_top_left": np.array(Image.open(f"{sprites_path}/{sprites[173]}")),
    "palm_tree_top_middle": np.array(Image.open(f"{sprites_path}/{sprites[174]}")),
    "palm_tree_top_right": np.array(Image.open(f"{sprites_path}/{sprites[175]}")),
    "palm_tree_middle_left": np.array(Image.open(f"{sprites_path}/{sprites[176]}")),
    "palm_tree_middle": np.array(Image.open(f"{sprites_path}/{sprites[177]}")),
    "palm_tree_middle_right": np.array(Image.open(f"{sprites_path}/{sprites[178]}")),
    "palm_tree_bottom_left": np.array(Image.open(f"{sprites_path}/{sprites[179]}")),
    "palm_tree_bottom_right": np.array(Image.open(f"{sprites_path}/{sprites[180]}")),
    "palm_tree_trunk_classic_background": np.array(
        Image.open(f"{sprites_path}/{sprites[181]}")
    ),
    "palm_tree_trunk_special_background": np.array(
        Image.open(f"{sprites_path}/{sprites[182]}")
    ),
    "palm_tree_trunk_sea_background": np.array(
        Image.open(f"{sprites_path}/{sprites[183]}")
    ),
    
    "little_flower_middle": np.array(Image.open(f"{sprites_path}/{sprites[160]}")),
    "flower_middle": np.array(Image.open(f"{sprites_path}/{sprites[161]}")),
    "two_flowers": np.array(Image.open(f"{sprites_path}/{sprites[162]}")),
    "two_flowers_top": np.array(Image.open(f"{sprites_path}/{sprites[163]}")),
    "two_flowers_bottom": np.array(Image.open(f"{sprites_path}/{sprites[164]}")),
    
    "bush": np.array(Image.open(f"{sprites_path}/{sprites[165]}")),
    
    # -- RINGS --
    "top_two_rings": np.array(Image.open(f"{sprites_path}/{sprites[112]}")),
    "bottom_two_rings": np.array(Image.open(f"{sprites_path}/{sprites[113]}")),
    "top_left_and_bottom_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[114]}")
    ),
    "bottom_left_and_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[115]}")
    ),
    "top_left_ring": np.array(Image.open(f"{sprites_path}/{sprites[116]}")),
    "top_right_ring": np.array(Image.open(f"{sprites_path}/{sprites[117]}")),
    "bottom_left_ring": np.array(Image.open(f"{sprites_path}/{sprites[118]}")),
    "bottom_right_ring": np.array(Image.open(f"{sprites_path}/{sprites[119]}")),
    
    # -- SPRINGS --
    "spring_from_bottom_middle": np.array(Image.open(f"{sprites_path}/{sprites[120]}")),
    "spring_from_bottom_middle_underwater": np.array(
        Image.open(f"{sprites_path}/{sprites[121]}")
    ),
    "spring_from_left_middle": np.array(Image.open(f"{sprites_path}/{sprites[122]}")),
    "spring_from_left_middle_underwater": np.array(
        Image.open(f"{sprites_path}/{sprites[123]}")
    ),
    "spring_from_right_middle": np.array(Image.open(f"{sprites_path}/{sprites[124]}")),
    "spring_from_right_middle_underwater": np.array(
        Image.open(f"{sprites_path}/{sprites[125]}")
    ),
    "spring_from_bottom_left": np.array(Image.open(f"{sprites_path}/{sprites[126]}")),
    "spring_from_bottom_left_underwater": np.array(
        Image.open(f"{sprites_path}/{sprites[127]}")
    ),
    "spring_from_bottom_right": np.array(Image.open(f"{sprites_path}/{sprites[128]}")),
    "spring_from_bottom_right_underwater": np.array(
        Image.open(f"{sprites_path}/{sprites[129]}")
    ),
    
    # -- SPIKES --
    "spike_from_bottom": np.array(Image.open(f"{sprites_path}/{sprites[130]}")),
    "spike_from_bottom_underwater": np.array(
        Image.open(f"{sprites_path}/{sprites[131]}")
    ),
    "spike_from_top": np.array(Image.open(f"{sprites_path}/{sprites[132]}")),
    "spike_from_top_underwater": np.array(Image.open(f"{sprites_path}/{sprites[133]}")),
    
    # I'll assume it's something to block sonic.
    "blocking_thing": np.array(Image.open(f"{sprites_path}/{sprites[134]}")),
    
    # -- WATER --
    "water_surface_1": np.array(Image.open(f"{sprites_path}/{sprites[142]}")),
    "water_surface_2": np.array(Image.open(f"{sprites_path}/{sprites[143]}")),
    "water_surface_3": np.array(Image.open(f"{sprites_path}/{sprites[172]}")),
    "water_surface_half": np.array(Image.open(f"{sprites_path}/{sprites[192]}")),
    
    "waterfall_start": np.array(Image.open(f"{sprites_path}/{sprites[184]}")),
    "waterfall_middle": np.array(Image.open(f"{sprites_path}/{sprites[185]}")),
    "waterfall_end": np.array(Image.open(f"{sprites_path}/{sprites[186]}")),
    "waterfall_start_with_background": np.array(
        Image.open(f"{sprites_path}/{sprites[187]}")
    ),
    "waterfall_middle_with_background": np.array(
        Image.open(f"{sprites_path}/{sprites[188]}")
    ),
    "waterfall_end_with_background": np.array(
        Image.open(f"{sprites_path}/{sprites[189]}")
    ),
    
    # -- CLOUDS --
    "mini_cloud": np.array(Image.open(f"{sprites_path}/{sprites[145]}")),
    
    "cloud_left": np.array(Image.open(f"{sprites_path}/{sprites[146]}")),
    "cloud_right": np.array(Image.open(f"{sprites_path}/{sprites[147]}")),
    
    # -- BACKGROUND TILES --
    "sea_background_v1": np.array(Image.open(f"{sprites_path}/{sprites[166]}")),
    "sea_background_v2": np.array(Image.open(f"{sprites_path}/{sprites[167]}")),
    "sea_background_v3": np.array(Image.open(f"{sprites_path}/{sprites[168]}")),
    
    "background_special": np.array(Image.open(f"{sprites_path}/{sprites[169]}")),
    "background_special_left": np.array(Image.open(f"{sprites_path}/{sprites[170]}")),
    "background_special_right": np.array(Image.open(f"{sprites_path}/{sprites[171]}")),
    
    "vertical_lines": np.array(Image.open(f"{sprites_path}/{sprites[253]}")),
    
    "background_tile_1": np.array(Image.open(f"{sprites_path}/{sprites[48]}")),
    "background_tile_2": np.array(Image.open(f"{sprites_path}/{sprites[49]}")),
    "background_tile_3": np.array(Image.open(f"{sprites_path}/{sprites[50]}")),
    "background_tile_4": np.array(Image.open(f"{sprites_path}/{sprites[51]}")),
    "background_tile_5": np.array(Image.open(f"{sprites_path}/{sprites[52]}")),
    "background_tile_6": np.array(Image.open(f"{sprites_path}/{sprites[53]}")),
    "background_tile_7": np.array(Image.open(f"{sprites_path}/{sprites[54]}")),
    "background_tile_8": np.array(Image.open(f"{sprites_path}/{sprites[55]}")),
    "background_tile_9": np.array(Image.open(f"{sprites_path}/{sprites[56]}")),
    "background_tile_10": np.array(Image.open(f"{sprites_path}/{sprites[57]}")),
    "background_tile_11": np.array(Image.open(f"{sprites_path}/{sprites[58]}")),
    "background_tile_12": np.array(Image.open(f"{sprites_path}/{sprites[59]}")),
    "background_tile_13": np.array(Image.open(f"{sprites_path}/{sprites[60]}")),
    "background_tile_14": np.array(Image.open(f"{sprites_path}/{sprites[61]}")),
    "background_tile_15": np.array(Image.open(f"{sprites_path}/{sprites[62]}")),
    "background_tile_16": np.array(Image.open(f"{sprites_path}/{sprites[63]}")),
    "background_tile_17": np.array(Image.open(f"{sprites_path}/{sprites[71]}")),
    "background_tile_18": np.array(Image.open(f"{sprites_path}/{sprites[72]}")),
    "background_tile_19": np.array(Image.open(f"{sprites_path}/{sprites[73]}")),
    "background_tile_20": np.array(Image.open(f"{sprites_path}/{sprites[74]}")),
    "background_tile_21": np.array(Image.open(f"{sprites_path}/{sprites[75]}")),
    "background_tile_22": np.array(Image.open(f"{sprites_path}/{sprites[76]}")),
    "background_tile_23": np.array(Image.open(f"{sprites_path}/{sprites[87]}")),
    "background_tile_24": np.array(Image.open(f"{sprites_path}/{sprites[88]}")),
    "background_tile_25": np.array(Image.open(f"{sprites_path}/{sprites[89]}")),
    "background_tile_26": np.array(Image.open(f"{sprites_path}/{sprites[90]}")),
    "background_tile_27": np.array(Image.open(f"{sprites_path}/{sprites[91]}")),
    "background_tile_28": np.array(Image.open(f"{sprites_path}/{sprites[92]}")),
    "background_tile_29": np.array(Image.open(f"{sprites_path}/{sprites[136]}")),
    "background_tile_30": np.array(Image.open(f"{sprites_path}/{sprites[137]}")),
    "background_tile_31": np.array(Image.open(f"{sprites_path}/{sprites[138]}")),
    "background_tile_32": np.array(Image.open(f"{sprites_path}/{sprites[139]}")),
    "background_tile_33": np.array(Image.open(f"{sprites_path}/{sprites[140]}")),
    "background_tile_34": np.array(Image.open(f"{sprites_path}/{sprites[141]}")),
    "background_tile_35": np.array(Image.open(f"{sprites_path}/{sprites[144]}")),
    "background_tile_36": np.array(Image.open(f"{sprites_path}/{sprites[190]}")),
    "background_tile_37": np.array(Image.open(f"{sprites_path}/{sprites[191]}")),
    "background_tile_38": np.array(Image.open(f"{sprites_path}/{sprites[193]}")),
    "background_tile_39": np.array(Image.open(f"{sprites_path}/{sprites[194]}")),
    "background_tile_40": np.array(Image.open(f"{sprites_path}/{sprites[195]}")),
    "background_tile_41": np.array(Image.open(f"{sprites_path}/{sprites[196]}")),
    "background_tile_42": np.array(Image.open(f"{sprites_path}/{sprites[197]}")),
    "background_tile_43": np.array(Image.open(f"{sprites_path}/{sprites[198]}")),
    "background_tile_44": np.array(Image.open(f"{sprites_path}/{sprites[199]}")),
    "background_tile_45": np.array(Image.open(f"{sprites_path}/{sprites[200]}")),
    "background_tile_46": np.array(Image.open(f"{sprites_path}/{sprites[201]}")),
    "background_tile_47": np.array(Image.open(f"{sprites_path}/{sprites[202]}")),
    "background_tile_48": np.array(Image.open(f"{sprites_path}/{sprites[203]}")),
    "background_tile_49": np.array(Image.open(f"{sprites_path}/{sprites[204]}")),
    "background_tile_50": np.array(Image.open(f"{sprites_path}/{sprites[205]}")),
    "background_tile_51": np.array(Image.open(f"{sprites_path}/{sprites[206]}")),
    "background_tile_52": np.array(Image.open(f"{sprites_path}/{sprites[207]}")),
    "background_tile_53": np.array(Image.open(f"{sprites_path}/{sprites[208]}")),
    "background_tile_54": np.array(Image.open(f"{sprites_path}/{sprites[209]}")),
    "background_tile_55": np.array(Image.open(f"{sprites_path}/{sprites[210]}")),
    "background_tile_56": np.array(Image.open(f"{sprites_path}/{sprites[211]}")),
    "background_tile_57": np.array(Image.open(f"{sprites_path}/{sprites[212]}")),
    "background_tile_58": np.array(Image.open(f"{sprites_path}/{sprites[213]}")),
    "background_tile_59": np.array(Image.open(f"{sprites_path}/{sprites[214]}")),
    "background_tile_60": np.array(Image.open(f"{sprites_path}/{sprites[215]}")),
    "background_tile_61": np.array(Image.open(f"{sprites_path}/{sprites[216]}")),
    "background_tile_62": np.array(Image.open(f"{sprites_path}/{sprites[217]}")),
    "background_tile_63": np.array(Image.open(f"{sprites_path}/{sprites[218]}")),
    "background_tile_64": np.array(Image.open(f"{sprites_path}/{sprites[219]}")),
    "background_tile_65": np.array(Image.open(f"{sprites_path}/{sprites[220]}")),
    "background_tile_66": np.array(Image.open(f"{sprites_path}/{sprites[221]}")),
    "background_tile_67": np.array(Image.open(f"{sprites_path}/{sprites[222]}")),
    "background_tile_68": np.array(Image.open(f"{sprites_path}/{sprites[223]}")),
    "background_tile_69": np.array(Image.open(f"{sprites_path}/{sprites[224]}")),
    "background_tile_70": np.array(Image.open(f"{sprites_path}/{sprites[225]}")),
    "background_tile_71": np.array(Image.open(f"{sprites_path}/{sprites[226]}")),
    "background_tile_72": np.array(Image.open(f"{sprites_path}/{sprites[227]}")),
    "background_tile_73": np.array(Image.open(f"{sprites_path}/{sprites[228]}")),
    "background_tile_74": np.array(Image.open(f"{sprites_path}/{sprites[229]}")),
    "background_tile_75": np.array(Image.open(f"{sprites_path}/{sprites[230]}")),
    "background_tile_76": np.array(Image.open(f"{sprites_path}/{sprites[231]}")),
    "background_tile_77": np.array(Image.open(f"{sprites_path}/{sprites[232]}")),
    "background_tile_78": np.array(Image.open(f"{sprites_path}/{sprites[233]}")),
    "background_tile_79": np.array(Image.open(f"{sprites_path}/{sprites[234]}")),
    "background_tile_80": np.array(Image.open(f"{sprites_path}/{sprites[235]}")),
    "background_tile_81": np.array(Image.open(f"{sprites_path}/{sprites[236]}")),
    "background_tile_82": np.array(Image.open(f"{sprites_path}/{sprites[240]}")),
    "background_tile_83": np.array(Image.open(f"{sprites_path}/{sprites[241]}")),
    "background_tile_84": np.array(Image.open(f"{sprites_path}/{sprites[242]}")),
    "background_tile_85": np.array(Image.open(f"{sprites_path}/{sprites[243]}")),
    "background_tile_86": np.array(Image.open(f"{sprites_path}/{sprites[244]}")),
    "background_tile_87": np.array(Image.open(f"{sprites_path}/{sprites[245]}")),
    "background_tile_88": np.array(Image.open(f"{sprites_path}/{sprites[246]}")),
    "background_tile_89": np.array(Image.open(f"{sprites_path}/{sprites[247]}")),
    "background_tile_90": np.array(Image.open(f"{sprites_path}/{sprites[248]}")),
    "background_tile_91": np.array(Image.open(f"{sprites_path}/{sprites[249]}")),
    "background_tile_92": np.array(Image.open(f"{sprites_path}/{sprites[250]}")),
    "background_tile_93": np.array(Image.open(f"{sprites_path}/{sprites[254]}")),
    "background_tile_94": np.array(Image.open(f"{sprites_path}/{sprites[255]}")),
}

# -------------------------------------------- LEVEL 2

level_coeff = 1

level_2_sprites = {
    # -- INCLINED / SLOPE PIECES --
    
    # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[0 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[1 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[2 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[3 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[4 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[5 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[6 + batch*level_coeff]}")
    ),
    
    # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[16 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[17 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[18 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[19 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[20 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[21 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[22 + batch*level_coeff]}")
    ),
    
    # -- LOOP & CORNER PIECES --

    # RIGHT SIDE
    "loop_bottom_middle_right": np.array(
        Image.open(f"{sprites_path}/{sprites[7 + batch*level_coeff]}")
    ),
    "loop_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[8 + batch*level_coeff]}")
    ),
    "loop_right_middle_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[9 + batch*level_coeff]}")
    ),
    "loop_right_middle_top": np.array(
        Image.open(f"{sprites_path}/{sprites[10 + batch*level_coeff]}")
    ),
    "loop_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[11 + batch*level_coeff]}")
    ),
    "loop_top_middle_right": np.array(
        Image.open(f"{sprites_path}/{sprites[12 + batch*level_coeff]}")
    ),
    
    # LEFT SIDE
    "loop_bottom_middle_left": np.array(
        Image.open(f"{sprites_path}/{sprites[23 + batch*level_coeff]}")
    ),
    "loop_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[24 + batch*level_coeff]}")
    ),
    "loop_left_middle_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[25 + batch*level_coeff]}")
    ),
    "loop_left_middle_top": np.array(
        Image.open(f"{sprites_path}/{sprites[26 + batch*level_coeff]}")
    ),
    "loop_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[27 + batch*level_coeff]}")
    ),
    "loop_top_middle_left": np.array(
        Image.open(f"{sprites_path}/{sprites[28 + batch*level_coeff]}")
    ),
    
    # -- GROUND / JUNGLE GROUND / CHECKER TILES --
    
        # GROUND TILES
            
            # LOW
    "low_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[13 + batch*level_coeff]}")
    ),
    "low_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[15 + batch*level_coeff]}")
    ),
    "low_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[29 + batch*level_coeff]}")
    ),
    "low_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[31 + batch*level_coeff]}")
    ),
    
    "triangle_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[30 + batch*level_coeff]}")
    ),
    
            # HIGH
    "curved_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[14 + batch*level_coeff]}")
    ),
    
    "high_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[33 + batch*level_coeff]}")
    ),
    "high_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[34 + batch*level_coeff]}")
    ),
    "high_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[36 + batch*level_coeff]}")
    ),
    "high_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[47 + batch*level_coeff]}")
    ),
    "high_ground_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[97 + batch*level_coeff]}")
    ),
    "high_ground_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[98 + batch*level_coeff]}")
    ),
    "high_ground_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[100 + batch*level_coeff]}")
    ),
    
    "high_ground_top_left_grass_v1_1": np.array(
        Image.open(f"{sprites_path}/{sprites[37 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v1_2": np.array(
        Image.open(f"{sprites_path}/{sprites[101 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v2_1": np.array(
        Image.open(f"{sprites_path}/{sprites[39 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v2_2": np.array(
        Image.open(f"{sprites_path}/{sprites[103 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v3_1": np.array(
        Image.open(f"{sprites_path}/{sprites[41 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v3_2": np.array(
        Image.open(f"{sprites_path}/{sprites[105 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v4_1": np.array(
        Image.open(f"{sprites_path}/{sprites[42 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v4_2": np.array(
        Image.open(f"{sprites_path}/{sprites[106 + batch*level_coeff]}")
    ),
    
    "high_ground_top_right_grass_v1_1": np.array(
        Image.open(f"{sprites_path}/{sprites[38 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v1_2": np.array(
        Image.open(f"{sprites_path}/{sprites[102 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v2_1": np.array(
        Image.open(f"{sprites_path}/{sprites[40 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v2_2": np.array(
        Image.open(f"{sprites_path}/{sprites[104 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v3_1": np.array(
        Image.open(f"{sprites_path}/{sprites[43 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v3_2": np.array(
        Image.open(f"{sprites_path}/{sprites[107 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v4_1": np.array(
        Image.open(f"{sprites_path}/{sprites[44 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v4_2": np.array(
        Image.open(f"{sprites_path}/{sprites[108 + batch*level_coeff]}")
    ),
    
        # JUNGLE GROUND TILES
    
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_jungle_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[64 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[65 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[66 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[67 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[68 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[69 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[70 + batch*level_coeff]}")
    ),
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_jungle_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[80 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[81 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[82 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[83 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[84 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[85 + batch*level_coeff]}")
    ),
    "inclined_jungle_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[86 + batch*level_coeff]}")
    ),
    
            # LOW
    "low_jungle_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[77 + batch*level_coeff]}")
    ),
    "low_jungle_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[79 + batch*level_coeff]}")
    ),
    "low_jungle_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[93 + batch*level_coeff]}")
    ),
    "low_jungle_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[95 + batch*level_coeff]}")
    ),
    "triangle_jungle_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[94 + batch*level_coeff]}")
    ),
    
            # HIGH
    "curved_jungle_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[78 + batch*level_coeff]}")
    ),
    
        # CHECKER TILES
            
            # LOW
    "low_checker_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[157 + batch*level_coeff]}")
    ),
    "low_checker_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[158 + batch*level_coeff]}")
    ),
    "low_checker_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[159 + batch*level_coeff]}")
    ),
            # HIGH
    "high_checker_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[32 + batch*level_coeff]}")
    ),
    "high_checker_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[35 + batch*level_coeff]}")
    ),
    "high_checker_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[45 + batch*level_coeff]}")
    ),
    "high_checker_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[46 + batch*level_coeff]}")
    ),
    "high_checker_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[96 + batch*level_coeff]}")
    ),
    "high_checker_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[99 + batch*level_coeff]}")
    ),
    "high_checker_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[109 + batch*level_coeff]}")
    ),
    "high_checker_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[110 + batch*level_coeff]}")
    ),
    "high_checker_v9": np.array(
        Image.open(f"{sprites_path}/{sprites[135 + batch*level_coeff]}")
    ),
    "high_checker_v10": np.array(
        Image.open(f"{sprites_path}/{sprites[139 + batch*level_coeff]}")
    ),
    "high_checker_v11": np.array(
        Image.open(f"{sprites_path}/{sprites[140 + batch*level_coeff]}")
    ),
    "high_checker_v12": np.array(
        Image.open(f"{sprites_path}/{sprites[141 + batch*level_coeff]}")
    ),
    "high_checker_v13": np.array(
        Image.open(f"{sprites_path}/{sprites[251 + batch*level_coeff]}")
    ),
    "high_checker_v14": np.array(
        Image.open(f"{sprites_path}/{sprites[252 + batch*level_coeff]}")
    ),
    
    # -- BRIDGE PIECES --
    "bridge_support_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[237 + batch*level_coeff]}")
    ),
    "bridge_support_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[238 + batch*level_coeff]}")
    ),
    "bridge_two_top_supports": np.array(
        Image.open(f"{sprites_path}/{sprites[239 + batch*level_coeff]}")
    ),
    
    # -- PALM TREES, BUSH & FLOWERS --
    "palm_tree_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[148 + batch*level_coeff]}")
    ),
    "palm_tree_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[149 + batch*level_coeff]}")
    ),
    "palm_tree_middle_left": np.array(
        Image.open(f"{sprites_path}/{sprites[150 + batch*level_coeff]}")
    ),
    "palm_tree_middle_right": np.array(
        Image.open(f"{sprites_path}/{sprites[151 + batch*level_coeff]}")
    ),
    "palm_tree_trunk_classic_background": np.array(
        Image.open(f"{sprites_path}/{sprites[152 + batch*level_coeff]}")
    ),
    "palm_tree_trunk_special_background": np.array(
        Image.open(f"{sprites_path}/{sprites[153 + batch*level_coeff]}")
    ),
    "palm_tree_trunk_jungle_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[154 + batch*level_coeff]}")
    ),
    "palm_tree_trunk_jungle_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[155 + batch*level_coeff]}")
    ),
    "palm_tree_trunk_jungle_background_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[156 + batch*level_coeff]}")
    ),
    
    "two_flowers_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[161 + batch*level_coeff]}")
    ),
    "two_flowers_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[162 + batch*level_coeff]}")
    ),
    "two_flowers_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[163 + batch*level_coeff]}")
    ),
    "two_flowers_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[164 + batch*level_coeff]}")
    ),
    
    "bush": np.array(Image.open(f"{sprites_path}/{sprites[160 + batch*level_coeff]}")),
    
    # -- RINGS --
    "top_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[112 + batch*level_coeff]}")
    ),
    "bottom_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[113 + batch*level_coeff]}")
    ),
    "top_left_and_bottom_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[114 + batch*level_coeff]}")
    ),
    "bottom_left_and_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[115 + batch*level_coeff]}")
    ),
    "top_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[116 + batch*level_coeff]}")
    ),
    "top_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[117 + batch*level_coeff]}")
    ),
    "bottom_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[118 + batch*level_coeff]}")
    ),
    "bottom_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[119 + batch*level_coeff]}")
    ),
    
    # -- SPRINGS --
    "spring_from_bottom_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[120 + batch*level_coeff]}")
    ),
    "spring_from_bottom_middle_jungle": np.array(
        Image.open(f"{sprites_path}/{sprites[121 + batch*level_coeff]}")
    ),
    "spring_from_left_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[122 + batch*level_coeff]}")
    ),
    "spring_from_left_middle_jungle": np.array(
        Image.open(f"{sprites_path}/{sprites[123 + batch*level_coeff]}")
    ),
    "spring_from_right_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[124 + batch*level_coeff]}")
    ),
    "spring_from_right_middle_jungle": np.array(
        Image.open(f"{sprites_path}/{sprites[125 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[126 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left_jungle": np.array(
        Image.open(f"{sprites_path}/{sprites[127 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[128 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right_jungle": np.array(
        Image.open(f"{sprites_path}/{sprites[129 + batch*level_coeff]}")
    ),
    
    # -- SPIKES --
    "spike_from_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[130 + batch*level_coeff]}")
    ),
    "spike_from_bottom_jungle": np.array(
        Image.open(f"{sprites_path}/{sprites[131 + batch*level_coeff]}")
    ),
    "spike_from_top": np.array(
        Image.open(f"{sprites_path}/{sprites[132 + batch*level_coeff]}")
    ),
    "spike_from_top_jungle": np.array(
        Image.open(f"{sprites_path}/{sprites[133 + batch*level_coeff]}")
    ),
    
    # I'll assume it's something to block sonic.
    "blocking_thing": np.array(
        Image.open(f"{sprites_path}/{sprites[134 + batch*level_coeff]}")
    ),
    
    # -- WATERFALLS --
    "waterfall_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[181 + batch*level_coeff]}")
    ),
    "waterfall_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[182 + batch*level_coeff]}")
    ),
    
    # -- BALLOONS --
    "one_balloon_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[183 + batch*level_coeff]}")
    ),
    "one_balloon_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[184 + batch*level_coeff]}")
    ),
    "two_balloon_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[185 + batch*level_coeff]}")
    ),
    "two_balloon_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[186 + batch*level_coeff]}")
    ),
    "two_balloon_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[187 + batch*level_coeff]}")
    ),
    "two_balloon_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[188 + batch*level_coeff]}")
    ),
    "top_balloon_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[189 + batch*level_coeff]}")
    ),
    "bottom_balloon_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[192 + batch*level_coeff]}")
    ),
    "top_balloon_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[191 + batch*level_coeff]}")
    ),
    "bottom_balloon_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[190 + batch*level_coeff]}")
    ),
    
    # -- Flag --
    "flag_top": np.array(
        Image.open(f"{sprites_path}/{sprites[172 + batch*level_coeff]}")
    ),
    "flag_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[173 + batch*level_coeff]}")
    ),
    "flag_bottom_classic_background": np.array(
        Image.open(f"{sprites_path}/{sprites[174 + batch*level_coeff]}")
    ),
    "flag_bottom_special_background": np.array(
        Image.open(f"{sprites_path}/{sprites[175 + batch*level_coeff]}")
    ),
    "flag_bottom_jungle_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[176 + batch*level_coeff]}")
    ),
    "flag_bottom_jungle_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[177 + batch*level_coeff]}")
    ),
    "flag_bottom_jungle_background_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[178 + batch*level_coeff]}")
    ),
    "flag_bottom_jungle_background_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[179 + batch*level_coeff]}")
    ),
    "flag_bottom_jungle_background_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[180 + batch*level_coeff]}")
    ),
    
    # -- BACKGROUND TILES --
    "jungle_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[168 + batch*level_coeff]}")
    ),
    "jungle_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[169 + batch*level_coeff]}")
    ),
    "jungle_background_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[170 + batch*level_coeff]}")
    ),
    
    "background_special": np.array(
        Image.open(f"{sprites_path}/{sprites[165 + batch*level_coeff]}")
    ),
    "background_special_left": np.array(
        Image.open(f"{sprites_path}/{sprites[166 + batch*level_coeff]}")
    ),
    "background_special_right": np.array(
        Image.open(f"{sprites_path}/{sprites[167 + batch*level_coeff]}")
    ),
    
    "vertical_lines": np.array(
        Image.open(f"{sprites_path}/{sprites[253 + batch*level_coeff]}")
    ),

    "background_tile_1": np.array(
        Image.open(f"{sprites_path}/{sprites[48 + batch*level_coeff]}")
    ),
    "background_tile_2": np.array(
        Image.open(f"{sprites_path}/{sprites[49 + batch*level_coeff]}")
    ),
    "background_tile_3": np.array(
        Image.open(f"{sprites_path}/{sprites[50 + batch*level_coeff]}")
    ),
    "background_tile_4": np.array(
        Image.open(f"{sprites_path}/{sprites[51 + batch*level_coeff]}")
    ),
    "background_tile_5": np.array(
        Image.open(f"{sprites_path}/{sprites[52 + batch*level_coeff]}")
    ),
    "background_tile_6": np.array(
        Image.open(f"{sprites_path}/{sprites[53 + batch*level_coeff]}")
    ),
    "background_tile_7": np.array(
        Image.open(f"{sprites_path}/{sprites[54 + batch*level_coeff]}")
    ),
    "background_tile_8": np.array(
        Image.open(f"{sprites_path}/{sprites[55 + batch*level_coeff]}")
    ),
    "background_tile_9": np.array(
        Image.open(f"{sprites_path}/{sprites[56 + batch*level_coeff]}")
    ),
    "background_tile_10": np.array(
        Image.open(f"{sprites_path}/{sprites[57 + batch*level_coeff]}")
    ),
    "background_tile_11": np.array(
        Image.open(f"{sprites_path}/{sprites[58 + batch*level_coeff]}")
    ),
    "background_tile_12": np.array(
        Image.open(f"{sprites_path}/{sprites[59 + batch*level_coeff]}")
    ),
    "background_tile_13": np.array(
        Image.open(f"{sprites_path}/{sprites[60 + batch*level_coeff]}")
    ),
    "background_tile_14": np.array(
        Image.open(f"{sprites_path}/{sprites[61 + batch*level_coeff]}")
    ),
    "background_tile_15": np.array(
        Image.open(f"{sprites_path}/{sprites[62 + batch*level_coeff]}")
    ),
    "background_tile_16": np.array(
        Image.open(f"{sprites_path}/{sprites[63 + batch*level_coeff]}")
    ),
    "background_tile_17": np.array(
        Image.open(f"{sprites_path}/{sprites[71 + batch*level_coeff]}")
    ),
    "background_tile_18": np.array(
        Image.open(f"{sprites_path}/{sprites[72 + batch*level_coeff]}")
    ),
    "background_tile_19": np.array(
        Image.open(f"{sprites_path}/{sprites[73 + batch*level_coeff]}")
    ),
    "background_tile_20": np.array(
        Image.open(f"{sprites_path}/{sprites[74 + batch*level_coeff]}")
    ),
    "background_tile_21": np.array(
        Image.open(f"{sprites_path}/{sprites[75 + batch*level_coeff]}")
    ),
    "background_tile_22": np.array(
        Image.open(f"{sprites_path}/{sprites[76 + batch*level_coeff]}")
    ),
    "background_tile_23": np.array(
        Image.open(f"{sprites_path}/{sprites[87 + batch*level_coeff]}")
    ),
    "background_tile_24": np.array(
        Image.open(f"{sprites_path}/{sprites[88 + batch*level_coeff]}")
    ),
    "background_tile_25": np.array(
        Image.open(f"{sprites_path}/{sprites[89 + batch*level_coeff]}")
    ),
    "background_tile_26": np.array(
        Image.open(f"{sprites_path}/{sprites[90 + batch*level_coeff]}")
    ),
    "background_tile_27": np.array(
        Image.open(f"{sprites_path}/{sprites[91 + batch*level_coeff]}")
    ),
    "background_tile_28": np.array(
        Image.open(f"{sprites_path}/{sprites[92 + batch*level_coeff]}")
    ),
    "background_tile_29": np.array(
        Image.open(f"{sprites_path}/{sprites[111 + batch*level_coeff]}")
    ),
    "background_tile_30": np.array(
        Image.open(f"{sprites_path}/{sprites[136 + batch*level_coeff]}")
    ),
    "background_tile_31": np.array(
        Image.open(f"{sprites_path}/{sprites[137 + batch*level_coeff]}")
    ),
    "background_tile_32": np.array(
        Image.open(f"{sprites_path}/{sprites[138 + batch*level_coeff]}")
    ),
    "background_tile_33": np.array(
        Image.open(f"{sprites_path}/{sprites[142 + batch*level_coeff]}")
    ),
    "background_tile_34": np.array(
        Image.open(f"{sprites_path}/{sprites[143 + batch*level_coeff]}")
    ),
    "background_tile_35": np.array(
        Image.open(f"{sprites_path}/{sprites[144 + batch*level_coeff]}")
    ),
    "background_tile_36": np.array(
        Image.open(f"{sprites_path}/{sprites[145 + batch*level_coeff]}")
    ),
    "background_tile_37": np.array(
        Image.open(f"{sprites_path}/{sprites[146 + batch*level_coeff]}")
    ),
    "background_tile_38": np.array(
        Image.open(f"{sprites_path}/{sprites[147 + batch*level_coeff]}")
    ),
    "background_tile_39": np.array(
        Image.open(f"{sprites_path}/{sprites[171 + batch*level_coeff]}")
    ),
    "background_tile_40": np.array(
        Image.open(f"{sprites_path}/{sprites[193 + batch*level_coeff]}")
    ),
    "background_tile_41": np.array(
        Image.open(f"{sprites_path}/{sprites[194 + batch*level_coeff]}")
    ),
    "background_tile_42": np.array(
        Image.open(f"{sprites_path}/{sprites[195 + batch*level_coeff]}")
    ),
    "background_tile_43": np.array(
        Image.open(f"{sprites_path}/{sprites[196 + batch*level_coeff]}")
    ),
    "background_tile_44": np.array(
        Image.open(f"{sprites_path}/{sprites[197 + batch*level_coeff]}")
    ),
    "background_tile_45": np.array(
        Image.open(f"{sprites_path}/{sprites[198 + batch*level_coeff]}")
    ),
    "background_tile_46": np.array(
        Image.open(f"{sprites_path}/{sprites[199 + batch*level_coeff]}")
    ),
    "background_tile_47": np.array(
        Image.open(f"{sprites_path}/{sprites[200 + batch*level_coeff]}")
    ),
    "background_tile_48": np.array(
        Image.open(f"{sprites_path}/{sprites[201 + batch*level_coeff]}")
    ),
    "background_tile_49": np.array(
        Image.open(f"{sprites_path}/{sprites[202 + batch*level_coeff]}")
    ),
    "background_tile_50": np.array(
        Image.open(f"{sprites_path}/{sprites[203 + batch*level_coeff]}")
    ),
    "background_tile_51": np.array(
        Image.open(f"{sprites_path}/{sprites[204 + batch*level_coeff]}")
    ),
    "background_tile_52": np.array(
        Image.open(f"{sprites_path}/{sprites[205 + batch*level_coeff]}")
    ),
    "background_tile_53": np.array(
        Image.open(f"{sprites_path}/{sprites[206 + batch*level_coeff]}")
    ),
    "background_tile_54": np.array(
        Image.open(f"{sprites_path}/{sprites[207 + batch*level_coeff]}")
    ),
    "background_tile_55": np.array(
        Image.open(f"{sprites_path}/{sprites[208 + batch*level_coeff]}")
    ),
    "background_tile_56": np.array(
        Image.open(f"{sprites_path}/{sprites[209 + batch*level_coeff]}")
    ),
    "background_tile_57": np.array(
        Image.open(f"{sprites_path}/{sprites[210 + batch*level_coeff]}")
    ),
    "background_tile_58": np.array(
        Image.open(f"{sprites_path}/{sprites[211 + batch*level_coeff]}")
    ),
    "background_tile_59": np.array(
        Image.open(f"{sprites_path}/{sprites[212 + batch*level_coeff]}")
    ),
    "background_tile_60": np.array(
        Image.open(f"{sprites_path}/{sprites[213 + batch*level_coeff]}")
    ),
    "background_tile_61": np.array(
        Image.open(f"{sprites_path}/{sprites[214 + batch*level_coeff]}")
    ),
    "background_tile_62": np.array(
        Image.open(f"{sprites_path}/{sprites[215 + batch*level_coeff]}")
    ),
    "background_tile_63": np.array(
        Image.open(f"{sprites_path}/{sprites[216 + batch*level_coeff]}")
    ),
    "background_tile_64": np.array(
        Image.open(f"{sprites_path}/{sprites[217 + batch*level_coeff]}")
    ),
    "background_tile_65": np.array(
        Image.open(f"{sprites_path}/{sprites[218 + batch*level_coeff]}")
    ),
    "background_tile_66": np.array(
        Image.open(f"{sprites_path}/{sprites[219 + batch*level_coeff]}")
    ),
    "background_tile_67": np.array(
        Image.open(f"{sprites_path}/{sprites[220 + batch*level_coeff]}")
    ),
    "background_tile_68": np.array(
        Image.open(f"{sprites_path}/{sprites[221 + batch*level_coeff]}")
    ),
    "background_tile_69": np.array(
        Image.open(f"{sprites_path}/{sprites[222 + batch*level_coeff]}")
    ),
    "background_tile_70": np.array(
        Image.open(f"{sprites_path}/{sprites[223 + batch*level_coeff]}")
    ),
    "background_tile_71": np.array(
        Image.open(f"{sprites_path}/{sprites[224 + batch*level_coeff]}")
    ),
    "background_tile_72": np.array(
        Image.open(f"{sprites_path}/{sprites[225 + batch*level_coeff]}")
    ),
    "background_tile_73": np.array(
        Image.open(f"{sprites_path}/{sprites[226 + batch*level_coeff]}")
    ),
    "background_tile_74": np.array(
        Image.open(f"{sprites_path}/{sprites[227 + batch*level_coeff]}")
    ),
    "background_tile_75": np.array(
        Image.open(f"{sprites_path}/{sprites[228 + batch*level_coeff]}")
    ),
    "background_tile_76": np.array(
        Image.open(f"{sprites_path}/{sprites[229 + batch*level_coeff]}")
    ),
    "background_tile_77": np.array(
        Image.open(f"{sprites_path}/{sprites[230 + batch*level_coeff]}")
    ),
    "background_tile_78": np.array(
        Image.open(f"{sprites_path}/{sprites[231 + batch*level_coeff]}")
    ),
    "background_tile_79": np.array(
        Image.open(f"{sprites_path}/{sprites[232 + batch*level_coeff]}")
    ),
    "background_tile_80": np.array(
        Image.open(f"{sprites_path}/{sprites[233 + batch*level_coeff]}")
    ),
    "background_tile_81": np.array(
        Image.open(f"{sprites_path}/{sprites[234 + batch*level_coeff]}")
    ),
    "background_tile_82": np.array(
        Image.open(f"{sprites_path}/{sprites[235 + batch*level_coeff]}")
    ),
    "background_tile_83": np.array(
        Image.open(f"{sprites_path}/{sprites[236 + batch*level_coeff]}")
    ),
    "background_tile_84": np.array(
        Image.open(f"{sprites_path}/{sprites[240 + batch*level_coeff]}")
    ),
    "background_tile_85": np.array(
        Image.open(f"{sprites_path}/{sprites[241 + batch*level_coeff]}")
    ),
    "background_tile_86": np.array(
        Image.open(f"{sprites_path}/{sprites[242 + batch*level_coeff]}")
    ),
    "background_tile_87": np.array(
        Image.open(f"{sprites_path}/{sprites[243 + batch*level_coeff]}")
    ),
    "background_tile_88": np.array(
        Image.open(f"{sprites_path}/{sprites[244 + batch*level_coeff]}")
    ),
    "background_tile_89": np.array(
        Image.open(f"{sprites_path}/{sprites[245 + batch*level_coeff]}")
    ),
    "background_tile_90": np.array(
        Image.open(f"{sprites_path}/{sprites[246 + batch*level_coeff]}")
    ),
    "background_tile_91": np.array(
        Image.open(f"{sprites_path}/{sprites[247 + batch*level_coeff]}")
    ),
    "background_tile_92": np.array(
        Image.open(f"{sprites_path}/{sprites[248 + batch*level_coeff]}")
    ),
    "background_tile_93": np.array(
        Image.open(f"{sprites_path}/{sprites[249 + batch*level_coeff]}")
    ),
    "background_tile_94": np.array(
        Image.open(f"{sprites_path}/{sprites[250 + batch*level_coeff]}")
    ),
    "background_tile_95": np.array(
        Image.open(f"{sprites_path}/{sprites[254 + batch*level_coeff]}")
    ),
    "background_tile_96": np.array(
        Image.open(f"{sprites_path}/{sprites[255 + batch*level_coeff]}")
    ),
}

# -------------------------------------------- LEVEL 3

level_coeff = 2

level_3_sprites = {
    # -- INCLINED / SLOPE PIECES --
    
    # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[0 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[1 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[2 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[3 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[4 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[5 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[6 + batch*level_coeff]}")
    ),
    
    # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[16 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[17 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[18 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[19 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[20 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[21 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[22 + batch*level_coeff]}")
    ),
    
    # -- LOOP & CORNER PIECES --

    # RIGHT SIDE
    "loop_bottom_middle_right": np.array(
        Image.open(f"{sprites_path}/{sprites[7 + batch*level_coeff]}")
    ),
    "loop_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[8 + batch*level_coeff]}")
    ),
    "loop_right_middle_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[9 + batch*level_coeff]}")
    ),
    "loop_right_middle_top": np.array(
        Image.open(f"{sprites_path}/{sprites[10 + batch*level_coeff]}")
    ),
    "loop_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[11 + batch*level_coeff]}")
    ),
    "loop_top_middle_right": np.array(
        Image.open(f"{sprites_path}/{sprites[12 + batch*level_coeff]}")
    ),
    
    # LEFT SIDE
    "loop_bottom_middle_left": np.array(
        Image.open(f"{sprites_path}/{sprites[23 + batch*level_coeff]}")
    ),
    "loop_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[24 + batch*level_coeff]}")
    ),
    "loop_left_middle_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[25 + batch*level_coeff]}")
    ),
    "loop_left_middle_top": np.array(
        Image.open(f"{sprites_path}/{sprites[26 + batch*level_coeff]}")
    ),
    "loop_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[27 + batch*level_coeff]}")
    ),
    "loop_top_middle_left": np.array(
        Image.open(f"{sprites_path}/{sprites[28 + batch*level_coeff]}")
    ),
    # -- GROUND / LAVA GROUND / CHECKER TILES --
        
        # GROUND TILES
    
            # LOW
    "low_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[13 + batch*level_coeff]}")
    ),
    "low_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[15 + batch*level_coeff]}")
    ),
    "low_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[29 + batch*level_coeff]}")
    ),
    "low_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[31 + batch*level_coeff]}")
    ),
    
    "triangle_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[30 + batch*level_coeff]}")
    ),
            # HIGH
    "curved_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[14 + batch*level_coeff]}")
    ),
    
    "high_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[33 + batch*level_coeff]}")
    ),
    "high_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[34 + batch*level_coeff]}")
    ),
    "high_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[36 + batch*level_coeff]}")
    ),
    "high_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[47 + batch*level_coeff]}")
    ),
    "high_ground_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[97 + batch*level_coeff]}")
    ),
    "high_ground_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[98 + batch*level_coeff]}")
    ),
    "high_ground_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[100 + batch*level_coeff]}")
    ),
    
    "high_ground_top_left_grass_v1_1": np.array(
        Image.open(f"{sprites_path}/{sprites[37 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v2_1": np.array(
        Image.open(f"{sprites_path}/{sprites[39 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v3_1": np.array(
        Image.open(f"{sprites_path}/{sprites[41 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v4_1": np.array(
        Image.open(f"{sprites_path}/{sprites[42 + batch*level_coeff]}")
    ),
    
    "high_ground_top_right_grass_v1_1": np.array(
        Image.open(f"{sprites_path}/{sprites[38 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v2_1": np.array(
        Image.open(f"{sprites_path}/{sprites[40 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v3_1": np.array(
        Image.open(f"{sprites_path}/{sprites[43 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v4_1": np.array(
        Image.open(f"{sprites_path}/{sprites[44 + batch*level_coeff]}")
    ),
    
        # LAVA GROUND TILES
    
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_lava_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[64 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[65 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[66 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[67 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[68 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[69 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[70 + batch*level_coeff]}")
    ),
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_lava_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[80 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[81 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[82 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[83 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[84 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[85 + batch*level_coeff]}")
    ),
    "inclined_lava_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[86 + batch*level_coeff]}")
    ),
            
            # LOW
    "low_lava_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[77 + batch*level_coeff]}")
    ),
    "low_lava_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[79 + batch*level_coeff]}")
    ),
    "low_lava_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[93 + batch*level_coeff]}")
    ),
    "low_lava_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[95 + batch*level_coeff]}")
    ),
    "triangle_lava_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[94 + batch*level_coeff]}")
    ),
            # HIGH
    "curved_lava_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[78 + batch*level_coeff]}")
    ),
    
        # CHECKER TILES
            
            # LOW (NONE)
            
            # HIGH
    "high_checker_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[32 + batch*level_coeff]}")
    ),
    "high_checker_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[35 + batch*level_coeff]}")
    ),
    "high_checker_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[45 + batch*level_coeff]}")
    ),
    "high_checker_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[46 + batch*level_coeff]}")
    ),
    "high_checker_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[96 + batch*level_coeff]}")
    ),
    "high_checker_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[99 + batch*level_coeff]}")
    ),
    "high_checker_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[109 + batch*level_coeff]}")
    ),
    "high_checker_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[110 + batch*level_coeff]}")
    ),
    "high_checker_v9": np.array(
        Image.open(f"{sprites_path}/{sprites[135 + batch*level_coeff]}")
    ),
    "high_checker_v10": np.array(
        Image.open(f"{sprites_path}/{sprites[136 + batch*level_coeff]}")
    ),
    "high_checker_v11": np.array(
        Image.open(f"{sprites_path}/{sprites[137 + batch*level_coeff]}")
    ),
    "high_checker_v12": np.array(
        Image.open(f"{sprites_path}/{sprites[138 + batch*level_coeff]}")
    ),
    "high_checker_v13": np.array(
        Image.open(f"{sprites_path}/{sprites[139 + batch*level_coeff]}")
    ),
    "high_checker_v14": np.array(
        Image.open(f"{sprites_path}/{sprites[140 + batch*level_coeff]}")
    ),
    "high_checker_v15": np.array(
        Image.open(f"{sprites_path}/{sprites[141 + batch*level_coeff]}")
    ),
    "high_checker_v16": np.array(
        Image.open(f"{sprites_path}/{sprites[155 + batch*level_coeff]}")
    ),
    "high_checker_v17": np.array(
        Image.open(f"{sprites_path}/{sprites[156 + batch*level_coeff]}")
    ),
    "high_checker_v18": np.array(
        Image.open(f"{sprites_path}/{sprites[157 + batch*level_coeff]}")
    ),
    "high_checker_v19": np.array(
        Image.open(f"{sprites_path}/{sprites[158 + batch*level_coeff]}")
    ),
    "high_checker_v20": np.array(
        Image.open(f"{sprites_path}/{sprites[159 + batch*level_coeff]}")
    ),
    "high_checker_v21": np.array(
        Image.open(f"{sprites_path}/{sprites[251 + batch*level_coeff]}")
    ),
    "high_checker_v22": np.array(
        Image.open(f"{sprites_path}/{sprites[252 + batch*level_coeff]}")
    ),
    
    # -- LAVA, CACTUS & BARRIL --
    "lava_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[148 + batch*level_coeff]}")
    ),
    "lava_left_top": np.array(
        Image.open(f"{sprites_path}/{sprites[149 + batch*level_coeff]}")
    ),
    "lava_left_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[150 + batch*level_coeff]}")
    ),
    "lava_left_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[151 + batch*level_coeff]}")
    ),
    "lava_right_top": np.array(
        Image.open(f"{sprites_path}/{sprites[152 + batch*level_coeff]}")
    ),
    "lava_right_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[153 + batch*level_coeff]}")
    ),
    "lava_right_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[154 + batch*level_coeff]}")
    ),
    
    "cactus_body_left_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[160 + batch*level_coeff]}")
    ),
    "cactus_body_right_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[167 + batch*level_coeff]}")
    ),
    "cactus_body_right_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[161 + batch*level_coeff]}")
    ),
    "cactus_body_left_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[166 + batch*level_coeff]}")
    ),
    "cactus_body_left_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[162 + batch*level_coeff]}")
    ),
    "cactus_body_right_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[169 + batch*level_coeff]}")
    ),
    "cactus_high_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[164 + batch*level_coeff]}")
    ),
    "cactus_high_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[171 + batch*level_coeff]}")
    ),
    "cactus_solo_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[170 + batch*level_coeff]}")
    ),
    "cactus_solo_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[165 + batch*level_coeff]}")
    ),
    "cactus_top_left_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[168 + batch*level_coeff]}")
    ),
    "cactus_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[163 + batch*level_coeff]}")
    ),
    "cactus_top_left_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[172 + batch*level_coeff]}")
    ),
    "cactus_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[173 + batch*level_coeff]}")
    ),
    "little_cactus_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[174 + batch*level_coeff]}")
    ),
    "little_cactus_top": np.array(
        Image.open(f"{sprites_path}/{sprites[175 + batch*level_coeff]}")
    ),
    "high_cactus_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[176 + batch*level_coeff]}")
    ),
    "high_cactus_top": np.array(
        Image.open(f"{sprites_path}/{sprites[177 + batch*level_coeff]}")
    ),
    
    "barril": np.array(
        Image.open(f"{sprites_path}/{sprites[111 + batch*level_coeff]}")
    ),
    
    # -- RINGS --
    "top_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[112 + batch*level_coeff]}")
    ),
    "bottom_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[113 + batch*level_coeff]}")
    ),
    "top_left_and_bottom_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[114 + batch*level_coeff]}")
    ),
    "bottom_left_and_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[115 + batch*level_coeff]}")
    ),
    "top_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[116 + batch*level_coeff]}")
    ),
    "top_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[117 + batch*level_coeff]}")
    ),
    "bottom_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[118 + batch*level_coeff]}")
    ),
    "bottom_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[119 + batch*level_coeff]}")
    ),
    
    # -- SPRINGS --
    "spring_from_bottom_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[120 + batch*level_coeff]}")
    ),
    "spring_from_bottom_middle_lava_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[121 + batch*level_coeff]}")
    ),
    "spring_from_left_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[122 + batch*level_coeff]}")
    ),
    "spring_from_left_middle_lava_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[123 + batch*level_coeff]}")
    ),
    "spring_from_right_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[124 + batch*level_coeff]}")
    ),
    "spring_from_right_middle_lava_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[125 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[126 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left_lava_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[127 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[128 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right_lava_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[129 + batch*level_coeff]}")
    ),
    
    # -- SPIKES --
    "spike_from_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[130 + batch*level_coeff]}")
    ),
    "spike_from_bottom_lava_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[131 + batch*level_coeff]}")
    ),
    "spike_from_top": np.array(
        Image.open(f"{sprites_path}/{sprites[132 + batch*level_coeff]}")
    ),
    "spike_from_top_lava_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[133 + batch*level_coeff]}")
    ),
    
    # I'll assume it's something to block sonic.
    "blocking_thing": np.array(
        Image.open(f"{sprites_path}/{sprites[134 + batch*level_coeff]}")
    ),
    
    # -- SAND WATERFALLS --
    "sand_waterfall_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[142 + batch*level_coeff]}")
    ),
    "sand_waterfall_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[143 + batch*level_coeff]}")
    ),
    
    # -- CLOUDS --
    "cloud": np.array(Image.open(f"{sprites_path}/{sprites[145 + batch*level_coeff]}")),
    "cloud_left": np.array(
        Image.open(f"{sprites_path}/{sprites[146 + batch*level_coeff]}")
    ),
    "cloud_right": np.array(
        Image.open(f"{sprites_path}/{sprites[147 + batch*level_coeff]}")
    ),
    
    # -- BACKGROUND TILES --
    "desert_mountain_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[178 + batch*level_coeff]}")
    ),
    "desert_mountain_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[179 + batch*level_coeff]}")
    ),
    "desert_mountain_background_left": np.array(
        Image.open(f"{sprites_path}/{sprites[180 + batch*level_coeff]}")
    ),
    "desert_mountain_background_right": np.array(
        Image.open(f"{sprites_path}/{sprites[181 + batch*level_coeff]}")
    ),
    
    "background_special_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[182 + batch*level_coeff]}")
    ),
    "background_special_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[183 + batch*level_coeff]}")
    ),
    
    "vertical_lines": np.array(
        Image.open(f"{sprites_path}/{sprites[253 + batch*level_coeff]}")
    ),

    "background_tile_1": np.array(
        Image.open(f"{sprites_path}/{sprites[48 + batch*level_coeff]}")
    ),
    "background_tile_2": np.array(
        Image.open(f"{sprites_path}/{sprites[49 + batch*level_coeff]}")
    ),
    "background_tile_3": np.array(
        Image.open(f"{sprites_path}/{sprites[50 + batch*level_coeff]}")
    ),
    "background_tile_4": np.array(
        Image.open(f"{sprites_path}/{sprites[51 + batch*level_coeff]}")
    ),
    "background_tile_5": np.array(
        Image.open(f"{sprites_path}/{sprites[52 + batch*level_coeff]}")
    ),
    "background_tile_6": np.array(
        Image.open(f"{sprites_path}/{sprites[53 + batch*level_coeff]}")
    ),
    "background_tile_7": np.array(
        Image.open(f"{sprites_path}/{sprites[54 + batch*level_coeff]}")
    ),
    "background_tile_8": np.array(
        Image.open(f"{sprites_path}/{sprites[55 + batch*level_coeff]}")
    ),
    "background_tile_9": np.array(
        Image.open(f"{sprites_path}/{sprites[56 + batch*level_coeff]}")
    ),
    "background_tile_10": np.array(
        Image.open(f"{sprites_path}/{sprites[57 + batch*level_coeff]}")
    ),
    "background_tile_11": np.array(
        Image.open(f"{sprites_path}/{sprites[58 + batch*level_coeff]}")
    ),
    "background_tile_12": np.array(
        Image.open(f"{sprites_path}/{sprites[59 + batch*level_coeff]}")
    ),
    "background_tile_13": np.array(
        Image.open(f"{sprites_path}/{sprites[60 + batch*level_coeff]}")
    ),
    "background_tile_14": np.array(
        Image.open(f"{sprites_path}/{sprites[61 + batch*level_coeff]}")
    ),
    "background_tile_15": np.array(
        Image.open(f"{sprites_path}/{sprites[62 + batch*level_coeff]}")
    ),
    "background_tile_16": np.array(
        Image.open(f"{sprites_path}/{sprites[63 + batch*level_coeff]}")
    ),
    "background_tile_17": np.array(
        Image.open(f"{sprites_path}/{sprites[71 + batch*level_coeff]}")
    ),
    "background_tile_18": np.array(
        Image.open(f"{sprites_path}/{sprites[72 + batch*level_coeff]}")
    ),
    "background_tile_19": np.array(
        Image.open(f"{sprites_path}/{sprites[73 + batch*level_coeff]}")
    ),
    "background_tile_20": np.array(
        Image.open(f"{sprites_path}/{sprites[74 + batch*level_coeff]}")
    ),
    "background_tile_21": np.array(
        Image.open(f"{sprites_path}/{sprites[75 + batch*level_coeff]}")
    ),
    "background_tile_22": np.array(
        Image.open(f"{sprites_path}/{sprites[76 + batch*level_coeff]}")
    ),
    "background_tile_23": np.array(
        Image.open(f"{sprites_path}/{sprites[87 + batch*level_coeff]}")
    ),
    "background_tile_24": np.array(
        Image.open(f"{sprites_path}/{sprites[88 + batch*level_coeff]}")
    ),
    "background_tile_25": np.array(
        Image.open(f"{sprites_path}/{sprites[89 + batch*level_coeff]}")
    ),
    "background_tile_26": np.array(
        Image.open(f"{sprites_path}/{sprites[90 + batch*level_coeff]}")
    ),
    "background_tile_27": np.array(
        Image.open(f"{sprites_path}/{sprites[91 + batch*level_coeff]}")
    ),
    "background_tile_28": np.array(
        Image.open(f"{sprites_path}/{sprites[92 + batch*level_coeff]}")
    ),
    "background_tile_29": np.array(
        Image.open(f"{sprites_path}/{sprites[101 + batch*level_coeff]}")
    ),
    "background_tile_30": np.array(
        Image.open(f"{sprites_path}/{sprites[102 + batch*level_coeff]}")
    ),
    "background_tile_31": np.array(
        Image.open(f"{sprites_path}/{sprites[103 + batch*level_coeff]}")
    ),
    "background_tile_32": np.array(
        Image.open(f"{sprites_path}/{sprites[104 + batch*level_coeff]}")
    ),
    "background_tile_33": np.array(
        Image.open(f"{sprites_path}/{sprites[105 + batch*level_coeff]}")
    ),
    "background_tile_34": np.array(
        Image.open(f"{sprites_path}/{sprites[106 + batch*level_coeff]}")
    ),
    "background_tile_35": np.array(
        Image.open(f"{sprites_path}/{sprites[107 + batch*level_coeff]}")
    ),
    "background_tile_36": np.array(
        Image.open(f"{sprites_path}/{sprites[108 + batch*level_coeff]}")
    ),
    "background_tile_37": np.array(
        Image.open(f"{sprites_path}/{sprites[144 + batch*level_coeff]}")
    ),
    "background_tile_38": np.array(
        Image.open(f"{sprites_path}/{sprites[184 + batch*level_coeff]}")
    ),
    "background_tile_39": np.array(
        Image.open(f"{sprites_path}/{sprites[185 + batch*level_coeff]}")
    ),
    "background_tile_40": np.array(
        Image.open(f"{sprites_path}/{sprites[186 + batch*level_coeff]}")
    ),
    "background_tile_41": np.array(
        Image.open(f"{sprites_path}/{sprites[187 + batch*level_coeff]}")
    ),
    "background_tile_42": np.array(
        Image.open(f"{sprites_path}/{sprites[188 + batch*level_coeff]}")
    ),
    "background_tile_43": np.array(
        Image.open(f"{sprites_path}/{sprites[189 + batch*level_coeff]}")
    ),
    "background_tile_44": np.array(
        Image.open(f"{sprites_path}/{sprites[190 + batch*level_coeff]}")
    ),
    "background_tile_45": np.array(
        Image.open(f"{sprites_path}/{sprites[191 + batch*level_coeff]}")
    ),
    "background_tile_46": np.array(
        Image.open(f"{sprites_path}/{sprites[192 + batch*level_coeff]}")
    ),
    "background_tile_47": np.array(
        Image.open(f"{sprites_path}/{sprites[193 + batch*level_coeff]}")
    ),
    "background_tile_48": np.array(
        Image.open(f"{sprites_path}/{sprites[194 + batch*level_coeff]}")
    ),
    "background_tile_49": np.array(
        Image.open(f"{sprites_path}/{sprites[195 + batch*level_coeff]}")
    ),
    "background_tile_50": np.array(
        Image.open(f"{sprites_path}/{sprites[196 + batch*level_coeff]}")
    ),
    "background_tile_51": np.array(
        Image.open(f"{sprites_path}/{sprites[197 + batch*level_coeff]}")
    ),
    "background_tile_52": np.array(
        Image.open(f"{sprites_path}/{sprites[198 + batch*level_coeff]}")
    ),
    "background_tile_53": np.array(
        Image.open(f"{sprites_path}/{sprites[199 + batch*level_coeff]}")
    ),
    "background_tile_54": np.array(
        Image.open(f"{sprites_path}/{sprites[200 + batch*level_coeff]}")
    ),
    "background_tile_55": np.array(
        Image.open(f"{sprites_path}/{sprites[201 + batch*level_coeff]}")
    ),
    "background_tile_56": np.array(
        Image.open(f"{sprites_path}/{sprites[202 + batch*level_coeff]}")
    ),
    "background_tile_57": np.array(
        Image.open(f"{sprites_path}/{sprites[203 + batch*level_coeff]}")
    ),
    "background_tile_58": np.array(
        Image.open(f"{sprites_path}/{sprites[204 + batch*level_coeff]}")
    ),
    "background_tile_59": np.array(
        Image.open(f"{sprites_path}/{sprites[205 + batch*level_coeff]}")
    ),
    "background_tile_60": np.array(
        Image.open(f"{sprites_path}/{sprites[206 + batch*level_coeff]}")
    ),
    "background_tile_61": np.array(
        Image.open(f"{sprites_path}/{sprites[207 + batch*level_coeff]}")
    ),
    "background_tile_62": np.array(
        Image.open(f"{sprites_path}/{sprites[208 + batch*level_coeff]}")
    ),
    "background_tile_63": np.array(
        Image.open(f"{sprites_path}/{sprites[209 + batch*level_coeff]}")
    ),
    "background_tile_64": np.array(
        Image.open(f"{sprites_path}/{sprites[210 + batch*level_coeff]}")
    ),
    "background_tile_65": np.array(
        Image.open(f"{sprites_path}/{sprites[211 + batch*level_coeff]}")
    ),
    "background_tile_66": np.array(
        Image.open(f"{sprites_path}/{sprites[212 + batch*level_coeff]}")
    ),
    "background_tile_67": np.array(
        Image.open(f"{sprites_path}/{sprites[213 + batch*level_coeff]}")
    ),
    "background_tile_68": np.array(
        Image.open(f"{sprites_path}/{sprites[214 + batch*level_coeff]}")
    ),
    "background_tile_69": np.array(
        Image.open(f"{sprites_path}/{sprites[215 + batch*level_coeff]}")
    ),
    "background_tile_70": np.array(
        Image.open(f"{sprites_path}/{sprites[216 + batch*level_coeff]}")
    ),
    "background_tile_71": np.array(
        Image.open(f"{sprites_path}/{sprites[217 + batch*level_coeff]}")
    ),
    "background_tile_72": np.array(
        Image.open(f"{sprites_path}/{sprites[218 + batch*level_coeff]}")
    ),
    "background_tile_73": np.array(
        Image.open(f"{sprites_path}/{sprites[219 + batch*level_coeff]}")
    ),
    "background_tile_74": np.array(
        Image.open(f"{sprites_path}/{sprites[220 + batch*level_coeff]}")
    ),
    "background_tile_75": np.array(
        Image.open(f"{sprites_path}/{sprites[221 + batch*level_coeff]}")
    ),
    "background_tile_76": np.array(
        Image.open(f"{sprites_path}/{sprites[222 + batch*level_coeff]}")
    ),
    "background_tile_77": np.array(
        Image.open(f"{sprites_path}/{sprites[223 + batch*level_coeff]}")
    ),
    "background_tile_78": np.array(
        Image.open(f"{sprites_path}/{sprites[224 + batch*level_coeff]}")
    ),
    "background_tile_79": np.array(
        Image.open(f"{sprites_path}/{sprites[225 + batch*level_coeff]}")
    ),
    "background_tile_80": np.array(
        Image.open(f"{sprites_path}/{sprites[226 + batch*level_coeff]}")
    ),
    "background_tile_81": np.array(
        Image.open(f"{sprites_path}/{sprites[227 + batch*level_coeff]}")
    ),
    "background_tile_82": np.array(
        Image.open(f"{sprites_path}/{sprites[228 + batch*level_coeff]}")
    ),
    "background_tile_83": np.array(
        Image.open(f"{sprites_path}/{sprites[229 + batch*level_coeff]}")
    ),
    "background_tile_84": np.array(
        Image.open(f"{sprites_path}/{sprites[230 + batch*level_coeff]}")
    ),
    "background_tile_85": np.array(
        Image.open(f"{sprites_path}/{sprites[231 + batch*level_coeff]}")
    ),
    "background_tile_86": np.array(
        Image.open(f"{sprites_path}/{sprites[232 + batch*level_coeff]}")
    ),
    "background_tile_87": np.array(
        Image.open(f"{sprites_path}/{sprites[233 + batch*level_coeff]}")
    ),
    "background_tile_88": np.array(
        Image.open(f"{sprites_path}/{sprites[234 + batch*level_coeff]}")
    ),
    "background_tile_89": np.array(
        Image.open(f"{sprites_path}/{sprites[235 + batch*level_coeff]}")
    ),
    "background_tile_90": np.array(
        Image.open(f"{sprites_path}/{sprites[236 + batch*level_coeff]}")
    ),
    "background_tile_91": np.array(
        Image.open(f"{sprites_path}/{sprites[237 + batch*level_coeff]}")
    ),
    "background_tile_92": np.array(
        Image.open(f"{sprites_path}/{sprites[238 + batch*level_coeff]}")
    ),
    "background_tile_93": np.array(
        Image.open(f"{sprites_path}/{sprites[239 + batch*level_coeff]}")
    ),
    "background_tile_94": np.array(
        Image.open(f"{sprites_path}/{sprites[240 + batch*level_coeff]}")
    ),
    "background_tile_95": np.array(
        Image.open(f"{sprites_path}/{sprites[241 + batch*level_coeff]}")
    ),
    "background_tile_96": np.array(
        Image.open(f"{sprites_path}/{sprites[242 + batch*level_coeff]}")
    ),
    "background_tile_97": np.array(
        Image.open(f"{sprites_path}/{sprites[243 + batch*level_coeff]}")
    ),
    "background_tile_98": np.array(
        Image.open(f"{sprites_path}/{sprites[244 + batch*level_coeff]}")
    ),
    "background_tile_99": np.array(
        Image.open(f"{sprites_path}/{sprites[245 + batch*level_coeff]}")
    ),
    "background_tile_100": np.array(
        Image.open(f"{sprites_path}/{sprites[246 + batch*level_coeff]}")
    ),
    "background_tile_101": np.array(
        Image.open(f"{sprites_path}/{sprites[247 + batch*level_coeff]}")
    ),
    "background_tile_102": np.array(
        Image.open(f"{sprites_path}/{sprites[248 + batch*level_coeff]}")
    ),
    "background_tile_103": np.array(
        Image.open(f"{sprites_path}/{sprites[249 + batch*level_coeff]}")
    ),
    "background_tile_104": np.array(
        Image.open(f"{sprites_path}/{sprites[250 + batch*level_coeff]}")
    ),
    "background_tile_105": np.array(
        Image.open(f"{sprites_path}/{sprites[254 + batch*level_coeff]}")
    ),
    "background_tile_106": np.array(
        Image.open(f"{sprites_path}/{sprites[255 + batch*level_coeff]}")
    ),
}

# -------------------------------------------- LEVEL 4

level_coeff = 3

level_4_sprites = {
    # -- INCLINED / SLOPE PIECES --
    
    # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[0 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[1 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[2 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[3 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[4 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[5 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[6 + batch*level_coeff]}")
    ),
    
    # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[16 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[17 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[18 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[19 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[20 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[21 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[22 + batch*level_coeff]}")
    ),
    
    # -- LOOP & CORNER PIECES --

    # RIGHT SIDE
    "loop_bottom_middle_right": np.array(
        Image.open(f"{sprites_path}/{sprites[7 + batch*level_coeff]}")
    ),
    "loop_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[8 + batch*level_coeff]}")
    ),
    "loop_right_middle_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[9 + batch*level_coeff]}")
    ),
    "loop_right_middle_top": np.array(
        Image.open(f"{sprites_path}/{sprites[10 + batch*level_coeff]}")
    ),
    "loop_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[11 + batch*level_coeff]}")
    ),
    "loop_top_middle_right": np.array(
        Image.open(f"{sprites_path}/{sprites[12 + batch*level_coeff]}")
    ),
    
    # LEFT SIDE
    "loop_bottom_middle_left": np.array(
        Image.open(f"{sprites_path}/{sprites[23 + batch*level_coeff]}")
    ),
    "loop_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[24 + batch*level_coeff]}")
    ),
    "loop_left_middle_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[25 + batch*level_coeff]}")
    ),
    "loop_left_middle_top": np.array(
        Image.open(f"{sprites_path}/{sprites[26 + batch*level_coeff]}")
    ),
    "loop_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[27 + batch*level_coeff]}")
    ),
    "loop_top_middle_left": np.array(
        Image.open(f"{sprites_path}/{sprites[28 + batch*level_coeff]}")
    ),
    # -- GROUND / ICE GROUND / CHECKER TILES --
        
        # GROUND TILES
            
            # LOW
    "low_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[13 + batch*level_coeff]}")
    ),
    "low_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[15 + batch*level_coeff]}")
    ),
    "low_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[29 + batch*level_coeff]}")
    ),
    "low_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[31 + batch*level_coeff]}")
    ),
    "triangle_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[30 + batch*level_coeff]}")
    ),
            # HIGH
    "curved_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[14 + batch*level_coeff]}")
    ),
    "high_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[33 + batch*level_coeff]}")
    ),
    "high_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[34 + batch*level_coeff]}")
    ),
    "high_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[36 + batch*level_coeff]}")
    ),
    "high_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[47 + batch*level_coeff]}")
    ),
    "high_ground_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[97 + batch*level_coeff]}")
    ),
    "high_ground_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[98 + batch*level_coeff]}")
    ),
    "high_ground_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[100 + batch*level_coeff]}")
    ),
    "high_ground_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[111 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[37 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[39 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[41 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[42 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[38 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[40 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[43 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[44 + batch*level_coeff]}")
    ),
    
        # ICE GROUND TILES
    
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_ice_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[64 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[65 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[66 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[67 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[68 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[69 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[70 + batch*level_coeff]}")
    ),
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_ice_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[80 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[81 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[82 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[83 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[84 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[85 + batch*level_coeff]}")
    ),
    "inclined_ice_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[86 + batch*level_coeff]}")
    ),
            
            # LOW
    "low_ice_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[77 + batch*level_coeff]}")
    ),
    "low_ice_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[79 + batch*level_coeff]}")
    ),
    "low_ice_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[93 + batch*level_coeff]}")
    ),
    "low_ice_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[95 + batch*level_coeff]}")
    ),
    "triangle_ice_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[94 + batch*level_coeff]}")
    ),
            # HIGH
    "curved_ice_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[78 + batch*level_coeff]}")
    ),
    
        # CHECKER TILES
            
            # LOW
    "low_checker_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[148 + batch*level_coeff]}")
    ),
    "low_checker_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[149 + batch*level_coeff]}")
    ),
    
            # HIGH
    "high_checker_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[32 + batch*level_coeff]}")
    ),
    "high_checker_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[35 + batch*level_coeff]}")
    ),
    "high_checker_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[45 + batch*level_coeff]}")
    ),
    "high_checker_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[46 + batch*level_coeff]}")
    ),
    "high_checker_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[96 + batch*level_coeff]}")
    ),
    "high_checker_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[99 + batch*level_coeff]}")
    ),
    "high_checker_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[109 + batch*level_coeff]}")
    ),
    "high_checker_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[110 + batch*level_coeff]}")
    ),
    "high_checker_v9": np.array(
        Image.open(f"{sprites_path}/{sprites[135 + batch*level_coeff]}")
    ),
    "high_checker_v10": np.array(
        Image.open(f"{sprites_path}/{sprites[150 + batch*level_coeff]}")
    ),
    "high_checker_v11": np.array(
        Image.open(f"{sprites_path}/{sprites[151 + batch*level_coeff]}")
    ),
    "high_checker_v12": np.array(
        Image.open(f"{sprites_path}/{sprites[152 + batch*level_coeff]}")
    ),
    "high_checker_v13": np.array(
        Image.open(f"{sprites_path}/{sprites[153 + batch*level_coeff]}")
    ),
    "high_checker_v14": np.array(
        Image.open(f"{sprites_path}/{sprites[154 + batch*level_coeff]}")
    ),
    "high_checker_v15": np.array(
        Image.open(f"{sprites_path}/{sprites[155 + batch*level_coeff]}")
    ),
    "high_checker_v16": np.array(
        Image.open(f"{sprites_path}/{sprites[156 + batch*level_coeff]}")
    ),
    "high_checker_v17": np.array(
        Image.open(f"{sprites_path}/{sprites[157 + batch*level_coeff]}")
    ),
    "high_checker_v18": np.array(
        Image.open(f"{sprites_path}/{sprites[158 + batch*level_coeff]}")
    ),
    "high_checker_v19": np.array(
        Image.open(f"{sprites_path}/{sprites[159 + batch*level_coeff]}")
    ),
    "high_checker_v20": np.array(
        Image.open(f"{sprites_path}/{sprites[251 + batch*level_coeff]}")
    ),
    "high_checker_v21": np.array(
        Image.open(f"{sprites_path}/{sprites[252 + batch*level_coeff]}")
    ),
    
    # -- ICE, TREE & GEMS --
    "two_vertical_gems": np.array(
        Image.open(f"{sprites_path}/{sprites[160 + batch*level_coeff]}")
    ),
    "four_gems_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[161 + batch*level_coeff]}")
    ),
    "four_gems_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[162 + batch*level_coeff]}")
    ),
    "four_gems_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[163 + batch*level_coeff]}")
    ),
    "four_gems_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[164 + batch*level_coeff]}")
    ),
    "bottom_right_gem": np.array(
        Image.open(f"{sprites_path}/{sprites[165 + batch*level_coeff]}")
    ),
    "bottom_left_gem": np.array(
        Image.open(f"{sprites_path}/{sprites[166 + batch*level_coeff]}")
    ),
    "bottom_two_gem": np.array(
        Image.open(f"{sprites_path}/{sprites[167 + batch*level_coeff]}")
    ),
    "tree_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[174 + batch*level_coeff]}")
    ),
    "tree_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[175 + batch*level_coeff]}")
    ),
    "tree_middle_left": np.array(
        Image.open(f"{sprites_path}/{sprites[176 + batch*level_coeff]}")
    ),
    "tree_middle_right": np.array(
        Image.open(f"{sprites_path}/{sprites[177 + batch*level_coeff]}")
    ),
    "tree_trunk_left": np.array(
        Image.open(f"{sprites_path}/{sprites[178 + batch*level_coeff]}")
    ),
    "tree_trunk_right": np.array(
        Image.open(f"{sprites_path}/{sprites[179 + batch*level_coeff]}")
    ),
    "tree_bottom_left_classic_background": np.array(
        Image.open(f"{sprites_path}/{sprites[180 + batch*level_coeff]}")
    ),
    "tree_bottom_right_classic_background": np.array(
        Image.open(f"{sprites_path}/{sprites[181 + batch*level_coeff]}")
    ),
    "tree_bottom_left_special_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[182 + batch*level_coeff]}")
    ),
    "tree_bottom_right_special_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[183 + batch*level_coeff]}")
    ),
    "tree_bottom_left_snow_background": np.array(
        Image.open(f"{sprites_path}/{sprites[184 + batch*level_coeff]}")
    ),
    "tree_bottom_right_snow_background": np.array(
        Image.open(f"{sprites_path}/{sprites[185 + batch*level_coeff]}")
    ),
    "tree_bottom_left_mountain_background": np.array(
        Image.open(f"{sprites_path}/{sprites[186 + batch*level_coeff]}")
    ),
    "tree_bottom_right_mountain_background": np.array(
        Image.open(f"{sprites_path}/{sprites[187 + batch*level_coeff]}")
    ),
    "tree_bottom_left_special_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[188 + batch*level_coeff]}")
    ),
    "tree_bottom_right_special_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[189 + batch*level_coeff]}")
    ),
    
    # -- RINGS --
    "top_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[112 + batch*level_coeff]}")
    ),
    "bottom_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[113 + batch*level_coeff]}")
    ),
    "top_left_and_bottom_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[114 + batch*level_coeff]}")
    ),
    "bottom_left_and_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[115 + batch*level_coeff]}")
    ),
    "top_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[116 + batch*level_coeff]}")
    ),
    "top_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[117 + batch*level_coeff]}")
    ),
    "bottom_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[118 + batch*level_coeff]}")
    ),
    "bottom_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[119 + batch*level_coeff]}")
    ),
    
    # -- SPRINGS --
    "spring_from_bottom_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[120 + batch*level_coeff]}")
    ),
    "spring_from_bottom_middle_ice_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[121 + batch*level_coeff]}")
    ),
    "spring_from_left_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[122 + batch*level_coeff]}")
    ),
    "spring_from_left_middle_ice_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[123 + batch*level_coeff]}")
    ),
    "spring_from_right_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[124 + batch*level_coeff]}")
    ),
    "spring_from_right_middle_ice_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[125 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[126 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left_ice_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[127 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[128 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right_ice_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[129 + batch*level_coeff]}")
    ),
    
    # -- SPIKES --
    "spike_from_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[130 + batch*level_coeff]}")
    ),
    "spike_from_bottom_ice_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[131 + batch*level_coeff]}")
    ),
    "spike_from_top": np.array(
        Image.open(f"{sprites_path}/{sprites[132 + batch*level_coeff]}")
    ),
    "spike_from_top_ice_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[133 + batch*level_coeff]}")
    ),
    "ice_spike": np.array(
        Image.open(f"{sprites_path}/{sprites[197 + batch*level_coeff]}")
    ),
    "ice_spike_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[198 + batch*level_coeff]}")
    ),
    "ice_spike_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[199 + batch*level_coeff]}")
    ),
    
    # I'll assume it's something to block sonic.
    "blocking_thing": np.array(
        Image.open(f"{sprites_path}/{sprites[134 + batch*level_coeff]}")
    ),
    
    # -- CLOUDS / SNOW --
    "snow_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[200 + batch*level_coeff]}")
    ),
    "snow_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[201 + batch*level_coeff]}")
    ),
    "snow_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[202 + batch*level_coeff]}")
    ),
    "snow_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[203 + batch*level_coeff]}")
    ),
    "snow_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[204 + batch*level_coeff]}")
    ),
    "snow_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[205 + batch*level_coeff]}")
    ),
    "snow_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[206 + batch*level_coeff]}")
    ),
    "snow_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[207 + batch*level_coeff]}")
    ),
    "snow_v9": np.array(
        Image.open(f"{sprites_path}/{sprites[208 + batch*level_coeff]}")
    ),
    "snow_v10": np.array(
        Image.open(f"{sprites_path}/{sprites[209 + batch*level_coeff]}")
    ),
    
    # -- BACKGROUND TILES --
    "ice_mountain_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[168 + batch*level_coeff]}")
    ),
    "ice_mountain_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[169 + batch*level_coeff]}")
    ),
    
    "background_special_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[170 + batch*level_coeff]}")
    ),
    "background_special_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[171 + batch*level_coeff]}")
    ),
    "background_special_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[172 + batch*level_coeff]}")
    ),
    
    "snow_background": np.array(
        Image.open(f"{sprites_path}/{sprites[173 + batch*level_coeff]}")
    ),
    
    "vertical_lines": np.array(
        Image.open(f"{sprites_path}/{sprites[253 + batch*level_coeff]}")
    ),

    "background_tile_1": np.array(
        Image.open(f"{sprites_path}/{sprites[48 + batch*level_coeff]}")
    ),
    "background_tile_2": np.array(
        Image.open(f"{sprites_path}/{sprites[49 + batch*level_coeff]}")
    ),
    "background_tile_3": np.array(
        Image.open(f"{sprites_path}/{sprites[50 + batch*level_coeff]}")
    ),
    "background_tile_4": np.array(
        Image.open(f"{sprites_path}/{sprites[51 + batch*level_coeff]}")
    ),
    "background_tile_5": np.array(
        Image.open(f"{sprites_path}/{sprites[52 + batch*level_coeff]}")
    ),
    "background_tile_6": np.array(
        Image.open(f"{sprites_path}/{sprites[53 + batch*level_coeff]}")
    ),
    "background_tile_7": np.array(
        Image.open(f"{sprites_path}/{sprites[54 + batch*level_coeff]}")
    ),
    "background_tile_8": np.array(
        Image.open(f"{sprites_path}/{sprites[55 + batch*level_coeff]}")
    ),
    "background_tile_9": np.array(
        Image.open(f"{sprites_path}/{sprites[56 + batch*level_coeff]}")
    ),
    "background_tile_10": np.array(
        Image.open(f"{sprites_path}/{sprites[57 + batch*level_coeff]}")
    ),
    "background_tile_11": np.array(
        Image.open(f"{sprites_path}/{sprites[58 + batch*level_coeff]}")
    ),
    "background_tile_12": np.array(
        Image.open(f"{sprites_path}/{sprites[59 + batch*level_coeff]}")
    ),
    "background_tile_13": np.array(
        Image.open(f"{sprites_path}/{sprites[60 + batch*level_coeff]}")
    ),
    "background_tile_14": np.array(
        Image.open(f"{sprites_path}/{sprites[61 + batch*level_coeff]}")
    ),
    "background_tile_15": np.array(
        Image.open(f"{sprites_path}/{sprites[62 + batch*level_coeff]}")
    ),
    "background_tile_16": np.array(
        Image.open(f"{sprites_path}/{sprites[63 + batch*level_coeff]}")
    ),
    "background_tile_17": np.array(
        Image.open(f"{sprites_path}/{sprites[71 + batch*level_coeff]}")
    ),
    "background_tile_18": np.array(
        Image.open(f"{sprites_path}/{sprites[72 + batch*level_coeff]}")
    ),
    "background_tile_19": np.array(
        Image.open(f"{sprites_path}/{sprites[73 + batch*level_coeff]}")
    ),
    "background_tile_20": np.array(
        Image.open(f"{sprites_path}/{sprites[74 + batch*level_coeff]}")
    ),
    "background_tile_21": np.array(
        Image.open(f"{sprites_path}/{sprites[75 + batch*level_coeff]}")
    ),
    "background_tile_22": np.array(
        Image.open(f"{sprites_path}/{sprites[76 + batch*level_coeff]}")
    ),
    "background_tile_23": np.array(
        Image.open(f"{sprites_path}/{sprites[87 + batch*level_coeff]}")
    ),
    "background_tile_24": np.array(
        Image.open(f"{sprites_path}/{sprites[88 + batch*level_coeff]}")
    ),
    "background_tile_25": np.array(
        Image.open(f"{sprites_path}/{sprites[89 + batch*level_coeff]}")
    ),
    "background_tile_26": np.array(
        Image.open(f"{sprites_path}/{sprites[90 + batch*level_coeff]}")
    ),
    "background_tile_27": np.array(
        Image.open(f"{sprites_path}/{sprites[91 + batch*level_coeff]}")
    ),
    "background_tile_28": np.array(
        Image.open(f"{sprites_path}/{sprites[92 + batch*level_coeff]}")
    ),
    "background_tile_29": np.array(
        Image.open(f"{sprites_path}/{sprites[101 + batch*level_coeff]}")
    ),
    "background_tile_30": np.array(
        Image.open(f"{sprites_path}/{sprites[102 + batch*level_coeff]}")
    ),
    "background_tile_31": np.array(
        Image.open(f"{sprites_path}/{sprites[103 + batch*level_coeff]}")
    ),
    "background_tile_32": np.array(
        Image.open(f"{sprites_path}/{sprites[104 + batch*level_coeff]}")
    ),
    "background_tile_33": np.array(
        Image.open(f"{sprites_path}/{sprites[105 + batch*level_coeff]}")
    ),
    "background_tile_34": np.array(
        Image.open(f"{sprites_path}/{sprites[106 + batch*level_coeff]}")
    ),
    "background_tile_35": np.array(
        Image.open(f"{sprites_path}/{sprites[107 + batch*level_coeff]}")
    ),
    "background_tile_36": np.array(
        Image.open(f"{sprites_path}/{sprites[108 + batch*level_coeff]}")
    ),
    "background_tile_37": np.array(
        Image.open(f"{sprites_path}/{sprites[136 + batch*level_coeff]}")
    ),
    "background_tile_38": np.array(
        Image.open(f"{sprites_path}/{sprites[137 + batch*level_coeff]}")
    ),
    "background_tile_39": np.array(
        Image.open(f"{sprites_path}/{sprites[138 + batch*level_coeff]}")
    ),
    "background_tile_40": np.array(
        Image.open(f"{sprites_path}/{sprites[139 + batch*level_coeff]}")
    ),
    "background_tile_41": np.array(
        Image.open(f"{sprites_path}/{sprites[140 + batch*level_coeff]}")
    ),
    "background_tile_42": np.array(
        Image.open(f"{sprites_path}/{sprites[141 + batch*level_coeff]}")
    ),
    "background_tile_43": np.array(
        Image.open(f"{sprites_path}/{sprites[142 + batch*level_coeff]}")
    ),
    "background_tile_44": np.array(
        Image.open(f"{sprites_path}/{sprites[143 + batch*level_coeff]}")
    ),
    "background_tile_45": np.array(
        Image.open(f"{sprites_path}/{sprites[144 + batch*level_coeff]}")
    ),
    "background_tile_46": np.array(
        Image.open(f"{sprites_path}/{sprites[145 + batch*level_coeff]}")
    ),
    "background_tile_47": np.array(
        Image.open(f"{sprites_path}/{sprites[146 + batch*level_coeff]}")
    ),
    "background_tile_48": np.array(
        Image.open(f"{sprites_path}/{sprites[147 + batch*level_coeff]}")
    ),
    "background_tile_49": np.array(
        Image.open(f"{sprites_path}/{sprites[190 + batch*level_coeff]}")
    ),
    "background_tile_50": np.array(
        Image.open(f"{sprites_path}/{sprites[191 + batch*level_coeff]}")
    ),
    "background_tile_51": np.array(
        Image.open(f"{sprites_path}/{sprites[192 + batch*level_coeff]}")
    ),
    "background_tile_52": np.array(
        Image.open(f"{sprites_path}/{sprites[193 + batch*level_coeff]}")
    ),
    "background_tile_53": np.array(
        Image.open(f"{sprites_path}/{sprites[194 + batch*level_coeff]}")
    ),
    "background_tile_54": np.array(
        Image.open(f"{sprites_path}/{sprites[195 + batch*level_coeff]}")
    ),
    "background_tile_55": np.array(
        Image.open(f"{sprites_path}/{sprites[196 + batch*level_coeff]}")
    ),
    "background_tile_56": np.array(
        Image.open(f"{sprites_path}/{sprites[210 + batch*level_coeff]}")
    ),
    "background_tile_57": np.array(
        Image.open(f"{sprites_path}/{sprites[211 + batch*level_coeff]}")
    ),
    "background_tile_58": np.array(
        Image.open(f"{sprites_path}/{sprites[212 + batch*level_coeff]}")
    ),
    "background_tile_59": np.array(
        Image.open(f"{sprites_path}/{sprites[213 + batch*level_coeff]}")
    ),
    "background_tile_60": np.array(
        Image.open(f"{sprites_path}/{sprites[214 + batch*level_coeff]}")
    ),
    "background_tile_61": np.array(
        Image.open(f"{sprites_path}/{sprites[215 + batch*level_coeff]}")
    ),
    "background_tile_62": np.array(
        Image.open(f"{sprites_path}/{sprites[216 + batch*level_coeff]}")
    ),
    "background_tile_63": np.array(
        Image.open(f"{sprites_path}/{sprites[217 + batch*level_coeff]}")
    ),
    "background_tile_64": np.array(
        Image.open(f"{sprites_path}/{sprites[218 + batch*level_coeff]}")
    ),
    "background_tile_65": np.array(
        Image.open(f"{sprites_path}/{sprites[219 + batch*level_coeff]}")
    ),
    "background_tile_66": np.array(
        Image.open(f"{sprites_path}/{sprites[220 + batch*level_coeff]}")
    ),
    "background_tile_67": np.array(
        Image.open(f"{sprites_path}/{sprites[221 + batch*level_coeff]}")
    ),
    "background_tile_68": np.array(
        Image.open(f"{sprites_path}/{sprites[222 + batch*level_coeff]}")
    ),
    "background_tile_69": np.array(
        Image.open(f"{sprites_path}/{sprites[223 + batch*level_coeff]}")
    ),
    "background_tile_70": np.array(
        Image.open(f"{sprites_path}/{sprites[224 + batch*level_coeff]}")
    ),
    "background_tile_71": np.array(
        Image.open(f"{sprites_path}/{sprites[225 + batch*level_coeff]}")
    ),
    "background_tile_72": np.array(
        Image.open(f"{sprites_path}/{sprites[226 + batch*level_coeff]}")
    ),
    "background_tile_73": np.array(
        Image.open(f"{sprites_path}/{sprites[227 + batch*level_coeff]}")
    ),
    "background_tile_74": np.array(
        Image.open(f"{sprites_path}/{sprites[228 + batch*level_coeff]}")
    ),
    "background_tile_75": np.array(
        Image.open(f"{sprites_path}/{sprites[229 + batch*level_coeff]}")
    ),
    "background_tile_76": np.array(
        Image.open(f"{sprites_path}/{sprites[230 + batch*level_coeff]}")
    ),
    "background_tile_77": np.array(
        Image.open(f"{sprites_path}/{sprites[231 + batch*level_coeff]}")
    ),
    "background_tile_78": np.array(
        Image.open(f"{sprites_path}/{sprites[232 + batch*level_coeff]}")
    ),
    "background_tile_79": np.array(
        Image.open(f"{sprites_path}/{sprites[233 + batch*level_coeff]}")
    ),
    "background_tile_80": np.array(
        Image.open(f"{sprites_path}/{sprites[234 + batch*level_coeff]}")
    ),
    "background_tile_81": np.array(
        Image.open(f"{sprites_path}/{sprites[235 + batch*level_coeff]}")
    ),
    "background_tile_82": np.array(
        Image.open(f"{sprites_path}/{sprites[236 + batch*level_coeff]}")
    ),
    "background_tile_83": np.array(
        Image.open(f"{sprites_path}/{sprites[237 + batch*level_coeff]}")
    ),
    "background_tile_84": np.array(
        Image.open(f"{sprites_path}/{sprites[238 + batch*level_coeff]}")
    ),
    "background_tile_85": np.array(
        Image.open(f"{sprites_path}/{sprites[239 + batch*level_coeff]}")
    ),
    "background_tile_86": np.array(
        Image.open(f"{sprites_path}/{sprites[240 + batch*level_coeff]}")
    ),
    "background_tile_87": np.array(
        Image.open(f"{sprites_path}/{sprites[241 + batch*level_coeff]}")
    ),
    "background_tile_88": np.array(
        Image.open(f"{sprites_path}/{sprites[242 + batch*level_coeff]}")
    ),
    "background_tile_89": np.array(
        Image.open(f"{sprites_path}/{sprites[243 + batch*level_coeff]}")
    ),
    "background_tile_90": np.array(
        Image.open(f"{sprites_path}/{sprites[244 + batch*level_coeff]}")
    ),
    "background_tile_91": np.array(
        Image.open(f"{sprites_path}/{sprites[245 + batch*level_coeff]}")
    ),
    "background_tile_92": np.array(
        Image.open(f"{sprites_path}/{sprites[246 + batch*level_coeff]}")
    ),
    "background_tile_93": np.array(
        Image.open(f"{sprites_path}/{sprites[247 + batch*level_coeff]}")
    ),
    "background_tile_94": np.array(
        Image.open(f"{sprites_path}/{sprites[248 + batch*level_coeff]}")
    ),
    "background_tile_95": np.array(
        Image.open(f"{sprites_path}/{sprites[249 + batch*level_coeff]}")
    ),
    "background_tile_96": np.array(
        Image.open(f"{sprites_path}/{sprites[250 + batch*level_coeff]}")
    ),
    "background_tile_97": np.array(
        Image.open(f"{sprites_path}/{sprites[254 + batch*level_coeff]}")
    ),
    "background_tile_98": np.array(
        Image.open(f"{sprites_path}/{sprites[255 + batch*level_coeff]}")
    ),
}

# -------------------------------------------- LEVEL 5

level_coeff = 4

level_5_sprites = {
    # -- INCLINED / SLOPE PIECES --
    
    # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[0 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[1 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[2 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[3 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[4 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[5 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[6 + batch*level_coeff]}")
    ),
    
    # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[16 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[17 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[18 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[19 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[20 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[21 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[22 + batch*level_coeff]}")
    ),
    
    # -- LOOP & CORNER PIECES --

    # LOOP
    "loop_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[50 + batch*level_coeff]}")
    ),
    "loop_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[51 + batch*level_coeff]}")
    ),
    "loop_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[52 + batch*level_coeff]}")
    ),
    "loop_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[53 + batch*level_coeff]}")
    ),
    
    "double_horizontal_wall_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[48 + batch*level_coeff]}")
    ),
    "double_horizontal_wall_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[61 + batch*level_coeff]}")
    ),
    "double_horizontal_wall_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[62 + batch*level_coeff]}")
    ),
    "double_vertical_wall_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[49 + batch*level_coeff]}")
    ),
    "double_vertical_wall_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[59 + batch*level_coeff]}")
    ),
    "double_vertical_wall_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[60 + batch*level_coeff]}")
    ),
    
    "up_entry_bottom_wall": np.array(
        Image.open(f"{sprites_path}/{sprites[54 + batch*level_coeff]}")
    ),
    "bottom_entry_top_wall": np.array(
        Image.open(f"{sprites_path}/{sprites[55 + batch*level_coeff]}")
    ),
    "right_entry_left_wall": np.array(
        Image.open(f"{sprites_path}/{sprites[56 + batch*level_coeff]}")
    ),
    "left_entry_right_wall": np.array(
        Image.open(f"{sprites_path}/{sprites[57 + batch*level_coeff]}")
    ),
    "all_entry": np.array(
        Image.open(f"{sprites_path}/{sprites[58 + batch*level_coeff]}")
    ),
    
    # WALL
    "left_wall": np.array(
        Image.open(f"{sprites_path}/{sprites[35 + batch*level_coeff]}")
    ),
    "right_wall": np.array(
        Image.open(f"{sprites_path}/{sprites[46 + batch*level_coeff]}")
    ),
    "double_vertical_wall": np.array(
        Image.open(f"{sprites_path}/{sprites[45 + batch*level_coeff]}")
    ),
    
    # -- GROUND / DARK GROUND / CHECKER TILES --
        
        # GROUND TILES
            
            # LOW
    "low_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[13 + batch*level_coeff]}")
    ),
    "low_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[15 + batch*level_coeff]}")
    ),
    "low_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[29 + batch*level_coeff]}")
    ),
    "low_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[31 + batch*level_coeff]}")
    ),
    
    "triangle_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[30 + batch*level_coeff]}")
    ),
            # HIGH
    "curved_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[14 + batch*level_coeff]}")
    ),
    
    "high_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[33 + batch*level_coeff]}")
    ),
    "high_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[34 + batch*level_coeff]}")
    ),
    "high_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[36 + batch*level_coeff]}")
    ),
    "high_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[47 + batch*level_coeff]}")
    ),
    "high_ground_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[139 + batch*level_coeff]}")
    ),
    "high_ground_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[140 + batch*level_coeff]}")
    ),
    "high_ground_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[141 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[37 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[39 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[42 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[38 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[40 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[43 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[44 + batch*level_coeff]}")
    ),
        
        # DARK GROUND TILES
            
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_dark_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[64 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[65 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[66 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[67 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[68 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[69 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[70 + batch*level_coeff]}")
    ),
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_dark_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[80 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[81 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[82 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[83 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[84 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[85 + batch*level_coeff]}")
    ),
    "inclined_dark_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[86 + batch*level_coeff]}")
    ),
            
            # LOW
    "low_dark_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[77 + batch*level_coeff]}")
    ),
    "low_dark_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[79 + batch*level_coeff]}")
    ),
    "low_dark_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[93 + batch*level_coeff]}")
    ),
    "low_dark_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[95 + batch*level_coeff]}")
    ),
    "triangle_dark_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[94 + batch*level_coeff]}")
    ),
    
            # HIGH
    "curved_dark_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[78 + batch*level_coeff]}")
    ),
    
        # CHECKER TILES
            
            # LOW (NONE)
            
            # HIGH
    "high_checker_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[135 + batch*level_coeff]}")
    ),
    "high_checker_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[251 + batch*level_coeff]}")
    ),
    "high_checker_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[252 + batch*level_coeff]}")
    ),
    
    # -- LAVA TILES --
    "lava_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[142 + batch*level_coeff]}")
    ),
    "lava_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[143 + batch*level_coeff]}")
    ),
    "lava_waterfall_top": np.array(
        Image.open(f"{sprites_path}/{sprites[150 + batch*level_coeff]}")
    ),
    "lava_waterfall_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[155 + batch*level_coeff]}")
    ),
    "lava_classic_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[151 + batch*level_coeff]}")
    ),
    "lava_classic_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[152 + batch*level_coeff]}")
    ),
    "lava_classic_background_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[153 + batch*level_coeff]}")
    ),
    "lava_special_background": np.array(
        Image.open(f"{sprites_path}/{sprites[154 + batch*level_coeff]}")
    ),
    
    # -- RINGS --
    "top_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[112 + batch*level_coeff]}")
    ),
    "bottom_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[113 + batch*level_coeff]}")
    ),
    "top_left_and_bottom_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[114 + batch*level_coeff]}")
    ),
    "bottom_left_and_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[115 + batch*level_coeff]}")
    ),
    "top_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[116 + batch*level_coeff]}")
    ),
    "top_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[117 + batch*level_coeff]}")
    ),
    "bottom_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[118 + batch*level_coeff]}")
    ),
    "bottom_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[119 + batch*level_coeff]}")
    ),
    
    # -- SPRINGS --
    "spring_from_bottom_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[120 + batch*level_coeff]}")
    ),
    "spring_from_bottom_middle_dark_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[121 + batch*level_coeff]}")
    ),
    "spring_from_left_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[122 + batch*level_coeff]}")
    ),
    "spring_from_left_middle_dark_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[123 + batch*level_coeff]}")
    ),
    "spring_from_right_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[124 + batch*level_coeff]}")
    ),
    "spring_from_right_middle_dark_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[125 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[126 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left_dark_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[127 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[128 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right_dark_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[129 + batch*level_coeff]}")
    ),
    
    # -- SPIKES --
    "spike_from_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[130 + batch*level_coeff]}")
    ),
    "spike_from_bottom_dark_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[131 + batch*level_coeff]}")
    ),
    "spike_from_top": np.array(
        Image.open(f"{sprites_path}/{sprites[132 + batch*level_coeff]}")
    ),
    "spike_from_top_dark_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[133 + batch*level_coeff]}")
    ),
    
    # I'll assume it's something to block sonic.
    "blocking_thing": np.array(
        Image.open(f"{sprites_path}/{sprites[134 + batch*level_coeff]}")
    ),
    
    # -- CLOUDS --
    "cloud": np.array(Image.open(f"{sprites_path}/{sprites[145 + batch*level_coeff]}")),
    "cloud_left": np.array(
        Image.open(f"{sprites_path}/{sprites[146 + batch*level_coeff]}")
    ),
    "cloud_right": np.array(
        Image.open(f"{sprites_path}/{sprites[147 + batch*level_coeff]}")
    ),
    
    # -- BACKGROUND TILES --
    "rock_background_from_bottom_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[156 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[157 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[158 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[159 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[160 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[161 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[162 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[176 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v9": np.array(
        Image.open(f"{sprites_path}/{sprites[177 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v10": np.array(
        Image.open(f"{sprites_path}/{sprites[178 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v11": np.array(
        Image.open(f"{sprites_path}/{sprites[179 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v12": np.array(
        Image.open(f"{sprites_path}/{sprites[180 + batch*level_coeff]}")
    ),
    "rock_background_from_bottom_v13": np.array(
        Image.open(f"{sprites_path}/{sprites[181 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[163 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[164 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[165 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[166 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[167 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[168 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[169 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[170 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v9": np.array(
        Image.open(f"{sprites_path}/{sprites[171 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v10": np.array(
        Image.open(f"{sprites_path}/{sprites[172 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v11": np.array(
        Image.open(f"{sprites_path}/{sprites[173 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v12": np.array(
        Image.open(f"{sprites_path}/{sprites[174 + batch*level_coeff]}")
    ),
    "rock_background_from_top_v13": np.array(
        Image.open(f"{sprites_path}/{sprites[175 + batch*level_coeff]}")
    ),
    "dark_mountain_background_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[186 + batch*level_coeff]}")
    ),
    "dark_mountain_background_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[187 + batch*level_coeff]}")
    ),
    "dark_mountain_background_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[188 + batch*level_coeff]}")
    ),
    "dark_mountain_background_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[189 + batch*level_coeff]}")
    ),
    "dark_mountain_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[190 + batch*level_coeff]}")
    ),
    "dark_mountain_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[191 + batch*level_coeff]}")
    ),
    "dark_mountain_background_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[192 + batch*level_coeff]}")
    ),
    "classic_background_tile": np.array(
        Image.open(f"{sprites_path}/{sprites[193 + batch*level_coeff]}")
    ),
    
    "ondulations": np.array(
        Image.open(f"{sprites_path}/{sprites[253 + batch*level_coeff]}")
    ),
    
    "special_background_tile_vertical_left": np.array(
        Image.open(f"{sprites_path}/{sprites[200 + batch*level_coeff]}")
    ),
    "special_background_tile_vertical_right": np.array(
        Image.open(f"{sprites_path}/{sprites[201 + batch*level_coeff]}")
    ),
    "special_background_tile_vertical_middle_right": np.array(
        Image.open(f"{sprites_path}/{sprites[202 + batch*level_coeff]}")
    ),
    "special_background_tile_vertical_middle_left": np.array(
        Image.open(f"{sprites_path}/{sprites[203 + batch*level_coeff]}")
    ),
    "special_background_tile_triangle_from_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[204 + batch*level_coeff]}")
    ),
    "special_background_tile_triangle_from_top": np.array(
        Image.open(f"{sprites_path}/{sprites[205 + batch*level_coeff]}")
    ),
    "special_background_tile_triangles_from_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[206 + batch*level_coeff]}")
    ),
    "special_background_tile_triangles_from_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[207 + batch*level_coeff]}")
    ),
    "special_background_tile_curved_in_top_right_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[208 + batch*level_coeff]}")
    ),
    "special_background_tile_curved_in_top_left_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[209 + batch*level_coeff]}")
    ),
    "special_background_tile_curved_in_bottom_right_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[210 + batch*level_coeff]}")
    ),
    "special_background_tile_curved_in_bottom_left_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[211 + batch*level_coeff]}")
    ),
    "special_background_tile_curved_in_top_left_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[212 + batch*level_coeff]}")
    ),
    "special_background_tile_curved_in_top_right_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[213 + batch*level_coeff]}")
    ),
    "special_background_tile_curved_in_bottom_left_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[214 + batch*level_coeff]}")
    ),
    "special_background_tile_curved_in_bottom_right_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[215 + batch*level_coeff]}")
    ),
    "special_background_tile_triangle_from_bottom_left_to_top_right_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[216 + batch*level_coeff]}")
    ),
    "special_background_tile_triangle_from_top_left_to_bottom_right_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[217 + batch*level_coeff]}")
    ),
    "special_background_tile_triangle_from_top_left_to_bottom_right_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[218 + batch*level_coeff]}")
    ),
    "special_background_tile_triangle_from_bottom_left_to_top_right_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[219 + batch*level_coeff]}")
    ),
    "special_background_tile_ondulations_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[220 + batch*level_coeff]}")
    ),
    "special_background_tile_ondulations_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[221 + batch*level_coeff]}")
    ),
    "special_background_tile_ondulations_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[222 + batch*level_coeff]}")
    ),
    "special_background_tile_ondulations_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[223 + batch*level_coeff]}")
    ),
    "background_tile_1": np.array(
        Image.open(f"{sprites_path}/{sprites[7 + batch*level_coeff]}")
    ),
    "background_tile_2": np.array(
        Image.open(f"{sprites_path}/{sprites[8 + batch*level_coeff]}")
    ),
    "background_tile_3": np.array(
        Image.open(f"{sprites_path}/{sprites[9 + batch*level_coeff]}")
    ),
    "background_tile_4": np.array(
        Image.open(f"{sprites_path}/{sprites[10 + batch*level_coeff]}")
    ),
    "background_tile_5": np.array(
        Image.open(f"{sprites_path}/{sprites[11 + batch*level_coeff]}")
    ),
    "background_tile_6": np.array(
        Image.open(f"{sprites_path}/{sprites[12 + batch*level_coeff]}")
    ),
    "background_tile_7": np.array(
        Image.open(f"{sprites_path}/{sprites[23 + batch*level_coeff]}")
    ),
    "background_tile_8": np.array(
        Image.open(f"{sprites_path}/{sprites[24 + batch*level_coeff]}")
    ),
    "background_tile_9": np.array(
        Image.open(f"{sprites_path}/{sprites[25 + batch*level_coeff]}")
    ),
    "background_tile_10": np.array(
        Image.open(f"{sprites_path}/{sprites[26 + batch*level_coeff]}")
    ),
    "background_tile_11": np.array(
        Image.open(f"{sprites_path}/{sprites[27 + batch*level_coeff]}")
    ),
    "background_tile_12": np.array(
        Image.open(f"{sprites_path}/{sprites[28 + batch*level_coeff]}")
    ),
    "background_tile_13": np.array(
        Image.open(f"{sprites_path}/{sprites[32 + batch*level_coeff]}")
    ),
    "background_tile_14": np.array(
        Image.open(f"{sprites_path}/{sprites[41 + batch*level_coeff]}")
    ),
    "background_tile_15": np.array(
        Image.open(f"{sprites_path}/{sprites[63 + batch*level_coeff]}")
    ),
    "background_tile_16": np.array(
        Image.open(f"{sprites_path}/{sprites[71 + batch*level_coeff]}")
    ),
    "background_tile_17": np.array(
        Image.open(f"{sprites_path}/{sprites[72 + batch*level_coeff]}")
    ),
    "background_tile_18": np.array(
        Image.open(f"{sprites_path}/{sprites[73 + batch*level_coeff]}")
    ),
    "background_tile_19": np.array(
        Image.open(f"{sprites_path}/{sprites[74 + batch*level_coeff]}")
    ),
    "background_tile_20": np.array(
        Image.open(f"{sprites_path}/{sprites[75 + batch*level_coeff]}")
    ),
    "background_tile_21": np.array(
        Image.open(f"{sprites_path}/{sprites[76 + batch*level_coeff]}")
    ),
    "background_tile_22": np.array(
        Image.open(f"{sprites_path}/{sprites[87 + batch*level_coeff]}")
    ),
    "background_tile_23": np.array(
        Image.open(f"{sprites_path}/{sprites[88 + batch*level_coeff]}")
    ),
    "background_tile_24": np.array(
        Image.open(f"{sprites_path}/{sprites[89 + batch*level_coeff]}")
    ),
    "background_tile_25": np.array(
        Image.open(f"{sprites_path}/{sprites[90 + batch*level_coeff]}")
    ),
    "background_tile_26": np.array(
        Image.open(f"{sprites_path}/{sprites[91 + batch*level_coeff]}")
    ),
    "background_tile_27": np.array(
        Image.open(f"{sprites_path}/{sprites[92 + batch*level_coeff]}")
    ),
    "background_tile_28": np.array(
        Image.open(f"{sprites_path}/{sprites[96 + batch*level_coeff]}")
    ),
    "background_tile_29": np.array(
        Image.open(f"{sprites_path}/{sprites[97 + batch*level_coeff]}")
    ),
    "background_tile_30": np.array(
        Image.open(f"{sprites_path}/{sprites[98 + batch*level_coeff]}")
    ),
    "background_tile_31": np.array(
        Image.open(f"{sprites_path}/{sprites[99 + batch*level_coeff]}")
    ),
    "background_tile_32": np.array(
        Image.open(f"{sprites_path}/{sprites[100 + batch*level_coeff]}")
    ),
    "background_tile_33": np.array(
        Image.open(f"{sprites_path}/{sprites[101 + batch*level_coeff]}")
    ),
    "background_tile_34": np.array(
        Image.open(f"{sprites_path}/{sprites[102 + batch*level_coeff]}")
    ),
    "background_tile_35": np.array(
        Image.open(f"{sprites_path}/{sprites[103 + batch*level_coeff]}")
    ),
    "background_tile_36": np.array(
        Image.open(f"{sprites_path}/{sprites[104 + batch*level_coeff]}")
    ),
    "background_tile_37": np.array(
        Image.open(f"{sprites_path}/{sprites[105 + batch*level_coeff]}")
    ),
    "background_tile_38": np.array(
        Image.open(f"{sprites_path}/{sprites[106 + batch*level_coeff]}")
    ),
    "background_tile_39": np.array(
        Image.open(f"{sprites_path}/{sprites[107 + batch*level_coeff]}")
    ),
    "background_tile_40": np.array(
        Image.open(f"{sprites_path}/{sprites[108 + batch*level_coeff]}")
    ),
    "background_tile_41": np.array(
        Image.open(f"{sprites_path}/{sprites[109 + batch*level_coeff]}")
    ),
    "background_tile_42": np.array(
        Image.open(f"{sprites_path}/{sprites[110 + batch*level_coeff]}")
    ),
    "background_tile_43": np.array(
        Image.open(f"{sprites_path}/{sprites[111 + batch*level_coeff]}")
    ),
    "background_tile_44": np.array(
        Image.open(f"{sprites_path}/{sprites[136 + batch*level_coeff]}")
    ),
    "background_tile_45": np.array(
        Image.open(f"{sprites_path}/{sprites[137 + batch*level_coeff]}")
    ),
    "background_tile_46": np.array(
        Image.open(f"{sprites_path}/{sprites[138 + batch*level_coeff]}")
    ),
    "background_tile_47": np.array(
        Image.open(f"{sprites_path}/{sprites[144 + batch*level_coeff]}")
    ),
    "background_tile_48": np.array(
        Image.open(f"{sprites_path}/{sprites[148 + batch*level_coeff]}")
    ),
    "background_tile_49": np.array(
        Image.open(f"{sprites_path}/{sprites[149 + batch*level_coeff]}")
    ),
    "background_tile_50": np.array(
        Image.open(f"{sprites_path}/{sprites[182 + batch*level_coeff]}")
    ),
    "background_tile_51": np.array(
        Image.open(f"{sprites_path}/{sprites[183 + batch*level_coeff]}")
    ),
    "background_tile_52": np.array(
        Image.open(f"{sprites_path}/{sprites[184 + batch*level_coeff]}")
    ),
    "background_tile_53": np.array(
        Image.open(f"{sprites_path}/{sprites[185 + batch*level_coeff]}")
    ),
    "background_tile_54": np.array(
        Image.open(f"{sprites_path}/{sprites[194 + batch*level_coeff]}")
    ),
    "background_tile_55": np.array(
        Image.open(f"{sprites_path}/{sprites[195 + batch*level_coeff]}")
    ),
    "background_tile_56": np.array(
        Image.open(f"{sprites_path}/{sprites[196 + batch*level_coeff]}")
    ),
    "background_tile_57": np.array(
        Image.open(f"{sprites_path}/{sprites[197 + batch*level_coeff]}")
    ),
    "background_tile_58": np.array(
        Image.open(f"{sprites_path}/{sprites[198 + batch*level_coeff]}")
    ),
    "background_tile_59": np.array(
        Image.open(f"{sprites_path}/{sprites[199 + batch*level_coeff]}")
    ),
    "background_tile_60": np.array(
        Image.open(f"{sprites_path}/{sprites[224 + batch*level_coeff]}")
    ),
    "background_tile_61": np.array(
        Image.open(f"{sprites_path}/{sprites[225 + batch*level_coeff]}")
    ),
    "background_tile_62": np.array(
        Image.open(f"{sprites_path}/{sprites[226 + batch*level_coeff]}")
    ),
    "background_tile_63": np.array(
        Image.open(f"{sprites_path}/{sprites[227 + batch*level_coeff]}")
    ),
    "background_tile_64": np.array(
        Image.open(f"{sprites_path}/{sprites[228 + batch*level_coeff]}")
    ),
    "background_tile_65": np.array(
        Image.open(f"{sprites_path}/{sprites[229 + batch*level_coeff]}")
    ),
    "background_tile_66": np.array(
        Image.open(f"{sprites_path}/{sprites[230 + batch*level_coeff]}")
    ),
    "background_tile_67": np.array(
        Image.open(f"{sprites_path}/{sprites[231 + batch*level_coeff]}")
    ),
    "background_tile_68": np.array(
        Image.open(f"{sprites_path}/{sprites[232 + batch*level_coeff]}")
    ),
    "background_tile_69": np.array(
        Image.open(f"{sprites_path}/{sprites[233 + batch*level_coeff]}")
    ),
    "background_tile_70": np.array(
        Image.open(f"{sprites_path}/{sprites[234 + batch*level_coeff]}")
    ),
    "background_tile_71": np.array(
        Image.open(f"{sprites_path}/{sprites[235 + batch*level_coeff]}")
    ),
    "background_tile_72": np.array(
        Image.open(f"{sprites_path}/{sprites[236 + batch*level_coeff]}")
    ),
    "background_tile_73": np.array(
        Image.open(f"{sprites_path}/{sprites[237 + batch*level_coeff]}")
    ),
    "background_tile_74": np.array(
        Image.open(f"{sprites_path}/{sprites[238 + batch*level_coeff]}")
    ),
    "background_tile_75": np.array(
        Image.open(f"{sprites_path}/{sprites[239 + batch*level_coeff]}")
    ),
    "background_tile_76": np.array(
        Image.open(f"{sprites_path}/{sprites[240 + batch*level_coeff]}")
    ),
    "background_tile_77": np.array(
        Image.open(f"{sprites_path}/{sprites[241 + batch*level_coeff]}")
    ),
    "background_tile_78": np.array(
        Image.open(f"{sprites_path}/{sprites[242 + batch*level_coeff]}")
    ),
    "background_tile_79": np.array(
        Image.open(f"{sprites_path}/{sprites[243 + batch*level_coeff]}")
    ),
    "background_tile_80": np.array(
        Image.open(f"{sprites_path}/{sprites[244 + batch*level_coeff]}")
    ),
    "background_tile_81": np.array(
        Image.open(f"{sprites_path}/{sprites[245 + batch*level_coeff]}")
    ),
    "background_tile_82": np.array(
        Image.open(f"{sprites_path}/{sprites[246 + batch*level_coeff]}")
    ),
    "background_tile_83": np.array(
        Image.open(f"{sprites_path}/{sprites[247 + batch*level_coeff]}")
    ),
    "background_tile_84": np.array(
        Image.open(f"{sprites_path}/{sprites[248 + batch*level_coeff]}")
    ),
    "background_tile_85": np.array(
        Image.open(f"{sprites_path}/{sprites[249 + batch*level_coeff]}")
    ),
    "background_tile_86": np.array(
        Image.open(f"{sprites_path}/{sprites[250 + batch*level_coeff]}")
    ),
    "background_tile_87": np.array(
        Image.open(f"{sprites_path}/{sprites[254 + batch*level_coeff]}")
    ),
    "background_tile_88": np.array(
        Image.open(f"{sprites_path}/{sprites[255 + batch*level_coeff]}")
    ),
}

# -------------------------------------------- LEVEL 6

level_coeff = 5

level_6_sprites = {
    # -- INCLINED / SLOPE PIECES --
    
    # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[0 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[1 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[2 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[3 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[4 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[5 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[6 + batch*level_coeff]}")
    ),
    
    # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[16 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[17 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[18 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[19 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[20 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[21 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[22 + batch*level_coeff]}")
    ),
    
    # -- LOOP & CORNER PIECES --

    # RIGHT SIDE
    "loop_bottom_middle_right": np.array(
        Image.open(f"{sprites_path}/{sprites[7 + batch*level_coeff]}")
    ),
    "loop_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[8 + batch*level_coeff]}")
    ),
    "loop_right_middle_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[9 + batch*level_coeff]}")
    ),
    "loop_right_middle_top": np.array(
        Image.open(f"{sprites_path}/{sprites[10 + batch*level_coeff]}")
    ),
    "loop_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[11 + batch*level_coeff]}")
    ),
    "loop_top_middle_right": np.array(
        Image.open(f"{sprites_path}/{sprites[12 + batch*level_coeff]}")
    ),
    
    # LEFT SIDE
    "loop_bottom_middle_left": np.array(
        Image.open(f"{sprites_path}/{sprites[23 + batch*level_coeff]}")
    ),
    "loop_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[24 + batch*level_coeff]}")
    ),
    "loop_left_middle_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[25 + batch*level_coeff]}")
    ),
    "loop_left_middle_top": np.array(
        Image.open(f"{sprites_path}/{sprites[26 + batch*level_coeff]}")
    ),
    "loop_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[27 + batch*level_coeff]}")
    ),
    "loop_top_middle_left": np.array(
        Image.open(f"{sprites_path}/{sprites[28 + batch*level_coeff]}")
    ),
    
    # -- GROUND / RAINY GROUND / CHECKER TILES --
        
        # GROUND TILES
    
            # LOW
    "low_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[13 + batch*level_coeff]}")
    ),
    "low_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[15 + batch*level_coeff]}")
    ),
    "low_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[29 + batch*level_coeff]}")
    ),
    "low_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[31 + batch*level_coeff]}")
    ),
    "triangle_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[30 + batch*level_coeff]}")
    ),
            # HIGH
    "curved_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[14 + batch*level_coeff]}")
    ),
    "high_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[33 + batch*level_coeff]}")
    ),
    "high_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[34 + batch*level_coeff]}")
    ),
    "high_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[36 + batch*level_coeff]}")
    ),
    "high_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[47 + batch*level_coeff]}")
    ),
    "high_ground_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[97 + batch*level_coeff]}")
    ),
    "high_ground_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[98 + batch*level_coeff]}")
    ),
    "high_ground_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[100 + batch*level_coeff]}")
    ),
    "high_ground_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[111 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[37 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[39 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[41 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[42 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[38 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[40 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[43 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[44 + batch*level_coeff]}")
    ),
    
        # RAINY GROUND TILES
            
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_rain_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[64 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[65 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[66 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[67 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[68 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[69 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[70 + batch*level_coeff]}")
    ),
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_rain_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[80 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[81 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[82 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[83 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[84 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[85 + batch*level_coeff]}")
    ),
    "inclined_rain_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[86 + batch*level_coeff]}")
    ),
    
            # LOW
    "low_rain_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[77 + batch*level_coeff]}")
    ),
    "low_rain_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[79 + batch*level_coeff]}")
    ),
    "low_rain_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[93 + batch*level_coeff]}")
    ),
    "low_rain_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[95 + batch*level_coeff]}")
    ),
    "triangle_rain_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[94 + batch*level_coeff]}")
    ),
            # HIGH
    "curved_rain_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[78 + batch*level_coeff]}")
    ),
    
        # CHECKER TILES
            
            # LOW (None)
            
            # HIGH
    "high_checker_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[32 + batch*level_coeff]}")
    ),
    "high_checker_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[35 + batch*level_coeff]}")
    ),
    "high_checker_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[45 + batch*level_coeff]}")
    ),
    "high_checker_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[46 + batch*level_coeff]}")
    ),
    "high_checker_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[96 + batch*level_coeff]}")
    ),
    "high_checker_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[99 + batch*level_coeff]}")
    ),
    "high_checker_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[109 + batch*level_coeff]}")
    ),
    "high_checker_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[110 + batch*level_coeff]}")
    ),
    "high_checker_v9": np.array(
        Image.open(f"{sprites_path}/{sprites[135 + batch*level_coeff]}")
    ),
    "high_checker_v10": np.array(
        Image.open(f"{sprites_path}/{sprites[136 + batch*level_coeff]}")
    ),
    "high_checker_v11": np.array(
        Image.open(f"{sprites_path}/{sprites[137 + batch*level_coeff]}")
    ),
    "high_checker_v12": np.array(
        Image.open(f"{sprites_path}/{sprites[138 + batch*level_coeff]}")
    ),
    "high_checker_v13": np.array(
        Image.open(f"{sprites_path}/{sprites[178 + batch*level_coeff]}")
    ),
    "high_checker_v14": np.array(
        Image.open(f"{sprites_path}/{sprites[179 + batch*level_coeff]}")
    ),
    "high_checker_v15": np.array(
        Image.open(f"{sprites_path}/{sprites[180 + batch*level_coeff]}")
    ),
    "high_checker_v16": np.array(
        Image.open(f"{sprites_path}/{sprites[181 + batch*level_coeff]}")
    ),
    "high_checker_v17": np.array(
        Image.open(f"{sprites_path}/{sprites[182 + batch*level_coeff]}")
    ),
    "high_checker_v18": np.array(
        Image.open(f"{sprites_path}/{sprites[183 + batch*level_coeff]}")
    ),
    "high_checker_v19": np.array(
        Image.open(f"{sprites_path}/{sprites[184 + batch*level_coeff]}")
    ),
    "high_checker_v20": np.array(
        Image.open(f"{sprites_path}/{sprites[185 + batch*level_coeff]}")
    ),
    "high_checker_v21": np.array(
        Image.open(f"{sprites_path}/{sprites[186 + batch*level_coeff]}")
    ),
    "high_checker_v22": np.array(
        Image.open(f"{sprites_path}/{sprites[251 + batch*level_coeff]}")
    ),
    "high_checker_v23": np.array(
        Image.open(f"{sprites_path}/{sprites[252 + batch*level_coeff]}")
    ),
    
    # -- CLIMATE, TREE & PLANT --
    "little_rain_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[142 + batch*level_coeff]}")
    ),
    "middle_rain_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[143 + batch*level_coeff]}")
    ),
    "large_rain_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[144 + batch*level_coeff]}")
    ),
    "little_rain_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[145 + batch*level_coeff]}")
    ),
    "middle_rain_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[146 + batch*level_coeff]}")
    ),
    "large_rain_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[147 + batch*level_coeff]}")
    ),
    "rain_column_left": np.array(
        Image.open(f"{sprites_path}/{sprites[148 + batch*level_coeff]}")
    ),
    "rain_column_right": np.array(
        Image.open(f"{sprites_path}/{sprites[149 + batch*level_coeff]}")
    ),
    "waterfall_top": np.array(
        Image.open(f"{sprites_path}/{sprites[187 + batch*level_coeff]}")
    ),
    "waterfall_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[188 + batch*level_coeff]}")
    ),
    "tree_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[189 + batch*level_coeff]}")
    ),
    "tree_top_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[190 + batch*level_coeff]}")
    ),
    "tree_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[191 + batch*level_coeff]}")
    ),
    "tree_trunk": np.array(
        Image.open(f"{sprites_path}/{sprites[192 + batch*level_coeff]}")
    ),
    "thunder_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[197 + batch*level_coeff]}")
    ),
    "thunder_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[198 + batch*level_coeff]}")
    ),
    "plant_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[193 + batch*level_coeff]}")
    ),
    "plant_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[194 + batch*level_coeff]}")
    ),
    "two_plants": np.array(
        Image.open(f"{sprites_path}/{sprites[195 + batch*level_coeff]}")
    ),
    
    # -- RINGS --
    "top_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[112 + batch*level_coeff]}")
    ),
    "bottom_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[113 + batch*level_coeff]}")
    ),
    "top_left_and_bottom_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[114 + batch*level_coeff]}")
    ),
    "bottom_left_and_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[115 + batch*level_coeff]}")
    ),
    "top_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[116 + batch*level_coeff]}")
    ),
    "top_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[117 + batch*level_coeff]}")
    ),
    "bottom_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[118 + batch*level_coeff]}")
    ),
    "bottom_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[119 + batch*level_coeff]}")
    ),
    
    # -- SPRINGS --
    "spring_from_bottom_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[120 + batch*level_coeff]}")
    ),
    "spring_from_bottom_middle_rain_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[121 + batch*level_coeff]}")
    ),
    "spring_from_left_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[122 + batch*level_coeff]}")
    ),
    "spring_from_left_middle_rain_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[123 + batch*level_coeff]}")
    ),
    "spring_from_right_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[124 + batch*level_coeff]}")
    ),
    "spring_from_right_middle_rain_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[125 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[126 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left_rain_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[127 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[128 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right_rain_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[129 + batch*level_coeff]}")
    ),
    
    # -- SPIKES --
    "spike_from_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[130 + batch*level_coeff]}")
    ),
    "spike_from_bottom_rain_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[131 + batch*level_coeff]}")
    ),
    "spike_from_top": np.array(
        Image.open(f"{sprites_path}/{sprites[132 + batch*level_coeff]}")
    ),
    "spike_from_top_rain_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[133 + batch*level_coeff]}")
    ),
    
    # I'll assume it's something to block sonic.
    "blocking_thing": np.array(
        Image.open(f"{sprites_path}/{sprites[134 + batch*level_coeff]}")
    ),
    
    # -- BRIDGE PIECES --
    "bridge_support_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[237 + batch*level_coeff]}")
    ),
    "bridge_support_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[238 + batch*level_coeff]}")
    ),
    "bridge_two_top_supports": np.array(
        Image.open(f"{sprites_path}/{sprites[239 + batch*level_coeff]}")
    ),
    
    # -- BACKGROUND TILES --
    "background_special_v1_1": np.array(
        Image.open(f"{sprites_path}/{sprites[150 + batch*level_coeff]}")
    ),
    "background_special_v1_2": np.array(
        Image.open(f"{sprites_path}/{sprites[151 + batch*level_coeff]}")
    ),
    "background_special_v1_3": np.array(
        Image.open(f"{sprites_path}/{sprites[152 + batch*level_coeff]}")
    ),
    "background_special_v1_4": np.array(
        Image.open(f"{sprites_path}/{sprites[153 + batch*level_coeff]}")
    ),
    "background_special_v2_1": np.array(
        Image.open(f"{sprites_path}/{sprites[154 + batch*level_coeff]}")
    ),
    "background_special_v2_2": np.array(
        Image.open(f"{sprites_path}/{sprites[155 + batch*level_coeff]}")
    ),
    "background_special_v2_3": np.array(
        Image.open(f"{sprites_path}/{sprites[156 + batch*level_coeff]}")
    ),
    "background_special_v2_4": np.array(
        Image.open(f"{sprites_path}/{sprites[157 + batch*level_coeff]}")
    ),
    "background_special_v2_5": np.array(
        Image.open(f"{sprites_path}/{sprites[158 + batch*level_coeff]}")
    ),
    "background_special_v2_6": np.array(
        Image.open(f"{sprites_path}/{sprites[159 + batch*level_coeff]}")
    ),
    "background_special_v2_7": np.array(
        Image.open(f"{sprites_path}/{sprites[160 + batch*level_coeff]}")
    ),
    "background_special_v2_8": np.array(
        Image.open(f"{sprites_path}/{sprites[161 + batch*level_coeff]}")
    ),
    "background_special_v2_9": np.array(
        Image.open(f"{sprites_path}/{sprites[162 + batch*level_coeff]}")
    ),
    "background_special_v2_10": np.array(
        Image.open(f"{sprites_path}/{sprites[163 + batch*level_coeff]}")
    ),
    "background_special_v2_11": np.array(
        Image.open(f"{sprites_path}/{sprites[164 + batch*level_coeff]}")
    ),
    "background_special_v2_12": np.array(
        Image.open(f"{sprites_path}/{sprites[165 + batch*level_coeff]}")
    ),
    "background_special_v2_13": np.array(
        Image.open(f"{sprites_path}/{sprites[166 + batch*level_coeff]}")
    ),
    "background_special_v2_14": np.array(
        Image.open(f"{sprites_path}/{sprites[168 + batch*level_coeff]}")
    ),
    "background_special_v2_15": np.array(
        Image.open(f"{sprites_path}/{sprites[171 + batch*level_coeff]}")
    ),
    "background_special_v2_16": np.array(
        Image.open(f"{sprites_path}/{sprites[172 + batch*level_coeff]}")
    ),
    "background_special_v2_17": np.array(
        Image.open(f"{sprites_path}/{sprites[173 + batch*level_coeff]}")
    ),
    "background_special_v2_18": np.array(
        Image.open(f"{sprites_path}/{sprites[174 + batch*level_coeff]}")
    ),
    "background_rain_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[139 + batch*level_coeff]}")
    ),
    "background_rain_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[140 + batch*level_coeff]}")
    ),
    "background_rain_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[141 + batch*level_coeff]}")
    ),
    "background_rain_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[167 + batch*level_coeff]}")
    ),
    "background_rain_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[169 + batch*level_coeff]}")
    ),
    "background_rain_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[170 + batch*level_coeff]}")
    ),
    "background_rain_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[175 + batch*level_coeff]}")
    ),
    "background_rain_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[176 + batch*level_coeff]}")
    ),
    "background_rain_v9": np.array(
        Image.open(f"{sprites_path}/{sprites[177 + batch*level_coeff]}")
    ),
    "background_rain_v10": np.array(
        Image.open(f"{sprites_path}/{sprites[196 + batch*level_coeff]}")
    ),
    "background_rain_v11": np.array(
        Image.open(f"{sprites_path}/{sprites[199 + batch*level_coeff]}")
    ),
    
    "vertical_lines": np.array(
        Image.open(f"{sprites_path}/{sprites[253 + batch*level_coeff]}")
    ),

    "background_tile_1": np.array(
        Image.open(f"{sprites_path}/{sprites[48 + batch*level_coeff]}")
    ),
    "background_tile_2": np.array(
        Image.open(f"{sprites_path}/{sprites[49 + batch*level_coeff]}")
    ),
    "background_tile_3": np.array(
        Image.open(f"{sprites_path}/{sprites[50 + batch*level_coeff]}")
    ),
    "background_tile_4": np.array(
        Image.open(f"{sprites_path}/{sprites[51 + batch*level_coeff]}")
    ),
    "background_tile_5": np.array(
        Image.open(f"{sprites_path}/{sprites[52 + batch*level_coeff]}")
    ),
    "background_tile_6": np.array(
        Image.open(f"{sprites_path}/{sprites[53 + batch*level_coeff]}")
    ),
    "background_tile_7": np.array(
        Image.open(f"{sprites_path}/{sprites[54 + batch*level_coeff]}")
    ),
    "background_tile_8": np.array(
        Image.open(f"{sprites_path}/{sprites[55 + batch*level_coeff]}")
    ),
    "background_tile_9": np.array(
        Image.open(f"{sprites_path}/{sprites[56 + batch*level_coeff]}")
    ),
    "background_tile_10": np.array(
        Image.open(f"{sprites_path}/{sprites[57 + batch*level_coeff]}")
    ),
    "background_tile_11": np.array(
        Image.open(f"{sprites_path}/{sprites[58 + batch*level_coeff]}")
    ),
    "background_tile_12": np.array(
        Image.open(f"{sprites_path}/{sprites[59 + batch*level_coeff]}")
    ),
    "background_tile_13": np.array(
        Image.open(f"{sprites_path}/{sprites[60 + batch*level_coeff]}")
    ),
    "background_tile_14": np.array(
        Image.open(f"{sprites_path}/{sprites[61 + batch*level_coeff]}")
    ),
    "background_tile_15": np.array(
        Image.open(f"{sprites_path}/{sprites[62 + batch*level_coeff]}")
    ),
    "background_tile_16": np.array(
        Image.open(f"{sprites_path}/{sprites[63 + batch*level_coeff]}")
    ),
    "background_tile_17": np.array(
        Image.open(f"{sprites_path}/{sprites[71 + batch*level_coeff]}")
    ),
    "background_tile_18": np.array(
        Image.open(f"{sprites_path}/{sprites[72 + batch*level_coeff]}")
    ),
    "background_tile_19": np.array(
        Image.open(f"{sprites_path}/{sprites[73 + batch*level_coeff]}")
    ),
    "background_tile_20": np.array(
        Image.open(f"{sprites_path}/{sprites[74 + batch*level_coeff]}")
    ),
    "background_tile_21": np.array(
        Image.open(f"{sprites_path}/{sprites[75 + batch*level_coeff]}")
    ),
    "background_tile_22": np.array(
        Image.open(f"{sprites_path}/{sprites[76 + batch*level_coeff]}")
    ),
    "background_tile_23": np.array(
        Image.open(f"{sprites_path}/{sprites[87 + batch*level_coeff]}")
    ),
    "background_tile_24": np.array(
        Image.open(f"{sprites_path}/{sprites[88 + batch*level_coeff]}")
    ),
    "background_tile_25": np.array(
        Image.open(f"{sprites_path}/{sprites[89 + batch*level_coeff]}")
    ),
    "background_tile_26": np.array(
        Image.open(f"{sprites_path}/{sprites[90 + batch*level_coeff]}")
    ),
    "background_tile_27": np.array(
        Image.open(f"{sprites_path}/{sprites[91 + batch*level_coeff]}")
    ),
    "background_tile_28": np.array(
        Image.open(f"{sprites_path}/{sprites[92 + batch*level_coeff]}")
    ),
    "background_tile_29": np.array(
        Image.open(f"{sprites_path}/{sprites[101 + batch*level_coeff]}")
    ),
    "background_tile_30": np.array(
        Image.open(f"{sprites_path}/{sprites[102 + batch*level_coeff]}")
    ),
    "background_tile_31": np.array(
        Image.open(f"{sprites_path}/{sprites[103 + batch*level_coeff]}")
    ),
    "background_tile_32": np.array(
        Image.open(f"{sprites_path}/{sprites[104 + batch*level_coeff]}")
    ),
    "background_tile_33": np.array(
        Image.open(f"{sprites_path}/{sprites[105 + batch*level_coeff]}")
    ),
    "background_tile_34": np.array(
        Image.open(f"{sprites_path}/{sprites[106 + batch*level_coeff]}")
    ),
    "background_tile_35": np.array(
        Image.open(f"{sprites_path}/{sprites[107 + batch*level_coeff]}")
    ),
    "background_tile_36": np.array(
        Image.open(f"{sprites_path}/{sprites[108 + batch*level_coeff]}")
    ),
    "background_tile_37": np.array(
        Image.open(f"{sprites_path}/{sprites[200 + batch*level_coeff]}")
    ),
    "background_tile_38": np.array(
        Image.open(f"{sprites_path}/{sprites[201 + batch*level_coeff]}")
    ),
    "background_tile_39": np.array(
        Image.open(f"{sprites_path}/{sprites[202 + batch*level_coeff]}")
    ),
    "background_tile_40": np.array(
        Image.open(f"{sprites_path}/{sprites[203 + batch*level_coeff]}")
    ),
    "background_tile_41": np.array(
        Image.open(f"{sprites_path}/{sprites[204 + batch*level_coeff]}")
    ),
    "background_tile_42": np.array(
        Image.open(f"{sprites_path}/{sprites[205 + batch*level_coeff]}")
    ),
    "background_tile_43": np.array(
        Image.open(f"{sprites_path}/{sprites[206 + batch*level_coeff]}")
    ),
    "background_tile_44": np.array(
        Image.open(f"{sprites_path}/{sprites[207 + batch*level_coeff]}")
    ),
    "background_tile_45": np.array(
        Image.open(f"{sprites_path}/{sprites[208 + batch*level_coeff]}")
    ),
    "background_tile_46": np.array(
        Image.open(f"{sprites_path}/{sprites[209 + batch*level_coeff]}")
    ),
    "background_tile_47": np.array(
        Image.open(f"{sprites_path}/{sprites[210 + batch*level_coeff]}")
    ),
    "background_tile_48": np.array(
        Image.open(f"{sprites_path}/{sprites[211 + batch*level_coeff]}")
    ),
    "background_tile_49": np.array(
        Image.open(f"{sprites_path}/{sprites[212 + batch*level_coeff]}")
    ),
    "background_tile_50": np.array(
        Image.open(f"{sprites_path}/{sprites[213 + batch*level_coeff]}")
    ),
    "background_tile_51": np.array(
        Image.open(f"{sprites_path}/{sprites[214 + batch*level_coeff]}")
    ),
    "background_tile_52": np.array(
        Image.open(f"{sprites_path}/{sprites[215 + batch*level_coeff]}")
    ),
    "background_tile_53": np.array(
        Image.open(f"{sprites_path}/{sprites[216 + batch*level_coeff]}")
    ),
    "background_tile_54": np.array(
        Image.open(f"{sprites_path}/{sprites[217 + batch*level_coeff]}")
    ),
    "background_tile_55": np.array(
        Image.open(f"{sprites_path}/{sprites[218 + batch*level_coeff]}")
    ),
    "background_tile_56": np.array(
        Image.open(f"{sprites_path}/{sprites[219 + batch*level_coeff]}")
    ),
    "background_tile_57": np.array(
        Image.open(f"{sprites_path}/{sprites[220 + batch*level_coeff]}")
    ),
    "background_tile_58": np.array(
        Image.open(f"{sprites_path}/{sprites[221 + batch*level_coeff]}")
    ),
    "background_tile_59": np.array(
        Image.open(f"{sprites_path}/{sprites[222 + batch*level_coeff]}")
    ),
    "background_tile_60": np.array(
        Image.open(f"{sprites_path}/{sprites[223 + batch*level_coeff]}")
    ),
    "background_tile_61": np.array(
        Image.open(f"{sprites_path}/{sprites[224 + batch*level_coeff]}")
    ),
    "background_tile_62": np.array(
        Image.open(f"{sprites_path}/{sprites[225 + batch*level_coeff]}")
    ),
    "background_tile_63": np.array(
        Image.open(f"{sprites_path}/{sprites[226 + batch*level_coeff]}")
    ),
    "background_tile_64": np.array(
        Image.open(f"{sprites_path}/{sprites[227 + batch*level_coeff]}")
    ),
    "background_tile_65": np.array(
        Image.open(f"{sprites_path}/{sprites[228 + batch*level_coeff]}")
    ),
    "background_tile_66": np.array(
        Image.open(f"{sprites_path}/{sprites[229 + batch*level_coeff]}")
    ),
    "background_tile_67": np.array(
        Image.open(f"{sprites_path}/{sprites[230 + batch*level_coeff]}")
    ),
    "background_tile_68": np.array(
        Image.open(f"{sprites_path}/{sprites[231 + batch*level_coeff]}")
    ),
    "background_tile_69": np.array(
        Image.open(f"{sprites_path}/{sprites[232 + batch*level_coeff]}")
    ),
    "background_tile_70": np.array(
        Image.open(f"{sprites_path}/{sprites[233 + batch*level_coeff]}")
    ),
    "background_tile_71": np.array(
        Image.open(f"{sprites_path}/{sprites[234 + batch*level_coeff]}")
    ),
    "background_tile_72": np.array(
        Image.open(f"{sprites_path}/{sprites[235 + batch*level_coeff]}")
    ),
    "background_tile_73": np.array(
        Image.open(f"{sprites_path}/{sprites[236 + batch*level_coeff]}")
    ),
    "background_tile_74": np.array(
        Image.open(f"{sprites_path}/{sprites[240 + batch*level_coeff]}")
    ),
    "background_tile_75": np.array(
        Image.open(f"{sprites_path}/{sprites[241 + batch*level_coeff]}")
    ),
    "background_tile_76": np.array(
        Image.open(f"{sprites_path}/{sprites[242 + batch*level_coeff]}")
    ),
    "background_tile_77": np.array(
        Image.open(f"{sprites_path}/{sprites[243 + batch*level_coeff]}")
    ),
    "background_tile_78": np.array(
        Image.open(f"{sprites_path}/{sprites[244 + batch*level_coeff]}")
    ),
    "background_tile_79": np.array(
        Image.open(f"{sprites_path}/{sprites[245 + batch*level_coeff]}")
    ),
    "background_tile_80": np.array(
        Image.open(f"{sprites_path}/{sprites[246 + batch*level_coeff]}")
    ),
    "background_tile_81": np.array(
        Image.open(f"{sprites_path}/{sprites[247 + batch*level_coeff]}")
    ),
    "background_tile_82": np.array(
        Image.open(f"{sprites_path}/{sprites[248 + batch*level_coeff]}")
    ),
    "background_tile_83": np.array(
        Image.open(f"{sprites_path}/{sprites[249 + batch*level_coeff]}")
    ),
    "background_tile_84": np.array(
        Image.open(f"{sprites_path}/{sprites[250 + batch*level_coeff]}")
    ),
    "background_tile_85": np.array(
        Image.open(f"{sprites_path}/{sprites[254 + batch*level_coeff]}")
    ),
    "background_tile_86": np.array(
        Image.open(f"{sprites_path}/{sprites[255 + batch*level_coeff]}")
    ),
}

# -------------------------------------------- LEVEL 7

level_coeff = 6

level_7_sprites = {
    # -- INCLINED / SLOPE PIECES --
    
    # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[0 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[1 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[2 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[3 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[4 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[5 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[6 + batch*level_coeff]}")
    ),
    
    # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[16 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[17 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[18 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[19 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[20 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[21 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[22 + batch*level_coeff]}")
    ),
    
    # -- LOOP & CORNER PIECES -- (None)
    
    # -- GROUND / IRON GROUND / CHECKER TILES --
        
        # GROUND TILES
            
            # LOW
    "low_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[13 + batch*level_coeff]}")
    ),
    "low_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[15 + batch*level_coeff]}")
    ),
    "low_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[29 + batch*level_coeff]}")
    ),
    "low_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[31 + batch*level_coeff]}")
    ),
    "triangle_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[30 + batch*level_coeff]}")
    ),
            # HIGH
    "curved_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[14 + batch*level_coeff]}")
    ),
    "high_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[33 + batch*level_coeff]}")
    ),
    "high_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[34 + batch*level_coeff]}")
    ),
    "high_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[36 + batch*level_coeff]}")
    ),
    "high_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[47 + batch*level_coeff]}")
    ),
    "high_ground_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[97 + batch*level_coeff]}")
    ),
    "high_ground_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[98 + batch*level_coeff]}")
    ),
    "high_ground_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[100 + batch*level_coeff]}")
    ),
    "high_ground_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[111 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[37 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[39 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[41 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[42 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[38 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[40 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[43 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[44 + batch*level_coeff]}")
    ),
    
        # IRON GROUND TILES
            
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_iron_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[64 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[65 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[66 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[67 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[68 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[69 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[70 + batch*level_coeff]}")
    ),
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_iron_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[80 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[81 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[82 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[83 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[84 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[85 + batch*level_coeff]}")
    ),
    "inclined_iron_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[86 + batch*level_coeff]}")
    ),
    
            # LOW
    "low_iron_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[77 + batch*level_coeff]}")
    ),
    "low_iron_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[79 + batch*level_coeff]}")
    ),
    "low_iron_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[93 + batch*level_coeff]}")
    ),
    "low_iron_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[95 + batch*level_coeff]}")
    ),
    "triangle_iron_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[94 + batch*level_coeff]}")
    ),
            
            # HIGH
    "curved_iron_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[78 + batch*level_coeff]}")
    ),
    
        # CHECKER TILES
            
            # LOW
    "low_checker_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[148 + batch*level_coeff]}")
    ),
    "low_checker_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[149 + batch*level_coeff]}")
    ),
            
            # HIGH
    "high_checker_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[32 + batch*level_coeff]}")
    ),
    "high_checker_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[35 + batch*level_coeff]}")
    ),
    "high_checker_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[45 + batch*level_coeff]}")
    ),
    "high_checker_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[46 + batch*level_coeff]}")
    ),
    "high_checker_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[96 + batch*level_coeff]}")
    ),
    "high_checker_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[99 + batch*level_coeff]}")
    ),
    "high_checker_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[109 + batch*level_coeff]}")
    ),
    "high_checker_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[110 + batch*level_coeff]}")
    ),
    "high_checker_v9": np.array(
        Image.open(f"{sprites_path}/{sprites[135 + batch*level_coeff]}")
    ),
    "high_checker_v10": np.array(
        Image.open(f"{sprites_path}/{sprites[150 + batch*level_coeff]}")
    ),
    "high_checker_v11": np.array(
        Image.open(f"{sprites_path}/{sprites[151 + batch*level_coeff]}")
    ),
    "high_checker_v12": np.array(
        Image.open(f"{sprites_path}/{sprites[152 + batch*level_coeff]}")
    ),
    "high_checker_v13": np.array(
        Image.open(f"{sprites_path}/{sprites[153 + batch*level_coeff]}")
    ),
    "high_checker_v14": np.array(
        Image.open(f"{sprites_path}/{sprites[154 + batch*level_coeff]}")
    ),
    "high_checker_v15": np.array(
        Image.open(f"{sprites_path}/{sprites[180 + batch*level_coeff]}")
    ),
    "high_checker_v16": np.array(
        Image.open(f"{sprites_path}/{sprites[181 + batch*level_coeff]}")
    ),
    "high_checker_v17": np.array(
        Image.open(f"{sprites_path}/{sprites[182 + batch*level_coeff]}")
    ),
    "high_checker_v18": np.array(
        Image.open(f"{sprites_path}/{sprites[183 + batch*level_coeff]}")
    ),
    "high_checker_v19": np.array(
        Image.open(f"{sprites_path}/{sprites[184 + batch*level_coeff]}")
    ),
    "high_checker_v20": np.array(
        Image.open(f"{sprites_path}/{sprites[185 + batch*level_coeff]}")
    ),
    "high_checker_v21": np.array(
        Image.open(f"{sprites_path}/{sprites[186 + batch*level_coeff]}")
    ),
    "high_checker_v22": np.array(
        Image.open(f"{sprites_path}/{sprites[187 + batch*level_coeff]}")
    ),
    "high_checker_v23": np.array(
        Image.open(f"{sprites_path}/{sprites[188 + batch*level_coeff]}")
    ),
    "high_checker_v24": np.array(
        Image.open(f"{sprites_path}/{sprites[189 + batch*level_coeff]}")
    ),
    "high_checker_v25": np.array(
        Image.open(f"{sprites_path}/{sprites[190 + batch*level_coeff]}")
    ),
    "high_checker_v26": np.array(
        Image.open(f"{sprites_path}/{sprites[191 + batch*level_coeff]}")
    ),
    "high_checker_v27": np.array(
        Image.open(f"{sprites_path}/{sprites[192 + batch*level_coeff]}")
    ),
    "high_checker_v28": np.array(
        Image.open(f"{sprites_path}/{sprites[193 + batch*level_coeff]}")
    ),
    "high_checker_v29": np.array(
        Image.open(f"{sprites_path}/{sprites[194 + batch*level_coeff]}")
    ),
    "high_checker_v30": np.array(
        Image.open(f"{sprites_path}/{sprites[251 + batch*level_coeff]}")
    ),
    "high_checker_v31": np.array(
        Image.open(f"{sprites_path}/{sprites[252 + batch*level_coeff]}")
    ),
    # -- SAW, BEAR & CHAINS --
    "saw_top_left_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[200 + batch*level_coeff]}")
    ),
    "saw_bottom_left_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[201 + batch*level_coeff]}")
    ),
    "saw_top_right_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[202 + batch*level_coeff]}")
    ),
    "saw_bottom_right_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[203 + batch*level_coeff]}")
    ),
    "saw_top_left_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[204 + batch*level_coeff]}")
    ),
    "saw_bottom_left_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[205 + batch*level_coeff]}")
    ),
    "saw_top_right_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[206 + batch*level_coeff]}")
    ),
    "saw_bottom_right_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[207 + batch*level_coeff]}")
    ),
    "little_bear": np.array(
        Image.open(f"{sprites_path}/{sprites[155 + batch*level_coeff]}")
    ),
    "big_bear": np.array(
        Image.open(f"{sprites_path}/{sprites[156 + batch*level_coeff]}")
    ),
    "two_bear": np.array(
        Image.open(f"{sprites_path}/{sprites[171 + batch*level_coeff]}")
    ),
    "big_bear_left": np.array(
        Image.open(f"{sprites_path}/{sprites[172 + batch*level_coeff]}")
    ),
    "big_bear_right": np.array(
        Image.open(f"{sprites_path}/{sprites[173 + batch*level_coeff]}")
    ),
    "chains_top_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[208 + batch*level_coeff]}")
    ),
    "chains_bottom_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[209 + batch*level_coeff]}")
    ),
    "chains_bottom_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[210 + batch*level_coeff]}")
    ),
    "chains_top_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[211 + batch*level_coeff]}")
    ),
    "chains_body_v2_1": np.array(
        Image.open(f"{sprites_path}/{sprites[212 + batch*level_coeff]}")
    ),
    "chains_body_v2_2": np.array(
        Image.open(f"{sprites_path}/{sprites[213 + batch*level_coeff]}")
    ),
    "chains_bottom_v2_2": np.array(
        Image.open(f"{sprites_path}/{sprites[214 + batch*level_coeff]}")
    ),
    "spinning_chains_p1_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[237 + batch*level_coeff]}")
    ),
    "spinning_chains_p2_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[238 + batch*level_coeff]}")
    ),
    "spinning_chains_p3_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[239 + batch*level_coeff]}")
    ),
    "spinning_chains_p4_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[240 + batch*level_coeff]}")
    ),
    "spinning_chains_p1_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[241 + batch*level_coeff]}")
    ),
    "spinning_chains_p2_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[242 + batch*level_coeff]}")
    ),
    "spinning_chains_p3_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[243 + batch*level_coeff]}")
    ),
    "spinning_chains_p4_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[244 + batch*level_coeff]}")
    ),
    
    # -- RINGS --
    "top_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[112 + batch*level_coeff]}")
    ),
    "bottom_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[113 + batch*level_coeff]}")
    ),
    "top_left_and_bottom_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[114 + batch*level_coeff]}")
    ),
    "bottom_left_and_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[115 + batch*level_coeff]}")
    ),
    "top_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[116 + batch*level_coeff]}")
    ),
    "top_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[117 + batch*level_coeff]}")
    ),
    "bottom_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[118 + batch*level_coeff]}")
    ),
    "bottom_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[119 + batch*level_coeff]}")
    ),
    
    # -- SPRINGS --
    "spring_from_bottom_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[120 + batch*level_coeff]}")
    ),
    "spring_from_bottom_middle_iron_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[121 + batch*level_coeff]}")
    ),
    "spring_from_left_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[122 + batch*level_coeff]}")
    ),
    "spring_from_left_middle_iron_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[123 + batch*level_coeff]}")
    ),
    "spring_from_right_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[124 + batch*level_coeff]}")
    ),
    "spring_from_right_middle_iron_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[125 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[126 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left_iron_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[127 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[128 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right_iron_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[129 + batch*level_coeff]}")
    ),
    
    # -- SPIKES --
    "spike_from_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[130 + batch*level_coeff]}")
    ),
    "spike_from_bottom_iron_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[131 + batch*level_coeff]}")
    ),
    "spike_from_top": np.array(
        Image.open(f"{sprites_path}/{sprites[132 + batch*level_coeff]}")
    ),
    "spike_from_top_iron_rock_background": np.array(
        Image.open(f"{sprites_path}/{sprites[133 + batch*level_coeff]}")
    ),
    
    # I'll assume it's something to block sonic.
    "blocking_thing": np.array(
        Image.open(f"{sprites_path}/{sprites[134 + batch*level_coeff]}")
    ),
    
    # -- CLOUDS --
    "cloud": np.array(Image.open(f"{sprites_path}/{sprites[144 + batch*level_coeff]}")),
    "cloud_left": np.array(
        Image.open(f"{sprites_path}/{sprites[145 + batch*level_coeff]}")
    ),
    "cloud_right": np.array(
        Image.open(f"{sprites_path}/{sprites[146 + batch*level_coeff]}")
    ),
    
    # -- BACKGROUND TILES --
    "checker_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[147 + batch*level_coeff]}")
    ),
    "checker_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[148 + batch*level_coeff]}")
    ),
    "checker_background_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[149 + batch*level_coeff]}")
    ),
    "checker_background_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[215 + batch*level_coeff]}")
    ),
    "checker_background_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[216 + batch*level_coeff]}")
    ),
    "checker_background_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[217 + batch*level_coeff]}")
    ),
    "industrial_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[159 + batch*level_coeff]}")
    ),
    "industrial_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[160 + batch*level_coeff]}")
    ),
    "industrial_background_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[161 + batch*level_coeff]}")
    ),
    "industrial_background_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[162 + batch*level_coeff]}")
    ),
    "industrial_background_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[164 + batch*level_coeff]}")
    ),
    "industrial_background_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[165 + batch*level_coeff]}")
    ),
    "industrial_background_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[166 + batch*level_coeff]}")
    ),
    "industrial_background_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[167 + batch*level_coeff]}")
    ),
    "industrial_background_v9": np.array(
        Image.open(f"{sprites_path}/{sprites[168 + batch*level_coeff]}")
    ),
    "industrial_background_v10": np.array(
        Image.open(f"{sprites_path}/{sprites[169 + batch*level_coeff]}")
    ),
    "industrial_background_v11": np.array(
        Image.open(f"{sprites_path}/{sprites[170 + batch*level_coeff]}")
    ),
    "industrial_background_v12": np.array(
        Image.open(f"{sprites_path}/{sprites[178 + batch*level_coeff]}")
    ),
    "industrial_background_v13": np.array(
        Image.open(f"{sprites_path}/{sprites[179 + batch*level_coeff]}")
    ),
    "tower_background_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[195 + batch*level_coeff]}")
    ),
    "tower_background_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[196 + batch*level_coeff]}")
    ),
    "tower_background_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[197 + batch*level_coeff]}")
    ),
    "tower_background_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[198 + batch*level_coeff]}")
    ),
    "tower_background_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[199 + batch*level_coeff]}")
    ),
    "background_special_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[157 + batch*level_coeff]}")
    ),
    "background_special_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[158 + batch*level_coeff]}")
    ),
    "background_special_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[174 + batch*level_coeff]}")
    ),
    "background_special_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[175 + batch*level_coeff]}")
    ),
    "background_special_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[176 + batch*level_coeff]}")
    ),
    "background_special_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[177 + batch*level_coeff]}")
    ),
    "vertical_lines": np.array(
        Image.open(f"{sprites_path}/{sprites[253 + batch*level_coeff]}")
    ),

    "background_tile_1": np.array(
        Image.open(f"{sprites_path}/{sprites[7 + batch*level_coeff]}")
    ),
    "background_tile_2": np.array(
        Image.open(f"{sprites_path}/{sprites[8 + batch*level_coeff]}")
    ),
    "background_tile_3": np.array(
        Image.open(f"{sprites_path}/{sprites[9 + batch*level_coeff]}")
    ),
    "background_tile_4": np.array(
        Image.open(f"{sprites_path}/{sprites[10 + batch*level_coeff]}")
    ),
    "background_tile_5": np.array(
        Image.open(f"{sprites_path}/{sprites[11 + batch*level_coeff]}")
    ),
    "background_tile_6": np.array(
        Image.open(f"{sprites_path}/{sprites[12 + batch*level_coeff]}")
    ),
    "background_tile_7": np.array(
        Image.open(f"{sprites_path}/{sprites[23 + batch*level_coeff]}")
    ),
    "background_tile_8": np.array(
        Image.open(f"{sprites_path}/{sprites[24 + batch*level_coeff]}")
    ),
    "background_tile_9": np.array(
        Image.open(f"{sprites_path}/{sprites[25 + batch*level_coeff]}")
    ),
    "background_tile_10": np.array(
        Image.open(f"{sprites_path}/{sprites[26 + batch*level_coeff]}")
    ),
    "background_tile_11": np.array(
        Image.open(f"{sprites_path}/{sprites[27 + batch*level_coeff]}")
    ),
    "background_tile_12": np.array(
        Image.open(f"{sprites_path}/{sprites[28 + batch*level_coeff]}")
    ),
    "background_tile_13": np.array(
        Image.open(f"{sprites_path}/{sprites[48 + batch*level_coeff]}")
    ),
    "background_tile_14": np.array(
        Image.open(f"{sprites_path}/{sprites[49 + batch*level_coeff]}")
    ),
    "background_tile_15": np.array(
        Image.open(f"{sprites_path}/{sprites[50 + batch*level_coeff]}")
    ),
    "background_tile_16": np.array(
        Image.open(f"{sprites_path}/{sprites[51 + batch*level_coeff]}")
    ),
    "background_tile_17": np.array(
        Image.open(f"{sprites_path}/{sprites[52 + batch*level_coeff]}")
    ),
    "background_tile_18": np.array(
        Image.open(f"{sprites_path}/{sprites[53 + batch*level_coeff]}")
    ),
    "background_tile_19": np.array(
        Image.open(f"{sprites_path}/{sprites[54 + batch*level_coeff]}")
    ),
    "background_tile_20": np.array(
        Image.open(f"{sprites_path}/{sprites[55 + batch*level_coeff]}")
    ),
    "background_tile_21": np.array(
        Image.open(f"{sprites_path}/{sprites[56 + batch*level_coeff]}")
    ),
    "background_tile_22": np.array(
        Image.open(f"{sprites_path}/{sprites[57 + batch*level_coeff]}")
    ),
    "background_tile_23": np.array(
        Image.open(f"{sprites_path}/{sprites[58 + batch*level_coeff]}")
    ),
    "background_tile_24": np.array(
        Image.open(f"{sprites_path}/{sprites[59 + batch*level_coeff]}")
    ),
    "background_tile_25": np.array(
        Image.open(f"{sprites_path}/{sprites[60 + batch*level_coeff]}")
    ),
    "background_tile_26": np.array(
        Image.open(f"{sprites_path}/{sprites[61 + batch*level_coeff]}")
    ),
    "background_tile_27": np.array(
        Image.open(f"{sprites_path}/{sprites[62 + batch*level_coeff]}")
    ),
    "background_tile_28": np.array(
        Image.open(f"{sprites_path}/{sprites[63 + batch*level_coeff]}")
    ),
    "background_tile_29": np.array(
        Image.open(f"{sprites_path}/{sprites[71 + batch*level_coeff]}")
    ),
    "background_tile_30": np.array(
        Image.open(f"{sprites_path}/{sprites[72 + batch*level_coeff]}")
    ),
    "background_tile_31": np.array(
        Image.open(f"{sprites_path}/{sprites[73 + batch*level_coeff]}")
    ),
    "background_tile_32": np.array(
        Image.open(f"{sprites_path}/{sprites[74 + batch*level_coeff]}")
    ),
    "background_tile_33": np.array(
        Image.open(f"{sprites_path}/{sprites[75 + batch*level_coeff]}")
    ),
    "background_tile_34": np.array(
        Image.open(f"{sprites_path}/{sprites[76 + batch*level_coeff]}")
    ),
    "background_tile_35": np.array(
        Image.open(f"{sprites_path}/{sprites[87 + batch*level_coeff]}")
    ),
    "background_tile_36": np.array(
        Image.open(f"{sprites_path}/{sprites[88 + batch*level_coeff]}")
    ),
    "background_tile_37": np.array(
        Image.open(f"{sprites_path}/{sprites[89 + batch*level_coeff]}")
    ),
    "background_tile_38": np.array(
        Image.open(f"{sprites_path}/{sprites[90 + batch*level_coeff]}")
    ),
    "background_tile_39": np.array(
        Image.open(f"{sprites_path}/{sprites[91 + batch*level_coeff]}")
    ),
    "background_tile_40": np.array(
        Image.open(f"{sprites_path}/{sprites[92 + batch*level_coeff]}")
    ),
    "background_tile_41": np.array(
        Image.open(f"{sprites_path}/{sprites[101 + batch*level_coeff]}")
    ),
    "background_tile_42": np.array(
        Image.open(f"{sprites_path}/{sprites[102 + batch*level_coeff]}")
    ),
    "background_tile_43": np.array(
        Image.open(f"{sprites_path}/{sprites[103 + batch*level_coeff]}")
    ),
    "background_tile_44": np.array(
        Image.open(f"{sprites_path}/{sprites[104 + batch*level_coeff]}")
    ),
    "background_tile_45": np.array(
        Image.open(f"{sprites_path}/{sprites[105 + batch*level_coeff]}")
    ),
    "background_tile_46": np.array(
        Image.open(f"{sprites_path}/{sprites[106 + batch*level_coeff]}")
    ),
    "background_tile_47": np.array(
        Image.open(f"{sprites_path}/{sprites[107 + batch*level_coeff]}")
    ),
    "background_tile_48": np.array(
        Image.open(f"{sprites_path}/{sprites[108 + batch*level_coeff]}")
    ),
    "background_tile_49": np.array(
        Image.open(f"{sprites_path}/{sprites[136 + batch*level_coeff]}")
    ),
    "background_tile_50": np.array(
        Image.open(f"{sprites_path}/{sprites[137 + batch*level_coeff]}")
    ),
    "background_tile_51": np.array(
        Image.open(f"{sprites_path}/{sprites[138 + batch*level_coeff]}")
    ),
    "background_tile_52": np.array(
        Image.open(f"{sprites_path}/{sprites[139 + batch*level_coeff]}")
    ),
    "background_tile_53": np.array(
        Image.open(f"{sprites_path}/{sprites[140 + batch*level_coeff]}")
    ),
    "background_tile_54": np.array(
        Image.open(f"{sprites_path}/{sprites[141 + batch*level_coeff]}")
    ),
    "background_tile_55": np.array(
        Image.open(f"{sprites_path}/{sprites[142 + batch*level_coeff]}")
    ),
    "background_tile_56": np.array(
        Image.open(f"{sprites_path}/{sprites[143 + batch*level_coeff]}")
    ),
    "background_tile_57": np.array(
        Image.open(f"{sprites_path}/{sprites[218 + batch*level_coeff]}")
    ),
    "background_tile_58": np.array(
        Image.open(f"{sprites_path}/{sprites[219 + batch*level_coeff]}")
    ),
    "background_tile_59": np.array(
        Image.open(f"{sprites_path}/{sprites[220 + batch*level_coeff]}")
    ),
    "background_tile_60": np.array(
        Image.open(f"{sprites_path}/{sprites[221 + batch*level_coeff]}")
    ),
    "background_tile_61": np.array(
        Image.open(f"{sprites_path}/{sprites[222 + batch*level_coeff]}")
    ),
    "background_tile_62": np.array(
        Image.open(f"{sprites_path}/{sprites[223 + batch*level_coeff]}")
    ),
    "background_tile_63": np.array(
        Image.open(f"{sprites_path}/{sprites[224 + batch*level_coeff]}")
    ),
    "background_tile_64": np.array(
        Image.open(f"{sprites_path}/{sprites[225 + batch*level_coeff]}")
    ),
    "background_tile_65": np.array(
        Image.open(f"{sprites_path}/{sprites[226 + batch*level_coeff]}")
    ),
    "background_tile_66": np.array(
        Image.open(f"{sprites_path}/{sprites[227 + batch*level_coeff]}")
    ),
    "background_tile_67": np.array(
        Image.open(f"{sprites_path}/{sprites[228 + batch*level_coeff]}")
    ),
    "background_tile_68": np.array(
        Image.open(f"{sprites_path}/{sprites[229 + batch*level_coeff]}")
    ),
    "background_tile_69": np.array(
        Image.open(f"{sprites_path}/{sprites[230 + batch*level_coeff]}")
    ),
    "background_tile_70": np.array(
        Image.open(f"{sprites_path}/{sprites[231 + batch*level_coeff]}")
    ),
    "background_tile_71": np.array(
        Image.open(f"{sprites_path}/{sprites[232 + batch*level_coeff]}")
    ),
    "background_tile_72": np.array(
        Image.open(f"{sprites_path}/{sprites[233 + batch*level_coeff]}")
    ),
    "background_tile_73": np.array(
        Image.open(f"{sprites_path}/{sprites[234 + batch*level_coeff]}")
    ),
    "background_tile_74": np.array(
        Image.open(f"{sprites_path}/{sprites[235 + batch*level_coeff]}")
    ),
    "background_tile_75": np.array(
        Image.open(f"{sprites_path}/{sprites[236 + batch*level_coeff]}")
    ),
    "background_tile_76": np.array(
        Image.open(f"{sprites_path}/{sprites[246 + batch*level_coeff]}")
    ),
    "background_tile_77": np.array(
        Image.open(f"{sprites_path}/{sprites[247 + batch*level_coeff]}")
    ),
    "background_tile_78": np.array(
        Image.open(f"{sprites_path}/{sprites[248 + batch*level_coeff]}")
    ),
    "background_tile_79": np.array(
        Image.open(f"{sprites_path}/{sprites[249 + batch*level_coeff]}")
    ),
    "background_tile_80": np.array(
        Image.open(f"{sprites_path}/{sprites[250 + batch*level_coeff]}")
    ),
    "background_tile_81": np.array(
        Image.open(f"{sprites_path}/{sprites[254 + batch*level_coeff]}")
    ),
    "background_tile_82": np.array(
        Image.open(f"{sprites_path}/{sprites[255 + batch*level_coeff]}")
    ),
}

# -------------------------------------------- LEVEL 8

level_coeff = 7

level_8_sprites = {
    # -- INCLINED / SLOPE PIECES --
    
    # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[0 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[1 + batch*level_coeff]}")
    ),
    "inclined_ground_30_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[2 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[3 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[4 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[5 + batch*level_coeff]}")
    ),
    "inclined_ground_15_bottom_left_to_top_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[6 + batch*level_coeff]}")
    ),
    
    # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[16 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[17 + batch*level_coeff]}")
    ),
    "inclined_ground_30_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[18 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[19 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[20 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[21 + batch*level_coeff]}")
    ),
    "inclined_ground_15_top_left_to_bottom_right_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[22 + batch*level_coeff]}")
    ),
    
    # -- LOOP & CORNER PIECES -- (None)
    
    # -- GROUND / SPACE GROUND / CHECKER TILES / SPECIAL GROUND --
        
        # GROUND TILES
        
            # LOW
    "low_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[13 + batch*level_coeff]}")
    ),
    "low_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[15 + batch*level_coeff]}")
    ),
    "low_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[29 + batch*level_coeff]}")
    ),
    "low_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[31 + batch*level_coeff]}")
    ),
    
            # HIGH
    "curved_ground": np.array(
        Image.open(f"{sprites_path}/{sprites[14 + batch*level_coeff]}")
    ),
    "high_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[33 + batch*level_coeff]}")
    ),
    "high_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[34 + batch*level_coeff]}")
    ),
    "high_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[36 + batch*level_coeff]}")
    ),
    "high_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[47 + batch*level_coeff]}")
    ),
    "high_ground_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[96 + batch*level_coeff]}")
    ),
    "high_ground_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[109 + batch*level_coeff]}")
    ),
    "high_ground_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[110 + batch*level_coeff]}")
    ),
    "high_ground_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[111 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[37 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[39 + batch*level_coeff]}")
    ),
    "high_ground_top_left_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[41 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[38 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[40 + batch*level_coeff]}")
    ),
    "high_ground_top_right_grass_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[44 + batch*level_coeff]}")
    ),
    
        # SPACE GROUND TILES
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_space_ground_45_top_left_to_bottom_right_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[64 + batch*level_coeff]}")
    ),
    "inclined_space_ground_30_top_left_to_bottom_right_p1_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[65 + batch*level_coeff]}")
    ),
    "inclined_space_ground_30_top_left_to_bottom_right_p2_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[66 + batch*level_coeff]}")
    ),
    "inclined_space_ground_15_top_left_to_bottom_right_p1_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[67 + batch*level_coeff]}")
    ),
    "inclined_space_ground_15_top_left_to_bottom_right_p2_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[68 + batch*level_coeff]}")
    ),
    "inclined_space_ground_15_top_left_to_bottom_right_p3_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[69 + batch*level_coeff]}")
    ),
    "inclined_space_ground_15_top_left_to_bottom_right_p4_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[70 + batch*level_coeff]}")
    ),
    
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_space_ground_45_bottom_left_to_top_right_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[80 + batch*level_coeff]}")
    ),
    "inclined_space_ground_30_bottom_left_to_top_right_p1_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[81 + batch*level_coeff]}")
    ),
    "inclined_space_ground_30_bottom_left_to_top_right_p2_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[82 + batch*level_coeff]}")
    ),
    "inclined_space_ground_15_bottom_left_to_top_right_p1_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[83 + batch*level_coeff]}")
    ),
    "inclined_space_ground_15_bottom_left_to_top_right_p2_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[84 + batch*level_coeff]}")
    ),
    "inclined_space_ground_15_bottom_left_to_top_right_p3_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[85 + batch*level_coeff]}")
    ),
    "inclined_space_ground_15_bottom_left_to_top_right_p4_inversed": np.array(
        Image.open(f"{sprites_path}/{sprites[86 + batch*level_coeff]}")
    ),
            
            # LOW
    "low_space_ground_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[77 + batch*level_coeff]}")
    ),
    "low_space_ground_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[79 + batch*level_coeff]}")
    ),
    "low_space_ground_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[93 + batch*level_coeff]}")
    ),
    "low_space_ground_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[95 + batch*level_coeff]}")
    ),
            
            # HIGH
    
        # CHECKER TILES
        
            # LOW (None)
            
            # HIGH
    "high_checker_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[32 + batch*level_coeff]}")
    ),
    "high_checker_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[35 + batch*level_coeff]}")
    ),
    "high_checker_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[42 + batch*level_coeff]}")
    ),
    "high_checker_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[43 + batch*level_coeff]}")
    ),
    "high_checker_v5": np.array(
        Image.open(f"{sprites_path}/{sprites[45 + batch*level_coeff]}")
    ),
    "high_checker_v6": np.array(
        Image.open(f"{sprites_path}/{sprites[46 + batch*level_coeff]}")
    ),
    "high_checker_v7": np.array(
        Image.open(f"{sprites_path}/{sprites[97 + batch*level_coeff]}")
    ),
    "high_checker_v8": np.array(
        Image.open(f"{sprites_path}/{sprites[98 + batch*level_coeff]}")
    ),
    "high_checker_v9": np.array(
        Image.open(f"{sprites_path}/{sprites[99 + batch*level_coeff]}")
    ),
    "high_checker_v10": np.array(
        Image.open(f"{sprites_path}/{sprites[100 + batch*level_coeff]}")
    ),
    "high_checker_v11": np.array(
        Image.open(f"{sprites_path}/{sprites[106 + batch*level_coeff]}")
    ),
    "high_checker_v12": np.array(
        Image.open(f"{sprites_path}/{sprites[107 + batch*level_coeff]}")
    ),
    "high_checker_v13": np.array(
        Image.open(f"{sprites_path}/{sprites[136 + batch*level_coeff]}")
    ),
    "high_checker_v14": np.array(
        Image.open(f"{sprites_path}/{sprites[251 + batch*level_coeff]}")
    ),
    "high_checker_v15": np.array(
        Image.open(f"{sprites_path}/{sprites[252 + batch*level_coeff]}")
    ),
    "high_checker_bottom_left_decoration_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[101 + batch*level_coeff]}")
    ),
    "high_checker_bottom_right_decoration_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[102 + batch*level_coeff]}")
    ),
    "high_checker_bottom_left_decoration_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[103 + batch*level_coeff]}")
    ),
    "high_checker_bottom_right_decoration_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[104 + batch*level_coeff]}")
    ),
    "high_checker_bottom_left_decoration_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[105 + batch*level_coeff]}")
    ),
    "high_checker_bottom_right_decoration_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[108 + batch*level_coeff]}")
    ),
    
    # SPECIAL TILES
    "special_ground_tiles_angle_in_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[50 + batch*level_coeff]}")
    ),
    "special_ground_tiles_angle_in_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[51 + batch*level_coeff]}")
    ),
    "special_ground_tiles_angle_in_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[52 + batch*level_coeff]}")
    ),
    "special_ground_tiles_angle_in_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[53 + batch*level_coeff]}")
    ),
    "special_ground_tiles_two_vertical_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[54 + batch*level_coeff]}")
    ),
    "special_ground_tiles_two_vertical_top": np.array(
        Image.open(f"{sprites_path}/{sprites[55 + batch*level_coeff]}")
    ),
    "special_ground_tiles_two_horizontal_left": np.array(
        Image.open(f"{sprites_path}/{sprites[56 + batch*level_coeff]}")
    ),
    "special_ground_tiles_two_horizontal_right": np.array(
        Image.open(f"{sprites_path}/{sprites[57 + batch*level_coeff]}")
    ),
    "special_ground_tiles_four_points": np.array(
        Image.open(f"{sprites_path}/{sprites[58 + batch*level_coeff]}")
    ),
    
    # -- PIPES, WINDOW, CHAINS, OBJECT BLOCK, LASER & ETC --
    "pipe_from_bottom_classic_background": np.array(
        Image.open(f"{sprites_path}/{sprites[59 + batch*level_coeff]}")
    ),
    "pipe_from_top_classic_background": np.array(
        Image.open(f"{sprites_path}/{sprites[60 + batch*level_coeff]}")
    ),
    "pipe_from_right_classic_background": np.array(
        Image.open(f"{sprites_path}/{sprites[61 + batch*level_coeff]}")
    ),
    "pipe_from_left_classic_background": np.array(
        Image.open(f"{sprites_path}/{sprites[62 + batch*level_coeff]}")
    ),
    "pipe_from_bottom_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[200 + batch*level_coeff]}")
    ),
    "pipe_from_top_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[201 + batch*level_coeff]}")
    ),
    "pipe_from_right_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[202 + batch*level_coeff]}")
    ),
    "pipe_from_left_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[203 + batch*level_coeff]}")
    ),
    "pipe_horizontal_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[204 + batch*level_coeff]}")
    ),
    "pipe_vertical_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[205 + batch*level_coeff]}")
    ),
    "window_top_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[150 + batch*level_coeff]}")
    ),
    "window_top_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[151 + batch*level_coeff]}")
    ),
    "window_top_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[152 + batch*level_coeff]}")
    ),
    "window_top_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[153 + batch*level_coeff]}")
    ),
    "window_top_p5": np.array(
        Image.open(f"{sprites_path}/{sprites[154 + batch*level_coeff]}")
    ),
    "window_middle_top_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[155 + batch*level_coeff]}")
    ),
    "window_middle_top_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[156 + batch*level_coeff]}")
    ),
    "window_middle_top_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[157 + batch*level_coeff]}")
    ),
    "window_middle_top_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[158 + batch*level_coeff]}")
    ),
    "window_middle_top_p5": np.array(
        Image.open(f"{sprites_path}/{sprites[159 + batch*level_coeff]}")
    ),
    "window_middle_bottom_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[160 + batch*level_coeff]}")
    ),
    "window_middle_bottom_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[161 + batch*level_coeff]}")
    ),
    "window_middle_bottom_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[162 + batch*level_coeff]}")
    ),
    "window_middle_bottom_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[163 + batch*level_coeff]}")
    ),
    "window_middle_bottom_p5": np.array(
        Image.open(f"{sprites_path}/{sprites[164 + batch*level_coeff]}")
    ),
    "window_bottom_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[165 + batch*level_coeff]}")
    ),
    "window_bottom_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[166 + batch*level_coeff]}")
    ),
    "window_bottom_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[167 + batch*level_coeff]}")
    ),
    "window_bottom_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[168 + batch*level_coeff]}")
    ),
    "window_bottom_p5": np.array(
        Image.open(f"{sprites_path}/{sprites[169 + batch*level_coeff]}")
    ),
    "window_bottom_bottom_p1": np.array(
        Image.open(f"{sprites_path}/{sprites[170 + batch*level_coeff]}")
    ),
    "window_bottom_bottom_p2": np.array(
        Image.open(f"{sprites_path}/{sprites[171 + batch*level_coeff]}")
    ),
    "window_bottom_bottom_p3": np.array(
        Image.open(f"{sprites_path}/{sprites[172 + batch*level_coeff]}")
    ),
    "window_bottom_bottom_p4": np.array(
        Image.open(f"{sprites_path}/{sprites[173 + batch*level_coeff]}")
    ),
    "window_bottom_bottom_p5": np.array(
        Image.open(f"{sprites_path}/{sprites[174 + batch*level_coeff]}")
    ),
    "open_block_classic_background": np.array(
        Image.open(f"{sprites_path}/{sprites[175 + batch*level_coeff]}")
    ),
    "open_block_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[176 + batch*level_coeff]}")
    ),
    "closed_block": np.array(
        Image.open(f"{sprites_path}/{sprites[177 + batch*level_coeff]}")
    ),
    "metal_girder_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[178 + batch*level_coeff]}")
    ),
    "metal_girder_left": np.array(
        Image.open(f"{sprites_path}/{sprites[179 + batch*level_coeff]}")
    ),
    "metal_girder_right": np.array(
        Image.open(f"{sprites_path}/{sprites[180 + batch*level_coeff]}")
    ),
    "laser_from_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[193 + batch*level_coeff]}")
    ),
    "laser_from_top": np.array(
        Image.open(f"{sprites_path}/{sprites[194 + batch*level_coeff]}")
    ),
    "laser_from_left": np.array(
        Image.open(f"{sprites_path}/{sprites[195 + batch*level_coeff]}")
    ),
    "laser_from_right": np.array(
        Image.open(f"{sprites_path}/{sprites[196 + batch*level_coeff]}")
    ),
    "two_pipes_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[197 + batch*level_coeff]}")
    ),
    "support_left": np.array(
        Image.open(f"{sprites_path}/{sprites[198 + batch*level_coeff]}")
    ),
    "support_right": np.array(
        Image.open(f"{sprites_path}/{sprites[199 + batch*level_coeff]}")
    ),
    "spinning_chains_left_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[237 + batch*level_coeff]}")
    ),
    "spinning_chains_middle_without_support_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[238 + batch*level_coeff]}")
    ),
    "spinning_chains_right_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[239 + batch*level_coeff]}")
    ),
    "spinning_chains_left_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[240 + batch*level_coeff]}")
    ),
    "spinning_chains_middle_without_support_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[241 + batch*level_coeff]}")
    ),
    "spinning_chains_right_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[242 + batch*level_coeff]}")
    ),
    "spinning_chains_middle_with_support_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[243 + batch*level_coeff]}")
    ),
    "spinning_chains_middle_with_support_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[244 + batch*level_coeff]}")
    ),
    "support_laser_bottom_firing": np.array(
        Image.open(f"{sprites_path}/{sprites[245 + batch*level_coeff]}")
    ),
    "bullets": np.array(
        Image.open(f"{sprites_path}/{sprites[246 + batch*level_coeff]}")
    ),
    "support_laser_top_firing": np.array(
        Image.open(f"{sprites_path}/{sprites[247 + batch*level_coeff]}")
    ),
    "support_laser_bottom_not_firing": np.array(
        Image.open(f"{sprites_path}/{sprites[248 + batch*level_coeff]}")
    ),
    "support_laser_top_not_firing": np.array(
        Image.open(f"{sprites_path}/{sprites[249 + batch*level_coeff]}")
    ),
    
    # -- RINGS --
    "top_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[112 + batch*level_coeff]}")
    ),
    "bottom_two_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[113 + batch*level_coeff]}")
    ),
    "top_left_and_bottom_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[114 + batch*level_coeff]}")
    ),
    "bottom_left_and_right_rings": np.array(
        Image.open(f"{sprites_path}/{sprites[115 + batch*level_coeff]}")
    ),
    "top_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[116 + batch*level_coeff]}")
    ),
    "top_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[117 + batch*level_coeff]}")
    ),
    "bottom_left_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[118 + batch*level_coeff]}")
    ),
    "bottom_right_ring": np.array(
        Image.open(f"{sprites_path}/{sprites[119 + batch*level_coeff]}")
    ),
    
    # -- SPRINGS --
    "spring_from_bottom_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[120 + batch*level_coeff]}")
    ),
    "spring_from_bottom_middle_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[121 + batch*level_coeff]}")
    ),
    "spring_from_left_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[122 + batch*level_coeff]}")
    ),
    "spring_from_left_middle_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[123 + batch*level_coeff]}")
    ),
    "spring_from_right_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[124 + batch*level_coeff]}")
    ),
    "spring_from_right_middle_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[125 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[126 + batch*level_coeff]}")
    ),
    "spring_from_bottom_left_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[127 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right": np.array(
        Image.open(f"{sprites_path}/{sprites[128 + batch*level_coeff]}")
    ),
    "spring_from_bottom_right_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[129 + batch*level_coeff]}")
    ),
    
    # -- SPIKES --
    "spike_from_bottom": np.array(
        Image.open(f"{sprites_path}/{sprites[130 + batch*level_coeff]}")
    ),
    "spike_from_bottom_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[131 + batch*level_coeff]}")
    ),
    "spike_from_top": np.array(
        Image.open(f"{sprites_path}/{sprites[132 + batch*level_coeff]}")
    ),
    "spike_from_top_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[133 + batch*level_coeff]}")
    ),
    
    # I'll assume it's something to block sonic.
    "blocking_thing_classic_background": np.array(
        Image.open(f"{sprites_path}/{sprites[134 + batch*level_coeff]}")
    ),
    "blocking_thing_space_background": np.array(
        Image.open(f"{sprites_path}/{sprites[135 + batch*level_coeff]}")
    ),
    
    # -- BACKGROUND TILES --
    "background_special_horizontal": np.array(
        Image.open(f"{sprites_path}/{sprites[48 + batch*level_coeff]}")
    ),
    "background_special_vertical": np.array(
        Image.open(f"{sprites_path}/{sprites[49 + batch*level_coeff]}")
    ),
    "background_special_top_left": np.array(
        Image.open(f"{sprites_path}/{sprites[138 + batch*level_coeff]}")
    ),
    "background_special_top_blank": np.array(
        Image.open(f"{sprites_path}/{sprites[139 + batch*level_coeff]}")
    ),
    "background_special_top_middle": np.array(
        Image.open(f"{sprites_path}/{sprites[140 + batch*level_coeff]}")
    ),
    "background_special_top_right": np.array(
        Image.open(f"{sprites_path}/{sprites[141 + batch*level_coeff]}")
    ),
    "background_special_middle_left_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[142 + batch*level_coeff]}")
    ),
    "background_special_middle_blank_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[143 + batch*level_coeff]}")
    ),
    "background_special_middle_middle_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[144 + batch*level_coeff]}")
    ),
    "background_special_middle_right_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[145 + batch*level_coeff]}")
    ),
    "background_special_middle_left_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[146 + batch*level_coeff]}")
    ),
    "background_special_middle_blank_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[147 + batch*level_coeff]}")
    ),
    "background_special_middle_middle_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[148 + batch*level_coeff]}")
    ),
    "background_special_middle_right_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[149 + batch*level_coeff]}")
    ),
    "background_special_top_right_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[181 + batch*level_coeff]}")
    ),
    "background_special_top_left_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[182 + batch*level_coeff]}")
    ),
    "background_special_top_right_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[183 + batch*level_coeff]}")
    ),
    "background_special_top_left_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[184 + batch*level_coeff]}")
    ),
    "background_special_top_right_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[185 + batch*level_coeff]}")
    ),
    "background_special_top_left_v3": np.array(
        Image.open(f"{sprites_path}/{sprites[186 + batch*level_coeff]}")
    ),
    "background_special_left_bar_half": np.array(
        Image.open(f"{sprites_path}/{sprites[187 + batch*level_coeff]}")
    ),
    "background_special_left_bar_v1": np.array(
        Image.open(f"{sprites_path}/{sprites[188 + batch*level_coeff]}")
    ),
    "background_special_left_bar_v2": np.array(
        Image.open(f"{sprites_path}/{sprites[189 + batch*level_coeff]}")
    ),
    "background_special_top_right_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[190 + batch*level_coeff]}")
    ),
    "background_special_bottom_left": np.array(
        Image.open(f"{sprites_path}/{sprites[191 + batch*level_coeff]}")
    ),
    "background_special_top_left_v4": np.array(
        Image.open(f"{sprites_path}/{sprites[192 + batch*level_coeff]}")
    ),
    "vertical_lines": np.array(
        Image.open(f"{sprites_path}/{sprites[253 + batch*level_coeff]}")
    ),

    "background_tile_1": np.array(
        Image.open(f"{sprites_path}/{sprites[7 + batch*level_coeff]}")
    ),
    "background_tile_2": np.array(
        Image.open(f"{sprites_path}/{sprites[8 + batch*level_coeff]}")
    ),
    "background_tile_3": np.array(
        Image.open(f"{sprites_path}/{sprites[9 + batch*level_coeff]}")
    ),
    "background_tile_4": np.array(
        Image.open(f"{sprites_path}/{sprites[10 + batch*level_coeff]}")
    ),
    "background_tile_5": np.array(
        Image.open(f"{sprites_path}/{sprites[11 + batch*level_coeff]}")
    ),
    "background_tile_6": np.array(
        Image.open(f"{sprites_path}/{sprites[12 + batch*level_coeff]}")
    ),
    "background_tile_7": np.array(
        Image.open(f"{sprites_path}/{sprites[23 + batch*level_coeff]}")
    ),
    "background_tile_8": np.array(
        Image.open(f"{sprites_path}/{sprites[24 + batch*level_coeff]}")
    ),
    "background_tile_9": np.array(
        Image.open(f"{sprites_path}/{sprites[25 + batch*level_coeff]}")
    ),
    "background_tile_10": np.array(
        Image.open(f"{sprites_path}/{sprites[26 + batch*level_coeff]}")
    ),
    "background_tile_11": np.array(
        Image.open(f"{sprites_path}/{sprites[27 + batch*level_coeff]}")
    ),
    "background_tile_12": np.array(
        Image.open(f"{sprites_path}/{sprites[28 + batch*level_coeff]}")
    ),
    "background_tile_13": np.array(
        Image.open(f"{sprites_path}/{sprites[30 + batch*level_coeff]}")
    ),
    "background_tile_14": np.array(
        Image.open(f"{sprites_path}/{sprites[63 + batch*level_coeff]}")
    ),
    "background_tile_15": np.array(
        Image.open(f"{sprites_path}/{sprites[71 + batch*level_coeff]}")
    ),
    "background_tile_16": np.array(
        Image.open(f"{sprites_path}/{sprites[72 + batch*level_coeff]}")
    ),
    "background_tile_17": np.array(
        Image.open(f"{sprites_path}/{sprites[73 + batch*level_coeff]}")
    ),
    "background_tile_18": np.array(
        Image.open(f"{sprites_path}/{sprites[74 + batch*level_coeff]}")
    ),
    "background_tile_19": np.array(
        Image.open(f"{sprites_path}/{sprites[75 + batch*level_coeff]}")
    ),
    "background_tile_20": np.array(
        Image.open(f"{sprites_path}/{sprites[76 + batch*level_coeff]}")
    ),
    "background_tile_21": np.array(
        Image.open(f"{sprites_path}/{sprites[78 + batch*level_coeff]}")
    ),
    "background_tile_22": np.array(
        Image.open(f"{sprites_path}/{sprites[87 + batch*level_coeff]}")
    ),
    "background_tile_23": np.array(
        Image.open(f"{sprites_path}/{sprites[88 + batch*level_coeff]}")
    ),
    "background_tile_24": np.array(
        Image.open(f"{sprites_path}/{sprites[89 + batch*level_coeff]}")
    ),
    "background_tile_25": np.array(
        Image.open(f"{sprites_path}/{sprites[90 + batch*level_coeff]}")
    ),
    "background_tile_26": np.array(
        Image.open(f"{sprites_path}/{sprites[91 + batch*level_coeff]}")
    ),
    "background_tile_27": np.array(
        Image.open(f"{sprites_path}/{sprites[92 + batch*level_coeff]}")
    ),
    "background_tile_28": np.array(
        Image.open(f"{sprites_path}/{sprites[94 + batch*level_coeff]}")
    ),
    "background_tile_29": np.array(
        Image.open(f"{sprites_path}/{sprites[137 + batch*level_coeff]}")
    ),
    "background_tile_30": np.array(
        Image.open(f"{sprites_path}/{sprites[206 + batch*level_coeff]}")
    ),
    "background_tile_31": np.array(
        Image.open(f"{sprites_path}/{sprites[207 + batch*level_coeff]}")
    ),
    "background_tile_32": np.array(
        Image.open(f"{sprites_path}/{sprites[208 + batch*level_coeff]}")
    ),
    "background_tile_33": np.array(
        Image.open(f"{sprites_path}/{sprites[209 + batch*level_coeff]}")
    ),
    "background_tile_34": np.array(
        Image.open(f"{sprites_path}/{sprites[210 + batch*level_coeff]}")
    ),
    "background_tile_35": np.array(
        Image.open(f"{sprites_path}/{sprites[211 + batch*level_coeff]}")
    ),
    "background_tile_36": np.array(
        Image.open(f"{sprites_path}/{sprites[212 + batch*level_coeff]}")
    ),
    "background_tile_37": np.array(
        Image.open(f"{sprites_path}/{sprites[213 + batch*level_coeff]}")
    ),
    "background_tile_38": np.array(
        Image.open(f"{sprites_path}/{sprites[214 + batch*level_coeff]}")
    ),
    "background_tile_39": np.array(
        Image.open(f"{sprites_path}/{sprites[215 + batch*level_coeff]}")
    ),
    "background_tile_40": np.array(
        Image.open(f"{sprites_path}/{sprites[216 + batch*level_coeff]}")
    ),
    "background_tile_41": np.array(
        Image.open(f"{sprites_path}/{sprites[217 + batch*level_coeff]}")
    ),
    "background_tile_42": np.array(
        Image.open(f"{sprites_path}/{sprites[218 + batch*level_coeff]}")
    ),
    "background_tile_43": np.array(
        Image.open(f"{sprites_path}/{sprites[219 + batch*level_coeff]}")
    ),
    "background_tile_44": np.array(
        Image.open(f"{sprites_path}/{sprites[220 + batch*level_coeff]}")
    ),
    "background_tile_45": np.array(
        Image.open(f"{sprites_path}/{sprites[221 + batch*level_coeff]}")
    ),
    "background_tile_46": np.array(
        Image.open(f"{sprites_path}/{sprites[222 + batch*level_coeff]}")
    ),
    "background_tile_47": np.array(
        Image.open(f"{sprites_path}/{sprites[223 + batch*level_coeff]}")
    ),
    "background_tile_48": np.array(
        Image.open(f"{sprites_path}/{sprites[224 + batch*level_coeff]}")
    ),
    "background_tile_49": np.array(
        Image.open(f"{sprites_path}/{sprites[225 + batch*level_coeff]}")
    ),
    "background_tile_50": np.array(
        Image.open(f"{sprites_path}/{sprites[226 + batch*level_coeff]}")
    ),
    "background_tile_51": np.array(
        Image.open(f"{sprites_path}/{sprites[227 + batch*level_coeff]}")
    ),
    "background_tile_52": np.array(
        Image.open(f"{sprites_path}/{sprites[228 + batch*level_coeff]}")
    ),
    "background_tile_53": np.array(
        Image.open(f"{sprites_path}/{sprites[229 + batch*level_coeff]}")
    ),
    "background_tile_54": np.array(
        Image.open(f"{sprites_path}/{sprites[230 + batch*level_coeff]}")
    ),
    "background_tile_55": np.array(
        Image.open(f"{sprites_path}/{sprites[231 + batch*level_coeff]}")
    ),
    "background_tile_56": np.array(
        Image.open(f"{sprites_path}/{sprites[232 + batch*level_coeff]}")
    ),
    "background_tile_57": np.array(
        Image.open(f"{sprites_path}/{sprites[233 + batch*level_coeff]}")
    ),
    "background_tile_58": np.array(
        Image.open(f"{sprites_path}/{sprites[234 + batch*level_coeff]}")
    ),
    "background_tile_59": np.array(
        Image.open(f"{sprites_path}/{sprites[235 + batch*level_coeff]}")
    ),
    "background_tile_60": np.array(
        Image.open(f"{sprites_path}/{sprites[236 + batch*level_coeff]}")
    ),
    "background_tile_61": np.array(
        Image.open(f"{sprites_path}/{sprites[250 + batch*level_coeff]}")
    ),
    "background_tile_62": np.array(
        Image.open(f"{sprites_path}/{sprites[254 + batch*level_coeff]}")
    ),
    "background_tile_63": np.array(
        Image.open(f"{sprites_path}/{sprites[255 + batch*level_coeff]}")
    ),
}


def convert_to_serializable(obj):
    """ Converts a numpy array to a serializable format """
    if isinstance(obj, np.ndarray):
        return obj.tolist()  # Convert NumPy array to list
    elif isinstance(obj, dict):
        return {
            key: convert_to_serializable(value) for key, value in obj.items()
        }  # Convert values in dict
    elif isinstance(obj, list):
        return [convert_to_serializable(item) for item in obj]  # Convert items in list
    else:
        return obj  # Return other types as is


# List of levels
levels = [
    level_1_sprites,
    level_2_sprites,
    level_3_sprites,
    level_4_sprites,
    level_5_sprites,
    level_6_sprites,
    level_7_sprites,
    level_8_sprites,
]

if sum(len(level) for level in levels) == len(sprites):
    output_dir_name = 'sprites_data'
    output_dir = os.makedirs(output_dir_name, exist_ok = True)
    
    for i, level_data in enumerate(levels):
        with open(f"{output_dir_name}/level_{i+1}.json", "w") as f:
            json.dump(convert_to_serializable(level_data), f, indent = 4)
            
    print("Levels sprites data created !!")
else:
    print(
        "Error: The number of sprites in the levels list does not match the total number of sprites !! Check again the sprites list."
    )
