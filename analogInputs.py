import serial as sl
import ValveIndicator
import configuration
import outputs


class TestState:
    testState = False


class SerialComms:
    if TestState.testState is False:
        ser = sl.Serial('/dev/ttyACM0', 9600)


class PressureVariables:
    psv1 = 0
    psv2 = 0
    psv3 = 0
    psv4 = 0
    psv5 = 0


class AnalogZero:
    channel1_zero = 0
    channel2_zero = 0
    channel3_zero = 0
    channel4_zero = 0
    channel5_zero = 0


class AnalogSpan:
    channel1_span = 450
    channel2_span = 450
    channel3_span = 450
    channel4_span = 450
    channel5_span = 450


class ValveStates:

    def valve1_close(self):
        ValveIndicator.ValveIndicator.valve1_state = ValveIndicator.ValveIndicator.valve_closed
        if TestState.testState is True:
            print('Valve 1 is closed')

        if TestState.testState is False:
            SerialComms.ser.write(b'0')

    def valve1_open(self):
        ValveIndicator.ValveIndicator.valve1_state = ValveIndicator.ValveIndicator.valve_open
        if TestState.testState is True:
            print('Valve 1 is open')

        if TestState.testState is False:
            SerialComms.ser.write(b'1')

    def valve2_close(self):
        ValveIndicator.ValveIndicator.valve2_state = ValveIndicator.ValveIndicator.valve_closed
        if TestState.testState is True:
            print('Valve 2 is closed')

        if TestState.testState is False:
            SerialComms.ser.write(b'2')

    def valve2_open(self):
        ValveIndicator.ValveIndicator.valve2_state = ValveIndicator.ValveIndicator.valve_open
        if TestState.testState is True:
            print('Valve 2 is open')

        if TestState.testState is False:
            SerialComms.ser.write(b'3')

    def valve3_close(self):
        ValveIndicator.ValveIndicator.valve3_state = ValveIndicator.ValveIndicator.valve_closed
        if TestState.testState is True:
            print('Valve 3 is closed')

        if TestState.testState is False:
            SerialComms.ser.write(b'4')

    def valve3_open(self):
        ValveIndicator.ValveIndicator.valve3_state = ValveIndicator.ValveIndicator.valve_open
        if TestState.testState is True:
            print('Valve 3 is open')

        if TestState.testState is False:
            SerialComms.ser.write(b'5')

    def valve4_close(self):
        ValveIndicator.ValveIndicator.valve4_state = ValveIndicator.ValveIndicator.valve_closed
        if TestState.testState is True:
            print('Valve 4 is closed')

        if TestState.testState is False:
            SerialComms.ser.write(b'6')

    def valve4_open(self):
        ValveIndicator.ValveIndicator.valve4_state = ValveIndicator.ValveIndicator.valve_open
        if TestState.testState is True:
            print('Valve 4 is open')

        if TestState.testState is False:
            SerialComms.ser.write(b'7')

    def valve5_close(self):
        ValveIndicator.ValveIndicator.valve5_state = ValveIndicator.ValveIndicator.valve_closed
        if TestState.testState is True:
            print('Valve 5 is closed')

        if TestState.testState is False:
            SerialComms.ser.write(b'8')

    def valve5_open(self):
        ValveIndicator.ValveIndicator.valve5_state = ValveIndicator.ValveIndicator.valve_open
        if TestState.testState is True:
            print('Valve 5 is open')

        if TestState.testState is False:
            SerialComms.ser.write(b'9')

    def valve6_close(self):
        ValveIndicator.ValveIndicator.valve6_state = ValveIndicator.ValveIndicator.valve_closed
        if TestState.testState is True:
            print('Valve 6 is closed')

        if TestState.testState is False:
            SerialComms.ser.write(b'10')

    def valve6_open(self):
        ValveIndicator.ValveIndicator.valve6_state = ValveIndicator.ValveIndicator.valve_open
        if TestState.testState is True:
            print('Valve 6 is open')

        if TestState.testState is False:
            SerialComms.ser.write(b'11')


def DeclareAnalogInputs():
    if TestState.testState is True:
        PressureVariables.psv1 = 512
        PressureVariables.psv2 = 512
        PressureVariables.psv3 = 512
        PressureVariables.psv4 = 512
        PressureVariables.psv5 = 512

    if TestState.testState is False:
        cookedserial = SerialComms.ser.readline().decode('utf-8').strip('\r\n')
        datasplit = cookedserial.split(',')
        PressureVariables.psv1 = datasplit[0].strip('<')
        PressureVariables.psv2 = datasplit[1]
        PressureVariables.psv3 = datasplit[2]
        PressureVariables.psv4 = datasplit[3]
        PressureVariables.psv5 = datasplit[4].strip('>')


def ConvertRawInputToPSI():
    ch1_zero = int(AnalogZero.channel1_zero)
    ch2_zero = int(AnalogZero.channel2_zero)
    ch3_zero = int(AnalogZero.channel3_zero)
    ch4_zero = int(AnalogZero.channel4_zero)
    ch5_zero = int(AnalogZero.channel5_zero)
    ch1_span = int(AnalogSpan.channel1_span)
    ch2_span = int(AnalogSpan.channel2_span)
    ch3_span = int(AnalogSpan.channel3_span)
    ch4_span = int(AnalogSpan.channel4_span)
    ch5_span = int(AnalogSpan.channel5_span)
    """PressureVariables.psv1 = int((int(PressureVariables.psv1) * (ch1_span - ch1_zero)) / 1024)
    PressureVariables.psv2 = int((int(PressureVariables.psv2) * (ch2_span - ch2_zero)) / 1024)
    PressureVariables.psv3 = int((int(PressureVariables.psv3) * (ch3_span - ch3_zero)) / 1024)
    PressureVariables.psv4 = int((int(PressureVariables.psv4) * (ch4_span - ch4_zero)) / 1024)
    PressureVariables.psv5 = int((int(PressureVariables.psv5) * (ch5_span - ch5_zero)) / 1024)"""


def Cylinder1Initialization(self):
    if self.psv1 < self.slider1_upper:
        ValveStates.valve1_open(self)
        ValveStates.valve2_close(self)
    if self.psv1 > self.slider1_lower and self.slider5_upper > self.psv5 > self.slider5_lower:
        ValveStates.valve1_close(self)
        ValveStates.valve2_close(self)


def Cylinder2Initialization(self):
    if self.psv2 < self.slider2_upper:
        ValveStates.valve2_open(self)
        ValveStates.valve3_close(self)
    if self.psv2 > self.slider2_lower and self.slider1_upper > self.psv1 > self.slider1_lower:
        ValveStates.valve2_close(self)
        ValveStates.valve3_close(self)


def Cylinder3Initialization(self):
    if self.psv3 < self.slider3_upper:
        ValveStates.valve3_open(self)
        ValveStates.valve4_close(self)
    if self.psv3 > self.slider3_lower and self.slider2_upper > self.psv2 > self.slider2_lower:
        ValveStates.valve3_close(self)
        ValveStates.valve4_close(self)


def Cylinder4Initialization(self):
    if self.psv4 < self.slider4_upper:
        ValveStates.valve4_open(self)
        ValveStates.valve5_close(self)
    if self.psv4 > self.slider4_lower and self.slider3_upper > self.psv3 > self.slider3_lower:
        ValveStates.valve4_close(self)
        ValveStates.valve5_close(self)


def Cylinder5Initialization(self):
    if self.psv5 < self.slider5_upper:
        ValveStates.valve5_open(self)
        ValveStates.valve6_close(self)
    if self.psv5 > self.slider5_lower and self.slider4_upper > self.psv4 > self.slider4_lower:
        ValveStates.valve5_close(self)
        ValveStates.valve6_close(self)


def CylinderComparisonLowPSI(self):
    if outputs.AutoBools.valveAll_auto is True:
        Cylinder1Initialization(self)
        Cylinder2Initialization(self)
        Cylinder3Initialization(self)
        Cylinder4Initialization(self)
        Cylinder5Initialization(self)


def Initialization(self):
    DeclareAnalogInputs()
    ConvertRawInputToPSI()
    CylinderComparisonLowPSI(self)
