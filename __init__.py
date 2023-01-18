# -*- coding: utf-8 -*-
import os

# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    from .colegio_riberalta import ColegioRiberalta
    

    return ColegioRiberalta(iface)
