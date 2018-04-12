# Box2d Optimizer

For more detailed explanation of this optimizer, refer to [upstream's REAMDE written by Leo and Alex](https://github.com/leonidk/Box2D/blob/master/README.md). This one is a simplified version.

## Install dependencies

Create a virtual environment of Python3. Python2 is not capatible since [Unpacking Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists) is not available in Python2. How to create a virtual environment? It's 1:30 a.m. and I'm too tired. just search on Google and learn something.

```
pip install -r requirements.txt
```

## Build
```
./premake5 gmake
cd Build/gmake/
make -j -l config=release
```

## Example Usage

```
python server.py
```
or if you want to tolerent yourself,
```
python optimize.py --part 7 differential_evolution --opt_iters 500
```
Why it is part 7? Because that's the code added by me, and I don't want to change the already too complicated structure. The code will not show any GUI and fail. Just ignore the error by now.

### What's actually happening?

The code reads setup from `tests/part_7.json`, hopefully comes from robot vision. It runs the optimizer to find the best pose of the blocks. Then it writes the result to `tests/part_7_optimization.json`, hopefully passed on to the ODE visualizer as well as Baxter robot.

### Why don't use ROS to communicate?

Because ROS Kinetic does not support Python3.
