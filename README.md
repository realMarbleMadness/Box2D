## Introduction

For more detailed explanation of this optimizer, refer to [upstream's REAMDE written by Leo and Alex](https://github.com/leonidk/Box2D/blob/master/README.md). This one is a simplified version.

## Install, Build and Run

### Install dependencies

Create a virtual environment of Python3. Python2 is not capatible since [Unpacking Argument Lists](https://docs.python.org/3/tutorial/controlflow.html#unpacking-argument-lists) is not available in Python2. How to create a virtual environment? It's 1:30 a.m. and I'm too tired. just search on Google and learn something.

```shell
pip install -r requirements.txt
```

### Build

```shell
./premake5 gmake
cd Build/gmake/
make -j -l config=release
```

### Run

To spin up the API server, run this:

```shell
python server.py
```

## How do I interact with it?

[Click me](https://realmarblemadness.github.io/slate/)

## Simple test

```
python optimize.py --part 7 differential_evolution --opt_iters 500
```
Why it is part 7? Because that's the code added by me, and I don't want to change the already too complicated structure. The code will not show any GUI and fail. Just ignore the error by now.