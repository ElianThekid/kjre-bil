joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P12, joystickbit.ButtonType.up, function () {
    radio.sendString("stop")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P14, joystickbit.ButtonType.down, function () {
    radio.sendString("bak")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.up, function () {
    radio.sendString("stop")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.down, function () {
    radio.sendString("høyre")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P15, joystickbit.ButtonType.up, function () {
    radio.sendString("stop")
})
function regnomy () {
    mellomregning = Math.map(joystickbit.getRockerValue(joystickbit.rockerType.X), 0, 1024, 100, -100)
    return mellomregning
}
function regnomx () {
    mellomregning = Math.map(joystickbit.getRockerValue(joystickbit.rockerType.Y), 0, 1024, 100, -100)
    return mellomregning
}
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P14, joystickbit.ButtonType.up, function () {
    radio.sendString("stop")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P13, joystickbit.ButtonType.down, function () {
    radio.sendString("venstre")
})
joystickbit.onButtonEvent(joystickbit.JoystickBitPin.P12, joystickbit.ButtonType.down, function () {
    radio.sendString("fram")
})
let y = 0
let x = 0
let mellomregning = 0
joystickbit.initJoystickBit()
radio.setGroup(10)
basic.forever(function () {
    x = regnomx()
    y = regnomx()
    if (Math.abs(x) > 5) {
        radio.sendValue("x", x)
    }
    if (Math.abs(y) > 5) {
        radio.sendValue("y", y)
    }
})
