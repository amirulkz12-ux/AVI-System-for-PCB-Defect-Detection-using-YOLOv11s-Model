# Automatic Visual Inspection System for PCB Defect Detection using YOLOv11s

This project implements an **Automatic Visual Inspection (AVI) System** for detecting surface-level defects on **Printed Circuit Boards (PCBs)** using the **YOLOv11s** object detection model. The system was developed as part of a Final Year Project (FYP) under Faculty of Electrical Engineering under UiTM Pulau Pinang.

---

## 📌 Overview
The proposed system integrates deep learning-based visual inspection with real-time decision output to classify PCB defects into six major categories:
- Missing Hole  
- Mouse Bite  
- Open Circuit  
- Short Circuit  
- Spur  
- Spurious Copper  
<img width="337" height="414" alt="image" src="https://github.com/user-attachments/assets/5e348064-2d5a-4b9b-9f4f-32af6568906f" />

The trained YOLOv11s model performs real-time inference using a consumer-grade PC and communicates results to an **ESP32 microcontroller** via serial UART for status indicatior.
<img width="2400" height="1200" alt="results" src="https://github.com/user-attachments/assets/4dec748b-fa54-41a7-b2f5-f4ecfa615b96" />
<img width="3000" height="2250" alt="confusion_matrix" src="https://github.com/user-attachments/assets/5d68b792-60f3-4e0e-a720-7e1c7404f82b" />

---

## ⚙️ System Architecture
- **Model:** YOLOv11s (Ultralytics implementation)
- **Framework:** PyTorch
- **Language:** Python
- **IDE:** Spyder (Anaconda)
- **Hardware:**  
  - PC (Ryzen 5 + RTX3050 GPU)  
  - ESP32 Microcontroller  
  - USB Camera
![photo_2_2025-10-08_22-47-10](https://github.com/user-attachments/assets/77ca1ed3-3522-4e2f-a65d-43b09969a61b)
![GUI](https://github.com/user-attachments/assets/4cf830d4-aec7-4862-9fa7-9778281c6e31)

---

## 🧠 Features
- Real-time defect detection and visualization  
- Classification of six PCB defect types  
- Automatic status feedback via ESP32  
- Lightweight YOLOv11s architecture for real-time processing  
- User-friendly folder structure for output storage  
