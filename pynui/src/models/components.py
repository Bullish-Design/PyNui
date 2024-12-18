# Imports
import pynvim
import json
from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union, Callable, TypeVar, Type

# from dataclasses import dataclass, asdict
from pydantic import BaseModel
# Library Imports


# Classes


class LuaCallable:
    """Wrapper for Python callbacks that will be converted to Lua functions"""

    def __init__(self, callback: Callable):
        self.callback = callback
        self.callback_id = str(id(callback))

    def to_lua(self) -> str:
        """Convert to Lua function string"""
        return f"""
        function(...)
            local args = vim.fn.json_encode({{...}})
            vim.fn.pynvim_callback("{self.callback_id}", args)
        end
        """


class BaseSettings(BaseModel):
    """Base settings model with Lua conversion support"""

    class Config:
        arbitrary_types_allowed = True

    def to_lua(self) -> Dict[str, Any]:
        """Convert settings to Lua-compatible format"""
        result = {}
        for key, value in self.dict(exclude_none=True).items():
            if isinstance(value, LuaCallable):
                result[key] = value.to_lua()
            elif isinstance(value, BaseSettings):
                result[key] = value.to_lua()
            else:
                result[key] = value
        return result

    def to_lua_code(self) -> str:
        """Convert settings to Lua code string"""
        return f"vim.fn.json_decode([==[{json.dumps(self.to_lua())}]==])"


class NuiComponent(ABC):
    """Base class for all Nui Components"""

    def __init__(self, nvim: pynvim.Nvim, settings: Type[BaseSettings]):
        self.nvim = nvim
        self.settings = settings
        self._component_id = str(id(self))
        self._lua_component = None

    def _init_lua_component(self):
        """Initialize the underlying Lua component"""
        lua_code = f"""
        local props = {self.settings.to_lua_code()}
        local component = require('nui-components.{self.component_name}')(props)
        return component
        """
        self._lua_component = self.nvim.lua.execute(lua_code)
        return self._lua_component

    @property
    @abstractmethod
    def component_name(self) -> str:
        """Return the name of the Lua component"""
        pass

    @property
    @abstractmethod
    def settings_class(self) -> Type[BaseSettings]:
        """Return the settings class for this component"""
        pass
