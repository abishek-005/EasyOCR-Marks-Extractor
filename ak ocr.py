import easyocr
import cv2
import re

img = cv2.imread(r"C:\Users\dell\Desktop\ak ocr\erp.png")

reader = easyocr.Reader(['en'], gpu=False)
results = reader.readtext(img, detail=0)

subjects = []
marks = []

i = 0
while i < len(results):
    text = results[i].strip()

    # Subject Name logic
    if text.lower() == "subject name":
        j = i + 1
        while j < len(results) and len(results[j].strip()) < 3:
            j += 1
        subjects.append(results[j].strip())

    # Marks logic
    if text.lower() == "marks":
        j = i + 1
        while j < len(results):
            num = re.findall(r"\d+", results[j])
            if num:
                marks.append(int(num[0]))
                break
            j += 1

    i += 1
print(results)
print(len(subjects[0]))
print("Subjects:", subjects)
print("Marks:", marks)
