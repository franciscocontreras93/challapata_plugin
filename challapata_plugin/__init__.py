# -*- coding: utf-8 -*-


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    from .colegio_riberalta import ColegioRiberalta
    return ColegioRiberalta(iface)
