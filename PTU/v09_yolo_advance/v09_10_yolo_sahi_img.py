from sahi.utils.file import download_from_url
# from sahi.utils.ultralytics import download_yolo26n_model

# # Download YOLO26 model
# model_path = "models/yolo26n.pt"
# download_yolo26n_model(model_path)

# Download test images
download_from_url(
    "https://raw.githubusercontent.com/obss/sahi/main/demo/demo_data/small-vehicles1.jpeg",
    "demo_data/small-vehicles1.jpeg",
)

download_from_url(
    "https://raw.githubusercontent.com/obss/sahi/main/demo/demo_data/terrain2.png",
    "demo_data/terrain2.png",
)