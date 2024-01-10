import os
import sys

import cv2 as cv
import numpy as np


def refill_boxes(f):
    # Load the image
    image = cv.imread(f)

    # Convert the image to grayscale
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    # Apply a binary threshold to isolate the objects (rectangles)
    _, thresholded = cv.threshold(gray, 137, 140, cv.THRESH_BINARY)

    # Find contours in the thresholded image
    contours, _ = cv.findContours(thresholded, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    # Define the fill color (B, G, R)
    fill_color = (0, 0, 255)  # Red in BGR

    # Loop through the detected contours and fill each rectangle
    for contour in contours:
        x, y, w, h = cv.boundingRect(contour)  # Get the bounding box of the contour
        cv.rectangle(image, (x, y), (x + w, y + h), fill_color, -1)  # Fill the rectangle

    # Save the modified image
    cv.imwrite("output_image.png", image)

    # Release resources
    cv.destroyAllWindows()


def dewatermark2(f):
    # Load the aerial image and convert to HSV colourspace
    print(f"loading {f}")

    base_directory = os.path.dirname(f)
    root_name, extension = os.path.splitext(os.path.basename(f))
    old_filename = base_directory + '/' + root_name + "_orig" + extension

    image = cv.imread(f)
    cv.imshow('f', np.asarray(image))
    # Define lower and upper limits of what to mask
    c_lo = np.array([229, 229, 229], dtype="uint16")
    c_hi = np.array([255, 255, 255], dtype="uint16")

    mask = cv.inRange(image, c_lo, c_hi)

    image2 = image
    image2[np.where(mask == [255])] = [255]
    print(f"moving {f} to {old_filename}")
    os.rename(f, old_filename)

    cv.imwrite(f, image2)


if __name__ == "__main__":
    # filename = f"{os.path.expanduser('~')}/Documents/Git/GitHub/TC57CIM/py/IEC61970/IEC61970Dependencies.png"
    # filename = f"{os.path.expanduser('~')}/Documents/Git/GitHub/TC57CIM/py/IEC61970/Base/AuxiliaryEquipment
    # /AuxiliaryEquipment.png"
    # filename = "C:/Users/pmora/Documents/Git/GitHub/TC57CIM/py/IEC61970/Base/DC/ACDCConnectivityModel.png"
    # filename = "C:/Users/pmora/Documents/Git/GitHub/TC57CIM/py/IEC61970/Base/DC/DocDC
    # /DCContainmentSymmetricalMonopole.png"
    # filename = "C:/Users/pmora/Documents/Git/GitHub/TC57CIM/py/IEC61968/AssetInfo/DCIMTransformerInfo.png"
    # dewatermark2(filename)

    if len(sys.argv) == 2:
        filename = sys.argv[1]
        dewatermark2(filename)
    else:
        filename = "C:/Users/pmora/Documents/Git/GitHub/TC57CIM/py/IEC61968/AssetInfo/DCIMTransformerInfo.png"
        refill_boxes(filename)

        # print("Usage: python convert_to_image.py <filename>")
        # sys.exit(1)
