colors = ["Blue",
"BlueViolet",
"CadetBlue",
"Chocolate",
"Coral",
"DodgerBlue",
"Firebrick",
"GoldenRod",
"Green",
"HotPink",
"OrangeRed",
"Red",
"SeaGreen",
"SpringGreen",
"YellowGreen"]

hexs = ["#0000FF",
"#8A2BE2",
"#5F9EA0",
"#D2691E",
"#FF7F50",
"#1E90FF",
"#B22222",
"#DAA520",
"#008000",
"#FF69B4",
"#FF4500",
"#FF0000",
"#2E8B57",
"#00FF7F",
"#9ACD32"]

color_hex = [[color, hexval] for color, hexval in zip(colors, hexs)]

color_to_hex = {color: hexval for color, hexval in zip(colors, hexs)}
hex_to_color = {hexval: color for color, hexval in color_to_hex.items()}