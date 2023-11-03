# lunaGUI

User interface for the Ohio State University Lunabotics team driver station. The code is written in python using imgui for the user interface and ZeroMQ websockets for the networking communications.

## Launching the Program

The main.py file launches the driver station UI and the server, compile main.py in whatever tool you use to run python programs or cd into the folder directory and run the following command:

```
python main.py
```

## Dependencies

In order to compile and run this project you will need imgui, pygame, psutil, and ZeroMQ installed on your computer.

### Imgui

```
pip install imgui[full]
```

### Pygame

```
pip install pygame
```

### Psutil

```
pip install psutil
```

### ZeroMQ

```
pip install pyzmq
```
