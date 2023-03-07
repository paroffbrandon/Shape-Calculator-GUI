import PySimpleGUI as sg
from os import system, name

sg.theme("DarkGrey10")

sqr_layout = [
    [
        sg.Text(
            "This is the Square Calculator, please leave everything you do not have an answer to blank"
        )
    ],
    [
        sg.Text("What is the Length of your square?", size=(15, 1)),
        sg.Input(key="-SQR_L-"),
    ],
    [
        sg.Text("What is the Area of your square?", size=(15, 1)),
        sg.Input(key="-SQR_A-"),
    ],
    [
        sg.Text("What is the Perimeter of your square?", size=(15, 1)),
        sg.Input(key="-SQR_P-"),
    ],
    [
        sg.Button("Calculate", key="-SQR_CA-"),
        sg.Button("Clear", key="-SQR_CL-"),
        sg.Button("Exit", key="-SQR_EX-"),
    ],
]

rct_layout = [
    [
        sg.Text(
            "This is the Rectangle Calculator, please leave everything you do not have an answer to blank"
        )
    ],
    [
        sg.Text("What is the Length of your rectangle?", size=(15, 1)),
        sg.Input(key="-RCT_L-"),
    ],
    [
        sg.Text("What is the Width of your rectangle?", size=(15, 1)),
        sg.Input(key="-RCT_W-"),
    ],
    [
        sg.Text("What is the Area of your rectangle?", size=(15, 1)),
        sg.Input(key="-RCT_A-"),
    ],
    [
        sg.Text("What is the Perimeter of your rectangle?", size=(15, 1)),
        sg.Input(key="-RCT_P-"),
    ],
    [
        sg.Button("Calculate", key="-RCT_CA-"),
        sg.Button("Clear", key="-RCT_CL-"),
        sg.Button("Exit", key="-RCT_EX-"),
    ],
]

tri_layout = [
    [
        sg.Text(
            "This is the Triangle Calculator, please leave everything you dont have an answer to blank"
        )
    ],
    [
        sg.Text("What is the Base of your rectangle?", size=(15, 1)),
        sg.Input(key="-TRI_B-"),
    ],
    [
        sg.Text("What is the Side of your rectangle?", size=(15, 1)),
        sg.Input(key="-TRI_S-"),
    ],
    [
        sg.Text("What is the Hypotenus of your rectangle?", size=(15, 1)),
        sg.Input(key="-TRI_H-"),
    ],
    [
        sg.Text("What is the Area of your rectangle?", size=(15, 1)),
        sg.Input(key="-TRI_A-"),
    ],
    [
        sg.Text("What is the Perimeter of your rectangle?", size=(15, 1)),
        sg.Input(key="-TRI_P-"),
    ],
    [
        sg.Button("Calculate", key="-TRI_CA-"),
        sg.Button("Clear", key="-TRI_CL-"),
        sg.Button("Exit", key="-TRI_EX-"),
    ],
]

layout = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab("Square", sqr_layout),
                    ("Rectangle", rct_layout),
                    ("Triangle", tri_layout),
                ]
            ]
        )
    ]
]


window = sg.Window("Calculator", layout)

while True:
    event, values = window.read
    print(event, values)
    if event == "SQR-CA":
        sql = values["-SQR_L-"]
        sqa = values["-SQR_A-"]
        sqp = values["-SQR_P-"]

        if sql == "":
            sql = 0.0
        if sqa == "":
            sqa = 0.0
        if sqp == "":
            sqp - 0.0

        sql = float(sql)
        sqa = float(sqa)
        sqp = float(sqp)

        sqls = 0.0
        sqas = 0.0
        sqps = 0.0

        if sql == 0 and sqa == 0 and sqp == 0:
            window["-SQR-L"].update("Conflicting Values, Try Again")
            window["-SQR-A"].update("Conflicting Values, Try Again")
            window["-SQR-P"].update("Conflicting Values, Try Again")

        elif event == sg.WIN_CLOSED or event == "Exit":
            break
window.close()
