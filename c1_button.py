# -*- coding: utf-8 -*-

from anki.hooks import addHook
from aqt.editor import Editor

def add_c1_brackets(editor):
    u"""Call js function to wrap text in the span."""
    editor.web.eval(ur"""wrap('\{\{c1::', '\}\}');""")


def setup_buttons(editor):
    u"""Add the buttons to the editor."""
    editor._addButton(
        "basic_c1_button", lambda ed=editor: add_c1_brackets(ed),
        text=u"[c1]", tip="Wrap in c1 brackets (Ctrl+Shift+i)", key="Ctrl+Shift+i")

Editor.add_c1_brackets = add_c1_brackets
addHook("setupEditorButtons", setup_buttons)
