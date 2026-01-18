from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

PATHS = {
    "COMFY_URL": "http://127.0.0.1:8188",
    "WORKFLOW": BASE_DIR/"assets"/"workflow_template.json",
    "AUDIO": BASE_DIR/"assets"/"song.mp3",
    "OUTPUT": BASE_DIR/"output",
    "TEMP": BASE_DIR/"temp"
}

SETTINGS = {
    "FPS": 16,
    "MOTION_LOW": 0.4,
    "MOTION_HIGH": 1.4,
    "SEED_MAX": 99999999
}

PROMPTS = {
    "POS": "masterpeice, best quality, 1boy, samurai, cyberpunk, neon lights, rain, <lora:v3_sd15_adapter_pan_felt:0.5>",
    "NEG": "bad hands, morphing, blurring, low res, text, watermark"
}