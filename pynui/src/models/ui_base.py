from __future__ import annotations
import pynvim
from typing import Any, Dict, List, Optional, Type, TypeVar

# from pynui.src.models.models_base import BaseSettings
from pynui.src.models.components import NuiComponent
from pynui.src.models.models_base import RendererSettings


class NuiRenderer:
    """Manages rendering of Nui components"""

    def __init__(self, nvim: pynvim.Nvim, settings: RendererSettings):
        self.nvim = nvim
        self.settings = settings
        self.id = str(id(self))
        self._lua_renderer = None
        self._components = []

    def render(self, components: List[NuiComponent]):
        """Render the given components"""
        self._components = components

        if not self._lua_renderer:
            lua_code = f"""
            local options = {self.settings.to_lua_code()}
            local renderer = require('nui-components.renderer').create(options)
            """
            self._lua_renderer = self.nvim.lua.execute(lua_code)

        # Initialize components
        for component in components:
            component._init_lua_component()

        # Create layout
        components_str = ",".join(f"component_{c._component_id}" for c in components)

        layout_code = f"""
        renderer:render(function()
            return require('nui-components').box({{
                direction = 'column',
                children = {{{components_str}}}
            }})
        end)
        """

        self.nvim.lua.execute(layout_code)

    def close(self):
        """Close the renderer"""
        if self._lua_renderer:
            self.nvim.lua.execute("renderer:close()")
            self._lua_renderer = None
            self._components = []
