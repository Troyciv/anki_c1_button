# -*- mode: python ; coding: utf-8 -*-
# original copyright 2013 Thomas TEMPE <thomas.tempe@alysse.org>
# as Strikethrough button in editor window
# and original copyright 2013 Roland Sieker <ospalh@gmail.com>
# as Spanify Text
#
# License: GNU AGPL, version 3 or later;
# http://www.gnu.org/licenses/agpl.html

u"""
Anki2 add-on to put text in c1 cloze tag.
This is an Anki2 add-on that adds a button to the card
editor. Clicking on the button wraps the selected text in
{{c1::}}.
"""

from anki.hooks import addHook
from aqt.editor import Editor

def add_c1_brackets(editor):
    u"""Call js function to wrap text in c1 tag."""
    editor.web.eval(ur"""wrap('\{\{c1::', '\}\}');""")


def setup_buttons(editor):
    u"""Add the buttons to the editor."""
    editor._addButton(
        "basic_c1_button", lambda ed=editor: add_c1_brackets(ed),
        text=u"[c1]", tip="Wrap in c1 brackets (Ctrl+Shift+i)", key="Ctrl+Shift+i")

Editor.add_c1_brackets = add_c1_brackets
addHook("setupEditorButtons", setup_buttons)
