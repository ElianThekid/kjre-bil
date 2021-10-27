def my_function():
    radio.send_string("stop")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.UP,
    my_function)

def my_function2():
    radio.send_string("bak")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.DOWN,
    my_function2)

def my_function3():
    radio.send_string("stop")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.UP,
    my_function3)

def my_function4():
    radio.send_string("høyre")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.DOWN,
    my_function4)

def my_function5():
    radio.send_string("stop")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P15,
    joystickbit.ButtonType.UP,
    my_function5)

def regnomy():
    global mellomregning
    mellomregning += Math.map(joystickbit.get_rocker_value(joystickbit.rockerType.X),
        0,
        1024,
        -100,
        4)
    return mellomregning
def regnomx():
    global mellomregning
    mellomregning += Math.map(joystickbit.get_rocker_value(joystickbit.rockerType.X),
        0,
        1024,
        -100,
        4)
    return mellomregning

def on_received_value(name, value):
    if name == "x":
        pass
    elif name == "y":
        pass
radio.on_received_value(on_received_value)

def my_function6():
    radio.send_string("stop")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P14,
    joystickbit.ButtonType.UP,
    my_function6)

def my_function7():
    radio.send_string("venstre")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P13,
    joystickbit.ButtonType.DOWN,
    my_function7)

def my_function8():
    radio.send_string("fram")
joystickbit.on_button_event(joystickbit.JoystickBitPin.P12,
    joystickbit.ButtonType.DOWN,
    my_function8)

y = 0
x = 0
mellomregning = 0
joystickbit.init_joystick_bit()
radio.set_group(10)

def on_forever():
    pass
basic.forever(on_forever)

def on_forever2():
    global x, y
    x = regnomx()
    y = regnomx()
    radio.send_value("x", x)
    radio.send_value("y", y)
basic.forever(on_forever2)
