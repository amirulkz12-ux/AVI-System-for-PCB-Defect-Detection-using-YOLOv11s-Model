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

The trained YOLOv11s model performs real-time inference using a consumer-grade PC and communicates results to an **ESP32 microcontroller** via serial UART for status indicatior.

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

---

## 🧠 Features
- Real-time defect detection and visualization  
- Classification of six PCB defect types  
- Automatic status feedback via ESP32  
- Lightweight YOLOv11s architecture for real-time processing  
- User-friendly folder structure for output storage  
