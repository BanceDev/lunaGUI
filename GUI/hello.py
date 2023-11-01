import imgui

def hello_world():
    # open new window context
    imgui.begin("Your first window!", True)

    # draw text label inside of current window
    imgui.text("Hello world!")

    # close current window context
    imgui.end()