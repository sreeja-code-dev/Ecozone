
from typing import Tuple

def classify_image_stub(image_bytes: bytes) -> Tuple[str, float]:
    # MVP stub: always predict plastic with confidence 0.85
    return "plastic", 0.85