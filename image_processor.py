import cv2
import numpy as np
import os


class ImageProcessor:

    def __init__(self):
        pass

    # -----------------------------
    # LOAD IMAGE
    # -----------------------------

    def load_image(self, image_path):

        image = cv2.imread(image_path)

        if image is None:
            raise ValueError(
                f"Cannot load image: {image_path}"
            )

        return image

    # -----------------------------
    # GRAYSCALE
    # -----------------------------

    def to_grayscale(self, image):

        return cv2.cvtColor(
            image,
            cv2.COLOR_BGR2GRAY
        )

    # -----------------------------
    # REMOVE NOISE
    # -----------------------------

    def remove_noise(self, image):

        return cv2.GaussianBlur(
            image,
            (5, 5),
            0
        )

    # -----------------------------
    # THRESHOLD
    # -----------------------------

    def threshold_image(self, image):

        _, thresh = cv2.threshold(
            image,
            0,
            255,
            cv2.THRESH_BINARY +
            cv2.THRESH_OTSU
        )

        return thresh

    # -----------------------------
    # RESIZE
    # -----------------------------

    def resize_image(
            self,
            image,
            scale=2):

        width = int(
            image.shape[1] * scale
        )

        height = int(
            image.shape[0] * scale
        )

        return cv2.resize(
            image,
            (width, height),
            interpolation=
            cv2.INTER_CUBIC
        )

    # -----------------------------
    # SHARPEN
    # -----------------------------

    def sharpen_image(
            self,
            image):

        kernel = np.array(
            [
                [0, -1, 0],
                [-1, 5, -1],
                [0, -1, 0]
            ]
        )

        return cv2.filter2D(
            image,
            -1,
            kernel
        )

    # -----------------------------
    # COMPLETE PIPELINE
    # -----------------------------

    def preprocess(
            self,
            image_path):

        image = self.load_image(
            image_path
        )

        gray = self.to_grayscale(
            image
        )

        denoise = self.remove_noise(
            gray
        )

        resized = self.resize_image(
            denoise
        )

        sharp = self.sharpen_image(
            resized
        )

        thresh = self.threshold_image(
            sharp
        )

        return thresh

    # -----------------------------
    # SAVE IMAGE
    # -----------------------------

    def save_processed_image(
            self,
            image,
            output_path):

        cv2.imwrite(
            output_path,
            image
        )

        return output_path