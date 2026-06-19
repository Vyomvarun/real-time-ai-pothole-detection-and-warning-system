from ultralytics import YOLO
import cv2
import winsound
import time

# Load Model
model = YOLO("best.pt")

# Webcam
cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)

width = 640
height = 480

# Save Output Video
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

out = cv2.VideoWriter(
    "output.mp4",
    fourcc,
    20,
    (width,height)
)

prev_time = time.time()

# Smart Beep Variable
beeped = False


while True:

    ret, frame = cap.read()

    if not ret:
        break


    # Light Blur

    blur = cv2.GaussianBlur(
        frame,
        (3,3),
        0
    )


    # Light Brightness

    bright = cv2.convertScaleAbs(

        blur,

        alpha=1.03,

        beta=3

    )


    # YOLO Detection

    results = model(

        bright,

        conf=0.30,

        imgsz=640,

        verbose=False

    )


    annotated_frame = results[0].plot()


    count = len(results[0].boxes)

    status = "SAFE"

    confidence = 0

    near_found = False


    for box in results[0].boxes:


        confidence = float(box.conf[0])


        x1,y1,x2,y2 = box.xyxy[0]


        w = x2-x1

        h = y2-y1


        area = w*h


        if area > 20000:

            status = "NEAR"

            near_found = True


        elif area > 7000:

            status = "MEDIUM"


        else:

            status = "FAR"



    # Smart Beep

    if near_found and not beeped:

        winsound.Beep(

            1000,

            150

        )

        beeped=True


    if not near_found:

        beeped=False



    # FPS

    current=time.time()

    fps=1/(current-prev_time)

    prev_time=current



    # TOP LEFT

    cv2.putText(

        annotated_frame,

        f"Potholes : {count}",

        (20,40),

        cv2.FONT_HERSHEY_SIMPLEX,

        1,

        (0,255,0),

        2

    )



    cv2.putText(

        annotated_frame,

        f"FPS : {int(fps)}",

        (20,80),

        cv2.FONT_HERSHEY_SIMPLEX,

        1,

        (0,255,255),

        2

    )



    color=(0,255,0)


    if status=="MEDIUM":

        color=(0,255,255)


    if status=="NEAR":

        color=(0,0,255)



    cv2.putText(

        annotated_frame,

        status,

        (20,120),

        cv2.FONT_HERSHEY_SIMPLEX,

        1,

        color,

        2

    )



    # TOP RIGHT

    cv2.putText(

        annotated_frame,

        f"Confidence : {confidence:.2f}",

        (350,40),

        cv2.FONT_HERSHEY_SIMPLEX,

        0.8,

        (255,255,0),

        2

    )



    # Bottom Warning

    if status=="NEAR":


        cv2.rectangle(

            annotated_frame,

            (0,height-50),

            (width,height),

            (0,0,255),

            -1

        )


        cv2.putText(

            annotated_frame,

            "WARNING : LARGE POTHOLE AHEAD",

            (50,height-18),

            cv2.FONT_HERSHEY_SIMPLEX,

            0.7,

            (255,255,255),

            2

        )



    # Save Video

    out.write(

        annotated_frame

    )



    # Display

    cv2.imshow(

        "AI Pothole Detector",

        annotated_frame

    )



    key=cv2.waitKey(1)



    # ESC

    if key==27:

        break



    # Screenshot

    if key==ord('s'):

        cv2.imwrite(

            "capture.jpg",

            annotated_frame

        )

        print("Screenshot Saved")



cap.release()

out.release()

cv2.destroyAllWindows()