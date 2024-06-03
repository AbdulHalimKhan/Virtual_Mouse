# Virtual Mouse with Hand Gestures

This project implements a virtual mouse controlled by hand gestures using OpenCV, Mediapipe, and PyAutoGUI. The webcam is used to track the hand and detect gestures to move the mouse pointer and perform click actions.

## Features
- Hand tracking using Mediapipe
- Gesture recognition for mouse control
- Real-time movement and click simulation

## Requirements
- Python 3.x
- OpenCV
- Mediapipe
- PyAutoGUI

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/AbdulHalimKhan/Virtual_Mouse.git
    cd virtual-mouse-hand-gestures
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the `virm_handges.py` script:
    ```bash
    python virm_handges.py
    ```

2. Ensure your hand is visible and well-lit for the webcam to detect and track.

3. Move your hand to control the mouse pointer. Bring your thumb and index finger together to simulate a mouse click.

## File Structure

- `virm_handges.py`: Main script to run the virtual mouse with hand gestures.
- `requirements.txt`: List of required Python packages.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

