import imgui

def do_thing():
    text_val = 'Type the your message here.'
    imgui.begin("Example: text input")
    changed, text_val = imgui.input_text_multiline(
        'Message:',
        text_val,
        2056
    )
    imgui.text('You wrote:')
    imgui.same_line()
    imgui.text(text_val)
    imgui.end()