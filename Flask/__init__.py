import cv2
import os
import numpy as np
from flask import *
from pathlib import Path
from PIL import Image, ImageEnhance
from scipy import ndimage
from werkzeug.utils import secure_filename

app = Flask(__name__)

current_dir = Path(__file__).parent
file_path = current_dir / 'static/uploads'
absolute_path = file_path.resolve()
app.config["UPLOAD_FOLDER"] = absolute_path


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        file = request.files["image"]
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
        file.save(filepath)

        image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE).astype("float64") / 255.0

        roberts_cross_v = np.array([[1, 0], [0, -1]])
        roberts_cross_h = np.array([[0, 1], [-1, 0]])
        roberts_vertical = ndimage.convolve(image, roberts_cross_v)
        roberts_horizontal = ndimage.convolve(image, roberts_cross_h)
        roberts_edge = np.sqrt(
            np.square(roberts_horizontal) + np.square(roberts_vertical)
        )
        roberts_edge_filename = "roberts_edge_" + filename
        roberts_edge_filepath = os.path.join(
            app.config["UPLOAD_FOLDER"], roberts_edge_filename
        )
        cv2.imwrite(roberts_edge_filepath, (roberts_edge * 255.0))

        sobel_x = cv2.Sobel(image, cv2.CV_64F, 1, 0, ksize=5)
        sobel_y = cv2.Sobel(image, cv2.CV_64F, 0, 1, ksize=5)
        sobel_edge = np.sqrt(np.square(sobel_x) + np.square(sobel_y))
        sobel_edge_filename = "sobel_edge_" + filename
        sobel_edge_filepath = os.path.join(
            app.config["UPLOAD_FOLDER"], sobel_edge_filename
        )
        cv2.imwrite(sobel_edge_filepath, (sobel_edge * 255.0))

        prewitt_kern_v = np.array([[1, 0, -1], [1, 0, -1], [1, 0, -1]])
        prewitt_kern_h = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
        prewitt_vertical = ndimage.convolve(image, prewitt_kern_v)
        prewitt_horizontal = ndimage.convolve(image, prewitt_kern_h)
        prewitt_edge = np.sqrt(
            np.square(prewitt_horizontal) + np.square(prewitt_vertical)
        )
        prewitt_edge_filename = "prewitt_edge_" + filename
        prewitt_edge_filepath = os.path.join(
            app.config["UPLOAD_FOLDER"], prewitt_edge_filename
        )
        cv2.imwrite(prewitt_edge_filepath, (prewitt_edge * 255.0))

        laplacian_edge = cv2.Laplacian(image, cv2.CV_64F)
        laplacian_edge_filename = "laplacian_edge_" + filename
        laplacian_edge_filepath = os.path.join(
            app.config["UPLOAD_FOLDER"], laplacian_edge_filename
        )
        cv2.imwrite(laplacian_edge_filepath, (laplacian_edge * 255.0))

        canny_low_threshold = 50
        canny_high_threshold = 150
        image_uint8 = (image * 255).astype(np.uint8)
        canny_edge = cv2.Canny(image_uint8, canny_low_threshold, canny_high_threshold)
        canny_edge_filename = "canny_edge_" + filename
        canny_edge_filepath = os.path.join(
            app.config["UPLOAD_FOLDER"], canny_edge_filename
        )
        cv2.imwrite(canny_edge_filepath, (canny_edge * 255.0))

        color_corrected_image = cv2.imread(filepath, cv2.IMREAD_COLOR)
        color_corrected_lab = cv2.cvtColor(color_corrected_image, cv2.COLOR_BGR2LAB)
        color_corrected_l, color_corrected_a, color_corrected_b = cv2.split(
            color_corrected_lab
        )
        color_corrected_clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        color_corrected_l = color_corrected_clahe.apply(color_corrected_l)
        color_corrected_lab = cv2.merge(
            (color_corrected_l, color_corrected_a, color_corrected_b)
        )
        color_corrected = cv2.cvtColor(color_corrected_lab, cv2.COLOR_LAB2BGR)
        color_corrected_filename = "color_corrected_" + filename
        color_corrected_filepath = os.path.join(
            app.config["UPLOAD_FOLDER"], color_corrected_filename
        )
        cv2.imwrite(color_corrected_filepath, (color_corrected))

        corrected_color_image = Image.open(filepath)
        corrected_color_brightness = float(request.form.get("brightness", 1))
        corrected_color_contrast = float(request.form.get("contrast", 1))
        corrected_color_saturation = float(request.form.get("saturation", 1))
        corrected_color_image = ImageEnhance.Brightness(corrected_color_image).enhance(
            corrected_color_brightness
        )
        corrected_color_image = ImageEnhance.Contrast(corrected_color_image).enhance(
            corrected_color_contrast
        )
        corrected_color_image = ImageEnhance.Color(corrected_color_image).enhance(
            corrected_color_saturation
        )
        corrected_color_filename = "corrected_color_" + filename
        corrected_color_filepath = os.path.join(
            app.config["UPLOAD_FOLDER"], corrected_color_filename
        )
        corrected_color_image.save(corrected_color_filepath)

        return render_template(
            "index.html",
            original=filename,
            roberts_edge=roberts_edge_filename,
            sobel_edge=sobel_edge_filename,
            prewitt_edge=prewitt_edge_filename,
            laplacian_edge=laplacian_edge_filename,
            canny_edge=canny_edge_filename,
            color_corrected=color_corrected_filename,
            corrected_color=corrected_color_filename,
        )

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
