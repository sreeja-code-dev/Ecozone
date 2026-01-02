TIPS = {
    "plastic": "Rinse and place in plastics bin; avoid single-use by carrying a steel bottle.",
    "paper": "Keep dry; recycle separately. Choose recycled paper products.",
    "glass": "Remove caps; recycle intact. Prefer returnable glass containers.",
    "metal": "Crush cans to save space; scrap centers accept aluminum and steel.",
    "organic": "Compost at home; keeps methane out of landfills.",
    "unknown": "Check local guidelines; reduce packaging where possible."
}

def tip_for(label: str) -> str:
    return TIPS.get(label.lower(), TIPS["unknown"])