# Sign_lang_interpreter
Sign language Interpreter

image_collecter.py

This Python script collects image data from a webcam for various classes by capturing and storing images in separate directories within the `./data` directory.

Here's a breakdown of the script:

### Libraries Imported
- `os`: Used for file/directory operations.
- `cv2` (OpenCV): Used for capturing images from the webcam and performing image-related operations.

### Constants Defined
- `DATA_DIR`: Specifies the directory where the image data will be stored (`'./data'`).
- `number_of_classes`: Indicates the number of classes (categories) for which the image data will be collected (e.g., hand gestures representing different classes).
- `dataset_size`: Determines the number of images to be collected for each class (e.g., 100 images per class).

### Capturing Image Data
- `cv2.VideoCapture(0)`: Initializes the webcam for capturing video frames. The index `0` represents the default camera (can be changed to `1`, `2`, etc., for different cameras if available).
- Iterates through each class from `0` to `number_of_classes - 1` using the `range()` function.

### Image Collection Loop
1. **Preparing for Image Capture**:
   - Creates a directory for the current class if it doesn't exist within the `./data` directory.
   - Displays a message on the screen indicating readiness to capture images and prompts to press "Q" to begin image collection.

2. **Image Capture Loop**:
   - Enters a loop to capture `dataset_size` number of images for the current class.
   - Displays the current frame from the webcam using `cv2.imshow()` continuously.
   - Waits for 25 milliseconds between frames (`cv2.waitKey(25)`) to control the frame display speed.
   - Captures the current frame using `cap.read()` and saves it as an image file (`{}.jpg`) in the corresponding class directory within `./data`.

3. **Release Resources**:
   - Releases the camera resource after image collection is complete using `cap.release()`.
   - Closes all OpenCV windows using `cv2.destroyAllWindows()`.

### Explanation Notes:
- The script sets up the webcam to capture video frames and stores the frames as individual image files (`{}.jpg`) for each class within the `./data` directory.
- Pressing the "Q" key while the script is running initiates image capture for each class.

Ensure that the webcam is properly connected and permissions are granted for camera access on your system before running this script. Adjust the `number_of_classes` and `dataset_size` variables as needed for your specific use case.


---------------------------------------------------------------------------------------------------
