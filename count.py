from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Load video
cap = cv2.VideoCapture("traffic.mp4")

# Counting variables
count = 0
line_y = 300
tracked_ids = set()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Run YOLO on frame
    results = model(frame)[0]

    # Process detections
    for box in results.boxes:
        cls = int(box.cls[0])
        label = model.names[cls]

        # Only count vehicles
        if label not in ["car", "truck", "bus", "motorbike"]:
            continue

        x1, y1, x2, y2 = map(int, box.xyxy[0])

        obj_id = int(box.id[0]) if box.id is not None else None

        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        # Draw center
        cv2.circle(frame, (cx, cy), 5, (255, 0, 0), -1)

        # Count when crossing line
        if cy > line_y and obj_id not in tracked_ids:
            tracked_ids.add(obj_id)
            count += 1

    # Draw counting line
    cv2.line(frame, (0, line_y), (1280, line_y), (0, 255, 0), 2)

    # Display count
    cv2.putText(frame, f"Count: {count}", (50, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

    cv2.imshow("Vehicle Counting", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
