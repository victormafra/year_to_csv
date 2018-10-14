import sys
import pyscreenshot as ImageGrab
import numpy as np
import pandas as pd
from PIL import Image
from datetime import date, timedelta


def color_dist(color_a, color_b):
    diff = np.subtract(color_a, color_b)
    diff = np.absolute(diff)
    diff = np.sum(diff)

    return diff


def get_scale(image_name):
    image = Image.open(image_name)
    image = image.convert('RGB')
    pixel = image.load()
    scale = [(255, 255, 255),
             pixel[64, 1222],
             pixel[137, 1222],
             pixel[209, 1222],
             pixel[282, 1222],
             pixel[353, 1222]]

    return scale


def color_from_scale(day_color, scale):
    diffs = []
    for color in scale:
        diffs.append(color_dist(day_color, color))

    return diffs.index(min(diffs))


def date_to_pixel(date):
    m = date.month
    d = date.day
    initial = 55
    distance = 36
    i = initial + distance * (m-1)
    j = initial + distance * (d-1)

    return i, j


def color_from_days(image_name, year, scale):
    image = Image.open(image_name)
    image = image.convert('RGB')
    pixel = image.load()

    dict = {}
    d = date(year, 1, 1)
    while d.year != year+1:
        i, j = date_to_pixel(d)
        color = color_from_scale(pixel[i, j], scale)
        dict[d] = color
        d += timedelta(days=1)

    return dict


if __name__ == '__main__':
    try:
        file = sys.argv[1]
        year = int(sys.argv[2])
    except:
        print("Usage: converter.py file.jpg YYYY")
        exit(0)

    scale = get_scale(file)
    data = color_from_days(file, year, scale)
    df = pd.DataFrame.from_dict(data, orient='index')
    df.to_csv('year.csv', header=['Color'], index_label='Date')
