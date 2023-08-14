import numpy as np
import cv2
from PIL import Image
from .config import FONT, TEXT_SCALE, COLOUR, TEXT_THICKNESS


def display(missing_products, pil_img):
    open_cv_image = np.array(pil_img)
    open_cv_image = open_cv_image[:, :, ::-1].copy()

    for idx, row in missing_products.iterrows():
        product_name = (
            row["class"].split("/")[1] + "/" + row["class"].split("/")[2][:-4]
            if len(row["class"].split("/")) == 3
            else row["class"].split("/")[2] + "/" + row["class"].split("/")[3][:-4]
        )
        cv2.rectangle(
            open_cv_image,
            (int(row["xmin"]), int(row["ymin"])),
            (int(row["xmax"]), int(row["ymax"])),
            COLOUR,
            20,
        )
        cv2.putText(
            open_cv_image,
            product_name,
            (int(row["xmin"]) - 50, int(row["ymin"]) - 50),
            FONT,
            TEXT_SCALE,
            COLOUR,
            TEXT_THICKNESS,
            cv2.LINE_AA,
        )

    result_img = Image.fromarray(open_cv_image[:, :, ::-1])
    return {
        "missing_products": [
            x.split("/")[1] + "/" + x.split("/")[2][:-4]
            if len(x.split("/")) == 3
            else x.split("/")[2] + "/" + x.split("/")[3][:-4]
            for x in missing_products["class"]
        ],
        "img": result_img,
    }