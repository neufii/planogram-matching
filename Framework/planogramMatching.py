import pandas as pd
from .config import IOU_THRESHOLD

def get_iou(detection, planogram):
    assert detection['xmin'] < detection['xmax']
    assert detection['ymin'] < detection['ymax']
    assert planogram['xmin'] < planogram['xmax']
    assert planogram['ymin'] < planogram['ymax']

    # determine the coordinates of the intersection rectangle
    x_left = max(detection['xmin'], planogram['xmin'])
    y_top = max(detection['ymin'], planogram['ymin'])
    x_right = min(detection['xmax'], planogram['xmax'])
    y_bottom = min(detection['ymax'], planogram['ymax'])

    if x_right < x_left or y_bottom < y_top:
        return False

    intersection_area = (x_right - x_left) * (y_bottom - y_top)

    detection_area = (detection['xmax'] - detection['xmin']) * (detection['ymax'] - detection['ymin'])
    planogram_area = (planogram['xmax'] - planogram['xmin']) * (planogram['ymax'] - planogram['ymin'])

    iou = intersection_area / float(detection_area + planogram_area - intersection_area)
    assert iou >= 0.0
    assert iou <= 1.0
    return round(iou, 2) >= IOU_THRESHOLD

def find_closet_bounding_box(planogram_row, detections, missing_products_index):
    if len(planogram_row['class'].split('/')) == 3:
        class_category, item_name, item_no = planogram_row['class'].split('/')
    else:
        class_category, class_sub_category, item_name, item_no = planogram_row['class'].split('/')
    item_no = item_no[:-4]
    product_name = item_name +'/'+item_no
    detections_filtered = detections[detections.apply(lambda x: get_iou(x, planogram_row), axis=1)]
    if not(product_name in list(detections_filtered['name'])):
        missing_products_index.append(planogram_row.name)

def match(detections, planogram):
   missing_products_index = []
   for i in range(planogram.shape[0]):
      find_closet_bounding_box(planogram.iloc[i], detections, missing_products_index)
   return planogram.iloc[missing_products_index]