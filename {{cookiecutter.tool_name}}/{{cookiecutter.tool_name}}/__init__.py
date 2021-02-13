# -*- coding: utf-8 -*-
from __future__ import print_function
from __future__ import unicode_literals
from __future__ import absolute_import
from __future__ import generators
from __future__ import division

from . import controller
from . import model
from . import view

from .gui import sample_gui

reload(controller)
reload(model)
reload(view)
reload(sample_gui)


def main():
    global {{cookiecutter.tool_slug}}_controller

    try:
        {{cookiecutter.tool_slug}}_controller.close_gui()
    except:
        pass

    {{cookiecutter.tool_slug}}_controller = controller.Controller()
    {{cookiecutter.tool_slug}}_controller.show_gui()
