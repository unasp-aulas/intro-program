from shiny.express import ui, input, render

with ui.sidebar(bg="#f8f8f8"):
    ui.input_select(
        "select",
        "Select",
        {
            "Olá": "Olá",
            "Hello": "Hello",
            "Hallo": "Hallo",
        },
    )

    ui.input_text("text", "Text input", "Enter name...")


@render.text
def value():
    return f"{input.select()} {input.text()}!"
