import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk
import numpy as np
from tensorflow.keras.models import load_model

# Load trained color classification model
vehicle_color_model = load_model('saved_models/custom_vehicle_color_predictor.keras')

# Color mapping used by the classifier
class_names = ['beige','black', 'blue','brown','gold','green','gray', 'orange', 'pink','purple','red', 'silver','tan','white' ,'yellow']


def identify_vehicle_color(image):
    resized_img = cv2.resize(image, (64, 64))  # match training size
    norm_img = resized_img.astype('float32') / 255.0
    input_tensor = np.expand_dims(norm_img, axis=0)  # shape becomes (1, 64, 64, 3)
    predictions = vehicle_color_model.predict(input_tensor)
    predicted_class = np.argmax(predictions[0])
    print(f"Prediction vector: {predictions[0]}")
    print(f"Predicted index: {predicted_class}")
    return class_names[predicted_class]



def mark_detected_objects(image_path):
    image = cv2.imread(image_path)
    output_image = image.copy()

    # Dummy detections to simulate object detection
    # Replace this with a real object detection model if required
    detected_cars = [(50, 50, 200, 200), (250, 100, 400, 250)]
    detected_people = [(100, 300, 150, 400)]

    car_count = 0
    people_count = 0

    for (x1, y1, x2, y2) in detected_cars:
        car_crop = image[y1:y2, x1:x2]
        predicted_color = identify_vehicle_color(car_crop)

        if predicted_color.lower() == 'blue':
            box_color = (0, 0, 255)  # Red box for blue cars
        else:
            box_color = (255, 0, 0)  # Blue box for other cars

        cv2.rectangle(output_image, (x1, y1), (x2, y2), box_color, 2)
        cv2.putText(output_image, predicted_color, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, box_color, 2)
        car_count += 1

    for (x1, y1, x2, y2) in detected_people:
        cv2.rectangle(output_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(output_image, "Person", (x1, y1 - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
        people_count += 1


    return output_image, car_count, people_count

def upload_image():
    file_path = filedialog.askopenfilename()
    if file_path:
        processed_image, car_count, people_count = mark_detected_objects(file_path)

        # Convert BGR to RGB for displaying with PIL
        processed_image_rgb = cv2.cvtColor(processed_image, cv2.COLOR_BGR2RGB)
        processed_image_pil = Image.fromarray(processed_image_rgb)
        processed_image_resized = processed_image_pil.resize((600, 400))  # resize for GUI
        processed_image_tk = ImageTk.PhotoImage(processed_image_resized)

        image_label.configure(image=processed_image_tk)
        image_label.image = processed_image_tk  # reference to avoid garbage collection

      #  stats_text.set(f"Cars detected: {car_count} | People detected: {people_count}")

# GUI setup
window = tk.Tk()
window.title("Car Colour Detection System")
window.geometry("800x600")

upload_button = tk.Button(window, text="Upload Image", command=upload_image)
upload_button.pack(pady=10)

image_label = tk.Label(window)
image_label.pack()

stats_text = tk.StringVar()
stats_label = tk.Label(window, textvariable=stats_text, font=("Arial", 12))
stats_label.pack(pady=10)

window.mainloop()
