import pynvim
from pynui.src.config import NUI_ROOT

# Constants ---------------------------------
lua_code = f"{NUI_ROOT}/lua/examples/simple_input.lua"
lua_file = "/home/andrew/Documents/Projects/PyNui/pynui/nui-components.nvim/lua/examples/simple_input.lua"


# Reference lua file ------------------------
def test():
    print_refs()


@pynvim.plugin
class TestInput(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.function("TestInput", sync=True)
    def testfunction(self, args):
        return "Hello, Nvim!"


# print(f"Test\n\n")
# with open(lua_code, "r") as f:
#    print(f.read())


# Run it ------------------------------------
# Can run test file with:
# :source /home/andrew/Documents/Projects/PyNui/pynui/nui-components.nvim/lua/examples/simple_input.lua


# Misc --------------------------------------
def print_refs():
    print(f"test")
    print(f"Nui Root: {NUI_ROOT}")
    print(f"Lua Code Loc: {lua_code}")
