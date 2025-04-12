import os
import json

sprites_path = r"C:\Users\axelo\Documents\Projects\level-auto-encoder\all_general_map_sprite"
sprites = os.listdir(sprites_path)

# -------------------------------------------- LEVEL 1

level_1_sprites = {
    # -- INCLINED / SLOPE PIECES --

        # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": "ig_45_bl_tr",
    "inclined_ground_30_bottom_left_to_top_right_p1": "ig_30_bl_tr_p1",
    "inclined_ground_30_bottom_left_to_top_right_p2": "ig_30_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p1": "ig_15_bl_tr_p1",
    "inclined_ground_15_bottom_left_to_top_right_p2": "ig_15_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p3": "ig_15_bl_tr_p3",
    "inclined_ground_15_bottom_left_to_top_right_p4": "ig_15_bl_tr_p4",
    
        # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": "ig_45_tl_br",
    "inclined_ground_30_top_left_to_bottom_right_p1": "ig_30_tl_br_p1",
    "inclined_ground_30_top_left_to_bottom_right_p2": "ig_30_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p1": "ig_15_tl_br_p1",
    "inclined_ground_15_top_left_to_bottom_right_p2": "ig_15_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p3": "ig_15_tl_br_p3",
    "inclined_ground_15_top_left_to_bottom_right_p4": "ig_15_tl_br_p4",
    
    # -- LOOP & CORNER PIECES --

        # RIGHT SIDE
    "loop_bottom_middle_right": "O_bm_r",
    "loop_bottom_right": "O_b_r",
    "loop_right_middle_bottom": "O_rm_b",
    "loop_right_middle_top": "O_rm_t",
    "loop_top_right": "O_t_r",
    "loop_top_middle_right": "O_tm_r",
    
        # LEFT SIDE
    "loop_bottom_middle_left": "O_bm_l",
    "loop_bottom_left": "O_b_l",
    "loop_left_middle_bottom": "O_lm_b",
    "loop_left_middle_top": "O_lm_t",
    "loop_top_left": "O_t_l",
    "loop_top_middle_left": "O_tm_l",
    
    # -- GROUND / SAND GROUND / CHECKER TILES --
    
        # GROUND TILES
        
            # LOW
    "low_ground_v1": "lg_v1",
    "low_ground_v2": "lg_v2",
    "low_ground_v3": "lg_v3",
    "low_ground_v4": "lg_v4",
    
    "triangle_ground": "tg",

            # HIGH
    "curved_ground": "Cg",
    
    "high_ground_v1": "hg_v1",
    "high_ground_v2": "hg_v2",
    "high_ground_v3": "hg_v3",
    "high_ground_v4": "hg_v4",
    
    "high_ground_top_left_grass_v1": "hg_tl_gr_v1",
    "high_ground_top_left_grass_v2": "hg_tl_gr_v2",
    "high_ground_top_left_grass_v3": "hg_tl_gr_v3",
    "high_ground_top_left_grass_v4": "hg_tl_gr_v4",
    
    "high_ground_top_right_grass_v1": "hg_tr_gr_v1",
    "high_ground_top_right_grass_v2": "hg_tr_gr_v2",
    "high_ground_top_right_grass_v3": "hg_tr_gr_v3",
    "high_ground_top_right_grass_v4": "hg_tr_gr_v4",
       
        # SAND GROUND TILES
        
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_sand_ground_45_bottom_left_to_top_right": "isg_45_bl_tr",
    "inclined_sand_ground_30_bottom_left_to_top_right_p1": "isg_30_bl_tr_p1",
    "inclined_sand_ground_30_bottom_left_to_top_right_p2": "isg_30_bl_tr_p2",
    "inclined_sand_ground_15_bottom_left_to_top_right_p1": "isg_15_bl_tr_p1",
    "inclined_sand_ground_15_bottom_left_to_top_right_p2": "isg_15_bl_tr_p2",
    "inclined_sand_ground_15_bottom_left_to_top_right_p3": "isg_15_bl_tr_p3",
    "inclined_sand_ground_15_bottom_left_to_top_right_p4": "isg_15_bl_tr_p4",
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_sand_ground_45_top_left_to_bottom_right": "isg_45_tl_br",
    "inclined_sand_ground_30_top_left_to_bottom_right_p1": "isg_30_tl_br_p1",
    "inclined_sand_ground_30_top_left_to_bottom_right_p2": "isg_30_tl_br_p2",
    "inclined_sand_ground_15_top_left_to_bottom_right_p1": "isg_15_tl_br_p1",
    "inclined_sand_ground_15_top_left_to_bottom_right_p2": "isg_15_tl_br_p2",
    "inclined_sand_ground_15_top_left_to_bottom_right_p3": "isg_15_tl_br_p3",
    "inclined_sand_ground_15_top_left_to_bottom_right_p4": "isg_15_tl_br_p4",
    
            # LOW
    "low_sand_ground_v1": "lsg_v1",
    "low_sand_ground_v2": "lsg_v2",
    
    "low_sand_ground_waterfall_v1": "lsg_wf_v1",
    "low_sand_ground_waterfall_v2": "lsg_wf_v2",
    
    "triangle_sand_ground": "tsg",

            # HIGH
    "curved_sand_ground": "Cs",
    
    "high_sand_ground_v1": "hsg_v1",
    "high_sand_ground_v2": "hsg_v2",
    "high_sand_ground_v3": "hsg_v3",
    "high_sand_ground_v4": "hsg_v4",
    "high_sand_ground_v5": "hsg_v5",
    "high_sand_ground_v6": "hsg_v6",
    "high_sand_ground_v7": "hsg_v7",
    "high_sand_ground_v8": "hsg_v8",
    "high_sand_ground_v9": "hsg_v9",
    "high_sand_ground_v10": "hsg_v10",
    "high_sand_ground_v11": "hsg_v11",
    "high_sand_ground_v12": "hsg_v12",
    "high_sand_ground_v13": "hsg_v13",
    "high_sand_ground_v14": "hsg_v14",
    "high_sand_ground_v15": "hsg_v15",
    "high_sand_ground_v16": "hsg_v16",
    
        # CHECKER TILES

            # LOW
    "low_checker_v1": "lch_v1",
    "low_checker_v2": "lch_v2",
        
            # HIGH
    "high_checker_v1": "hch_v1",
    "high_checker_v2": "hch_v2",
    "high_checker_v3": "hch_v3",
    "high_checker_v4": "hch_v4",
    "high_checker_v5": "hch_v5",
    "high_checker_v6": "hch_v6",
    "high_checker_v7": "hch_v7",
    "high_checker_v8": "hch_v8",
    "high_checker_v9": "hch_v9",
    "high_checker_v10": "hch_v10",
    "high_checker_v11": "hch_v11",
    "high_checker_v12": "hch_v12",
    "high_checker_v13": "hch_v13",
    "high_checker_v14": "hch_v14",
    "high_checker_v15": "hch_v15",
    
    # -- BRIDGE PIECES --
    "bridge_piece_from_left": "br_fl",
    "bridge_piece_from_right": "br_fr",
    
    "bridge_support_top_right": "br_s_tr",
    "bridge_support_top_left": "br_s_tl",
    "bridge_two_top_supports": "br_s_2t",
    
    # -- PALM TREES, BUSH & FLOWERS --
    "palm_tree_top_left": "pt_tl",
    "palm_tree_top_middle": "pt_tm",
    "palm_tree_top_right": "pt_tr",
    "palm_tree_middle_left": "pt_ml",
    "palm_tree_middle": "pt_m",
    "palm_tree_middle_right": "pt_mr",
    "palm_tree_bottom_left": "pt_bl",
    "palm_tree_bottom_right": "pt_br",
    "palm_tree_trunk_classic_background": "pt_tc",
    "palm_tree_trunk_special_background": "pt_tsp", 
    "palm_tree_trunk_sea_background": "pt_tsea",
    
    "little_flower_middle": "fl_m",
    "flower_middle": "f_m",
    "two_flowers": "f_2",
    "two_flowers_top": "f_2t",
    "two_flowers_bottom": "f_2b",
    
    "bush": "B",

    # -- RINGS --
    "top_two_rings": "r_tt",
    "bottom_two_rings": "r_tb",
    "top_left_and_bottom_right_rings": "r_tlbr",
    "bottom_left_and_right_rings": "r_blr",
    "top_left_ring": "r_tl",
    "top_right_ring": "r_tr",
    "bottom_left_ring": "r_bl",
    "bottom_right_ring": "r_br",

    # -- SPRINGS --
    "spring_from_bottom_middle": "s_fbm",
    "spring_from_bottom_middle_underwater": "s_fbm_uw",
    "spring_from_left_middle": "s_flm",
    "spring_from_left_middle_underwater": "s_flm_uw",
    "spring_from_right_middle": "s_frm",
    "spring_from_right_middle_underwater": "s_frm_uw",
    "spring_from_bottom_left": "s_fbl",
    "spring_from_bottom_left_underwater": "s_fbl_uw",
    "spring_from_bottom_right": "s_fbr",
    "spring_from_bottom_right_underwater": "s_fbr_uw",
    
    # -- SPIKES --
    "spike_from_bottom": "S_fb",
    "spike_from_bottom_underwater": "S_fb_uw",
    "spike_from_top": "S_ft",
    "spike_from_top_underwater": "S_ft_uw",

    # I'll assume it's something to block sonic.
    "blocking_thing": "K",

    # -- WATER -- 
    "water_surface_1": "w_1",
    "water_surface_2": "w_2",
    "water_surface_3": "w_3",
    "water_surface_half": "w_h",
    
    "waterfall_start": "W_1",
    "waterfall_middle": "W_2",
    "waterfall_end": "W_3",
    
    "waterfall_start_with_background": "W_1b",
    "waterfall_middle_with_background": "W_2b",
    "waterfall_end_with_background": "W_3b",
    
    # -- CLOUDS --
    "mini_cloud": "c",
    
    "cloud_left": "c_l",
    "cloud_right": "c_r",

    # -- BACKGROUND TILES --
    "sea_background_v1": "e1",
    "sea_background_v2": "e2",
    "sea_background_v3": "e3",
    
    "background_special": "_",
    "background_special_left": "_l",
    "background_special_right": "_r",
    
    "vertical_lines": "vl",
    
    "background_tile_1": "-",
    "background_tile_2": "-", 
    "background_tile_3": "-",
    "background_tile_4": "-", 
    "background_tile_5": "-",
    "background_tile_6": "-", 
    "background_tile_7": "-",
    "background_tile_8": "-", 
    "background_tile_9": "-",
    "background_tile_10": "-", 
    "background_tile_11": "-",
    "background_tile_12": "-", 
    "background_tile_13": "-",
    "background_tile_14": "-", 
    "background_tile_15": "-",
    "background_tile_16": "-", 
    "background_tile_17": "-",
    "background_tile_18": "-", 
    "background_tile_19": "-",
    "background_tile_20": "-", 
    "background_tile_21": "-" ,
    "background_tile_22": "-", 
    "background_tile_23": "-",
    "background_tile_24": "-", 
    "background_tile_25": "-",
    "background_tile_26": "-", 
    "background_tile_27": "-",
    "background_tile_28": "-", 
    "background_tile_29": "-",
    "background_tile_30": "-", 
    "background_tile_31": "-",
    "background_tile_32": "-", 
    "background_tile_33": "-",
    "background_tile_34": "-", 
    "background_tile_35": "-",
    "background_tile_36": "-",
    "background_tile_37": "-", 
    "background_tile_38": "-",
    "background_tile_39": "-", 
    "background_tile_40": "-",
    "background_tile_41": "-", 
    "background_tile_42": "-",
    "background_tile_43": "-", 
    "background_tile_44": "-",
    "background_tile_45": "-", 
    "background_tile_46": "-",
    "background_tile_47": "-", 
    "background_tile_48": "-", 
    "background_tile_49": "-", 
    "background_tile_50": "-", 
    "background_tile_51": "-", 
    "background_tile_52": "-", 
    "background_tile_53": "-", 
    "background_tile_54": "-", 
    "background_tile_55": "-", 
    "background_tile_56": "-", 
    "background_tile_57": "-",
    "background_tile_58": "-", 
    "background_tile_59": "-",
    "background_tile_60": "-", 
    "background_tile_61": "-",
    "background_tile_62": "-", 
    "background_tile_63": "-", 
    "background_tile_64": "-", 
    "background_tile_65": "-", 
    "background_tile_66": "-", 
    "background_tile_67": "-", 
    "background_tile_68": "-", 
    "background_tile_69": "-", 
    "background_tile_70": "-", 
    "background_tile_71": "-", 
    "background_tile_72": "-",
    "background_tile_73": "-", 
    "background_tile_74": "-",
    "background_tile_75": "-", 
    "background_tile_76": "-",
    "background_tile_77": "-", 
    "background_tile_78": "-",
    "background_tile_79": "-", 
    "background_tile_80": "-",
    "background_tile_81": "-", 
    "background_tile_82": "-", 
    "background_tile_83": "-", 
    "background_tile_84": "-", 
    "background_tile_85": "-", 
    "background_tile_86": "-", 
    "background_tile_87": "-", 
    "background_tile_88": "-", 
    "background_tile_89": "-", 
    "background_tile_90": "-", 
    "background_tile_91": "-",
    "background_tile_92": "-", 
    "background_tile_93": "-", 
    "background_tile_94": "-", 
}

# -------------------------------------------- LEVEL 2

level_2_sprites = {
    # -- INCLINED / SLOPE PIECES --

        # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": "ig_45_bl_tr",
    "inclined_ground_30_bottom_left_to_top_right_p1": "ig_30_bl_tr_p1",
    "inclined_ground_30_bottom_left_to_top_right_p2": "ig_30_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p1": "ig_15_bl_tr_p1",
    "inclined_ground_15_bottom_left_to_top_right_p2": "ig_15_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p3": "ig_15_bl_tr_p3",
    "inclined_ground_15_bottom_left_to_top_right_p4": "ig_15_bl_tr_p4",
    
        # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": "ig_45_tl_br",
    "inclined_ground_30_top_left_to_bottom_right_p1": "ig_30_tl_br_p1",
    "inclined_ground_30_top_left_to_bottom_right_p2": "ig_30_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p1": "ig_15_tl_br_p1",
    "inclined_ground_15_top_left_to_bottom_right_p2": "ig_15_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p3": "ig_15_tl_br_p3",
    "inclined_ground_15_top_left_to_bottom_right_p4": "ig_15_tl_br_p4",
    
    # -- LOOP & CORNER PIECES --

        # RIGHT SIDE
    "loop_bottom_middle_right": "O_bm_r",
    "loop_bottom_right": "O_br",
    "loop_right_middle_bottom": "O_rm_b",
    "loop_right_middle_top": "O_rm_t",
    "loop_top_right": "O_tr",
    "loop_top_middle_right": "O_tm_r",
    
        # LEFT SIDE
    "loop_bottom_middle_left": "O_bm_l",
    "loop_bottom_left": "O_bl",
    "loop_left_middle_bottom": "O_lm_b",
    "loop_left_middle_top": "O_lm_t",
    "loop_top_left": "O_tl",
    "loop_top_middle_left": "O_tm_l",
    
    # -- GROUND / JUNGLE GROUND / CHECKER TILES --
    
        # GROUND TILES
        
            # LOW
    "low_ground_v1": "lg_v1",
    "low_ground_v2": "lg_v2",
    "low_ground_v3": "lg_v3",
    "low_ground_v4": "lg_v4",
    
    "triangle_ground": "tg",

            # HIGH
    "curved_ground": "Cg",
    
    "high_ground_v1": "hg_v1",
    "high_ground_v2": "hg_v2",
    "high_ground_v3": "hg_v3",
    "high_ground_v4": "hg_v4",
    "high_ground_v5": "hg_v5",
    "high_ground_v6": "hg_v6",
    "high_ground_v7": "hg_v7",
    
    "high_ground_top_left_grass_v1_1": "hg_tl_gr_v1_1",
    "high_ground_top_left_grass_v1_2": "hg_tl_gr_v1_2",
    "high_ground_top_left_grass_v2_1": "hg_tl_gr_v2_1",
    "high_ground_top_left_grass_v2_2": "hg_tl_gr_v2_2",
    "high_ground_top_left_grass_v3_1": "hg_tl_gr_v3_1",
    "high_ground_top_left_grass_v3_2": "hg_tl_gr_v3_2",
    "high_ground_top_left_grass_v4_1": "hg_tl_gr_v4_1",
    "high_ground_top_left_grass_v4_2": "hg_tl_gr_v4_2",
    
    "high_ground_top_right_grass_v1_1": "hg_tr_gr_v1_1",
    "high_ground_top_right_grass_v1_2": "hg_tr_gr_v1_2",
    "high_ground_top_right_grass_v2_1": "hg_tr_gr_v2_1",
    "high_ground_top_right_grass_v2_2": "hg_tr_gr_v2_2",
    "high_ground_top_right_grass_v3_1": "hg_tr_gr_v3_1",
    "high_ground_top_right_grass_v3_2": "hg_tr_gr_v3_2",
    "high_ground_top_right_grass_v4_1": "hg_tr_gr_v4_1",
    "high_ground_top_right_grass_v4_2": "hg_tr_gr_v4_2",
       
        # JUNGLE GROUND TILES
        
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_jungle_ground_45_bottom_left_to_top_right": "ijg_45_bl_to_tr",
    "inclined_jungle_ground_30_bottom_left_to_top_right_p1": "ijg_30_bl_to_tr_p1",
    "inclined_jungle_ground_30_bottom_left_to_top_right_p2": "ijg_30_bl_to_tr_p2",
    "inclined_jungle_ground_15_bottom_left_to_top_right_p1": "ijg_15_bl_to_tr_p1",
    "inclined_jungle_ground_15_bottom_left_to_top_right_p2": "ijg_15_bl_to_tr_p2",
    "inclined_jungle_ground_15_bottom_left_to_top_right_p3": "ijg_15_bl_to_tr_p3",
    "inclined_jungle_ground_15_bottom_left_to_top_right_p4": "ijg_15_bl_to_tr_p4",
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_jungle_ground_45_top_left_to_bottom_right": "ijg_45_tl_to_br",
    "inclined_jungle_ground_30_top_left_to_bottom_right_p1": "ijg_30_tl_to_br_p1",
    "inclined_jungle_ground_30_top_left_to_bottom_right_p2": "ijg_30_tl_to_br_p2",
    "inclined_jungle_ground_15_top_left_to_bottom_right_p1": "ijg_15_tl_to_br_p1",
    "inclined_jungle_ground_15_top_left_to_bottom_right_p2": "ijg_15_tl_to_br_p2",
    "inclined_jungle_ground_15_top_left_to_bottom_right_p3": "ijg_15_tl_to_br_p3",
    "inclined_jungle_ground_15_top_left_to_bottom_right_p4": "ijg_15_tl_to_br_p4",
    
            # LOW
    "low_jungle_ground_v1": "ljg_v1",
    "low_jungle_ground_v2": "ljg_v2",
    "low_jungle_ground_v3": "ljg_v3",
    "low_jungle_ground_v4": "ljg_v4",
    
    "triangle_jungle_ground": "tjg",

            # HIGH
    "curved_jungle_ground": "C_jg",
    
        # CHECKER TILES

            # LOW
    "low_checker_v1": "lch_v1",
    "low_checker_v2": "lch_v2",
    "low_checker_v3": "lch_v3",
        
            # HIGH
    "high_checker_v1": "hch_v1",
    "high_checker_v2": "hch_v2",
    "high_checker_v3": "hch_v3",
    "high_checker_v4": "hch_v4",
    "high_checker_v5": "hch_v5",
    "high_checker_v6": "hch_v6",
    "high_checker_v7": "hch_v7",
    "high_checker_v8": "hch_v8",
    "high_checker_v9": "hch_v9",
    "high_checker_v10": "hch_v10",
    "high_checker_v11": "hch_v11",
    "high_checker_v12": "hch_v12",
    "high_checker_v13": "hch_v13",
    "high_checker_v14": "hch_v14",
    
    # -- BRIDGE PIECES --    
    "bridge_support_top_right": "br_s_tr",
    "bridge_support_top_left": "br_s_tl",
    "bridge_two_top_supports": "br_2ts",
    
    # -- PALM TREES, BUSH & FLOWERS --
    "palm_tree_top_left": "pt_tl",
    "palm_tree_top_right": "pt_tr",
    "palm_tree_middle_left": "pt_ml",
    "palm_tree_middle_right": "pt_mr",
    "palm_tree_trunk_classic_background": "pt_tc",
    "palm_tree_trunk_special_background": "pt_ts",
    "palm_tree_trunk_jungle_background_v1": "pt_tj_v1",
    "palm_tree_trunk_jungle_background_v2": "pt_tj_v2",
    "palm_tree_trunk_jungle_background_v3": "pt_tj_v3",
    
    "two_flowers_v1": "f1",
    "two_flowers_v2": "f2",
    "two_flowers_v3": "f3",
    "two_flowers_v4": "f4",
    
    "bush": "B",

    # -- RINGS --
    "top_two_rings": "r_2t",
    "bottom_two_rings": "r_2b",
    "top_left_and_bottom_right_rings": "r_tl_br",
    "bottom_left_and_right_rings": "r_bl_br",
    "top_left_ring": "r_tl",
    "top_right_ring": "r_tr",
    "bottom_left_ring": "r_bl",
    "bottom_right_ring": "r_br",

    # -- SPRINGS --
    "spring_from_bottom_middle": "s_fbm",
    "spring_from_bottom_middle_jungle": "s_fbm_j",
    "spring_from_left_middle": "s_flm",
    "spring_from_left_middle_jungle": "s_flm_j",
    "spring_from_right_middle": "s_frm",
    "spring_from_right_middle_jungle": "s_frm_j",
    "spring_from_bottom_left": "s_fbl",
    "spring_from_bottom_left_jungle": "s_fbl_j",
    "spring_from_bottom_right": "s_fbr",
    "spring_from_bottom_right_jungle": "s_fbr_j",
    
    # -- SPIKES --
    "spike_from_bottom": "S_b",
    "spike_from_bottom_jungle": "S_b_j",
    "spike_from_top": "S_t",
    "spike_from_top_jungle": "S_t_j",

    # I'll assume it's something to block sonic.
    "blocking_thing": "K",

    # -- WATERFALLS -- 
    "waterfall_v1": "W1",
    "waterfall_v2": "W2",
    
    # -- BALLOONS -- 
    "one_balloon_v1": "o_1_1",
    "one_balloon_v2": "o_1_2",
    
    "two_balloon_v1": "o_2_1",
    "two_balloon_v2": "o_2_2",
    "two_balloon_v3": "o_2_3",
    "two_balloon_v4": "o_2_4",
    
    "top_balloon_v1": "o_t_1",
    "bottom_balloon_v1": "o_b_1",
    
    "top_balloon_v2": "o_t_2",
    "bottom_balloon_v2": "o_b_2",
    
    # -- Flag --
    "flag_top": "F_t",
    "flag_middle": "F_m",
    "flag_bottom_classic_background": "F_b_cb",
    "flag_bottom_special_background": "F_b_sb",
    "flag_bottom_jungle_background_v1": "F_b_jb_1",
    "flag_bottom_jungle_background_v2": "F_b_jb_2",
    "flag_bottom_jungle_background_v3": "F_b_jb_3",
    "flag_bottom_jungle_background_v4": "F_b_jb_4",       
    "flag_bottom_jungle_background_v5": "F_b_jb_5",
    

    # -- BACKGROUND TILES --
    "jungle_background_v1": "j_b_1",
    "jungle_background_v2": "j_b_2",
    "jungle_background_v3": "j_b_3",
    
    "background_special": "e",
    "background_special_left": "e_l",
    "background_special_right": "e_r",
    
    "vertical_lines": "v",
    
    "background_tile_1": "-",
    "background_tile_2": "-", 
    "background_tile_3": "-",
    "background_tile_4": "-", 
    "background_tile_5": "-",
    "background_tile_6": "-", 
    "background_tile_7": "-",
    "background_tile_8": "-", 
    "background_tile_9": "-",
    "background_tile_10": "-", 
    "background_tile_11": "-",
    "background_tile_12": "-", 
    "background_tile_13": "-",
    "background_tile_14": "-", 
    "background_tile_15": "-",
    "background_tile_16": "-", 
    "background_tile_17": "-",
    "background_tile_18": "-", 
    "background_tile_19": "-",
    "background_tile_20": "-", 
    "background_tile_21": "-",
    "background_tile_22": "-", 
    "background_tile_23": "-",
    "background_tile_24": "-", 
    "background_tile_25": "-",
    "background_tile_26": "-", 
    "background_tile_27": "-",
    "background_tile_28": "-", 
    "background_tile_29": "-",
    "background_tile_30": "-",
    "background_tile_31": "-", 
    "background_tile_32": "-",
    "background_tile_33": "-",
    "background_tile_34": "-",
    "background_tile_35": "-",
    "background_tile_36": "-",
    "background_tile_37": "-",
    "background_tile_38": "-",
    "background_tile_39": "-",
    "background_tile_40": "-",
    "background_tile_41": "-", 
    "background_tile_42": "-",
    "background_tile_43": "-", 
    "background_tile_44": "-",
    "background_tile_45": "-", 
    "background_tile_46": "-",
    "background_tile_47": "-", 
    "background_tile_48": "-",
    "background_tile_49": "-", 
    "background_tile_50": "-", 
    "background_tile_51": "-", 
    "background_tile_52": "-", 
    "background_tile_53": "-", 
    "background_tile_54": "-", 
    "background_tile_55": "-", 
    "background_tile_56": "-", 
    "background_tile_57": "-", 
    "background_tile_58": "-", 
    "background_tile_59": "-",
    "background_tile_60": "-", 
    "background_tile_61": "-",
    "background_tile_62": "-", 
    "background_tile_63": "-",
    "background_tile_64": "-", 
    "background_tile_65": "-", 
    "background_tile_66": "-", 
    "background_tile_67": "-", 
    "background_tile_68": "-", 
    "background_tile_69": "-", 
    "background_tile_70": "-", 
    "background_tile_71": "-", 
    "background_tile_72": "-", 
    "background_tile_73": "-", 
    "background_tile_74": "-",
    "background_tile_75": "-", 
    "background_tile_76": "-",
    "background_tile_77": "-", 
    "background_tile_78": "-",
    "background_tile_79": "-", 
    "background_tile_80": "-",
    "background_tile_81": "-", 
    "background_tile_82": "-",
    "background_tile_83": "-", 
    "background_tile_84": "-", 
    "background_tile_85": "-", 
    "background_tile_86": "-", 
    "background_tile_87": "-", 
    "background_tile_88": "-", 
    "background_tile_89": "-", 
    "background_tile_90": "-", 
    "background_tile_91": "-", 
    "background_tile_92": "-", 
    "background_tile_93": "-",
    "background_tile_94": "-", 
    "background_tile_95": "-", 
    "background_tile_96": "-", 
}

# -------------------------------------------- LEVEL 3

level_3_sprites = {
    # -- INCLINED / SLOPE PIECES --

        # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": "ig_45_bl_tr",
    "inclined_ground_30_bottom_left_to_top_right_p1": "ig_30_bl_tr_p1",
    "inclined_ground_30_bottom_left_to_top_right_p2": "ig_30_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p1": "ig_15_bl_tr_p1",
    "inclined_ground_15_bottom_left_to_top_right_p2": "ig_15_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p3": "ig_15_bl_tr_p3",
    "inclined_ground_15_bottom_left_to_top_right_p4": "ig_15_bl_tr_p4",
    
        # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": "ig_45_tl_br",
    "inclined_ground_30_top_left_to_bottom_right_p1": "ig_30_tl_br_p1",
    "inclined_ground_30_top_left_to_bottom_right_p2": "ig_30_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p1": "ig_15_tl_br_p1",
    "inclined_ground_15_top_left_to_bottom_right_p2": "ig_15_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p3": "ig_15_tl_br_p3",
    "inclined_ground_15_top_left_to_bottom_right_p4": "ig_15_tl_br_p4",
    
    # -- LOOP & CORNER PIECES --

        # RIGHT SIDE
    "loop_bottom_middle_right": "O_bm_r",
    "loop_bottom_right": "O_br",
    "loop_right_middle_bottom": "O_rm_b",
    "loop_right_middle_top": "O_rm_t",
    "loop_top_right": "O_tr",
    "loop_top_middle_right": "O_tm_r",
    
        # LEFT SIDE
    "loop_bottom_middle_left": "O_bm_l",
    "loop_bottom_left": "O_bl",
    "loop_left_middle_bottom": "O_lm_b",
    "loop_left_middle_top": "O_lm_t",
    "loop_top_left": "O_tl",
    "loop_top_middle_left": "O_tm_l",
    
    # -- GROUND / LAVA GROUND / CHECKER TILES --
    
        # GROUND TILES
        
            # LOW
    "low_ground_v1": "lg_v1",
    "low_ground_v2": "lg_v2",
    "low_ground_v3": "lg_v3",
    "low_ground_v4": "lg_v4",
    
    "triangle_ground": "tg",

            # HIGH
    "curved_ground": "Cg",
    
    "high_ground_v1": "hg_v1",
    "high_ground_v2": "hg_v2",
    "high_ground_v3": "hg_v3",
    "high_ground_v4": "hg_v4",
    "high_ground_v5": "hg_v5",
    "high_ground_v6": "hg_v6",
    "high_ground_v7": "hg_v7",
    
    "high_ground_top_left_grass_v1_1": "hg_tl_gr_v1_1",
    "high_ground_top_left_grass_v2_1": "hg_tl_gr_v2_1",
    "high_ground_top_left_grass_v3_1": "hg_tl_gr_v3_1",
    "high_ground_top_left_grass_v4_1": "hg_tl_gr_v4_1",
    
    "high_ground_top_right_grass_v1_1": "hg_tr_gr_v1_1",
    "high_ground_top_right_grass_v2_1": "hg_tr_gr_v2_1",
    "high_ground_top_right_grass_v3_1": "hg_tr_gr_v3_1",
    "high_ground_top_right_grass_v4_1": "hg_tr_gr_v4_1",
       
        # LAVA GROUND TILES
        
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_lava_ground_45_bottom_left_to_top_right": "ilg_45_bl_to_tr",
    "inclined_lava_ground_30_bottom_left_to_top_right_p1": "ilg_30_bl_to_tr_p1",
    "inclined_lava_ground_30_bottom_left_to_top_right_p2": "ilg_30_bl_to_tr_p2",
    "inclined_lava_ground_15_bottom_left_to_top_right_p1": "ilg_15_bl_to_tr_p1",
    "inclined_lava_ground_15_bottom_left_to_top_right_p2": "ilg_15_bl_to_tr_p2",
    "inclined_lava_ground_15_bottom_left_to_top_right_p3": "ilg_15_bl_to_tr_p3",
    "inclined_lava_ground_15_bottom_left_to_top_right_p4": "ilg_15_bl_to_tr_p4",
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_lava_ground_45_top_left_to_bottom_right": "ilg_45_tl_to_br",
    "inclined_lava_ground_30_top_left_to_bottom_right_p1": "ilg_30_tl_to_br_p1",
    "inclined_lava_ground_30_top_left_to_bottom_right_p2": "ilg_30_tl_to_br_p2",
    "inclined_lava_ground_15_top_left_to_bottom_right_p1": "ilg_15_tl_to_br_p1",
    "inclined_lava_ground_15_top_left_to_bottom_right_p2": "ilg_15_tl_to_br_p2",
    "inclined_lava_ground_15_top_left_to_bottom_right_p3": "ilg_15_tl_to_br_p3",
    "inclined_lava_ground_15_top_left_to_bottom_right_p4": "ilg_15_tl_to_br_p4",
    
            # LOW
    "low_lava_ground_v1": "llg_v1",
    "low_lava_ground_v2": "llg_v2",
    "low_lava_ground_v3": "llg_v3",
    "low_lava_ground_v4": "llg_v4",
    
    "triangle_lava_ground": "tlg",

            # HIGH
    "curved_lava_ground": "Cl",
    
        # CHECKER TILES

            # LOW (NONE)
        
            # HIGH
    "high_checker_v1": "hc_v1",
    "high_checker_v2": "hc_v2",
    "high_checker_v3": "hc_v3",
    "high_checker_v4": "hc_v4",
    "high_checker_v5": "hc_v5",
    "high_checker_v6": "hc_v6",
    "high_checker_v7": "hc_v7",
    "high_checker_v8": "hc_v8",
    "high_checker_v9": "hc_v9",
    "high_checker_v10": "hc_v10",
    "high_checker_v11": "hc_v11",
    "high_checker_v12": "hc_v12",
    "high_checker_v13": "hc_v13",
    "high_checker_v14": "hc_v14",
    "high_checker_v15": "hc_v15",
    "high_checker_v16": "hc_v16",
    "high_checker_v17": "hc_v17",
    "high_checker_v18": "hc_v18",
    "high_checker_v19": "hc_v19",
    "high_checker_v20": "hc_v20",
    "high_checker_v21": "hc_v21",
    "high_checker_v22": "hc_v22",
    
    # -- LAVA, CACTUS & BARRIL --
    "lava_rock_background": "Lr_b",
    
    "lava_left_top": "L_lt",
    "lava_left_middle": "L_lm",
    "lava_left_bottom": "L_lb",
    
    "lava_right_top": "L_rt",
    "lava_right_middle": "L_rm",
    "lava_right_bottom": "L_rb",
    
    "cactus_body_left_v1": "Q_l_v1",
    "cactus_body_right_v1": "Q_r_v1",
    "cactus_body_right_v2": "Q_r_v2",
    "cactus_body_left_v2": "Q_l_v2",
    "cactus_body_left_v3": "Q_l_v3",
    "cactus_body_right_v3": "Q_r_v3",
    
    "cactus_high_top_left": "Q_h_tl",
    "cactus_high_top_right": "Q_h_tr",
    "cactus_solo_top_left": "Q_s_tl",
    "cactus_solo_top_right": "Q_s_tr",
    
    "cactus_top_left_p1": "Q_tl_p1",
    "cactus_top_right_p1": "Q_tr_p1",
    "cactus_top_left_p2": "Q_tl_p2",
    "cactus_top_right_p2": "Q_tr_p2",
    
    "little_cactus_bottom": "Q_b",
    "little_cactus_top": "Q_t",
    
    "high_cactus_bottom": "Q_h_b",
    "high_cactus_top": "Q_h_t",

    "barril": "B",

    # -- RINGS --
    "top_two_rings": "r_2_t",
    "bottom_two_rings": "r_2_b",
    "top_left_and_bottom_right_rings": "r_tl_br",
    "bottom_left_and_right_rings": "r_bl_r",
    "top_left_ring": "r_tl",
    "top_right_ring": "r_tr",
    "bottom_left_ring": "r_bl",
    "bottom_right_ring": "r_br",

    # -- SPRINGS --
    "spring_from_bottom_middle": "s_fbm",
    "spring_from_bottom_middle_lava_rock_background": "s_fbm_lrb",
    "spring_from_left_middle": "s_flm",
    "spring_from_left_middle_lava_rock_background": "s_flm_lrb",
    "spring_from_right_middle": "s_frm",
    "spring_from_right_middle_lava_rock_background": "s_frm_lrb",
    "spring_from_bottom_left": "s_fbl",
    "spring_from_bottom_left_lava_rock_background": "s_fbl_lrb",
    "spring_from_bottom_right": "s_fbr",
    "spring_from_bottom_right_lava_rock_background": "s_fbr_lrb",
    
    # -- SPIKES --
    "spike_from_bottom": "S_b",
    "spike_from_bottom_lava_rock_background": "S_b_lrb",
    "spike_from_top": "S_t",
    "spike_from_top_lava_rock_background": "S_t_lrb",

    # I'll assume it's something to block sonic.
    "blocking_thing": "K",

    # -- SAND WATERFALLS -- 
    "sand_waterfall_v1": "W_1",
    "sand_waterfall_v2": "W_2",
    
    # -- CLOUDS --
    "cloud": "c",
    
    "cloud_left": "c_l",
    "cloud_right": "c_r",

    # -- BACKGROUND TILES --
    "desert_mountain_background_v1": "dm_b_1",
    "desert_mountain_background_v2": "dm_b_2",
    "desert_mountain_background_left": "dm_b_l",
    "desert_mountain_background_right": "dm_b_r",
    
    "background_special_v1": "e_1",
    "background_special_v2": "e_2",
    
    "vertical_lines": "v",
    
    "background_tile_1": "-",
    "background_tile_2": "-", 
    "background_tile_3": "-",
    "background_tile_4": "-", 
    "background_tile_5": "-",
    "background_tile_6": "-", 
    "background_tile_7": "-",
    "background_tile_8": "-", 
    "background_tile_9": "-",
    "background_tile_10": "-", 
    "background_tile_11": "-",
    "background_tile_12": "-", 
    "background_tile_13": "-",
    "background_tile_14": "-", 
    "background_tile_15": "-",
    "background_tile_16": "-", 
    "background_tile_17": "-",
    "background_tile_18": "-", 
    "background_tile_19": "-",
    "background_tile_20": "-", 
    "background_tile_21": "-",
    "background_tile_22": "-", 
    "background_tile_23": "-",
    "background_tile_24": "-", 
    "background_tile_25": "-",
    "background_tile_26": "-", 
    "background_tile_27": "-",
    "background_tile_28": "-", 
    "background_tile_29": "-",
    "background_tile_30": "-",
    "background_tile_31": "-",
    "background_tile_32": "-",
    "background_tile_33": "-",
    "background_tile_34": "-",
    "background_tile_35": "-",
    "background_tile_36": "-",
    "background_tile_37": "-",
    "background_tile_38": "-",
    "background_tile_39": "-",
    "background_tile_40": "-",
    "background_tile_41": "-", 
    "background_tile_42": "-",
    "background_tile_43": "-", 
    "background_tile_44": "-",
    "background_tile_45": "-", 
    "background_tile_46": "-",
    "background_tile_47": "-", 
    "background_tile_48": "-",
    "background_tile_49": "-", 
    "background_tile_50": "-", 
    "background_tile_51": "-", 
    "background_tile_52": "-", 
    "background_tile_53": "-", 
    "background_tile_54": "-", 
    "background_tile_55": "-", 
    "background_tile_56": "-", 
    "background_tile_57": "-", 
    "background_tile_58": "-", 
    "background_tile_59": "-",
    "background_tile_60": "-", 
    "background_tile_61": "-",
    "background_tile_62": "-", 
    "background_tile_63": "-",
    "background_tile_64": "-", 
    "background_tile_65": "-", 
    "background_tile_66": "-", 
    "background_tile_67": "-", 
    "background_tile_68": "-", 
    "background_tile_69": "-", 
    "background_tile_70": "-", 
    "background_tile_71": "-", 
    "background_tile_72": "-", 
    "background_tile_73": "-", 
    "background_tile_74": "-",
    "background_tile_75": "-", 
    "background_tile_76": "-",
    "background_tile_77": "-", 
    "background_tile_78": "-",
    "background_tile_79": "-", 
    "background_tile_80": "-",
    "background_tile_81": "-", 
    "background_tile_82": "-",
    "background_tile_83": "-", 
    "background_tile_84": "-", 
    "background_tile_85": "-", 
    "background_tile_86": "-", 
    "background_tile_87": "-", 
    "background_tile_88": "-", 
    "background_tile_89": "-", 
    "background_tile_90": "-", 
    "background_tile_91": "-", 
    "background_tile_92": "-", 
    "background_tile_93": "-",
    "background_tile_94": "-", 
    "background_tile_95": "-", 
    "background_tile_96": "-", 
    "background_tile_97": "-", 
    "background_tile_98": "-", 
    "background_tile_99": "-", 
    "background_tile_100": "-", 
    "background_tile_101": "-", 
    "background_tile_102": "-", 
    "background_tile_103": "-", 
    "background_tile_104": "-", 
    "background_tile_105": "-", 
    "background_tile_106": "-", 
}

# -------------------------------------------- LEVEL 4

level_4_sprites = {
    # -- INCLINED / SLOPE PIECES --

        # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": "ig_45_bl_tr",
    "inclined_ground_30_bottom_left_to_top_right_p1": "ig_30_bl_tr_p1",
    "inclined_ground_30_bottom_left_to_top_right_p2": "ig_30_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p1": "ig_15_bl_tr_p1",
    "inclined_ground_15_bottom_left_to_top_right_p2": "ig_15_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p3": "ig_15_bl_tr_p3",
    "inclined_ground_15_bottom_left_to_top_right_p4": "ig_15_bl_tr_p4",
    
        # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": "ig_45_tl_br",
    "inclined_ground_30_top_left_to_bottom_right_p1": "ig_30_tl_br_p1",
    "inclined_ground_30_top_left_to_bottom_right_p2": "ig_30_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p1": "ig_15_tl_br_p1",
    "inclined_ground_15_top_left_to_bottom_right_p2": "ig_15_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p3": "ig_15_tl_br_p3",
    "inclined_ground_15_top_left_to_bottom_right_p4": "ig_15_tl_br_p4",
    
    # -- LOOP & CORNER PIECES --

        # RIGHT SIDE
    "loop_bottom_middle_right": "O_bm_r",
    "loop_bottom_right": "O_br",
    "loop_right_middle_bottom": "O_rm_b",
    "loop_right_middle_top": "O_rm_t",
    "loop_top_right": "O_tr",
    "loop_top_middle_right": "O_tm_r",
    
        # LEFT SIDE
    "loop_bottom_middle_left": "O_bm_l",
    "loop_bottom_left": "O_bl",
    "loop_left_middle_bottom": "O_lm_b",
    "loop_left_middle_top": "O_lm_t",
    "loop_top_left": "O_tl",
    "loop_top_middle_left": "O_tml",
    
    # -- GROUND / ICE GROUND / CHECKER TILES --
    
        # GROUND TILES
        
            # LOW
    "low_ground_v1": "lg_v1",
    "low_ground_v2": "lg_v2",
    "low_ground_v3": "lg_v3",
    "low_ground_v4": "lg_v4",
    
    "triangle_ground": "tg",

            # HIGH
    "curved_ground": "Cg",
    
    "high_ground_v1": "hg_v1",
    "high_ground_v2": "hg_v2",
    "high_ground_v3": "hg_v3",
    "high_ground_v4": "hg_v4",
    "high_ground_v5": "hg_v5",
    "high_ground_v6": "hg_v6",
    "high_ground_v7": "hg_v7",
    "high_ground_v8": "hg_v8",
    
    "high_ground_top_left_grass_v1": "hg_tl_gr_v1",
    "high_ground_top_left_grass_v2": "hg_tl_gr_v2",
    "high_ground_top_left_grass_v3": "hg_tl_gr_v3",
    "high_ground_top_left_grass_v4": "hg_tl_gr_v4",
    
    "high_ground_top_right_grass_v1": "hg_tr_gr_v1",
    "high_ground_top_right_grass_v2": "hg_tr_gr_v2",
    "high_ground_top_right_grass_v3": "hg_tr_gr_v3",
    "high_ground_top_right_grass_v4": "hg_tr_gr_v4",
       
        # ICE GROUND TILES
        
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_ice_ground_45_bottom_left_to_top_right": "iig_45_bl_to_tr",
    "inclined_ice_ground_30_bottom_left_to_top_right_p1": "iig_30_bl_to_tr_p1",
    "inclined_ice_ground_30_bottom_left_to_top_right_p2": "iig_30_bl_to_tr_p2",
    "inclined_ice_ground_15_bottom_left_to_top_right_p1": "iig_15_bl_to_tr_p1",
    "inclined_ice_ground_15_bottom_left_to_top_right_p2": "iig_15_bl_to_tr_p2",
    "inclined_ice_ground_15_bottom_left_to_top_right_p3": "iig_15_bl_to_tr_p3",
    "inclined_ice_ground_15_bottom_left_to_top_right_p4": "iig_15_bl_to_tr_p4",
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_ice_ground_45_top_left_to_bottom_right": "iig_45_tl_to_br",
    "inclined_ice_ground_30_top_left_to_bottom_right_p1": "iig_30_tl_to_br_p1",
    "inclined_ice_ground_30_top_left_to_bottom_right_p2": "iig_30_tl_to_br_p2",
    "inclined_ice_ground_15_top_left_to_bottom_right_p1": "iig_15_tl_to_br_p1",
    "inclined_ice_ground_15_top_left_to_bottom_right_p2": "iig_15_tl_to_br_p2",
    "inclined_ice_ground_15_top_left_to_bottom_right_p3": "iig_15_tl_to_br_p3",
    "inclined_ice_ground_15_top_left_to_bottom_right_p4": "iig_15_tl_to_br_p4",
    
            # LOW
    "low_ice_ground_v1": "lig_v1",
    "low_ice_ground_v2": "lig_v2",
    "low_ice_ground_v3": "lig_v3",
    "low_ice_ground_v4": "lig_v4",
    
    "triangle_ice_ground": "tig",

            # HIGH
    "curved_ice_ground": "Cig",
    
        # CHECKER TILES

            # LOW
    "low_checker_v1": "lc_v1",
    "low_checker_v2": "lc_v2",
        
            # HIGH
    "high_checker_v1": "hc_v1",
    "high_checker_v2": "hc_v2",
    "high_checker_v3": "hc_v3",
    "high_checker_v4": "hc_v4",
    "high_checker_v5": "hc_v5",
    "high_checker_v6": "hc_v6",
    "high_checker_v7": "hc_v7",
    "high_checker_v8": "hc_v8",
    "high_checker_v9": "hc_v9",
    "high_checker_v10": "hc_v10",
    "high_checker_v11": "hc_v11",
    "high_checker_v12": "hc_v12",
    "high_checker_v13": "hc_v13",
    "high_checker_v14": "hc_v14",
    "high_checker_v15": "hc_v15",
    "high_checker_v16": "hc_v16",
    "high_checker_v17": "hc_v17",
    "high_checker_v18": "hc_v18",
    "high_checker_v19": "hc_v19",
    "high_checker_v20": "hc_v20",
    "high_checker_v21": "hc_v21",
    
    # -- ICE, TREE & GEMS --
    "two_vertical_gems": "G_2v",
    
    "four_gems_v1": "G_4v1",
    "four_gems_v2": "G_4v2",
    "four_gems_v3": "G_4v3",
    "four_gems_v4": "G_4v4",
    
    "bottom_right_gem": "G_br",
    "bottom_left_gem": "G_bl",
    "bottom_two_gem": "G_bt",
    
    "tree_top_left": "T_tl",
    "tree_top_right": "T_tr",
    "tree_middle_left": "T_ml",
    "tree_middle_right": "T_mr",
    "tree_trunk_left": "T_tl",
    "tree_trunk_right": "T_tr",
    "tree_bottom_left_classic_background": "T_bl",
    "tree_bottom_right_classic_background": "T_br",
    "tree_bottom_left_special_background_v1": "T_bl_s1",
    "tree_bottom_right_special_background_v1": "T_br_s1",
    "tree_bottom_left_snow_background": "T_bl_s",
    "tree_bottom_right_snow_background": "T_br_s",
    "tree_bottom_left_mountain_background": "T_bl_m",
    "tree_bottom_right_mountain_background": "T_br_m",
    "tree_bottom_left_special_background_v2": "T_bl_s2",
    "tree_bottom_right_special_background_v2": "T_br_s2",
    
    # -- RINGS --
    "top_two_rings": "r_2t",
    "bottom_two_rings": "r_2b",
    "top_left_and_bottom_right_rings": "r_tl_br",
    "bottom_left_and_right_rings": "r_bl_br",
    "top_left_ring": "r_tl",
    "top_right_ring": "r_tr",
    "bottom_left_ring": "r_bl",
    "bottom_right_ring": "r_br",

    # -- SPRINGS --
    "spring_from_bottom_middle": "s_bm",
    "spring_from_bottom_middle_ice_rock_background": "s_bm_ir",
    "spring_from_left_middle": "s_lm",
    "spring_from_left_middle_ice_rock_background": "s_lm_ir",
    "spring_from_right_middle": "s_rm",
    "spring_from_right_middle_ice_rock_background": "s_rm_ir",
    "spring_from_bottom_left": "s_bl",
    "spring_from_bottom_left_ice_rock_background": "s_bl_ir",
    "spring_from_bottom_right": "s_br",
    "spring_from_bottom_right_ice_rock_background": "s_br_ir",
    
    # -- SPIKES --
    "spike_from_bottom": "S_fb",
    "spike_from_bottom_ice_rock_background": "S_fb_ir",
    "spike_from_top": "S_ft",
    "spike_from_top_ice_rock_background": "S_ft_ir",
    
    "ice_spike": "IS",
    "ice_spike_top_left": "IS_tl",
    "ice_spike_top_right": "IS_tr",

    # I'll assume it's something to block sonic.
    "blocking_thing": "K",
    
    # -- CLOUDS / SNOW --
    "snow_v1": "N_v1",
    "snow_v2": "N_v2",
    "snow_v3": "N_v3",
    "snow_v4": "N_v4",
    "snow_v5": "N_v5",
    "snow_v6": "N_v6",
    "snow_v7": "N_v7",
    "snow_v8": "N_v8",
    "snow_v9": "N_v9",
    "snow_v10": "N_v10",

    # -- BACKGROUND TILES --
    "ice_mountain_background_v1": "M_i_v1",
    "ice_mountain_background_v2": "M_i_v2",
    
    "background_special_v1": "e_1",
    "background_special_v2": "e_2",
    "background_special_v3": "e_3",
    
    "snow_background": "n",
    
    "vertical_lines": "v",
    
    "background_tile_1": "-",
    "background_tile_2": "-", 
    "background_tile_3": "-",
    "background_tile_4": "-", 
    "background_tile_5": "-",
    "background_tile_6": "-", 
    "background_tile_7": "-",
    "background_tile_8": "-", 
    "background_tile_9": "-",
    "background_tile_10": "-", 
    "background_tile_11": "-",
    "background_tile_12": "-", 
    "background_tile_13": "-",
    "background_tile_14": "-", 
    "background_tile_15": "-",
    "background_tile_16": "-", 
    "background_tile_17": "-",
    "background_tile_18": "-", 
    "background_tile_19": "-",
    "background_tile_20": "-", 
    "background_tile_21": "-",
    "background_tile_22": "-", 
    "background_tile_23": "-",
    "background_tile_24": "-", 
    "background_tile_25": "-",
    "background_tile_26": "-", 
    "background_tile_27": "-",
    "background_tile_28": "-", 
    "background_tile_29": "-",
    "background_tile_30": "-",
    "background_tile_31": "-",
    "background_tile_32": "-",
    "background_tile_33": "-",
    "background_tile_34": "-",
    "background_tile_35": "-",
    "background_tile_36": "-",
    "background_tile_37": "-",
    "background_tile_38": "-",
    "background_tile_39": "-",
    "background_tile_40": "-",
    "background_tile_41": "-",
    "background_tile_42": "-",
    "background_tile_43": "-",
    "background_tile_44": "-",
    "background_tile_45": "-",
    "background_tile_46": "-",
    "background_tile_47": "-",
    "background_tile_48": "-",
    "background_tile_49": "-",
    "background_tile_50": "-", 
    "background_tile_51": "-",
    "background_tile_52": "-", 
    "background_tile_53": "-",
    "background_tile_54": "-", 
    "background_tile_55": "-", 
    "background_tile_56": "-", 
    "background_tile_57": "-", 
    "background_tile_58": "-", 
    "background_tile_59": "-", 
    "background_tile_60": "-", 
    "background_tile_61": "-", 
    "background_tile_62": "-", 
    "background_tile_63": "-", 
    "background_tile_64": "-", 
    "background_tile_65": "-", 
    "background_tile_66": "-",
    "background_tile_67": "-", 
    "background_tile_68": "-",
    "background_tile_69": "-", 
    "background_tile_70": "-",
    "background_tile_71": "-", 
    "background_tile_72": "-",
    "background_tile_73": "-", 
    "background_tile_74": "-",
    "background_tile_75": "-", 
    "background_tile_76": "-", 
    "background_tile_77": "-", 
    "background_tile_78": "-", 
    "background_tile_79": "-", 
    "background_tile_80": "-", 
    "background_tile_81": "-", 
    "background_tile_82": "-", 
    "background_tile_83": "-", 
    "background_tile_84": "-", 
    "background_tile_85": "-",
    "background_tile_86": "-", 
    "background_tile_87": "-", 
    "background_tile_88": "-", 
    "background_tile_89": "-", 
    "background_tile_90": "-", 
    "background_tile_91": "-", 
    "background_tile_92": "-", 
    "background_tile_93": "-", 
    "background_tile_94": "-", 
    "background_tile_95": "-", 
    "background_tile_96": "-", 
    "background_tile_97": "-", 
    "background_tile_98": "-", 
}

# -------------------------------------------- LEVEL 5

level_5_sprites = {
    # -- INCLINED / SLOPE PIECES --

        # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": "ig_45_bl_tr",
    "inclined_ground_30_bottom_left_to_top_right_p1": "ig_30_bl_tr_p1",
    "inclined_ground_30_bottom_left_to_top_right_p2": "ig_30_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p1": "ig_15_bl_tr_p1",
    "inclined_ground_15_bottom_left_to_top_right_p2": "ig_15_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p3": "ig_15_bl_tr_p3",
    "inclined_ground_15_bottom_left_to_top_right_p4": "ig_15_bl_tr_p4",
    
        # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": "ig_45_tl_br",
    "inclined_ground_30_top_left_to_bottom_right_p1": "ig_30_tl_br_p1",
    "inclined_ground_30_top_left_to_bottom_right_p2": "ig_30_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p1": "ig_15_tl_br_p1",
    "inclined_ground_15_top_left_to_bottom_right_p2": "ig_15_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p3": "ig_15_tl_br_p3",
    "inclined_ground_15_top_left_to_bottom_right_p4": "ig_15_tl_br_p4",
    
    # -- LOOP & CORNER PIECES --

        # LOOP
    "loop_top_left": "O_tl",
    "loop_top_right": "O_tr",
    "loop_bottom_left": "O_bl",
    "loop_bottom_right": "O_br",
        
    "double_horizontal_wall_v1": "w_2h_v1",
    "double_horizontal_wall_v2": "w_2h_v2",
    "double_horizontal_wall_v3": "w_2h_v3",
    
    "double_vertical_wall_v1": "w_2v_v1",
    "double_vertical_wall_v2": "w_2v_v2",
    "double_vertical_wall_v3": "w_2v_v3",
    
    "up_entry_bottom_wall": "w_ue_b",
    "bottom_entry_top_wall": "w_be_t",
    "right_entry_left_wall": "w_re_l",
    "left_entry_right_wall": "w_le_r",
    "all_entry": "w_ae",

        # WALL
    "left_wall": "H_l",
    "right_wall": "H_r",
    "double_vertical_wall": "H_2v",
    
    # -- GROUND / DARK GROUND / CHECKER TILES --
    
        # GROUND TILES
        
            # LOW
    "low_ground_v1": "lg_v1",
    "low_ground_v2": "lg_v2",
    "low_ground_v3": "lg_v3",
    "low_ground_v4": "lg_v4",
    
    "triangle_ground": "tg",

            # HIGH
    "curved_ground": "Cg",
    
    "high_ground_v1": "hg_v1",
    "high_ground_v2": "hg_v2",
    "high_ground_v3": "hg_v3",
    "high_ground_v4": "hg_v4",
    "high_ground_v5": "hg_v5",
    "high_ground_v6": "hg_v6",
    "high_ground_v7": "hg_v7",
    
    
    "high_ground_top_left_grass_v1": "hg_tl_gr_v1",
    "high_ground_top_left_grass_v2": "hg_tl_gr_v2",
    "high_ground_top_left_grass_v3": "hg_tl_gr_v3",
    
    "high_ground_top_right_grass_v1": "hg_tr_gr_v1",
    "high_ground_top_right_grass_v2": "hg_tr_gr_v2",
    "high_ground_top_right_grass_v3": "hg_tr_gr_v3",
    "high_ground_top_right_grass_v4": "hg_tr_gr_v4",
       
        # DARK GROUND TILES
        
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_dark_ground_45_bottom_left_to_top_right": "idg_45_bl_tr",
    "inclined_dark_ground_30_bottom_left_to_top_right_p1": "idg_30_bl_tr_p1",
    "inclined_dark_ground_30_bottom_left_to_top_right_p2": "idg_30_bl_tr_p2",
    "inclined_dark_ground_15_bottom_left_to_top_right_p1": "idg_15_bl_tr_p1",
    "inclined_dark_ground_15_bottom_left_to_top_right_p2": "idg_15_bl_tr_p2",
    "inclined_dark_ground_15_bottom_left_to_top_right_p3": "idg_15_bl_tr_p3",
    "inclined_dark_ground_15_bottom_left_to_top_right_p4": "idg_15_bl_tr_p4",
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_dark_ground_45_top_left_to_bottom_right": "idg_45_tl_br",
    "inclined_dark_ground_30_top_left_to_bottom_right_p1": "idg_30_tl_br_p1",
    "inclined_dark_ground_30_top_left_to_bottom_right_p2": "idg_30_tl_br_p2",
    "inclined_dark_ground_15_top_left_to_bottom_right_p1": "idg_15_tl_br_p1",
    "inclined_dark_ground_15_top_left_to_bottom_right_p2": "idg_15_tl_br_p2",
    "inclined_dark_ground_15_top_left_to_bottom_right_p3": "idg_15_tl_br_p3",
    "inclined_dark_ground_15_top_left_to_bottom_right_p4": "idg_15_tl_br_p4",
    
            # LOW
    "low_dark_ground_v1": "ldg_v1",
    "low_dark_ground_v2": "ldg_v2",
    "low_dark_ground_v3": "ldg_v3",
    "low_dark_ground_v4": "ldg_v4",
    
    "triangle_dark_ground": "tdg",

            # HIGH
    "curved_dark_ground": "Cdg",
    
        # CHECKER TILES

            # LOW (NONE)
        
            # HIGH
    "high_checker_v1": "hc_v1",
    "high_checker_v2": "hc_v2",
    "high_checker_v3": "hc_v3",
    
    # -- LAVA TILES -- 
    "lava_v1": "L_1",
    "lava_v2": "L_2",
    
    "lava_waterfall_top": "WL_t",
    "lava_waterfall_bottom": "WL_b",
    
    "lava_classic_background_v1": "YLcb_v1",
    "lava_classic_background_v2": "YLcb_v2",
    "lava_classic_background_v3": "YLcb_v3",
    "lava_special_background": "YLsb",
    
    # -- RINGS --
    "top_two_rings": "r_2t",
    "bottom_two_rings": "r_2b",
    "top_left_and_bottom_right_rings": "r_tl_br",
    "bottom_left_and_right_rings": "r_bl_br",
    "top_left_ring": "r_tl",
    "top_right_ring": "r_tr",
    "bottom_left_ring": "r_bl",
    "bottom_right_ring": "r_br",

    # -- SPRINGS --
    "spring_from_bottom_middle": "s_bm",
    "spring_from_bottom_middle_dark_rock_background": "s_bm_dr",
    "spring_from_left_middle": "s_lm",
    "spring_from_left_middle_dark_rock_background": "s_lm_dr",
    "spring_from_right_middle": "s_rm",
    "spring_from_right_middle_dark_rock_background": "s_rm_dr",
    "spring_from_bottom_left": "s_bl",
    "spring_from_bottom_left_dark_rock_background": "s_bl_dr",
    "spring_from_bottom_right": "s_br",
    "spring_from_bottom_right_dark_rock_background": "s_br_dr",
    
    # -- SPIKES --
    "spike_from_bottom": "S_b",
    "spike_from_bottom_dark_rock_background": "S_b_dr",
    "spike_from_top": "S_t",
    "spike_from_top_dark_rock_background": "S_t_dr",

    # I'll assume it's something to block sonic.
    "blocking_thing": "K",

    # -- CLOUDS --
    "cloud": "c",
    
    "cloud_left": "c_l",
    "cloud_right": "c_r",

    # -- BACKGROUND TILES --
    "rock_background_from_bottom_v1": "R_b_v1",
    "rock_background_from_bottom_v2": "R_b_v2",
    "rock_background_from_bottom_v3": "R_b_v3",
    "rock_background_from_bottom_v4": "R_b_v4",
    "rock_background_from_bottom_v5": "R_b_v5",
    "rock_background_from_bottom_v6": "R_b_v6",
    "rock_background_from_bottom_v7": "R_b_v7",
    "rock_background_from_bottom_v8": "R_b_v8",
    "rock_background_from_bottom_v9": "R_b_v9",
    "rock_background_from_bottom_v10": "R_b_v10",
    "rock_background_from_bottom_v11": "R_b_v11",
    "rock_background_from_bottom_v12": "R_b_v12",
    "rock_background_from_bottom_v13": "R_b_v13",
    
    "rock_background_from_top_v1": "R_t_v1",
    "rock_background_from_top_v2": "R_t_v2",
    "rock_background_from_top_v3": "R_t_v3",
    "rock_background_from_top_v4": "R_t_v4",
    "rock_background_from_top_v5": "R_t_v5",
    "rock_background_from_top_v6": "R_t_v6",
    "rock_background_from_top_v7": "R_t_v7",
    "rock_background_from_top_v8": "R_t_v8",
    "rock_background_from_top_v9": "R_t_v9",
    "rock_background_from_top_v10": "R_t_v10",
    "rock_background_from_top_v11": "R_t_v11",
    "rock_background_from_top_v12": "R_t_v12",
    "rock_background_from_top_v13": "R_t_v13",
    
    "dark_mountain_background_p1": "M_p1",
    "dark_mountain_background_p2": "M_p2",
    "dark_mountain_background_p3": "M_p3",
    "dark_mountain_background_p4": "M_p4",
    "dark_mountain_background_v1": "M_v1",
    "dark_mountain_background_v2": "M_v2",
    "dark_mountain_background_v3": "M_v3",
    
    "classic_background_tile": "e",
    
    "ondulations": "o",
    
    "special_background_tile_vertical_left": "E_v_l",
    "special_background_tile_vertical_right": "E_v_r",
    "special_background_tile_vertical_middle_right": "E_v_m_r",
    "special_background_tile_vertical_middle_left": "E_v_m_l",
    "special_background_tile_triangle_from_bottom": "E_t_b",
    "special_background_tile_triangle_from_top": "E_t_t",
    "special_background_tile_triangles_from_top_left": "E_t_t_l",
    "special_background_tile_triangles_from_top_right": "E_t_t_r",
    "special_background_tile_curved_in_top_right_v1": "E_c_i_t_r_v1",
    "special_background_tile_curved_in_top_left_v1": "E_c_i_t_l_v1",
    "special_background_tile_curved_in_bottom_right_v1": "E_c_i_b_r_v1",
    "special_background_tile_curved_in_bottom_left_v1": "E_c_i_b_l_v1",
    "special_background_tile_curved_in_top_left_v2": "E_c_i_t_l_v2",
    "special_background_tile_curved_in_top_right_v2": "E_c_i_t_r_v2",
    "special_background_tile_curved_in_bottom_left_v2": "E_c_i_b_l_v2",
    "special_background_tile_curved_in_bottom_right_v2": "E_c_i_b_r_v2",
    "special_background_tile_triangle_from_bottom_left_to_top_right_v1": "E_t_b_l_t_r_v1",
    "special_background_tile_triangle_from_top_left_to_bottom_right_v1": "E_t_t_l_b_r_v1",
    "special_background_tile_triangle_from_top_left_to_bottom_right_v2": "E_t_t_l_b_r_v2",
    "special_background_tile_triangle_from_bottom_left_to_top_right_v2": "E_t_b_l_t_r_v2",
    "special_background_tile_ondulations_v1": "E_o_v1",
    "special_background_tile_ondulations_v2": "E_o_v2",
    "special_background_tile_ondulations_v3": "E_o_v3",
    "special_background_tile_ondulations_v4": "E_o_v4",
    
    "background_tile_1": "-",
    "background_tile_2": "-", 
    "background_tile_3": "-",
    "background_tile_4": "-", 
    "background_tile_5": "-",
    "background_tile_6": "-", 
    "background_tile_7": "-",
    "background_tile_8": "-", 
    "background_tile_9": "-",
    "background_tile_10": "-", 
    "background_tile_11": "-",
    "background_tile_12": "-", 
    "background_tile_13": "-",
    "background_tile_14": "-", 
    "background_tile_15": "-",
    "background_tile_16": "-", 
    "background_tile_17": "-",
    "background_tile_18": "-", 
    "background_tile_19": "-",
    "background_tile_20": "-", 
    "background_tile_21": "-",
    "background_tile_22": "-", 
    "background_tile_23": "-",
    "background_tile_24": "-", 
    "background_tile_25": "-",
    "background_tile_26": "-", 
    "background_tile_27": "-",
    "background_tile_28": "-", 
    "background_tile_29": "-",
    "background_tile_30": "-",
    "background_tile_31": "-",
    "background_tile_32": "-",
    "background_tile_33": "-",
    "background_tile_34": "-",
    "background_tile_35": "-",
    "background_tile_36": "-",
    "background_tile_37": "-",
    "background_tile_38": "-",
    "background_tile_39": "-",
    "background_tile_40": "-",
    "background_tile_41": "-",
    "background_tile_42": "-", 
    "background_tile_43": "-",
    "background_tile_44": "-", 
    "background_tile_45": "-",
    "background_tile_46": "-", 
    "background_tile_47": "-",
    "background_tile_48": "-", 
    "background_tile_49": "-",
    "background_tile_50": "-", 
    "background_tile_51": "-", 
    "background_tile_52": "-", 
    "background_tile_53": "-", 
    "background_tile_54": "-", 
    "background_tile_55": "-", 
    "background_tile_56": "-", 
    "background_tile_57": "-", 
    "background_tile_58": "-", 
    "background_tile_59": "-", 
    "background_tile_60": "-",
    "background_tile_61": "-",
    "background_tile_62": "-", 
    "background_tile_63": "-",
    "background_tile_64": "-", 
    "background_tile_65": "-",
    "background_tile_66": "-", 
    "background_tile_67": "-", 
    "background_tile_68": "-", 
    "background_tile_69": "-", 
    "background_tile_70": "-", 
    "background_tile_71": "-", 
    "background_tile_72": "-", 
    "background_tile_73": "-", 
    "background_tile_74": "-", 
    "background_tile_75": "-", 
    "background_tile_76": "-",
    "background_tile_77": "-", 
    "background_tile_78": "-",
    "background_tile_79": "-", 
    "background_tile_80": "-",
    "background_tile_81": "-", 
    "background_tile_82": "-",
    "background_tile_83": "-", 
    "background_tile_84": "-",
    "background_tile_85": "-", 
    "background_tile_86": "-", 
    "background_tile_87": "-", 
    "background_tile_88": "-", 
}

# -------------------------------------------- LEVEL 6

level_6_sprites = {
    # -- INCLINED / SLOPE PIECES --

        # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right":  "ig_45_bl_tr",
    "inclined_ground_30_bottom_left_to_top_right_p1": "ig_30_bl_tr_p1",
    "inclined_ground_30_bottom_left_to_top_right_p2": "ig_30_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p1": "ig_15_bl_tr_p1",
    "inclined_ground_15_bottom_left_to_top_right_p2": "ig_15_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p3": "ig_15_bl_tr_p3",
    "inclined_ground_15_bottom_left_to_top_right_p4": "ig_15_bl_tr_p4",
    
        # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": "ig_45_tl_br",
    "inclined_ground_30_top_left_to_bottom_right_p1": "ig_30_tl_br_p1",
    "inclined_ground_30_top_left_to_bottom_right_p2": "ig_30_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p1": "ig_15_tl_br_p1",
    "inclined_ground_15_top_left_to_bottom_right_p2": "ig_15_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p3": "ig_15_tl_br_p3",
    "inclined_ground_15_top_left_to_bottom_right_p4": "ig_15_tl_br_p4",
    
    # -- LOOP & CORNER PIECES --

        # RIGHT SIDE
    "loop_bottom_middle_right": "O_bm_r",
    "loop_bottom_right": "O_br",
    "loop_right_middle_bottom": "O_rm_b",
    "loop_right_middle_top": "O_rm_t",
    "loop_top_right": "O_tr",
    "loop_top_middle_right": "O_tm_r",
    
        # LEFT SIDE
    "loop_bottom_middle_left": "O_bm_l",
    "loop_bottom_left": "O_bl",
    "loop_left_middle_bottom": "O_lm_b",
    "loop_left_middle_top": "O_lm_t",
    "loop_top_left": "O_tl",
    "loop_top_middle_left": "O_tm_l",
    
    # -- GROUND / RAINY GROUND / CHECKER TILES --
    
        # GROUND TILES
        
            # LOW
    "low_ground_v1": "lg_v1",
    "low_ground_v2": "lg_v2",
    "low_ground_v3": "lg_v3",
    "low_ground_v4": "lg_v4",
    
    "triangle_ground": "tg",

            # HIGH
    "curved_ground": "Cg",
    
    "high_ground_v1": "hg_v1",
    "high_ground_v2": "hg_v2",
    "high_ground_v3": "hg_v3",
    "high_ground_v4": "hg_v4",
    "high_ground_v5": "hg_v5",
    "high_ground_v6": "hg_v6",
    "high_ground_v7": "hg_v7",
    "high_ground_v8": "hg_v8",
    
    "high_ground_top_left_grass_v1": "hg_tl_gr_v1",
    "high_ground_top_left_grass_v2": "hg_tl_gr_v2",
    "high_ground_top_left_grass_v3": "hg_tl_gr_v3",
    "high_ground_top_left_grass_v4": "hg_tl_gr_v4",
    
    "high_ground_top_right_grass_v1": "hg_tr_gr_v1",
    "high_ground_top_right_grass_v2": "hg_tr_gr_v2",
    "high_ground_top_right_grass_v3": "hg_tr_gr_v3",
    "high_ground_top_right_grass_v4": "hg_tr_gr_v4",
       
        # RAINY GROUND TILES
        
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_rain_ground_45_bottom_left_to_top_right": "irg_45_bl_to_tr",
    "inclined_rain_ground_30_bottom_left_to_top_right_p1": "irg_30_bl_to_tr_p1",
    "inclined_rain_ground_30_bottom_left_to_top_right_p2": "irg_30_bl_to_tr_p2",
    "inclined_rain_ground_15_bottom_left_to_top_right_p1": "irg_15_bl_to_tr_p1",
    "inclined_rain_ground_15_bottom_left_to_top_right_p2": "irg_15_bl_to_tr_p2",
    "inclined_rain_ground_15_bottom_left_to_top_right_p3": "irg_15_bl_to_tr_p3",
    "inclined_rain_ground_15_bottom_left_to_top_right_p4": "irg_15_bl_to_tr_p4",
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_rain_ground_45_top_left_to_bottom_right": "irg_45_tl_to_br",
    "inclined_rain_ground_30_top_left_to_bottom_right_p1": "irg_30_tl_to_br_p1",
    "inclined_rain_ground_30_top_left_to_bottom_right_p2": "irg_30_tl_to_br_p2",
    "inclined_rain_ground_15_top_left_to_bottom_right_p1": "irg_15_tl_to_br_p1",
    "inclined_rain_ground_15_top_left_to_bottom_right_p2": "irg_15_tl_to_br_p2",
    "inclined_rain_ground_15_top_left_to_bottom_right_p3": "irg_15_tl_to_br_p3",
    "inclined_rain_ground_15_top_left_to_bottom_right_p4": "irg_15_tl_to_br_p4",
    
            # LOW
    "low_rain_ground_v1": "lr_v1",
    "low_rain_ground_v2": "lr_v2",
    "low_rain_ground_v3": "lr_v3",
    "low_rain_ground_v4": "lr_v4",
    
    "triangle_rain_ground": "trg",

            # HIGH
    "curved_rain_ground": "Crg",
    
        # CHECKER TILES

            # LOW (None)
        
            # HIGH
    "high_checker_v1": "hc_v1",
    "high_checker_v2": "hc_v2",
    "high_checker_v3": "hc_v3",
    "high_checker_v4": "hc_v4",
    "high_checker_v5": "hc_v5",
    "high_checker_v6": "hc_v6",
    "high_checker_v7": "hc_v7",
    "high_checker_v8": "hc_v8",
    "high_checker_v9": "hc_v9",
    "high_checker_v10": "hc_v10",
    "high_checker_v11": "hc_v11",
    "high_checker_v12": "hc_v12",
    "high_checker_v13": "hc_v13",
    "high_checker_v14": "hc_v14",
    "high_checker_v15": "hc_v15",
    "high_checker_v16": "hc_v16",
    "high_checker_v17": "hc_v17",
    "high_checker_v18": "hc_v18",
    "high_checker_v19": "hc_v19",
    "high_checker_v20": "hc_v20",
    "high_checker_v21": "hc_v21",
    "high_checker_v22": "hc_v22",
    "high_checker_v23": "hc_v23",
    
    # -- CLIMATE, TREE & PLANT --
    "little_rain_bottom_right": "R_l_br",
    "middle_rain_bottom_right": "R_m_br",
    "large_rain_bottom_right": "R_l_br",
    "little_rain_bottom_left": "R_l_bl",
    "middle_rain_bottom_left": "R_m_bl",
    "large_rain_bottom_left": "R_l_bl",
    "rain_column_left": "R_cl",
    "rain_column_right": "R_cr",
    
    "waterfall_top": "W_t",
    "waterfall_bottom": "W_b",
    
    "tree_top_left": "T_t_l",
    "tree_top_middle": "T_t_m",
    "tree_top_right": "T_t_r",
    "tree_trunk": "T_tr",
    
    "thunder_v1": "X_v1",
    "thunder_v2": "X_v2",
    
    "plant_bottom_right": "P_br",
    "plant_bottom_left": "P_bl",
    "two_plants": "P_2",
    
    # -- RINGS --
    "top_two_rings": "r_2t",
    "bottom_two_rings": "r_2b",
    "top_left_and_bottom_right_rings": "r_tl_br",
    "bottom_left_and_right_rings": "r_bl_r",
    "top_left_ring": "r_tl",
    "top_right_ring": "r_tr",
    "bottom_left_ring": "r_bl",
    "bottom_right_ring": "r_br",

    # -- SPRINGS --
    "spring_from_bottom_middle": "s_b_m",
    "spring_from_bottom_middle_rain_rock_background": "s_b_m_r",
    "spring_from_left_middle": "s_l_m",
    "spring_from_left_middle_rain_rock_background": "s_l_m_r",
    "spring_from_right_middle": "s_r_m",
    "spring_from_right_middle_rain_rock_background": "s_r_m_r",
    "spring_from_bottom_left": "s_b_l",
    "spring_from_bottom_left_rain_rock_background": "s_b_l_r",
    "spring_from_bottom_right": "s_b_r",
    "spring_from_bottom_right_rain_rock_background": "s_b_r_r",
    
    # -- SPIKES --
    "spike_from_bottom": "S_b",
    "spike_from_bottom_rain_rock_background": "S_b_r",
    "spike_from_top": "S_t",
    "spike_from_top_rain_rock_background": "S_t_r",

    # I'll assume it's something to block sonic.
    "blocking_thing": "K",

    # -- BRIDGE PIECES --    
    "bridge_support_top_right": "b_s_tr",
    "bridge_support_top_left": "b_s_tl",
    "bridge_two_top_supports": "b_2t",
    
    # -- BACKGROUND TILES --
    "background_special_v1_1": "e_v1_1",
    "background_special_v1_2": "e_v1_2",
    "background_special_v1_3": "e_v1_3",
    "background_special_v1_4": "e_v1_4",
    "background_special_v2_1": "e_v2_1",
    "background_special_v2_2": "e_v2_2",
    "background_special_v2_3": "e_v2_3",
    "background_special_v2_4": "e_v2_4",
    "background_special_v2_5": "e_v2_5",
    "background_special_v2_6": "e_v2_6",
    "background_special_v2_7": "e_v2_7",
    "background_special_v2_8": "e_v2_8",
    "background_special_v2_9": "e_v2_9",
    "background_special_v2_10": "e_v2_10",
    "background_special_v2_11": "e_v2_11",
    "background_special_v2_12": "e_v2_12",
    "background_special_v2_13": "e_v2_13",
    "background_special_v2_14": "e_v2_14",
    "background_special_v2_15": "e_v2_15",
    "background_special_v2_16": "e_v2_16",
    "background_special_v2_17": "e_v2_17",
    "background_special_v2_18": "e_v2_18",
    
    "background_rain_v1": "d_v1",
    "background_rain_v2": "d_v2",
    "background_rain_v3": "d_v3",
    "background_rain_v4": "d_v4",
    "background_rain_v5": "d_v5",
    "background_rain_v6": "d_v6",
    "background_rain_v7": "d_v7",
    "background_rain_v8": "d_v8",
    "background_rain_v9": "d_v9",
    "background_rain_v10": "d_v10",
    "background_rain_v11": "d_v11",
    
    "vertical_lines": "v",
    
    "background_tile_1": "-",
    "background_tile_2": "-", 
    "background_tile_3": "-",
    "background_tile_4": "-", 
    "background_tile_5": "-",
    "background_tile_6": "-", 
    "background_tile_7": "-",
    "background_tile_8": "-", 
    "background_tile_9": "-",
    "background_tile_10": "-", 
    "background_tile_11": "-",
    "background_tile_12": "-", 
    "background_tile_13": "-",
    "background_tile_14": "-", 
    "background_tile_15": "-",
    "background_tile_16": "-", 
    "background_tile_17": "-",
    "background_tile_18": "-", 
    "background_tile_19": "-",
    "background_tile_20": "-", 
    "background_tile_21": "-",
    "background_tile_22": "-", 
    "background_tile_23": "-",
    "background_tile_24": "-", 
    "background_tile_25": "-",
    "background_tile_26": "-", 
    "background_tile_27": "-",
    "background_tile_28": "-", 
    "background_tile_29": "-",
    "background_tile_30": "-",
    "background_tile_31": "-",
    "background_tile_32": "-",
    "background_tile_33": "-",
    "background_tile_34": "-",
    "background_tile_35": "-",
    "background_tile_36": "-",
    "background_tile_37": "-",
    "background_tile_38": "-",
    "background_tile_39": "-",
    "background_tile_40": "-",
    "background_tile_41": "-",
    "background_tile_42": "-",
    "background_tile_43": "-",
    "background_tile_44": "-",
    "background_tile_45": "-",
    "background_tile_46": "-",
    "background_tile_47": "-", 
    "background_tile_48": "-", 
    "background_tile_49": "-", 
    "background_tile_50": "-", 
    "background_tile_51": "-", 
    "background_tile_52": "-", 
    "background_tile_53": "-", 
    "background_tile_54": "-", 
    "background_tile_55": "-", 
    "background_tile_56": "-", 
    "background_tile_57": "-",
    "background_tile_58": "-", 
    "background_tile_59": "-",
    "background_tile_60": "-", 
    "background_tile_61": "-",
    "background_tile_62": "-", 
    "background_tile_63": "-",
    "background_tile_64": "-", 
    "background_tile_65": "-",
    "background_tile_66": "-", 
    "background_tile_67": "-", 
    "background_tile_68": "-", 
    "background_tile_69": "-", 
    "background_tile_70": "-", 
    "background_tile_71": "-", 
    "background_tile_72": "-", 
    "background_tile_73": "-",
    "background_tile_74": "-", 
    "background_tile_75": "-", 
    "background_tile_76": "-", 
    "background_tile_77": "-", 
    "background_tile_78": "-", 
    "background_tile_79": "-", 
    "background_tile_80": "-", 
    "background_tile_81": "-", 
    "background_tile_82": "-", 
    "background_tile_83": "-", 
    "background_tile_84": "-", 
    "background_tile_85": "-", 
    "background_tile_86": "-", 
}

# -------------------------------------------- LEVEL 7

level_7_sprites = {
    # -- INCLINED / SLOPE PIECES --

        # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": "ig_45_bl_tr",
    "inclined_ground_30_bottom_left_to_top_right_p1": "ig_30_bl_tr_p1",
    "inclined_ground_30_bottom_left_to_top_right_p2": "ig_30_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p1": "ig_15_bl_tr_p1",
    "inclined_ground_15_bottom_left_to_top_right_p2": "ig_15_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p3": "ig_15_bl_tr_p3",
    "inclined_ground_15_bottom_left_to_top_right_p4": "ig_15_bl_tr_p4",
    
        # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": "ig_45_tl_br",
    "inclined_ground_30_top_left_to_bottom_right_p1": "ig_30_tl_br_p1",
    "inclined_ground_30_top_left_to_bottom_right_p2": "ig_30_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p1": "ig_15_tl_br_p1",
    "inclined_ground_15_top_left_to_bottom_right_p2": "ig_15_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p3": "ig_15_tl_br_p3",
    "inclined_ground_15_top_left_to_bottom_right_p4": "ig_15_tl_br_p4",
    
    # -- LOOP & CORNER PIECES -- (None)
      
    # -- GROUND / IRON GROUND / CHECKER TILES --
    
        # GROUND TILES
        
            # LOW
    "low_ground_v1": "lg_v1",
    "low_ground_v2": "lg_v2",
    "low_ground_v3": "lg_v3",
    "low_ground_v4": "lg_v4",
    
    "triangle_ground": "tg",

            # HIGH
    "curved_ground": "Cg",
    
    "high_ground_v1": "hg_v1",
    "high_ground_v2": "hg_v2",
    "high_ground_v3": "hg_v3",
    "high_ground_v4": "hg_v4",
    "high_ground_v5": "hg_v5",
    "high_ground_v6": "hg_v6",
    "high_ground_v7": "hg_v7",
    "high_ground_v8": "hg_v8",
    
    "high_ground_top_left_grass_v1": "hg_tl_grass_v1",
    "high_ground_top_left_grass_v2": "hg_tl_grass_v2",
    "high_ground_top_left_grass_v3": "hg_tl_grass_v3",
    "high_ground_top_left_grass_v4": "hg_tl_grass_v4",
    
    "high_ground_top_right_grass_v1": "hg_tr_grass_v1",
    "high_ground_top_right_grass_v2": "hg_tr_grass_v2",
    "high_ground_top_right_grass_v3": "hg_tr_grass_v3",
    "high_ground_top_right_grass_v4": "hg_tr_grass_v4",
       
        # IRON GROUND TILES
        
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_iron_ground_45_bottom_left_to_top_right": "ig_45_bl_tr",
    "inclined_iron_ground_30_bottom_left_to_top_right_p1": "ig_30_bl_tr_p1",
    "inclined_iron_ground_30_bottom_left_to_top_right_p2": "ig_30_bl_tr_p2",
    "inclined_iron_ground_15_bottom_left_to_top_right_p1": "ig_15_bl_tr_p1",
    "inclined_iron_ground_15_bottom_left_to_top_right_p2": "ig_15_bl_tr_p2",
    "inclined_iron_ground_15_bottom_left_to_top_right_p3": "ig_15_bl_tr_p3",
    "inclined_iron_ground_15_bottom_left_to_top_right_p4": "ig_15_bl_tr_p4",
    
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_iron_ground_45_top_left_to_bottom_right": "ig_45_tl_br",
    "inclined_iron_ground_30_top_left_to_bottom_right_p1": "ig_30_tl_br_p1",
    "inclined_iron_ground_30_top_left_to_bottom_right_p2": "ig_30_tl_br_p2",
    "inclined_iron_ground_15_top_left_to_bottom_right_p1": "ig_15_tl_br_p1",
    "inclined_iron_ground_15_top_left_to_bottom_right_p2": "ig_15_tl_br_p2",
    "inclined_iron_ground_15_top_left_to_bottom_right_p3": "ig_15_tl_br_p3",
    "inclined_iron_ground_15_top_left_to_bottom_right_p4": "ig_15_tl_br_p4",
    
            # LOW
    "low_iron_ground_v1": "lg_v1",
    "low_iron_ground_v2": "lg_v2",
    "low_iron_ground_v3": "lg_v3",
    "low_iron_ground_v4": "lg_v4",
    
    "triangle_iron_ground": "tig",

            # HIGH
    "curved_iron_ground": "Cig",
    
        # CHECKER TILES

            # LOW
    "low_checker_v1": "lc_v1",
    "low_checker_v2": "lc_v2",
        
            # HIGH
    "high_checker_v1": "hc_v1",
    "high_checker_v2": "hc_v2",
    "high_checker_v3": "hc_v3",
    "high_checker_v4": "hc_v4",
    "high_checker_v5": "hc_v5",
    "high_checker_v6": "hc_v6",
    "high_checker_v7": "hc_v7",
    "high_checker_v8": "hc_v8",
    "high_checker_v9": "hc_v9",
    "high_checker_v10": "hc_v10",
    "high_checker_v11": "hc_v11",
    "high_checker_v12": "hc_v12",
    "high_checker_v13": "hc_v13",
    "high_checker_v14": "hc_v14",
    "high_checker_v15": "hc_v15",
    "high_checker_v16": "hc_v16",
    "high_checker_v17": "hc_v17",
    "high_checker_v18": "hc_v18",
    "high_checker_v19": "hc_v19",
    "high_checker_v20": "hc_v20",
    "high_checker_v21": "hc_v21",
    "high_checker_v22": "hc_v22",
    "high_checker_v23": "hc_v23",   
    "high_checker_v24": "hc_v24",
    "high_checker_v25": "hc_v25",
    "high_checker_v26": "hc_v26",
    "high_checker_v27": "hc_v27",
    "high_checker_v28": "hc_v28",
    "high_checker_v29": "hc_v29",
    "high_checker_v30": "hc_v30",
    "high_checker_v31": "hc_v31",
    
    # -- SAW, BEAR & CHAINS --  
    "saw_top_left_v1": "Z_tl_v1",
    "saw_bottom_left_v1": "Z_bl_v1",
    "saw_top_right_v1": "Z_tr_v1",
    "saw_bottom_right_v1": "Z_br_v1",
    "saw_top_left_v2": "Z_tl_v2",
    "saw_bottom_left_v2": "Z_bl_v2",
    "saw_top_right_v2": "Z_tr_v2",
    "saw_bottom_right_v2": "Z_br_v2",
    
    "little_bear": "D_l",
    "big_bear": "D_b",
    "two_bear": "D_2",
    "big_bear_left": "D_b_l",
    "big_bear_right": "D_b_r",
    
    "chains_top_v1": "U_t_v1",
    "chains_bottom_v1": "U_b_v1",
    "chains_bottom_v2": "U_b_v2",
    "chains_top_v2": "U_t_v2",
    "chains_body_v2_1": "U_b_v2_1",
    "chains_body_v2_2": "U_b_v2_2",
    "chains_bottom_v2_2": "U_b_v2_2",
    
    "spinning_chains_p1_v1": "u_p1_v1",
    "spinning_chains_p2_v1": "u_p2_v1",
    "spinning_chains_p3_v1": "u_p3_v1",
    "spinning_chains_p4_v1": "u_p4_v1",
    "spinning_chains_p1_v2": "u_p1_v2",
    "spinning_chains_p2_v2": "u_p2_v2",
    "spinning_chains_p3_v2": "u_p3_v2",
    "spinning_chains_p4_v2": "u_p4_v2",
    
    # -- RINGS --
    "top_two_rings": "r_2t",
    "bottom_two_rings": "r_2b",
    "top_left_and_bottom_right_rings": "r_lbr",
    "bottom_left_and_right_rings": "r_lbr",
    "top_left_ring": "r_lt",
    "top_right_ring": "r_rt",
    "bottom_left_ring": "r_lb",
    "bottom_right_ring": "r_rb",

    # -- SPRINGS --
    "spring_from_bottom_middle": "s_b_m",
    "spring_from_bottom_middle_iron_rock_background": "s_b_m_i",
    "spring_from_left_middle": "s_l_m",
    "spring_from_left_middle_iron_rock_background": "s_l_m_i",
    "spring_from_right_middle": "s_r_m",
    "spring_from_right_middle_iron_rock_background": "s_r_m_i",
    "spring_from_bottom_left": "s_b_l",
    "spring_from_bottom_left_iron_rock_background": "s_b_l_i",
    "spring_from_bottom_right": "s_b_r",
    "spring_from_bottom_right_iron_rock_background": "s_b_r_i",
    
    # -- SPIKES --
    "spike_from_bottom": "S_b",
    "spike_from_bottom_iron_rock_background": "S_b_i",
    "spike_from_top": "S_t",
    "spike_from_top_iron_rock_background": "S_t_i",

    # I'll assume it's something to block sonic.
    "blocking_thing": "K",
    
    # -- CLOUDS --
    "cloud": "c",
    
    "cloud_left": "c_l",
    "cloud_right": "c_r",

    # -- BACKGROUND TILES --
    "checker_background_v1": "d_v1",
    "checker_background_v2": "d_v2",
    "checker_background_v3": "d_v3",
    "checker_background_v4": "d_v4",
    "checker_background_v5": "d_v5",
    "checker_background_v6": "d_v6",
    
    "industrial_background_v1": "e_v1",
    "industrial_background_v2": "e_v2",
    "industrial_background_v3": "e_v3",
    "industrial_background_v4": "e_v4",
    "industrial_background_v5": "e_v5",
    "industrial_background_v6": "e_v6",
    "industrial_background_v7": "e_v7",
    "industrial_background_v8": "e_v8",
    "industrial_background_v9": "e_v9",
    "industrial_background_v10": "e_v10",
    "industrial_background_v11": "e_v11",
    "industrial_background_v12": "e_v12",
    "industrial_background_v13": "e_v13",
    
    "tower_background_v1": "j_v1",
    "tower_background_v2": "j_v2",
    "tower_background_v3": "j_v3",
    "tower_background_v4": "j_v4",
    "tower_background_v5": "j_v5",
    
    "background_special_v1": "__v1",
    "background_special_v2": "__v2",
    "background_special_v3": "__v3",
    "background_special_v4": "__v4",
    "background_special_v5": "__v5",
    "background_special_v6": "__v6",
    
    "vertical_lines": "v",
    
    "background_tile_1": "-",
    "background_tile_2": "-", 
    "background_tile_3": "-",
    "background_tile_4": "-", 
    "background_tile_5": "-",
    "background_tile_6": "-", 
    "background_tile_7": "-",
    "background_tile_8": "-", 
    "background_tile_9": "-",
    "background_tile_10": "-",
    "background_tile_11": "-", 
    "background_tile_12": "-",
    "background_tile_13": "-",
    "background_tile_14": "-", 
    "background_tile_15": "-",
    "background_tile_16": "-", 
    "background_tile_17": "-",
    "background_tile_18": "-", 
    "background_tile_19": "-",
    "background_tile_20": "-", 
    "background_tile_21": "-",
    "background_tile_22": "-", 
    "background_tile_23": "-",
    "background_tile_24": "-", 
    "background_tile_25": "-",
    "background_tile_26": "-", 
    "background_tile_27": "-",
    "background_tile_28": "-", 
    "background_tile_29": "-",
    "background_tile_30": "-", 
    "background_tile_31": "-",
    "background_tile_32": "-", 
    "background_tile_33": "-",
    "background_tile_34": "-", 
    "background_tile_35": "-",
    "background_tile_36": "-", 
    "background_tile_37": "-",
    "background_tile_38": "-", 
    "background_tile_39": "-",
    "background_tile_40": "-", 
    "background_tile_41": "-",
    "background_tile_42": "-",
    "background_tile_43": "-",
    "background_tile_44": "-",
    "background_tile_45": "-",
    "background_tile_46": "-",
    "background_tile_47": "-",
    "background_tile_48": "-",
    "background_tile_49": "-",
    "background_tile_50": "-",
    "background_tile_51": "-",
    "background_tile_52": "-",
    "background_tile_53": "-",
    "background_tile_54": "-",
    "background_tile_55": "-",
    "background_tile_56": "-",
    "background_tile_57": "-", 
    "background_tile_58": "-", 
    "background_tile_59": "-",
    "background_tile_60": "-", 
    "background_tile_61": "-",
    "background_tile_62": "-", 
    "background_tile_63": "-",
    "background_tile_64": "-", 
    "background_tile_65": "-",
    "background_tile_66": "-", 
    "background_tile_67": "-",
    "background_tile_68": "-", 
    "background_tile_69": "-", 
    "background_tile_70": "-", 
    "background_tile_71": "-", 
    "background_tile_72": "-", 
    "background_tile_73": "-", 
    "background_tile_74": "-", 
    "background_tile_75": "-", 
    "background_tile_76": "-", 
    "background_tile_77": "-", 
    "background_tile_78": "-", 
    "background_tile_79": "-", 
    "background_tile_80": "-", 
    "background_tile_81": "-", 
    "background_tile_82": "-", 
}

# -------------------------------------------- LEVEL 8

level_8_sprites = {
    # -- INCLINED / SLOPE PIECES --

        # BOTTOM LEFT TO TOP RIGHT
    "inclined_ground_45_bottom_left_to_top_right": "ig_45_bl_tr",
    "inclined_ground_30_bottom_left_to_top_right_p1": "ig_30_bl_tr_p1",
    "inclined_ground_30_bottom_left_to_top_right_p2": "ig_30_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p1": "ig_15_bl_tr_p1",
    "inclined_ground_15_bottom_left_to_top_right_p2": "ig_15_bl_tr_p2",
    "inclined_ground_15_bottom_left_to_top_right_p3": "ig_15_bl_tr_p3",
    "inclined_ground_15_bottom_left_to_top_right_p4": "ig_15_bl_tr_p4",
    
        # TOP LEFT TO BOTTOM RIGHT
    "inclined_ground_45_top_left_to_bottom_right": "ig_45_tl_br",
    "inclined_ground_30_top_left_to_bottom_right_p1": "ig_30_tl_br_p1",
    "inclined_ground_30_top_left_to_bottom_right_p2": "ig_30_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p1": "ig_15_tl_br_p1",
    "inclined_ground_15_top_left_to_bottom_right_p2": "ig_15_tl_br_p2",
    "inclined_ground_15_top_left_to_bottom_right_p3": "ig_15_tl_br_p3",
    "inclined_ground_15_top_left_to_bottom_right_p4": "ig_15_tl_br_p4",
    
    # -- LOOP & CORNER PIECES -- (None)
    
    # -- GROUND / SPACE GROUND / CHECKER TILES / SPECIAL GROUND --
    
        # GROUND TILES
        
            # LOW
    "low_ground_v1": "lg_v1",
    "low_ground_v2": "lg_v2",
    "low_ground_v3": "lg_v3",
    "low_ground_v4": "lg_v4",

            # HIGH
    "curved_ground": "Cg",
    
    "high_ground_v1": "hg_v1",
    "high_ground_v2": "hg_v2",
    "high_ground_v3": "hg_v3",
    "high_ground_v4": "hg_v4",
    "high_ground_v5": "hg_v5",
    "high_ground_v6": "hg_v6",
    "high_ground_v7": "hg_v7",
    "high_ground_v8": "hg_v8",
    
    "high_ground_top_left_grass_v1": "hg_tl_gr_v1",
    "high_ground_top_left_grass_v2": "hg_tl_gr_v2",
    "high_ground_top_left_grass_v3": "hg_tl_gr_v3",
    
    "high_ground_top_right_grass_v1": "hg_tr_gr_v1",
    "high_ground_top_right_grass_v2": "hg_tr_gr_v2",
    "high_ground_top_right_grass_v3": "hg_tr_gr_v3",
       
        # SPACE GROUND TILES
        
            # TOP LEFT TO BOTTOM RIGHT
    "inclined_space_ground_45_top_left_to_bottom_right_inversed": "isg_45_tl_br_inv",
    "inclined_space_ground_30_top_left_to_bottom_right_p1_inversed": "isg_30_tl_br_p1_inv",
    "inclined_space_ground_30_top_left_to_bottom_right_p2_inversed": "isg_30_tl_br_p2_inv",
    "inclined_space_ground_15_top_left_to_bottom_right_p1_inversed": "isg_15_tl_br_p1_inv",
    "inclined_space_ground_15_top_left_to_bottom_right_p2_inversed": "isg_15_tl_br_p2_inv",
    "inclined_space_ground_15_top_left_to_bottom_right_p3_inversed": "isg_15_tl_br_p3_inv",
    "inclined_space_ground_15_top_left_to_bottom_right_p4_inversed": "isg_15_tl_br_p4_inv",
    
            # BOTTOM LEFT TO TOP RIGHT
    "inclined_space_ground_45_bottom_left_to_top_right_inversed": "isg_45_bl_tr_inv",
    "inclined_space_ground_30_bottom_left_to_top_right_p1_inversed": "isg_30_bl_tr_p1_inv",
    "inclined_space_ground_30_bottom_left_to_top_right_p2_inversed": "isg_30_bl_tr_p2_inv",
    "inclined_space_ground_15_bottom_left_to_top_right_p1_inversed": "isg_15_bl_tr_p1_inv",
    "inclined_space_ground_15_bottom_left_to_top_right_p2_inversed": "isg_15_bl_tr_p2_inv",
    "inclined_space_ground_15_bottom_left_to_top_right_p3_inversed": "isg_15_bl_tr_p3_inv",
    "inclined_space_ground_15_bottom_left_to_top_right_p4_inversed": "isg_15_bl_tr_p4_inv",
    
            # LOW
    "low_space_ground_v1": "ls_v1",
    "low_space_ground_v2": "ls_v2",
    "low_space_ground_v3": "ls_v3",
    "low_space_ground_v4": "ls_v4",

            # HIGH
    
        # CHECKER TILES

            # LOW (None)
        
            # HIGH
    "high_checker_v1": "hc_v1",
    "high_checker_v2": "hc_v2",
    "high_checker_v3": "hc_v3",
    "high_checker_v4": "hc_v4",
    "high_checker_v5": "hc_v5",
    "high_checker_v6": "hc_v6",
    "high_checker_v7": "hc_v7",
    "high_checker_v8": "hc_v8",
    "high_checker_v9": "hc_v9",
    "high_checker_v10": "hc_v10",
    "high_checker_v11": "hc_v11",
    "high_checker_v12": "hc_v12",
    "high_checker_v13": "hc_v13",
    "high_checker_v14": "hc_v14",
    "high_checker_v15": "hc_v15",
    
    "high_checker_bottom_left_decoration_v1": "hc_bl_dec_v1",
    "high_checker_bottom_right_decoration_v1": "hc_br_dec_v1",
    "high_checker_bottom_left_decoration_v2": "hc_bl_dec_v2",
    "high_checker_bottom_right_decoration_v2": "hc_br_dec_v2",
    "high_checker_bottom_left_decoration_v3": "hc_bl_dec_v3",
    "high_checker_bottom_right_decoration_v3": "hc_br_dec_v3",
        
        # SPECIAL TILES
    "special_ground_tiles_angle_in_bottom_right": "gs_ai_br",
    "special_ground_tiles_angle_in_bottom_left": "gs_ai_bl",
    "special_ground_tiles_angle_in_top_right": "gs_ai_tr",
    "special_ground_tiles_angle_in_top_left": "gs_ai_tl",
    "special_ground_tiles_two_vertical_bottom": "gs_2v_b",
    "special_ground_tiles_two_vertical_top": "gs_2v_t",
    "special_ground_tiles_two_horizontal_left": "gs_2h_l",
    "special_ground_tiles_two_horizontal_right": "gs_2h_r",
    "special_ground_tiles_four_points": "gs_4p",
    
    # -- PIPES, WINDOW, CHAINS, OBJECT BLOCK, LASER & ETC --
    "pipe_from_bottom_classic_background": "pb_c_b",
    "pipe_from_top_classic_background": "pt_c_b",
    "pipe_from_right_classic_background": "pr_c_b",
    "pipe_from_left_classic_background": "pl_c_b",
    "pipe_from_bottom_space_background": "pb_s_b",
    "pipe_from_top_space_background": "pt_s_b",
    "pipe_from_right_space_background": "pr_s_b",
    "pipe_from_left_space_background": "pl_s_b",
    "pipe_horizontal_space_background": "ph_s_b",
    "pipe_vertical_space_background": "pv_s_b",
    
    "window_top_p1": "At_p1",
    "window_top_p2": "At_p2",
    "window_top_p3": "At_p3",
    "window_top_p4": "At_p4",
    "window_top_p5": "At_p5",
    "window_middle_top_p1": "Atm_p1",
    "window_middle_top_p2": "Atm_p2",
    "window_middle_top_p3": "Atm_p3",
    "window_middle_top_p4": "Atm_p4",
    "window_middle_top_p5": "Atm_p5",
    "window_middle_bottom_p1": "Atmb_p1",
    "window_middle_bottom_p2": "Atmb_p2",
    "window_middle_bottom_p3": "Atmb_p3",
    "window_middle_bottom_p4": "Atmb_p4",
    "window_middle_bottom_p5": "Atmb_p5",
    "window_bottom_p1": "Ab_p1",
    "window_bottom_p2": "Ab_p2",
    "window_bottom_p3": "Ab_p3",
    "window_bottom_p4": "Ab_p4",
    "window_bottom_p5": "Ab_p5",
    "window_bottom_bottom_p1": "Abb_p1",
    "window_bottom_bottom_p2": "Abb_p2",
    "window_bottom_bottom_p3": "Abb_p3",
    "window_bottom_bottom_p4": "Abb_p4",
    "window_bottom_bottom_p5": "Abb_p5",
    
    "open_block_classic_background": "a_c_bg",
    "open_block_space_background": "a_s_bg",
    "closed_block": "a",
    
    "metal_girder_middle": "kg_m",
    "metal_girder_left": "kg_l",
    "metal_girder_right": "kg_r",
    
    "laser_from_bottom": "I_fl",
    "laser_from_top": "I_ft",
    "laser_from_left": "I_fl",
    "laser_from_right": "I_fr",
    
    "two_pipes_middle": "q",
    
    "support_left": "z_l",
    "support_right": "z_r",
    
    "spinning_chains_left_v1": "u_l_v1",
    "spinning_chains_middle_without_support_v1": "u_m_v1",
    "spinning_chains_right_v1": "u_r_v1",
    "spinning_chains_left_v2": "u_l_v2",
    "spinning_chains_middle_without_support_v2": "u_m_v2",
    "spinning_chains_right_v2": "u_r_v2",
    "spinning_chains_middle_with_support_v1": "u_m_s_v1",
    "spinning_chains_middle_with_support_v2": "u_m_s_v2",
    
    "support_laser_bottom_firing": "x_b_f",
    "bullets": ".",
    "support_laser_top_firing": "x_t_f",
    "support_laser_bottom_not_firing": "x_b_nf",
    "support_laser_top_not_firing": "x_t_nf",
    
    # -- RINGS --
    "top_two_rings": "r_2t",
    "bottom_two_rings": "r_2b",
    "top_left_and_bottom_right_rings": "r_l_b_r",
    "bottom_left_and_right_rings": "r_l_r",
    "top_left_ring": "r_lt",
    "top_right_ring": "r_rt",
    "bottom_left_ring": "r_lb",
    "bottom_right_ring": "r_rb",

    # -- SPRINGS --
    "spring_from_bottom_middle": "s_b_m",
    "spring_from_bottom_middle_space_background": "s_b_m_s",
    "spring_from_left_middle": "s_l_m",
    "spring_from_left_middle_space_background": "s_l_m_s",
    "spring_from_right_middle": "s_r_m",
    "spring_from_right_middle_space_background": "s_r_m_s",
    "spring_from_bottom_left": "s_b_l",
    "spring_from_bottom_left_space_background": "s_b_l_s",
    "spring_from_bottom_right": "s_b_r",
    "spring_from_bottom_right_space_background": "s_b_r_s",
    
    # -- SPIKES --
    "spike_from_bottom": "S_b",
    "spike_from_bottom_space_background": "S_b_s",
    "spike_from_top": "S_t",
    "spike_from_top_space_background": "S_t_s",

    # I'll assume it's something to block sonic.
    "blocking_thing_classic_background": "K_c",
    "blocking_thing_space_background": "K_s",
    
    # -- BACKGROUND TILES --
    "background_special_horizontal": "d_h",
    "background_special_vertical": "d_v",
    "background_special_top_left": "d_tl",
    "background_special_top_blank": "d_tb",
    "background_special_top_middle": "d_tm",
    "background_special_top_right": "d_tr",
    "background_special_middle_left_v1": "d_ml_v1",
    "background_special_middle_blank_v1": "d_mb_v1",
    "background_special_middle_middle_v1": "d_mm_v1",
    "background_special_middle_right_v1": "d_mr_v1",
    "background_special_middle_left_v2": "d_ml_v2",
    "background_special_middle_blank_v2": "d_mb_v2",
    "background_special_middle_middle_v2": "d_mm_v2",
    "background_special_middle_right_v2": "d_mr_v2",
    
    "background_special_top_right_v1": "e_tr_v1",
    "background_special_top_left_v1": "e_tl_v1",
    "background_special_top_right_v2": "e_tr_v2",
    "background_special_top_left_v2": "e_tl_v2",
    "background_special_top_right_v3": "e_tr_v3",
    "background_special_top_left_v3": "e_tl_v3",
    "background_special_left_bar_half": "e_l_b_h",
    "background_special_left_bar_v1": "e_l_b_v1",
    "background_special_left_bar_v2": "e_l_b_v2",
    "background_special_top_right_v4": "e_tr_v4",
    "background_special_bottom_left": "e_bl",
    "background_special_top_left_v4": "e_tl_v4",
    
    "vertical_lines": "v",
    
    "background_tile_1": "-",
    "background_tile_2": "-", 
    "background_tile_3": "-",
    "background_tile_4": "-", 
    "background_tile_5": "-",
    "background_tile_6": "-", 
    "background_tile_7": "-",
    "background_tile_8": "-", 
    "background_tile_9": "-",
    "background_tile_10": "-", 
    "background_tile_11": "-",
    "background_tile_12": "-", 
    "background_tile_13": "-",
    "background_tile_14": "-", 
    "background_tile_15": "-",
    "background_tile_16": "-", 
    "background_tile_17": "-",
    "background_tile_18": "-", 
    "background_tile_19": "-",
    "background_tile_20": "-", 
    "background_tile_21": "-", 
    "background_tile_22": "-",
    "background_tile_23": "-", 
    "background_tile_24": "-",
    "background_tile_25": "-", 
    "background_tile_26": "-",
    "background_tile_27": "-", 
    "background_tile_28": "-", 
    "background_tile_29": "-", 
    "background_tile_30": "-", 
    "background_tile_31": "-", 
    "background_tile_32": "-", 
    "background_tile_33": "-", 
    "background_tile_34": "-", 
    "background_tile_35": "-", 
    "background_tile_36": "-", 
    "background_tile_37": "-", 
    "background_tile_38": "-", 
    "background_tile_39": "-", 
    "background_tile_40": "-", 
    "background_tile_41": "-", 
    "background_tile_42": "-", 
    "background_tile_43": "-", 
    "background_tile_44": "-",
    "background_tile_45": "-", 
    "background_tile_46": "-",
    "background_tile_47": "-", 
    "background_tile_48": "-",
    "background_tile_49": "-", 
    "background_tile_50": "-",
    "background_tile_51": "-", 
    "background_tile_52": "-",
    "background_tile_53": "-", 
    "background_tile_54": "-", 
    "background_tile_55": "-", 
    "background_tile_56": "-", 
    "background_tile_57": "-", 
    "background_tile_58": "-", 
    "background_tile_59": "-", 
    "background_tile_60": "-", 
    "background_tile_61": "-", 
    "background_tile_62": "-", 
    "background_tile_63": "-", 
}
 
def get_main_token(level_dict: dict) -> dict:
    """ 
    Returns dict with the main token of the given level dictionary.

    Args:
        level_dict (_type_): Dictionary containing the level information.

    Returns:
        level_dict: Dictionary containing the main token of the level.
    """
    for key, value in level_dict.items():
        level_dict[key] = value[0]
    return level_dict
        
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
    output_dir_name_full_token = "sprites_token/full_token"
    output_dir_full_token = os.makedirs(output_dir_name_full_token, exist_ok=True)
    
    output_dir_name_main_token = "sprites_token/main_token"
    output_dir_main_token = os.makedirs(output_dir_name_main_token, exist_ok=True)
    
    for i, level_data in enumerate(levels):
        with open(f"{output_dir_name_full_token}/level_{i+1}_full_token.json", "w") as f:
            json.dump(level_data, f, indent=4)
        with open(f"{output_dir_name_main_token}/level_{i+1}_main_token.json", "w") as f:
            json.dump(get_main_token(level_data), f, indent=4)
            
    print("Levels sprite token created !!")        
else:
    print(f"Error: The number of sprites {sum(len(level) for level in levels)} in the levels list does not match the total number of sprites {len(sprites)} !! Check again the sprites list.")