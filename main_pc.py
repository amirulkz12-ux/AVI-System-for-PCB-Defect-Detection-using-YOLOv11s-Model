import os
import time
from ultralytics import YOLO

# Path to your configuration file
config_path = r'dataset.yaml'

# Load a pre-trained YOLOv10 model
model = YOLO("yolo11s.pt")  # load pre-trained model

# Start timer
start_time = time.time()

# Use the model to train
model.train(data=config_path, epochs=200, batch=32, device=0)  # train the model

# End timer
end_time = time.time()
total_duration = end_time - start_time

# Print the total duration of the training process
print(f"Training completed in {total_duration // 3600:.0f} hours, "
      f"{(total_duration % 3600) // 60:.0f} minutes, "
      f"{total_duration % 60:.2f} seconds.")