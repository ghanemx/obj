#install_requires=['numpy', 'progressbar', 'requests', 'pillow','imutils']
# import necessary packages
import cvlib as cv
from cvlib.object_detection import draw_bbox
from cvlib.object_detection import line_to_speak
import cv2

# read input image
image = cv2.imread(r'C:\Users\Ghanem\Downloads\spoon.jpeg')

# apply object detection
bbox, label, conf = cv.detect_common_objects(image,model='yolov4')

#line to speak
text=line_to_speak(label)
print(text)

'''
#print(label, conf)

# draw bounding box over detected objects
out = draw_bbox(image, bbox, label, conf)

# display output
# press any key to close window           
cv2.imshow("object_detection", out)
cv2.waitKey()

# release resources
cv2.destroyAllWindows()

'''