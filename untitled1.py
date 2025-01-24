elements = {
    1: {"name": "Hydrogen", "symbol": "H", "electronic_configuration": "1s^1", "properties": "Non-metal, colorless, odorless, tasteless gas"},
    2: {"name": "Helium", "symbol": "He", "electronic_configuration": "1s^2", "properties": "Noble gas, colorless, odorless, tasteless gas"},
    3: {"name": "Lithium", "symbol": "Li", "electronic_configuration": "[He] 2s^1", "properties": "Soft, silvery metal, highly reactive"},
    4: {"name": "Beryllium", "symbol": "Be", "electronic_configuration": "[He] 2s^2", "properties": "Hard, brittle metal, relatively non-reactive"},
    5: {"name": "Boron", "symbol": "B", "electronic_configuration": "[He] 2s^2 2p^1", "properties": "Metalloid, hard, brittle, black or brown in color"},
    6: {"name": "Carbon", "symbol": "C", "electronic_configuration": "[He] 2s^2 2p^2", "properties": "Non-metal, essential for life, forms a wide variety of compounds"},
    7: {"name": "Nitrogen", "symbol": "N", "electronic_configuration": "[He] 2s^2 2p^3", "properties": "Non-metal, diatomic gas, essential for life"},
    8: {"name": "Oxygen", "symbol": "O", "electronic_configuration": "[He] 2s^2 2p^4", "properties": "Non-metal, diatomic gas, supports combustion, essential for respiration"},
    9: {"name": "Fluorine", "symbol": "F", "electronic_configuration": "[He] 2s^2 2p^5", "properties": "Halogen, highly reactive, pale yellow gas"},
    10: {"name": "Neon", "symbol": "Ne", "electronic_configuration": "[He] 2s^2 2p^6", "properties": "Noble gas, colorless, odorless, and inert gas"},
    11: {"name": "Sodium", "symbol": "Na", "electronic_configuration": "[Ne] 3s^1", "properties": "Soft, silvery, highly reactive metal"},
    12: {"name": "Magnesium", "symbol": "Mg", "electronic_configuration": "[Ne] 3s^2", "properties": "Shiny, silvery metal, moderately reactive"},
    13: {"name": "Aluminum", "symbol": "Al", "electronic_configuration": "[Ne] 3s^2 3p^1", "properties": "Light, ductile, corrosion-resistant metal"},
    14: {"name": "Silicon", "symbol": "Si", "electronic_configuration": "[Ne] 3s^2 3p^2", "properties": "Metalloid, used in semiconductors, brittle crystalline solid"},
    15: {"name": "Phosphorus", "symbol": "P", "electronic_configuration": "[Ne] 3s^2 3p^3", "properties": "Non-metal, occurs in white, red, and black allotropes"},
    16: {"name": "Sulfur", "symbol": "S", "electronic_configuration": "[Ne] 3s^2 3p^4", "properties": "Non-metal, yellow, brittle solid, essential for life"},
    17: {"name": "Chlorine", "symbol": "Cl", "electronic_configuration": "[Ne] 3s^2 3p^5", "properties": "Halogen, greenish-yellow gas, highly reactive"},
    18: {"name": "Argon", "symbol": "Ar", "electronic_configuration": "[Ne] 3s^2 3p^6", "properties": "Noble gas, colorless, odorless, inert gas"},
    19: {"name": "Potassium", "symbol": "K", "electronic_configuration": "[Ar] 4s^1", "properties": "Soft, silvery, highly reactive metal"},
    20: {"name": "Calcium", "symbol": "Ca", "electronic_configuration": "[Ar] 4s^2", "properties": "Soft, silvery, alkaline earth metal"},
    21: {"name": "Scandium", "symbol": "Sc", "electronic_configuration": "[Ar] 3d^1 4s^2", "properties": "Light, silvery, transition metal"},
    22: {"name": "Titanium", "symbol": "Ti", "electronic_configuration": "[Ar] 3d^2 4s^2", "properties": "Strong, lightweight, corrosion-resistant metal"},
    23: {"name": "Vanadium", "symbol": "V", "electronic_configuration": "[Ar] 3d^3 4s^2", "properties": "Hard, silvery-grey metal, used in alloys"},
    24: {"name": "Chromium", "symbol": "Cr", "electronic_configuration": "[Ar] 3d^5 4s^1", "properties": "Shiny, steel-gray metal, highly corrosion-resistant"},
    25: {"name": "Manganese", "symbol": "Mn", "electronic_configuration": "[Ar] 3d^5 4s^2", "properties": "Hard, brittle metal, used in steel production"},
    26: {"name": "Iron", "symbol": "Fe", "electronic_configuration": "[Ar] 3d^6 4s^2", "properties": "Strong, ductile metal, used in construction and manufacturing"},
    27: {"name": "Cobalt", "symbol": "Co", "electronic_configuration": "[Ar] 3d^7 4s^2", "properties": "Hard, magnetic metal, used in alloys and batteries"},
    28: {"name": "Nickel", "symbol": "Ni", "electronic_configuration": "[Ar] 3d^8 4s^2", "properties": "Shiny, silvery metal, resistant to corrosion"},
    29: {"name": "Copper", "symbol": "Cu", "electronic_configuration": "[Ar] 3d^10 4s^1", "properties": "Ductile, conductive metal, used in electrical wiring"},
    30: {"name": "Zinc", "symbol": "Zn", "electronic_configuration": "[Ar] 3d^10 4s^2", "properties": "Bluish-white, brittle metal, used in galvanizing and alloys"},
    31: {"name": "Gallium", "symbol": "Ga", "electronic_configuration": "[Ar] 3d^10 4s^2 4p^1", "properties": "Soft, silvery metal, used in semiconductors"},
    32: {"name": "Germanium", "symbol": "Ge", "electronic_configuration": "[Ar] 3d^10 4s^2 4p^2", "properties": "Brittle, metalloid, used in transistors"},
    33: {"name": "Arsenic", "symbol": "As", "electronic_configuration": "[Ar] 3d^10 4s^2 4p^3", "properties": "Metalloid, toxic, occurs in various allotropes"},
    34: {"name": "Selenium", "symbol": "Se", "electronic_configuration": "[Ar] 3d^10 4s^2 4p^4", "properties": "Non-metal, brittle, semiconductor properties"},
    35: {"name": "Bromine", "symbol": "Br", "electronic_configuration": "[Ar] 3d^10 4s^2 4p^5", "properties": "Halogen, reddish-brown liquid, toxic, used in disinfectants"},
    36: {"name": "Krypton", "symbol": "Kr", "electronic_configuration": "[Ar] 3d^10 4s^2 4p^6", "properties": "Noble gas, colorless, odorless, inert gas"},
    37: {"name": "Rubidium", "symbol": "Rb", "electronic_configuration": "[Kr] 5s^1", "properties": "Soft, silvery, highly reactive metal"},
    38: {"name": "Strontium", "symbol": "Sr", "electronic_configuration": "[Kr] 5s^2", "properties": "Soft, silvery metal, highly reactive, used in fireworks"},
    39: {"name": "Yttrium", "symbol": "Y", "electronic_configuration": "[Kr] 4d^1 5s^2", "properties": "Silvery metal, used in LEDs and superconductors"},
    40: {"name": "Zirconium", "symbol": "Zr", "electronic_configuration": "[Kr] 4d^2 5s^2", "properties": "Strong, corrosion-resistant metal, used in nuclear reactors"},
    41: {"name": "Niobium", "symbol": "Nb", "electronic_configuration": "[Kr] 4d^4 5s^1", "properties": "Soft, grey, ductile metal, used in superconducting materials"},
    42: {"name": "Molybdenum", "symbol": "Mo", "electronic_configuration": "[Kr] 4d^5 5s^1", "properties": "Hard, silvery metal, used in steel alloys"},
    43: {"name": "Technetium", "symbol": "Tc", "electronic_configuration": "[Kr] 4d^5 5s^2", "properties": "Radioactive metal, used in medical imaging"},
    44: {"name": "Ruthenium", "symbol": "Ru", "electronic_configuration": "[Kr] 4d^7 5s^1", "properties": "Rare, corrosion-resistant metal, used in electronics"},
    45: {"name": "Rhodium", "symbol": "Rh", "electronic_configuration": "[Kr] 4d^8 5s^1", "properties": "Silvery-white metal, used in catalytic converters"},
    46: {"name": "Palladium", "symbol": "Pd", "electronic_configuration": "[Kr] 4d^10", "properties": "Shiny, silvery metal, used in catalytic converters"},
    47: {"name": "Silver", "symbol": "Ag", "electronic_configuration": "[Kr] 4d^10 5s^1", "properties": "Soft, white, lustrous metal, used in jewelry and electronics"},
    48: {"name": "Cadmium", "symbol": "Cd", "electronic_configuration": "[Kr] 4d^10 5s^2", "properties": "Soft, bluish-white metal, toxic, used in batteries"},
    49: {"name": "Indium", "symbol": "In", "electronic_configuration": "[Kr] 4d^10 5s^2 5p^1", "properties": "Soft, malleable metal, used in electronics and alloys"},
    50: {"name": "Tin", "symbol": "Sn", "electronic_configuration": "[Kr] 4d^10 5s^2 5p^2", "properties": "Soft, silvery metal, used in coating other metals"},
    51: {"name": "Antimony", "symbol": "Sb", "electronic_configuration": "[Kr] 4d^10 5s^2 5p^3", "properties": "Metalloid, used in flame retardants and alloys"},
    52: {"name": "Tellurium", "symbol": "Te", "electronic_configuration": "[Kr] 4d^10 5s^2 5p^4", "properties": "Metalloid, brittle, used in semiconductors"},
    53: {"name": "Iodine", "symbol": "I", "electronic_configuration": "[Kr] 4d^10 5s^2 5p^5", "properties": "Halogen, violet solid, used in antiseptics"},
    54: {"name": "Xenon", "symbol": "Xe", "electronic_configuration": "[Kr] 4d^10 5s^2 5p^6", "properties": "Noble gas, colorless, odorless, inert gas"},
    55: {"name": "Cesium", "symbol": "Cs", "electronic_configuration": "[Xe] 6s^1", "properties": "Soft, silvery-golden, highly reactive metal"},
    56: {"name": "Barium", "symbol": "Ba", "electronic_configuration": "[Xe] 6s^2", "properties": "Soft, silvery alkaline earth metal, used in fireworks"},
    57: {"name": "Lanthanum", "symbol": "La", "electronic_configuration": "[Xe] 5d^1 6s^2", "properties": "Soft, silvery-white metal, used in catalysts"},
    58: {"name": "Cerium", "symbol": "Ce", "electronic_configuration": "[Xe] 4f^1 5d^1 6s^2", "properties": "Soft, silvery metal, used in catalytic converters"},
    59: {"name": "Praseodymium", "symbol": "Pr", "electronic_configuration": "[Xe] 4f^3 6s^2", "properties": "Soft, silvery metal, used in magnets and lasers"},
    60: {"name": "Neodymium", "symbol": "Nd", "electronic_configuration": "[Xe] 4f^4 6s^2", "properties": "Hard, silvery metal, used in permanent magnets"},
    61: {"name": "Promethium", "symbol": "Pm", "electronic_configuration": "[Xe] 4f^5 6s^2", "properties": "Radioactive metal, used in atomic batteries"},
    62: {"name": "Samarium", "symbol": "Sm", "electronic_configuration": "[Xe] 4f^6 6s^2", "properties": "Silvery metal, used in magnets and nuclear reactors"},
    63: {"name": "Europium", "symbol": "Eu", "electronic_configuration": "[Xe] 4f^7 6s^2", "properties": "Soft, silvery metal, used in phosphorescent applications"},
    64: {"name": "Gadolinium", "symbol": "Gd", "electronic_configuration": "[Xe] 4f^7 5d^1 6s^2", "properties": "Silvery-white metal, used in MRI contrast agents"},
    65: {"name": "Terbium", "symbol": "Tb", "electronic_configuration": "[Xe] 4f^9 6s^2", "properties": "Soft, silvery metal, used in phosphors and lasers"},
    66: {"name": "Dysprosium", "symbol": "Dy", "electronic_configuration": "[Xe] 4f^10 6s^2", "properties": "Soft, silvery metal, used in magnets and nuclear reactors"},
    67: {"name": "Holmium", "symbol": "Ho", "electronic_configuration": "[Xe] 4f^11 6s^2", "properties": "Soft, silvery metal, used in lasers and nuclear reactors"},
    68: {"name": "Erbium", "symbol": "Er", "electronic_configuration": "[Xe] 4f^12 6s^2", "properties": "Silvery metal, used in optical fibers and lasers"},
    69: {"name": "Thulium", "symbol": "Tm", "electronic_configuration": "[Xe] 4f^13 6s^2", "properties": "Soft, silvery metal, used in lasers and radiation therapy"},
    70: {"name": "Ytterbium", "symbol": "Yb", "electronic_configuration": "[Xe] 4f^14 6s^2", "properties": "Silvery-white metal, used in lasers and nuclear reactors"},
    71: {"name": "Lutetium", "symbol": "Lu", "electronic_configuration": "[Xe] 4f^14 5d^1 6s^2", "properties": "Hard, silvery metal, used in electronics and catalysis"},
    72: {"name": "Hafnium", "symbol": "Hf", "electronic_configuration": "[Xe] 4f^14 5d^2 6s^2", "properties": "Corrosion-resistant metal, used in nuclear reactors"},
    73: {"name": "Tantalum", "symbol": "Ta", "electronic_configuration": "[Xe] 4f^14 5d^3 6s^2", "properties": "Hard, dense metal, used in electronics and aerospace"},
    74: {"name": "Tungsten", "symbol": "W", "electronic_configuration": "[Xe] 4f^14 5d^4 6s^2", "properties": "Hard, dense metal, used in light bulb filaments and cutting tools"},
    75: {"name": "Rhenium", "symbol": "Re", "electronic_configuration": "[Xe] 4f^14 5d^5 6s^2", "properties": "Hard, dense metal, used in high-temperature applications"},
    76: {"name": "Osmium", "symbol": "Os", "electronic_configuration": "[Xe] 4f^14 5d^6 6s^2", "properties": "Dense, bluish-white metal, used in electrical contacts"},
    77: {"name": "Iridium", "symbol": "Ir", "electronic_configuration": "[Xe] 4f^14 5d^7 6s^2", "properties": "Dense, corrosion-resistant metal, used in spark plugs"},
    78: {"name": "Platinum", "symbol": "Pt", "electronic_configuration": "[Xe] 4f^14 5d^9 6s^1", "properties": "Heavy, silvery metal, used in catalytic converters and jewelry"},
    79: {"name": "Gold", "symbol": "Au", "electronic_configuration": "[Xe] 4f^14 5d^10 6s^1", "properties": "Soft, yellow metal, used in jewelry and currency"},
    80: {"name": "Mercury", "symbol": "Hg", "electronic_configuration": "[Xe] 4f^14 5d^10 6s^2", "properties": "Liquid at room temperature, toxic, used in thermometers and electrical switches"},
    81: {"name": "Thallium", "symbol": "Tl", "electronic_configuration": "[Xe] 4f^14 5d^10 6s^2 6p^1", "properties": "Soft, gray metal, toxic, used in electronics"},
    82: {"name": "Lead", "symbol": "Pb", "electronic_configuration": "[Xe] 4f^14 5d^10 6s^2 6p^2", "properties": "Soft, dense metal, toxic, used in batteries and radiation shielding"},
    83: {"name": "Bismuth", "symbol": "Bi", "electronic_configuration": "[Xe] 4f^14 5d^10 6s^2 6p^3", "properties": "Brittle, heavy metal, used in cosmetics and pharmaceuticals"},
    84: {"name": "Polonium", "symbol": "Po", "electronic_configuration": "[Xe] 4f^14 5d^10 6s^2 6p^4", "properties": "Radioactive, toxic metal, used in nuclear applications"},
    85: {"name": "Astatine", "symbol": "At", "electronic_configuration": "[Xe] 4f^14 5d^10 6s^2 6p^5", "properties": "Highly radioactive, rare halogen, used in cancer treatment"},
    86: {"name": "Radon", "symbol": "Rn", "electronic_configuration": "[Xe] 4f^14 5d^10 6s^2 6p^6", "properties": "Radioactive, colorless, odorless gas, linked to lung cancer risk"},
    87: {"name": "Francium", "symbol": "Fr", "electronic_configuration": "[Rn] 7s^1", "properties": "Highly radioactive, alkali metal, very unstable"},
    88: {"name": "Radium", "symbol": "Ra", "electronic_configuration": "[Rn] 7s^2", "properties": "Radioactive, alkaline earth metal, used in early cancer treatments"},
    89: {"name": "Actinium", "symbol": "Ac", "electronic_configuration": "[Rn] 6d^1 7s^2", "properties": "Radioactive metal, used in radiation therapy"},
    90: {"name": "Thorium", "symbol": "Th", "electronic_configuration": "[Rn] 6d^2 7s^2", "properties": "Radioactive metal, used as nuclear fuel"},
    91: {"name": "Protactinium", "symbol": "Pa", "electronic_configuration": "[Rn] 5f^2 6d^1 7s^2", "properties": "Radioactive, used in nuclear reactors"},
    92: {"name": "Uranium", "symbol": "U", "electronic_configuration": "[Rn] 5f^3 6d^1 7s^2", "properties": "Radioactive, heavy metal, used as nuclear fuel"},
    93: {"name": "Neptunium", "symbol": "Np", "electronic_configuration": "[Rn] 5f^4 6d^1 7s^2", "properties": "Radioactive, used in nuclear reactors"},
    94: {"name": "Plutonium", "symbol": "Pu", "electronic_configuration": "[Rn] 5f^6 6d^1 7s^2", "properties": "Radioactive, used in nuclear weapons and reactors"},
    95: {"name": "Americium", "symbol": "Am", "electronic_configuration": "[Rn] 5f^7 6d^1 7s^2", "properties": "Radioactive, used in smoke detectors and nuclear research"},
    96: {"name": "Curium", "symbol": "Cm", "electronic_configuration": "[Rn] 5f^7 6d^1 7s^2", "properties": "Radioactive, used in research and nuclear reactors"},
    97: {"name": "Berkelium", "symbol": "Bk", "electronic_configuration": "[Rn] 5f^9 6d^1 7s^2", "properties": "Radioactive, used in scientific research"},
    98: {"name": "Californium", "symbol": "Cf", "electronic_configuration": "[Rn] 5f^10 6d^1 7s^2", "properties": "Radioactive, used in neutron sources and medical applications"},
    99: {"name": "Einsteinium", "symbol": "Es", "electronic_configuration": "[Rn] 5f^11 6d^1 7s^2", "properties": "Radioactive, used in research applications"},
    100: {"name": "Fermium", "symbol": "Fm", "electronic_configuration": "[Rn] 5f^12 6d^1 7s^2", "properties": "Radioactive, used in research applications"},
    101: {"name": "Mendelevium", "symbol": "Md", "electronic_configuration": "[Rn] 5f^13 6d^1 7s^2", "properties": "Radioactive, used in research applications"},
    102: {"name": "Nobelium", "symbol": "No", "electronic_configuration": "[Rn] 5f^14 6d^1 7s^2", "properties": "Radioactive, used in research"},
    103: {"name": "Lawrencium", "symbol": "Lr", "electronic_configuration": "[Rn] 5f^14 6d^1 7s^2", "properties": "Radioactive, used in scientific research"},
    104: {"name": "Rutherfordium", "symbol": "Rf", "electronic_configuration": "[Rn] 5f^14 6d^2 7s^2", "properties": "Radioactive, used in scientific research"},
    105: {"name": "Dubnium", "symbol": "Db", "electronic_configuration": "[Rn] 5f^14 6d^3 7s^2", "properties": "Radioactive, used in scientific research"},
    106: {"name": "Seaborgium", "symbol": "Sg", "electronic_configuration": "[Rn] 5f^14 6d^4 7s^2", "properties": "Radioactive, used in scientific research"},
    107: {"name": "Bohrium", "symbol": "Bh", "electronic_configuration": "[Rn] 5f^14 6d^5 7s^2", "properties": "Radioactive, used in scientific research"},
    108: {"name": "Hassium", "symbol": "Hs", "electronic_configuration": "[Rn] 5f^14 6d^6 7s^2", "properties": "Radioactive, used in scientific research"},
    109: {"name": "Meitnerium", "symbol": "Mt", "electronic_configuration": "[Rn] 5f^14 6d^7 7s^2", "properties": "Radioactive, used in scientific research"},
    110: {"name": "Darmstadtium", "symbol": "Ds", "electronic_configuration": "[Rn] 5f^14 6d^8 7s^2", "properties": "Radioactive, used in scientific research"},
    111: {"name": "Roentgenium", "symbol": "Rg", "electronic_configuration": "[Rn] 5f^14 6d^9 7s^2", "properties": "Radioactive, used in scientific research"},
    112: {"name": "Copernicium", "symbol": "Cn", "electronic_configuration": "[Rn] 5f^14 6d^10 7s^2", "properties": "Radioactive, used in scientific research"},
    113: {"name": "Nihonium", "symbol": "Nh", "electronic_configuration": "[Rn] 5f^14 6d^10 7p^1", "properties": "Radioactive, used in scientific research"},
    114: {"name": "Flerovium", "symbol": "Fl", "electronic_configuration": "[Rn] 5f^14 6d^10 7p^2", "properties": "Radioactive, used in scientific research"},
    115: {"name": "Moscovium", "symbol": "Mc", "electronic_configuration": "[Rn] 5f^14 6d^10 7p^3", "properties": "Radioactive, used in scientific research"},
    116: {"name": "Livermorium", "symbol": "Lv", "electronic_configuration": "[Rn] 5f^14 6d^10 7p^4", "properties": "Radioactive, used in scientific research"},
    117: {"name": "Tennessine", "symbol": "Ts", "electronic_configuration": "[Rn] 5f^14 6d^10 7p^5", "properties": "Radioactive, used in scientific research"},
    118: {"name": "Oganesson", "symbol": "Og", "electronic_configuration": "[Rn] 5f^14 6d^10 7s^2 7p^6", "properties": "Noble gas, highly unstable and radioactive"}
}
while True:
    
 at = int(input("Enter the atomic number of the element (1-118): "))
 if at<1 or at>118:
     print("Enter a number between 1 and 118")
 else:
     break
for x in elements:
    if x == at:
        print("Name:",elements[x]['name'])
        print("Symbol:", elements[x]['symbol'])
        print("Electronic Configuration:", elements[x]['electronic_configuration'])
        print("Properties:", elements[x]['properties'])
    
config= elements[at]["electronic_configuration"]
if 's' in config.split()[-1]:
        print("s-block")
elif 'p' in config.split()[-1]:
        print("p-block")
elif 'd' in config.split()[-1]:
        print("d-block")
elif 'f' in config.split()[-1]:
        print("f-block")
else:
        block = "Unknown"
if at <=2:
    print("period 1")
elif at >2 and at <=10:
    print("period 2")  
elif at >10 and at <=18:
    print("period 3")  
elif at >18 and at <=36:
    print("period 4")  
elif at >36 and at <=54:
    print("period 5")  
elif at >=55 and at <=55:
    print("period 6")  
elif at >=71 and at <=86:
    print("period 6") 
elif at >=87 and at <=88:
    print("period 7") 
elif at >=103 and at <=118:
    print("period 7") 
elif at >=57 and at <=70:
    print("Lanthanoid")
elif at >=89 and at <=102:
    print("Actinide")

