from __future__ import annotations
from pydantic import BaseModel, Field, validator
from typing import Any, Dict, List, Optional, Union, Callable, TypeVar
from dataclasses import dataclass

# from abc import ABC
# import json

from pynui.src.models.components import NuiComponent, BaseSettings, LuaCallable


class TextInput(NuiComponent):
    @property
    def component_name(self) -> str:
        return "text-input"

    @property
    def settings_class(self) -> TextInputSettings:
        return TextInputSettings


class Button(NuiComponent):
    @property
    def component_name(self) -> str:
        return "button"

    @property
    def settings_class(self) -> ButtonSettings:
        return ButtonSettings


class Select(NuiComponent):
    @property
    def component_name(self) -> str:
        return "select"

    @property
    def settings_class(self) -> SelectSettings:
        return SelectSettings

    @staticmethod
    def option(text: str, data: Optional[Dict[str, Any]] = None) -> SelectOption:
        return SelectOption(text=text, **(data or {}))


class ComponentSettings(BaseSettings):
    """Base settings for all components"""

    size: Optional[int] = 1
    is_focusable: bool = True
    autofocus: bool = False


class TextInputSettings(ComponentSettings):
    """Settings for TextInput component"""

    placeholder: Optional[str] = None
    value: Optional[str] = None
    on_change: Optional[LuaCallable] = None
    max_lines: Optional[int] = None


class ButtonSettings(ComponentSettings):
    """Settings for Button component"""

    label: str
    on_press: Optional[LuaCallable] = None
    is_active: bool = False


class SelectOption(BaseSettings):
    """Settings for Select option"""

    text: str
    id: Optional[str] = None
    _type: str = Field("option", alias="_type")


class SelectSettings(ComponentSettings):
    """Settings for Select component"""

    data: List[SelectOption] = []
    selected: Optional[Union[str, List[str]]] = None
    multiselect: bool = False
    on_change: Optional[LuaCallable] = None


class RendererSettings(BaseSettings):
    """Settings for NuiRenderer"""

    relative: str = "editor"
    position: str = "50%"
    size: Dict[str, int] = Field(default_factory=lambda: {"width": 60, "height": 20})
