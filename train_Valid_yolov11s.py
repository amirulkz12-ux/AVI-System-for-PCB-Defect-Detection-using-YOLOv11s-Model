# ──────────────────────────────────────────────────────────────
# train_yolov10s.py
# Created : 2025  |  Author : Kz
# Trains YOLOv11s on the PCB-defect dataset
# ──────────────────────────────────────────────────────────────

import os
from ultralytics import YOLO

# 1️⃣  Absolute path to your YOLOv11s project folder
PROJECT_DIR = r"C:\Users\User\Downloads\PCB-Defects-Detection-Using-YOLOv11s-main"

# 2️⃣  Make that the current working directory (keeps relative paths simple)
os.chdir(PROJECT_DIR)
print("Current directory :", os.getcwd())
print("Contents          :", os.listdir())

# 3️⃣  Wrap training in a function (Windows-multiprocessing safe)
def run_training() -> None:
    """Train YOLOv11-small on the PCB-defect dataset."""
    model = YOLO("yolo11s.pt")                 # auto-downloads if not present

    model.train(
        data="dataset.yaml",                   # check paths inside your YAML
        epochs=200,                            # tweak later
        batch=32,                              # drop if GPU OOMs
        imgsz=690,                             # square input, good default
        device=0,                              # 0 = first GPU | "cpu" = CPU
        workers=2,                             # Spyder/Win safe
        half=True,                             # FP16 mixed precision (set False if errors)
        project=os.path.join(PROJECT_DIR, "runs"),
        name="pcb_yolov11s",                    # run folder: runs/train/pcb_yolov8n
        exist_ok=True                          # overwrite if re-running
    )

# 4️⃣  Guard for Windows & Spyder
if __name__ == "__main__":
    run_training()