import cv2

def capture_photos(num_photos):
    # Open the default camera
    cap = cv2.VideoCapture(0)

    # Check if the camera was opened successfully
    if not cap.isOpened():
        print("Failed to open the camera")
        return

    # Initialize a counter for captured photos
    photos_taken = 0

    # Capture and save photos until the desired number is reached
    while photos_taken < num_photos:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Display the resulting frame (optional)
        cv2.imshow('Camera', frame)

        # Wait for key press
        key = cv2.waitKey(1)

        # Press 's' to save the current frame as an image
        if key == ord('s'):
            # Define the filename for the captured photo
            filename = f'photo{photos_taken+1}.jpg'

            # Save the frame as an image
            cv2.imwrite(filename, frame)

            # Increment the counter
            photos_taken += 1
            print(f"Photo {photos_taken} captured!")

        # Press 'q' to quit the program
        if key == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()

# Call the function to capture 50 photos
capture_photos(50)
