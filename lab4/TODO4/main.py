import cv2
def rotate_image(image, angle):
    height, width = image.shape[:2]
    rotation_matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1)
    cos_angle = abs(rotation_matrix[0, 0])
    sin_angle = abs(rotation_matrix[0, 1])
    new_width = int((height * sin_angle) + (width * cos_angle))
    new_height = int((height * cos_angle) + (width * sin_angle))
    rotation_matrix[0, 2] += (new_width / 2) - width / 2
    rotation_matrix[1, 2] += (new_height / 2) - height / 2
    rotated_resized_image = cv2.warpAffine(image, rotation_matrix, (new_width, new_height))
    return rotated_resized_image
def on_trackbar(val):
    global angle
    angle = val
    rotated_image = rotate_image(image, angle)
    cv2.imshow("Image", rotated_image)

image = cv2.imread("dog.jpg")
image = cv2.resize(image,(600,300))
cv2.namedWindow("Image")
cv2.createTrackbar("Angle", "Image", 0, 360, on_trackbar)
angle = 0
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
