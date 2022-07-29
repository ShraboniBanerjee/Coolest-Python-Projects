import pywhatkit as kit
import cv2
Handwrite=input("Enter text to convert into handwritten format :")
kit.text_to_handwriting(Handwrite, save_to="test.png")
img = cv2.imread("test.png")
cv2.imshow("Test Output", img)
cv2.waitKey(0)
cv2.destroyAllWindows()