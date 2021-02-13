# -*- coding: utf-8 -*-
"""model
"""
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

from maya import cmds


class {{cookiecutter.tool_name}}(object):
    def print_select_object_name(self):
        selected_object = cmds.ls(selection=True)
        print(selected_object)
