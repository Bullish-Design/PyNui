# Imports
import pynvim
from pynui.src.models.models_base import (
    BaseSettings,
    RendererSettings,
    TextInput,
    TextInputSettings,
    Button,
    ButtonSettings,
    Select,
    SelectSettings,
    SelectOption,
    LuaCallable,
)
from pynui.src.models.ui_base import NuiRenderer  # NuiComponent

print(f"Hello?")


# Plugin code
# @pynvim.plugin
class MyPlugin:
    def __init__(self, nvim):
        self.nvim = nvim

    # @pynvim.command("MyPluginForm", nargs="*", sync=False)
    def show_form(self, args):
        """Show a form using PyNui components"""
        # Create renderer with settings
        renderer = NuiRenderer(
            self.nvim, RendererSettings(size={"width": 60, "height": 20})
        )

        # Create text input
        text_input = TextInput(
            self.nvim,
            TextInputSettings(
                placeholder="Enter text...", on_change=LuaCallable(self._on_text_change)
            ),
        )

        # Create select
        select = Select(
            self.nvim,
            SelectSettings(
                size=3,
                data=[
                    SelectOption(text="Option 1"),
                    SelectOption(text="Option 2"),
                    SelectOption(text="Option 3"),
                ],
                on_change=LuaCallable(self._on_select_change),
            ),
        )

        # Create button
        button = Button(
            self.nvim,
            ButtonSettings(label="Submit", on_press=LuaCallable(self._on_submit)),
        )

        # Render components
        renderer.render([text_input, select, button])

    def _on_text_change(self, value: str):
        self.nvim.command(f'echo "Text changed: {value}"')

    def _on_select_change(self, value: dict):
        self.nvim.command(f'echo "Selection changed: {value}"')

    def _on_submit(self):
        self.nvim.command('echo "Form submitted!"')
