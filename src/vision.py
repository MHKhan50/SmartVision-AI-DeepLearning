import numpy as np

def analyse_image(image):
    arr = np.asarray(image.convert("RGB"), dtype=np.float32) / 255.0
    gray = arr.mean(axis=2)
    return {
        "width": int(image.width),
        "height": int(image.height),
        "brightness": round(float(gray.mean()), 4),
        "contrast": round(float(gray.std()), 4),
        "red_mean": round(float(arr[:, :, 0].mean()), 4),
        "green_mean": round(float(arr[:, :, 1].mean()), 4),
        "blue_mean": round(float(arr[:, :, 2].mean()), 4),
        "note": "Basic pixel statistics only; no object recognition is performed."
    }

def demo_classify(brightness, contrast):
    if brightness < 0.25:
        label = "Low-light image"
        score = min(0.95, 0.60 + (0.25 - brightness))
        explanation = "The brightness value is low. Consider checking exposure or lighting."
    elif contrast > 0.60:
        label = "High-contrast image"
        score = min(0.95, 0.60 + (contrast - 0.60))
        explanation = "The contrast value is high. Check for harsh shadows or strong highlights."
    else:
        label = "Balanced image"
        score = 0.70
        explanation = "The selected brightness and contrast fall within the demo's balanced range."
    return label, float(score), explanation
