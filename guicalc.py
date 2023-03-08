import PySimpleGUI as sg
import math

# Theme for the window
sg.theme("Topanga")

# Square Tab Layout  -  Default text would be zero
sqr_layout = [
    [
        sg.Text(
            "This is the Square Calculator, please leave everything you do not have an answer to as a zero"
        )
    ],
    [
        sg.Text("What is the Length of your square?", size=(30, 1)),
        sg.Input(key="-SQR_L-", default_text="0"),
    ],
    [
        sg.Text("What is the Area of your square?", size=(30, 1)),
        sg.Input(key="-SQR_A-", default_text="0"),
    ],
    [
        sg.Text("What is the Perimeter of your square?", size=(30, 1)),
        sg.Input(key="-SQR_P-", default_text="0"),
    ],
    [sg.Text("")],
    [sg.Text("")],
    [
        sg.Button("Calculate", key="-SQR_CA-"),
        sg.Button("Clear", key="-SQR_CL-"),
    ],
]

# Rectangle Tab Layout  -  Default text would be zero
rct_layout = [
    [
        sg.Text(
            "This is the Rectangle Calculator, please leave everything you do not have an answer to blank"
        )
    ],
    [
        sg.Text("What is the Length of your rectangle?", size=(30, 1)),
        sg.Input(key="-RCT_L-", default_text="0"),
    ],
    [
        sg.Text("What is the Width of your rectangle?", size=(30, 1)),
        sg.Input(key="-RCT_W-", default_text="0"),
    ],
    [
        sg.Text("What is the Area of your rectangle?", size=(30, 1)),
        sg.Input(key="-RCT_A-", default_text="0"),
    ],
    [
        sg.Text("What is the Perimeter of your rectangle?", size=(30, 1)),
        sg.Input(key="-RCT_P-", default_text="0"),
    ],
    [sg.Text("")],
    [sg.Button("Calculate", key="-RCT_CA-"), sg.Button("Clear", key="-RCT_CL-")],
]

# Triangle Tab Layout  -  Default text would be zero
tri_layout = [
    [
        sg.Text(
            "This is the Triangle Calculator, please leave everything you dont have an answer to blank"
        )
    ],
    [
        sg.Text("What is the Base of your triangle?", size=(30, 1)),
        sg.Input(key="-TRI_B-", default_text="0"),
    ],
    [
        sg.Text("What is the Side of your triangle?", size=(30, 1)),
        sg.Input(key="-TRI_S-", default_text="0"),
    ],
    [
        sg.Text("What is the Hypotenus of your triangle?", size=(30, 1)),
        sg.Input(key="-TRI_H-", default_text="0"),
    ],
    [
        sg.Text("What is the Area of your triangle?", size=(30, 1)),
        sg.Input(key="-TRI_A-", default_text="0"),
    ],
    [
        sg.Text("What is the Perimeter of your triangle?", size=(30, 1)),
        sg.Input(key="-TRI_P-", default_text="0"),
    ],
    [sg.Button("Calculate", key="-TRI_CA-"), sg.Button("Clear", key="-TRI_CL-")],
]

# Layout for the application window
layout = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab("Square", sqr_layout),
                    sg.Tab("Rectangle", rct_layout),
                    sg.Tab("Triangle", tri_layout),
                ]
            ]
        )
    ]
]

# Set variable for the window
window = sg.Window("Calculator", layout)

while True:
    # Update the events from window, print window.read() output into console for debugging perposes
    event, values = window.read()
    print(event, values)

    # Asking PySimpleGUI to change back to "blank" won't work, so I made a function to set it equal to zero
    blank = 0

    # Caclulations for Square Tab
    if event == "-SQR_CA-":
        # Set values for inputs to variables
        sql = values["-SQR_L-"]
        sqa = values["-SQR_A-"]
        sqp = values["-SQR_P-"]

        # If the input was untouced, set it to float 0.0
        if sql == "0":
            sql = 0.0
        if sqa == "0":
            sqa = 0.0
        if sqp == "0":
            sqp = 0.0

        # Convert every input to float
        sql = float(sql)
        sqa = float(sqa)
        sqp = float(sqp)

        # Reset solved variable to float 0.0
        sqls = 0.0
        sqas = 0.0
        sqps = 0.0

        # If all of the values are left blank, then there is no way for the calculator to calculate
        if sql == 0 and sqa == 0 and sqp == 0:
            window["-SQR_L-"].update("No Values Input, please try again")
            window["-SQR_A-"].update("No Values Input, please try again")
            window["-SQR_P-"].update("No Values Input, please try again")
        # So far how I set these is check down a checklist of possible combinations of inputs to solutions, math may be done twice or more, and at the end there will be error checking
        # Math for length input
        if sql != 0:
            sqls = sql
            sqas = sql * sql
            sqps = sql * 4
        # Math for area input
        elif sqa != 0:
            sqls = math.sqrt(sqa)
            sqas = sqa
            sqps = math.sqrt(sqa) * 4
        # Math for perimeter input
        elif sqp != 0:
            sqls = sqp / 4
            sqas = (sqp / 4) * (sqp / 4)
            sqps = sqp

        # If the math cannot be done, this message pops up saying the calculator is not coded to deal with this type of math
        else:
            window["-SQR_L-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )
            window["-SQR_A-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )
            window["-SQR_P-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )

        # Make sure that solved variables are floats, not needed but extra insurance I guess
        sqls = float(sqls)
        sqas = float(sqas)
        sqps = float(sqps)

        # If there is any conflicting inputs compared to solutions notify user
        if (
            (sql != 0 and sql != sqls)
            or (sqa != 0 and sqa != sqas)
            or (sqp != 0 and sqp != sqps)
        ):
            window["-SQR_L-"].update("There are Conflicting Values Present, Try Again")
            window["-SQR_A-"].update("There are Conflicting Values Present, Try Again")
            window["-SQR_P-"].update("There are Conflicting Values Present, Try Again")

        # Update window with solved values
        else:
            window["-SQR_L-"].update(sqls)
            window["-SQR_A-"].update(sqas)
            window["-SQR_P-"].update(sqps)

    # Sets all values back to zero
    elif event == "-SQR_CL-":
        window["-SQR_L-"].update(blank)
        window["-SQR_A-"].update(blank)
        window["-SQR_P-"].update(blank)

    # Calculations for Rectangle Tab
    elif event == "-RCT_CA-":
        # Convert Values to Variables
        rctl = values["-RCT_L-"]
        rctw = values["-RCT_W-"]
        rcta = values["-RCT_A-"]
        rctp = values["-RCT_P-"]

        # Convert blanks to float 0.0
        if rctl == "0":
            rctl = 0.0
        if rctw == "0":
            rctw = 0.0
        if rcta == "0":
            rcta = 0.0
        if rctp == "0":
            rctp = 0.0

        # Converts input to float
        rctl = float(rctl)
        rctw = float(rctw)
        rcta = float(rcta)
        rctp = float(rctp)

        # Reverts previous calculation to float 0.0
        rctls = 0.0
        rctws = 0.0
        rctas = 0.0
        rctps = 0.0

        # If nothing is input, notify user
        if rctl == 0 and rctw == 0 and rcta == 0 and rctp == 0:
            window["-RCT_L-"].update("No Values Input, please try again")
            window["-RCT_W-"].update("No Values Input, please try again")
            window["-RCT_A-"].update("No Values Input, please try again")
            window["-RCT_P-"].update("No Values Input, please try again")
        # Math for length and width input
        elif rctl != 0 and rctw != 0:
            rctls = rctl
            rctws = rctw
            rctas = rctl * rctw
            rctps = (rctl * 2) + (rctw * 2)
        # Math for length and area input
        elif rctl != 0 and rcta != 0:
            rctls = rctl
            rctws = rcta / rctl
            rctas = rcta
            rctps = (rctl * 2) + ((rcta / rctl) * 2)
        # Math for width and area input
        elif rctw != 0 and rcta != 0:
            rctls = rcta / rctw
            rctws = rctw
            rctas = rcta
            rctps = ((rcta / rctw) * 2) + (rctw * 2)
        # Math for length and perimeter input
        elif rctl != 0 and rctp != 0:
            rctls = rctl
            rctws = (rctp - (rctl * 2)) / 2
            rctas = rctl * ((rctp - (rctl * 2)) / 2)
            rctps = rctp
        # Math for width and perimeter input
        elif rctw != 0 and rctp != 0:
            rctls = (rctp - (rctw * 2)) / 2
            rctws = rctw
            rctas = rctw * ((rctp - (rctw * 2)) / 2)
            rctps = rctp

        # If the math cannot be done, this message pops up saying the calculator is not coded to deal with this type of math
        else:
            window["-RCT_L-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )
            window["-RCT_W-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )
            window["-RCT_A-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )
            window["-RCT_P-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )

        # Ensures solved variables are floats
        rctls = float(rctls)
        rctws = float(rctws)
        rctas = float(rctas)
        rctps = float(rctps)

        # Notifies user about conflicting values
        if (
            (rctl != 0 and rctl != rctls)
            or (rctw != 0 and rctw != rctws)
            or (rcta != 0 and rcta != rctas)
            or (rctp != 0 and rctp != rctps)
        ):
            window["-RCT_L-"].update("There are Conflicting Values Present, Try Again")
            window["-RCT_W-"].update("There are Conflicting Values Present, Try Again")
            window["-RCT_A-"].update("There are Conflicting Values Present, Try Again")
            window["-RCT_P-"].update("There are Conflicting Values Present, Try Again")

        # Update the window to calculated values
        else:
            window["-RCT_L-"].update(rctls)
            window["-RCT_W-"].update(rctws)
            window["-RCT_A-"].update(rctas)
            window["-RCT_P-"].update(rctps)

    # Set all values equal to zero again
    elif event == "-RCT_CL-":
        window["-RCT_L-"].update(blank)
        window["-RCT_W-"].update(blank)
        window["-RCT_A-"].update(blank)
        window["-RCT_P-"].update(blank)

    # Calculations for Triangle Tab
    elif event == "-TRI_CA-":
        trb = values["-TRI_B-"]
        trs = values["-TRI_S-"]
        trh = values["-TRI_H-"]
        tra = values["-TRI_A-"]
        trp = values["-TRI_P-"]

        # If there was no value given, then the value will be set to 0.0
        if trb == "0":
            trb = 0.0
        if trs == "0":
            trs = 0.0
        if trh == "0":
            trh = 0.0
        if tra == "0":
            tra = 0.0
        if trp == "0":
            trp = 0.0

            # Converting values to floats for math
            trb = float(trb)
            trs = float(trs)
            trh = float(trh)
            tra = float(tra)
            trp = float(trp)

            # Setting the solved values to 0 before math to clear up old math
            trbs = 0.0
            trss = 0.0
            trhs = 0.0
            tras = 0.0
            trps = 0.0

        # Update the window to nofity user there is no values input
        if trb == 0 and trs == 0 and trh == 0 and tra == 0 and trp == 0:
            window["-TRI_B-"].update("No Values Input, please try again")
            window["-TRI_S-"].update("No Values Input, please try again")
            window["-TRI_H-"].update("No Values Input, please try again")
            window["-TRI_A-"].update("No Values Input, please try again")
            window["-TRI_P-"].update("No Values Input, please try again")

        # TRIANGLES -  I do not like triangles
        # Math for base and side input
        if trb != 0 and trs != 0:
            trbs = trb
            trss = trs
            trhs = math.sqrt(((trb**2) + (trs**2)))
            tras = (trb * trs) * 0.5
            trps = (trb + trs) + (math.sqrt(((trb**2) + (trs**2))))
        # Math for base and hypotenus input
        elif trb != 0 and trh != 0:
            trbs = trb
            trss = math.sqrt(((trh**2) - (trb**2)))
            trhs = trh
            tras = (trb * (math.sqrt(((trh**2) - (trb**2))))) / 2
            trps = (trb + trh) + (math.sqrt(((trh**2) - (trb**2))))
        # Math for base and area input
        elif trb != 0 and tra != 0:
            trbs = trb
            trss = tra / trb
            trhs = math.sqrt(((trb**2) + ((tra / trb) ** 2)))
            tras = tra
            trps = (trb + (tra / trb)) + (math.sqrt(((trb**2) + ((tra / trb) ** 2))))
        # Math for side and hypotenus input
        elif trs != 0 and trh != 0:
            trbs = math.sqrt(((trh**2) - (trs**2)))
            trss = trs
            trhs = trh
            tras = (trs * (math.sqrt(((trh**2) - (trs**2))))) / 2
            trps = (trs + trh) + (math.sqrt(((trh**2) - (trs**2))))
        # Math for side and area input
        elif trs != 0 and tra != 0:
            trbs = (tra * 2) / trs
            trss = trs
            trhs = math.sqrt(((trs**2) + ((tra / trs) ** 2)))
            tras = tra
            trps = (trs + (tra / trs)) + (math.sqrt(((trs**2) + ((tra / trs) ** 2))))

        # If the math cannot be done, this message pops up saying the calculator is not coded to deal with this type of math
        else:
            window["-TRI_B-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )
            window["-TRI_S-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )
            window["-TRI_H-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )
            window["-TRI_A-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )
            window["-TRI_P-"].update(
                "Currently this calculator is not able to calculate everything based off of these values"
            )

        # Ensures solved variables are floats
        trbs = float(trbs)
        trss = float(trss)
        trhs = float(trhs)
        tras = float(tras)
        trps = float(trps)

        # Notifies the user of conflicting arguments
        if (
            (trb != 0 and trb != trbs)
            or (trs != 0 and trs != trss)
            or (trh != 0 and trh != trhs)
            or (tra != 0 and tra != tras)
            or (trp != 0 and trp != trps)
        ):
            window["-TRI_B-"].update("There are Conflicting Values Present, Try Again")
            window["-TRI_S-"].update("There are Conflicting Values Present, Try Again")
            window["-TRI_H-"].update("There are Conflicting Values Present, Try Again")
            window["-TRI_A-"].update("There are Conflicting Values Present, Try Again")
            window["-TRI_P-"].update("There are Conflicting Values Present, Try Again")

            # Updates windows with calcualted values
        else:
            window["-TRI_B-"].update(trbs)
            window["-TRI_S-"].update(trss)
            window["-TRI_H-"].update(trhs)
            window["-TRI_A-"].update(tras)
            window["-TRI_P-"].update(trps)

    # Set all values equal to zero
    elif event == "-TRI_CL-":
        window["-TRI_B-"].update(blank)
        window["-TRI_S-"].update(blank)
        window["-TRI_H-"].update(blank)
        window["-TRI_A-"].update(blank)
        window["-TRI_P-"].update(blank)

    elif event == sg.WIN_CLOSED:
        break
window.close()
