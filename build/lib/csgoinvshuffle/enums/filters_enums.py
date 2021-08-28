from enum import Enum, unique


"""
This file contains enums for filtering through inventories
"""


class StrEnum(str, Enum):
    pass


@unique
class TagsInternalName(StrEnum):
    """
    Common internal names of tags you can filter by
    There are a lot more internal names which are out of scope of this project

    This is work in progress.
    Some knives and collections are missing.
    """
    NEGEV = 'weapon_negev'
    M249 = 'weapon_m249'
    G3SG1 = 'weapon_g3sg1'
    SCAR_20 = 'weapon_scar20'
    GALIL_AR = 'weapon_galilar'
    MP7 = 'weapon_mp7'
    FIVE_SEVEN = 'weapon_fiveseven'
    CZ75 = 'weapon_cz75a'
    USP_S = 'weapon_usp_silencer'
    P2000 = 'weapon_hkp2000'
    PP_BIZON = 'weapon_bizon'
    SG553 = 'weapon_sg556'
    DEAGLE = 'weapon_deagle'
    M4A4 = 'weapon_m4a1'
    NOVA = 'weapon_nova'
    BUTTERFLY_KNIFE = 'weapon_knife_butterfly'
    P90 = 'weapon_p90'
    AK_47 = 'weapon_ak47'
    GLOCK_18 = 'weapon_glock'
    AUG = 'weapon_aug'
    TEC_9 = 'weapon_tec9'
    UMP_45 = 'weapon_ump45'
    M4A1_S = 'weapon_m4a1_silencer'
    KARAMBIT_KNIFE = 'weapon_knife_karambit'
    MAG_7 = 'weapon_mag7'
    STRANGE = 'strange'
    DUAL_BERETTAS = 'weapon_elite'
    AWP = 'weapon_awp'
    P250 = 'weapon_p250'
    SSG_08 = 'weapon_ssg08'
    MAC_10 = 'weapon_mac10'
    AGENTS_BROKEN_FANG = 'set_op10_characters'
    AGENTS_SHATTERED_WEB = 'set_op9_characters'
    REVOLVER = 'weapon_revolver'
    MP9 = 'weapon_mp9'
    CLASSIC_KNIFE = 'weapon_knife_css'
    XM1014 = 'weapon_xm1014'
    M9_BAYONET = 'weapon_knife_m9_bayonet'
    UNUSUAL = 'unusual'
    SAWED_OFF = 'weapon_sawedoff'
    FAMAS = 'weapon_famas'
    MP5 = 'weapon_mp5sd'
    KNIVES = 'CSGO_Type_Knife'
    GLOVES = 'Type_Hands'
    MACHINE_GUNS = 'CSGO_Type_Machinegun'
    SNIPER_RIFLES = 'CSGO_Type_SniperRifle'
    RIFLES = 'CSGO_Type_Rifle'
    SMGS = 'CSGO_Type_SMG'
    PISTOLS = 'CSGO_Type_Pistol'
    SHOTGUNS = 'CSGO_Type_Shotgun'
    MUSIC_KITS = 'CSGO_Type_MusicKit'
    AGENTS = 'Type_CustomPlayer'
    RARITY_COMMON = 'Rarity_Common'
    COLLECTION_NUKE2 = 'set_nuke_2'
    COLLECTION_NUKE = 'set_nuke'
    COLLECTION_DUST_2 = 'set_dust_2'
    COLLECTION_LAKE = 'set_lake'
    COLLECTION_BANK = 'set_bank'
    COLLECTION_SAFEHOUSE = 'set_safehouse'
    COLLECTION_ITALY = 'set_italy'
    RARITY_RARE = 'Rarity_Rare'
    COLLECTION_CONTROL = 'set_op10_ct'
    COLLECTION_INFERNO2 = 'set_inferno_2'
    COLLECTION_INFERNO = 'set_inferno'
    RARITY_MYTHICAL = 'Rarity_Mythical'
    RARITY_ANCIENT = 'Rarity_Ancient'
    RARITY_LEGENDARY = 'Rarity_Legendary'
    COLLECTION_CANALS = 'set_canals'
    COLLECTION_NORSE = 'set_norse'
    COLLECTION_STMARC = 'set_stmarc'
    COLLECTION_OVERPASS = 'set_overpass'
    COLLECTION_BLACKSITE = 'set_blacksite'
    COLLECTION_GAMMA_2 = 'set_gamma_2'
    WEAR_MINIMAL_WEAR = 'WearCategory1'
    WEAR_BATTLE_SCARRED = 'WearCategory4'
    WEAR_FIELD_TESTED = 'WearCategory2'
    WEAR_FACTORY_NEW = 'WearCategory0'
    WEAR_WELL_WORN = 'WearCategory3'
