# 🚗 Car Colour Detection and Object Counting

This project implements a computer vision system that detects vehicles and people from traffic images, predicts vehicle colors using a custom-trained model, and overlays colored rectangles based on specified rules.

---

## 🎯 Project Objectives

1. **Detect Cars and People** in an input traffic image.
2. **Classify Car Colors** using a trained deep learning model.
3. **Draw Bounding Boxes** with color-coded rules:
   - 🔴 **Red** box around cars predicted as **Blue**.
   - 🔵 **Blue** box around cars of all other colors.
   - 🟢 **Green** box around detected people.
4. **Count Cars and People** and display them in the GUI.
5. **Graphical User Interface** (GUI) using Tkinter for image upload and preview.

---

## 🧠 Model Training

We trained a custom CNN model using TensorFlow/Keras.

### 🏷️ Classes Used:
-beige, black , blue, brown, gold, green,  gray, orange, pink, purple, red, silver, tan, white ,yellow


### 🧪 Input Image Size:
- `64 x 64 x 3`

### 🧾 Training Script:
- `color_model_trainer_cleaned.py`

### 📁 Output Model:
- Saved as `saved_models/vehicle_color_model.keras`

---

## 🖥️ GUI Application

### File: `traffic_gui_cleaned.py`

#### Features:
- Upload an image.
- Process it with the model.
- Highlight and count vehicles and people.
- Color logic:
  - Red box → Blue car
  - Blue box → Any other car
  - Green box → Person

---

## 📦 How to Run

### 1. Install Dependencies

```
pip install -r requirements.txt
```
 ### 2. Train Model (Optional)
If not using provided weights:

```
python color_model_trainer_cleaned.py
```
This will save the model as:

```
saved_models/vehicle_color_model.keras
```
3. Run GUI App
```
python traffic_gui_cleaned.py
```
📁 Folder Structure
```
car_colour_detection/
├── saved_models/
│   └── vehicle_color_model.keras
├── traffic_gui_cleaned.py
├── color_model_trainer_cleaned.py
├── sample_traffic_image.jpg
└── README.md
```
