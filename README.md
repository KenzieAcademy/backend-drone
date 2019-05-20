<img width="300" src="img/tello_drone_1.jpg" />

# UNDER CONSTRUCTION

# backend-drone
Students will use python to control a `Tello` hobby drone, and fly around an obstacle course.  The drone can be purchased from the [DJI Store](https://store.dji.com/shop/tello-series)
for $99.00.  This particular drone is programmable in Python, with sample code in GitHub.

## Setup
- Future version will require building a h264 video decoder library.
- For now, just clone the repo and create your local virtual environment.

## Tello LED Lights
- flashing blue: charging
- solid blue: charged
- flashing purple: booting up
- flashing yellow fast: wifi network set up,waiting for connection
- flashing yellow: User connected

## Demo (no video)
1. Open wifi connections list
1. Tello drone power on with side button
2. Wait for wifi signal, then connect direct to TELLO-xxxxx wifi
3. Run the `tello_test.py` program
4. Drone will takeoff and fly a 1-meter triangle pattern, and then land.

## References
- [Tello-Python](https://github.com/dji-sdk/Tello-Python)
- [DJITelloPy](https://github.com/damiafuentes/DJITelloPy)
- [Tello Pilots Forum](https://tellopilots.com/)
- [Tello CV Tracker](https://github.com/Ubotica/telloCV/)
- [Tello Gesture Control](https://github.com/GalBrandwine/HalloPy)

