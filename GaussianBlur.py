


def subtract_gaussian_blur(img):
    gb_img = cv2.GaussianBlur(img, (0, 0), 5)
    return cv2.addWeighted(img, 4, gb_img, -4, 128)