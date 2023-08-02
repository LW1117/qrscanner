import cv2
from pyzbar.pyzbar import decode


def read_qr_code(image_path):
    # Read the image
    image = cv2.imread(image_path)

    # Decode the QR code
    decoded_objects = decode(image)

    # Process the results
    for obj in decoded_objects:
        data = obj.data.decode('utf-8')
        return data
    print('ERROR!!!!')
    return 0
