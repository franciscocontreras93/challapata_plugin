# -*- coding: utf-8 -*-
from qgis.PyQt.QtCore import QSettings, QTranslator, QCoreApplication, QVariant
from qgis.PyQt.QtGui import QIcon, QFont, QColor
from qgis.PyQt.QtWidgets import QAction
from qgis.PyQt.QtXml import QDomDocument

from PyQt5.QtWidgets import QMessageBox

import processing
import requests

from qgis.gui import *
from qgis.core import * 
from qgis.utils import iface

#import lib.utils_api as utils_api
from functools import partial

# Import the code for the dialog
from .colegio_riberalta_dialog import ColegioRiberaltaDialog
from .colegio_riberalta_dialog import ExportTitular
from .colegio_riberalta_dialog import ExportTitularFeature
from .colegio_riberalta_dialog import ExportDatabase
from .colegio_riberalta_dialog import ExportDatabaseFeature
from .colegio_riberalta_dialog import GenerarLayout
from .colegio_riberalta_dialog import GenerarInforme
from .colegio_riberalta_dialog import SeleccionarHuso
from .colegio_riberalta_dialog import SeleccionarHusoLayout
from .colegio_riberalta_dialog import SeleccionarHusoInforme
from .colegio_riberalta_dialog import GuardarFeature
from .colegio_riberalta_dialog import ExportDatabaseFeature
from .colegio_riberalta_dialog import SeleccionarHusoFeature
from .colegio_riberalta_dialog import GuardarFeatureConstruccion
from .colegio_riberalta_dialog import ExportDatabaseFeatureConstruccion
from .colegio_riberalta_dialog import SeleccionarHusoFeatureConstruccion
from .colegio_riberalta_dialog import ExportPlantas
from .colegio_riberalta_dialog import SeleccionarHusoInforme2
from .colegio_riberalta_dialog import SeleccionarHusoInforme3
from .colegio_riberalta_dialog import GenerarInforme2
from .colegio_riberalta_dialog import GenerarInforme3
from .colegio_riberalta_dialog import ListarConstruccion
from .colegio_riberalta_dialog import ListarConstruccionPlantas

from .colegio_riberalta_dialog import ExportDatabaseEspecial
from .colegio_riberalta_dialog import ExportDatabaseMejoras
from .colegio_riberalta_dialog import ExportDatabasePlantas

from .colegio_riberalta_dialog import SelectTitular
from .colegio_riberalta_dialog import SelectTitularFeature

from .colegio_riberalta_dialog import SelectTitularBuscaRef
from .colegio_riberalta_dialog import SelectTitularBuscaNombre

from .colegio_riberalta_dialog import SelectTitularFeatureBuscaRef
from .colegio_riberalta_dialog import SelectTitularFeatureBuscaNombre

from .colegio_riberalta_dialog import SelectConstruccionPlantaBuscaRef

from .colegio_riberalta_dialog import SelectTerrenoLayoutBuscaRef
from .colegio_riberalta_dialog import SelectTerrenoLayoutBuscaNombre

from .colegio_riberalta_dialog import SelectTerrenoInformeBuscaRef
from .colegio_riberalta_dialog import SelectTerrenoInformeBuscaNombre

from .colegio_riberalta_dialog import SelectTerrenoInforme2BuscaRef
from .colegio_riberalta_dialog import SelectTerrenoInforme2BuscaNombre

from .colegio_riberalta_dialog import SelectTerrenoInforme3BuscaRef
from .colegio_riberalta_dialog import SelectTerrenoInforme3BuscaNombre


from .colegio_riberalta_dialog import GuardarFeatureCambioTitular
from .colegio_riberalta_dialog import SelecTitularCambioTitular
from .colegio_riberalta_dialog import SelectTitularCambioTitularBuscaRef
from .colegio_riberalta_dialog import SelectTitularCambioTitularBuscaNombre
from .colegio_riberalta_dialog import ConfirmarGuardarTitular


from .colegio_riberalta_dialog import GuardarFeatureUnion
from .colegio_riberalta_dialog import SelecTitularUnion
from .colegio_riberalta_dialog import SelectTitularUnionBuscaRef
from .colegio_riberalta_dialog import SelectTitularUnionBuscaNombre
from .colegio_riberalta_dialog import ConfirmarUnion



from .colegio_riberalta_dialog import InfoFormaUnion
from .colegio_riberalta_dialog import InfoInclinacionUnion
from .colegio_riberalta_dialog import InfoMaterialCalzadaUnion
from .colegio_riberalta_dialog import InfoTipoCalzadaUnion
from .colegio_riberalta_dialog import InfoUbicacionUnion
from .colegio_riberalta_dialog import InfoCodigoUnion
from .colegio_riberalta_dialog import InfoZonaUnion




from .colegio_riberalta_dialog import GuardarFeatureDivide
from .colegio_riberalta_dialog import GuardarLineaDivide
from .colegio_riberalta_dialog import SelecTitularDivide1
from .colegio_riberalta_dialog import SelecTitularDivide2
from .colegio_riberalta_dialog import SelectTitularDivide1BuscaRef
from .colegio_riberalta_dialog import SelectTitularDivide2BuscaRef
from .colegio_riberalta_dialog import SelectTitularDivide1BuscaNombre
from .colegio_riberalta_dialog import SelectTitularDivide2BuscaNombre
from .colegio_riberalta_dialog import ConfirmarDivide
from .colegio_riberalta_dialog import InfoCodigoDivide1
from .colegio_riberalta_dialog import InfoCodigoDivide2





import os.path
from datetime import date, datetime





class ColegioRiberalta:
    """QGIS Plugin Implementation."""

    def __init__(self, iface):
        
        # Save reference to the QGIS interface
        self.iface = iface
        
        
        # initialize plugin directory
        self.plugin_dir = os.path.dirname(__file__)
      

        # Declare instance attributes
        self.actions = []
        self.menu = 'Colegio Riberalta'

        # Check if plugin was started the first time in current QGIS session
        # Must be set in initGui() to survive plugin reloads
        self.first_start = None
    
    
    def unload(self):
        """Removes the plugin menu item and icon from QGIS GUI."""
        for action in self.actions:
            self.iface.removePluginMenu('&Colegio Riberalta',action)
            self.iface.removeToolBarIcon(action)

   
    def add_action(self, icon_path, text, callback, add_to_menu=True, add_to_toolbar=True, status_tip=None, whats_this=None, parent=None):
     
        icon = QIcon(icon_path)
        action = QAction(icon, text, parent)
        
        
        action.triggered.connect(callback)
        action.setEnabled(True)

        if add_to_toolbar:
            # Adds plugin icon to Plugins toolbar
            self.iface.addToolBarIcon(action)

        if add_to_menu:
            self.iface.addPluginToMenu(self.menu, action)

        self.actions.append(action)

        return action
        

    def initGui(self):
        """Create the menu entries and toolbar icons inside the QGIS GUI."""
        
        icon_path = self.plugin_dir + "/icon/user.jpg"
        self.add_action(
            icon_path,
            text= 'Carga Datos Titular',
            callback=self.abrir_dialogo_titular,
            parent=self.iface.mainWindow())

        icon_path = self.plugin_dir + "/icon/folder.png"
        self.add_action(
            icon_path,
            text= 'Carga Archivo en BBDD',
            callback=self.abrir_dialogo_cargacsv,
            parent=self.iface.mainWindow())
            
            
        icon_path = self.plugin_dir + "/icon/map.png"
        self.add_action(
            icon_path,
            text= 'Carga Parcela desde Interfaz',
            callback=self.abrir_dialogo_guardarfeature, 
            parent=self.iface.mainWindow())
            
            
        icon_path = self.plugin_dir + "/icon/house.png"
        self.add_action(
            icon_path,
            text= 'Carga Construcción desde Interfaz',
            callback=self.abrir_dialogo_guardarfeature_construccion,
            parent=self.iface.mainWindow())
            
        icon_path = self.plugin_dir + "/icon/cement.png"
        self.add_action(
            icon_path,
            text= 'Carga Materiales de Construcción',
            callback=self.abrir_dialogo_listarconstruccion_plantas,
            parent=self.iface.mainWindow())
            
            
        icon_path = self.plugin_dir + "/icon/layout.png"
        self.add_action(
            icon_path,
            text= 'Generar Plano',
            callback=self.abrir_dialogo_layout,
            parent=self.iface.mainWindow())
            
            
        icon_path = self.plugin_dir + "/icon/report.png"
        self.add_action(
            icon_path,
            text= 'Generar Informe',
            callback=self.abrir_dialogo_informe,
            parent=self.iface.mainWindow())
            
            
        icon_path = self.plugin_dir + "/icon/report2.png"
        self.add_action(
            icon_path,
            text= 'Generar Certificado Catastral',
            callback=self.abrir_dialogo_informe2,
            parent=self.iface.mainWindow())
            
            
        icon_path = self.plugin_dir + "/icon/report3.png"
        self.add_action(
            icon_path,
            text= 'Generar Certificado de Avalúo',
            callback=self.abrir_dialogo_informe3,
            parent=self.iface.mainWindow())
            



        icon_path = self.plugin_dir + "/icon/usersicon.png"
        self.add_action(
            icon_path,
            text= 'Cambiar Titular de Terreno',
            callback=self.abrir_dialogo_guardarfeature_cambiarTitular,
            parent=self.iface.mainWindow())
            


        icon_path = self.plugin_dir + "/icon/uniricon.png"
        self.add_action(
            icon_path,
            text= 'Unir dos Terrenos',
            callback=self.abrir_guardar_feature_union,
            parent=self.iface.mainWindow())
            
            
            
            
        icon_path = self.plugin_dir + "/icon/dividiricon.png"
        self.add_action(
            icon_path,
            text= 'Separar Terreno',
            callback=self.abrir_guardar_feature_divide,
            parent=self.iface.mainWindow())
            

        ######################################################################VARIABLES CARGADAS DE DIALOG##########################################
        



        # will be set False in run()
        self.first_start = True
        
        self.dlg = ColegioRiberaltaDialog()
        
        self.dlg_export_titular = ExportTitular()
        self.dlg_export_titular_feature = ExportTitularFeature()
        
        self.dlg_export = ExportDatabase()
        self.dlg_export_feature = ExportDatabaseFeature()
        
        self.dlg_layout = GenerarLayout()
        self.dlg_informe = GenerarInforme()
        self.dlg_huso = SeleccionarHuso()
        self.dlg_huso_layout = SeleccionarHusoLayout()
        self.dlg_huso_informe = SeleccionarHusoInforme()
        self.dlg_guardar_feature = GuardarFeature()
        self.dlg_export_feature = ExportDatabaseFeature()
        self.dlg_huso_feature = SeleccionarHusoFeature()
        self.dlg_guardar_feature_construccion = GuardarFeatureConstruccion()
        self.dlg_export_feature_construccion = ExportDatabaseFeatureConstruccion()
        self.dlg_huso_feature_construccion = SeleccionarHusoFeatureConstruccion()
        self.dlg_export_plantas = ExportPlantas()
        self.dlg_huso_informe2 = SeleccionarHusoInforme2()
        self.dlg_huso_informe3 = SeleccionarHusoInforme3()
        self.dlg_informe2 = GenerarInforme2()
        self.dlg_informe3 = GenerarInforme3()
        self.dlg_listar_construccion = ListarConstruccion()
        
        self.dlg_listar_construccion_plantas = ListarConstruccionPlantas()
        
        self.dlg_export_especial = ExportDatabaseEspecial()
        self.dlg_export_mejora = ExportDatabaseMejoras()
        self.dlg_export_planta = ExportDatabasePlantas()
        
        
        self.dlg_select_titular = SelectTitular()
        self.dlg_select_titular_feature = SelectTitularFeature()
        
        
        self.dlg_select_titular_busca_ref = SelectTitularBuscaRef()
        self.dlg_select_titular_busca_nombre = SelectTitularBuscaNombre()
        
        self.dlg_select_titular_feature_busca_ref = SelectTitularFeatureBuscaRef()
        self.dlg_select_titular_feature_busca_nombre = SelectTitularFeatureBuscaNombre()
        
        self.dlg_select_construccion_planta_busca_ref = SelectConstruccionPlantaBuscaRef()
        
        self.dlg_select_terreno_layout_busca_ref = SelectTerrenoLayoutBuscaRef()
        self.dlg_select_terreno_layout_busca_nombre = SelectTerrenoLayoutBuscaNombre()
        
        self.dlg_select_terreno_informe_busca_ref = SelectTerrenoInformeBuscaRef()
        self.dlg_select_terreno_informe_busca_nombre = SelectTerrenoInformeBuscaNombre()
 
        self.dlg_select_terreno_informe2_busca_ref = SelectTerrenoInforme2BuscaRef()
        self.dlg_select_terreno_informe2_busca_nombre = SelectTerrenoInforme2BuscaNombre() 
        
        self.dlg_select_terreno_informe3_busca_ref = SelectTerrenoInforme3BuscaRef()
        self.dlg_select_terreno_informe3_busca_nombre = SelectTerrenoInforme3BuscaNombre()
        
        
        self.dlg_guardar_feature_cambiar_titular = GuardarFeatureCambioTitular()
        self.dlg_select_titular_cambio_titular = SelecTitularCambioTitular()
        self.dlg_select_titular_cambio_titular_busca_ref = SelectTitularCambioTitularBuscaRef()
        self.dlg_select_titular_cambio_titular_busca_nombre = SelectTitularCambioTitularBuscaNombre()
        self.confirmar_guardar_titular = ConfirmarGuardarTitular()
        
        self.dlg_guardar_feature_union = GuardarFeatureUnion()
        self.dlg_select_titular_union = SelecTitularUnion()
        self.dlg_select_titular_union_busca_ref = SelectTitularUnionBuscaRef()
        self.dlg_select_titular_union_busca_nombre = SelectTitularUnionBuscaNombre()
        self.dlg_confirmar_union = ConfirmarUnion()   
        
        
        self.dlg_info_forma_union = InfoFormaUnion()
        self.dlg_info_inclinacion_union = InfoInclinacionUnion()
        self.dlg_info_material_calzada_union = InfoMaterialCalzadaUnion()
        self.dlg_info_tipo_calzada_union = InfoTipoCalzadaUnion()
        self.dlg_info_ubicacion_union = InfoUbicacionUnion()
        self.dlg_info_codigo_union = InfoCodigoUnion()
        self.dlg_info_zona_union = InfoZonaUnion()
        
 

        self.dlg_guardar_feature_divide = GuardarFeatureDivide()
        self.dlg_guardar_linea_divide = GuardarLineaDivide()
        self.dlg_select_titular_divide1 = SelecTitularDivide1()
        self.dlg_select_titular_divide2 = SelecTitularDivide2()
        self.dlg_select_titular_divide1_buscar_ref = SelectTitularDivide1BuscaRef()
        self.dlg_select_titular_divide2_buscar_ref = SelectTitularDivide2BuscaRef()
        self.dlg_select_titular_divide1_buscar_nombre = SelectTitularDivide1BuscaNombre()
        self.dlg_select_titular_divide2_buscar_nombre = SelectTitularDivide2BuscaNombre()
        self.dlg_confirmar_divide = ConfirmarDivide()
        
        self.dlg_info_codigo_divide1 = InfoCodigoDivide1()
        self.dlg_info_codigo_divide2 = InfoCodigoDivide2()

 
        
        #################################CAMBIO TITULOS EN DIALOGS#####################################################################
        
        
        self.dlg_export_titular.setWindowTitle("Carga Datos del Titular de la Parcela en la Base de Datos")
        
        self.dlg_export.setWindowTitle("Carga Datos de la Parcela en la Base de Datos")
        self.dlg_informe.setWindowTitle("Selecciona una Parcela y Genera un Informe")
        self.dlg_huso.setWindowTitle("Selecciona Huso Horario")
        self.dlg_guardar_feature.setWindowTitle("Selecciona un Polígono")
        
        self.dlg_huso.setWindowTitle("Selecciona un Huso Horario")
        self.dlg_huso_feature.setWindowTitle("Selecciona un Huso Horario")
        self.dlg_export_feature.setWindowTitle("Carga Datos de la Parcela Seleccionada en la Base de Datos")
        
        self.dlg_guardar_feature_construccion.setWindowTitle("Selecciona un Polígono")
        self.dlg_huso_feature_construccion.setWindowTitle("Selecciona un Huso Horario")
        self.dlg_export_feature_construccion.setWindowTitle("Carga Datos de la Construcción Seleccionada en la Base de Datos")
        
        self.dlg_huso_layout.setWindowTitle("Selecciona Huso Horario")
        self.dlg_layout.setWindowTitle("Selecciona una Parcela y Genera un Plano")
        
        self.dlg_huso_informe.setWindowTitle("Selecciona Huso Horario")
        self.dlg_huso_informe2.setWindowTitle("Selecciona Huso Horario")
        self.dlg_huso_informe3.setWindowTitle("Selecciona Huso Horario")
        
        self.dlg_informe2.setWindowTitle("Selecciona una Parcela y Genera un Informe")
        self.dlg_informe3.setWindowTitle("Selecciona una Parcela")
        
        self.dlg_listar_construccion.setWindowTitle("Selecciona una Construcción y Genera un Informe")
        
        self.dlg_export_especial.setWindowTitle("Carga Nueva Edficación Especial")
        self.dlg_export_mejora.setWindowTitle("Carga Nueva Mejora")
        self.dlg_export_planta.setWindowTitle("Carga Nueva Planta")
        
        
        self.dlg_select_titular.setWindowTitle("Selecciona Titular del Terreno")
        self.dlg_select_titular_feature.setWindowTitle("Selecciona Titular del Terreno")
        
        
        self.dlg_select_titular_busca_ref.setWindowTitle("Ingresa un Documento")
        self.dlg_select_titular_busca_nombre.setWindowTitle("Ingresa un Nombre y/o Apellidos")
        
        self.dlg_select_titular_feature_busca_ref.setWindowTitle("Ingresa un Documento")
        self.dlg_select_titular_feature_busca_nombre.setWindowTitle("Ingresa un Nombre y/o Apellidos")
        
        
        self.dlg_listar_construccion_plantas.setWindowTitle("Selecciona una Construcción")
        
        
        self.dlg_select_terreno_layout_busca_ref.setWindowTitle("Ingesa Código Catastral")
        self.dlg_select_terreno_layout_busca_nombre.setWindowTitle("Ingesa un Nombre y/o Apellidos")


        self.dlg_select_terreno_informe_busca_ref.setWindowTitle("Ingesa Código Catastral")
        self.dlg_select_terreno_informe_busca_nombre.setWindowTitle("Ingesa un Nombre y/o Apellidos")


        self.dlg_select_terreno_informe2_busca_ref.setWindowTitle("Ingesa Código Catastral")
        self.dlg_select_terreno_informe2_busca_nombre.setWindowTitle("Ingesa un Nombre y/o Apellidos")

        
        self.dlg_select_terreno_informe3_busca_ref.setWindowTitle("Ingesa Código Catastral")
        self.dlg_select_terreno_informe3_busca_nombre.setWindowTitle("Ingesa un Nombre y/o Apellidos")
        
        
        self.dlg_guardar_feature_cambiar_titular.setWindowTitle("Selecciona Un Terreno")
        self.dlg_select_titular_cambio_titular.setWindowTitle("Selecciona el Nuevo Titular")
        self.dlg_select_titular_cambio_titular_busca_ref.setWindowTitle("Ingresa un Documento")
        self.dlg_select_titular_cambio_titular_busca_nombre.setWindowTitle("Ingresa un Nombre y/o Apellidos")
        self.confirmar_guardar_titular.setWindowTitle("Cambio de Titular")
        
        
        self.dlg_guardar_feature_union.setWindowTitle("Selecciona Dos Terrenos Contiguos")
        self.dlg_select_titular_union.setWindowTitle("Selecciona el Nuevo Titular")
        self.dlg_select_titular_union_busca_ref.setWindowTitle("Ingresa un Documento")
        self.dlg_select_titular_union_busca_nombre.setWindowTitle("Ingresa un Nombre y/o Apellidos")
        self.dlg_confirmar_union.setWindowTitle("Unir Dos Terrenos") 



        self.dlg_info_forma_union.setWindowTitle("Selecciona Dos Terrenos Contiguos")
        self.dlg_info_inclinacion_union.setWindowTitle("Selecciona Dos Terrenos Contiguos")
        self.dlg_info_material_calzada_union.setWindowTitle("Selecciona Dos Terrenos Contiguos")
        self.dlg_info_tipo_calzada_union.setWindowTitle("Selecciona Dos Terrenos Contiguos")
        self.dlg_info_ubicacion_union.setWindowTitle("Selecciona Dos Terrenos Contiguos")
        self.dlg_info_codigo_union.setWindowTitle("Selecciona Dos Terrenos Contiguos")
        self.dlg_info_zona_union.setWindowTitle("Selecciona Dos Terrenos Contiguos")



        self.dlg_guardar_feature_divide.setWindowTitle("Selecciona Un Terreno")
        self.dlg_guardar_linea_divide.setWindowTitle("Selecciona Una Linea de División")
        self.dlg_select_titular_divide1.setWindowTitle("Selecciona Titular del Terreno de la Izqda")
        self.dlg_select_titular_divide2.setWindowTitle("Selecciona Titular del Terreno de la Drcha")
        self.dlg_select_titular_divide1_buscar_ref.setWindowTitle("Ingresa un Documento")
        self.dlg_select_titular_divide2_buscar_ref.setWindowTitle("Ingresa un Documento")
        self.dlg_select_titular_divide1_buscar_nombre.setWindowTitle("Ingresa un Nombre y/o Apellidos")
        self.dlg_select_titular_divide2_buscar_nombre.setWindowTitle("Ingresa un Nombre y/o Apellidos")
        self.dlg_confirmar_divide.setWindowTitle("Divide el Terreno")
        
        self.dlg_info_codigo_divide1.setWindowTitle("Ingresa el nuevo Codigo y Dirección")
        self.dlg_info_codigo_divide2.setWindowTitle("Ingresa el nuevo Codigo y Dirección")


        
        #########################################################################################################
        ################################ FUNCIONES CARGA BOTONES #################################################
        
        
        
        ##################################################### PRIMER BOTON CARGA TITULAR ############################################################ 
        


        
        self.dlg_export_titular.btn_cancelar_prop.clicked.connect(self.cerrar_dialogo_exportartitular)  
        
        
        self.dlg_export_titular.btn_guardar_prop.clicked.connect(self.guardar_titular)
        # self.dlg_export_titular.btn_guardar_prop.clicked.connect(self.abrir_dialogo_exportbbdd)
        self.dlg_export_titular.btn_guardar_prop.clicked.connect(self.cerrar_dialogo_exportartitular)
   
      
               
                
                
 
        ##################################################### BOTON CARGA CSV Y GUARDA ############################################################  
        
        self.dlg_select_titular.btn_select_titular.clicked.connect(self.abrir_dialogo_exportbbdd)
        self.dlg_select_titular.btn_select_titular.clicked.connect(self.cerrar_dialogo_listar_titular)
        
        self.dlg_select_titular.btn_titular_selec_ref.clicked.connect(self.abrir_dialogo_listar_titular_buscar_ref)
  
  
        self.dlg_select_titular_busca_ref.btn_busca.clicked.connect(self.titular_busca_ref)
        self.dlg_select_titular_busca_ref.btn_busca.clicked.connect(self.cerrar_dialogo_listar_titular_buscar_ref)
        
        
        
        self.dlg_select_titular_busca_ref.btn_aceptar.clicked.connect(self.cerrar_dialogo_listar_titular_buscar_ref)
        self.dlg_select_titular_busca_ref.btn_cancelar.clicked.connect(self.cerrar_dialogo_listar_titular_buscar_ref)
        
        
        self.dlg_select_titular.btn_titular_selec_nombre.clicked.connect(self.abrir_dialogo_listar_titular_buscar_nombre)
        
        
        self.dlg_select_titular_busca_nombre.btn_busca.clicked.connect(self.titular_busca_nombre)
        self.dlg_select_titular_busca_nombre.btn_busca.clicked.connect(self.cerrar_dialogo_listar_titular_buscar_nombre)
        
        
        self.dlg_select_titular_busca_nombre.btn_aceptar.clicked.connect(self.cerrar_dialogo_listar_titular_buscar_nombre)
        self.dlg_select_titular_busca_nombre.btn_cancelar.clicked.connect(self.cerrar_dialogo_listar_titular_buscar_nombre)
        
        
        self.dlg_select_titular.btn_titular_limpiar.clicked.connect(self.cargar_titular)
                 
        
        
        self.dlg.btn_guardarbbdd.clicked.connect(self.abrir_dialogo_listar_titular)
        self.dlg.btn_guardarbbdd.clicked.connect(self.cargar_titular)
        self.dlg.btn_guardarbbdd.clicked.connect(self.cerrar_dialogo_cargacsv)
        
               

        
        
 
        
        self.dlg_export.btn_exportdb.clicked.connect(self.cargar_csv)
        self.dlg_export.btn_exportdb.clicked.connect(self.cerrar_dialogo_exportbbdd)
        
        
        
        ##################################################### SEGUNDO BOTON SELCCIONA FEATURE Y GUARDA ############################################################
        
        self.dlg_guardar_feature.btn_guardar.clicked.connect(self.abrir_dialogo_listar_titular_feature)
        self.dlg_guardar_feature.btn_guardar.clicked.connect(self.cargar_titular_feature)
        self.dlg_guardar_feature.btn_guardar.clicked.connect(self.cerrar_dialogo_guardarfeature)
        
        self.dlg_guardar_feature.btn_cancelar.clicked.connect(self.cerrar_dialogo_guardarfeature)
        self.dlg_guardar_feature.btn_cancelar.clicked.connect(self.desactiva_seleccion)
        self.dlg_guardar_feature.btn_cancelar.clicked.connect(self.cerrar_dialogo_listar_titular_feature)
        
        
        
        
        self.dlg_select_titular_feature.btn_select_titular.clicked.connect(self.abrir_dialogo_exportbbdd_feature)
        self.dlg_select_titular_feature.btn_select_titular.clicked.connect(self.cerrar_dialogo_listar_titular_feature)
        
        
        self.dlg_select_titular_feature.btn_titular_selec_ref.clicked.connect(self.abrir_dialogo_listar_titular_feature_buscar_ref)
        self.dlg_select_titular_feature.btn_titular_selec_nombre.clicked.connect(self.abrir_dialogo_listar_titular_feature_buscar_nombre)
        self.dlg_select_titular_feature.btn_titular_limpiar.clicked.connect(self.cargar_titular_feature)
        
        
        
        self.dlg_select_titular_feature_busca_ref.btn_busca.clicked.connect(self.titular_feature_busca_ref)
        self.dlg_select_titular_feature_busca_ref.btn_busca.clicked.connect(self.cerrar_dialogo_listar_titular_feature_buscar_ref)
       
        
        self.dlg_select_titular_feature_busca_ref.btn_aceptar.clicked.connect(self.cerrar_dialogo_listar_titular_feature_buscar_ref)
        self.dlg_select_titular_feature_busca_ref.btn_cancelar.clicked.connect(self.cerrar_dialogo_listar_titular_feature_buscar_ref)
        
        
        self.dlg_select_titular_feature_busca_nombre.btn_busca.clicked.connect(self.titular_feature_busca_nombre)
        self.dlg_select_titular_feature_busca_nombre.btn_busca.clicked.connect(self.cerrar_dialogo_listar_titular_feature_buscar_nombre)
        
        
        self.dlg_select_titular_feature_busca_nombre.btn_aceptar.clicked.connect(self.cerrar_dialogo_listar_titular_feature_buscar_nombre)
        self.dlg_select_titular_feature_busca_nombre.btn_cancelar.clicked.connect(self.cerrar_dialogo_listar_titular_feature_buscar_nombre)
               
        
        self.dlg_export_feature.btn_exportdb.clicked.connect(self.selecciona_feature)
        self.dlg_export_feature.btn_exportdb.clicked.connect(self.cerrar_dialogo_exportbbdd_feature)
        
        
        
   
        
        ##################################################### CARGA Y GUARDA DATOS DEL TITULAR DESDE SELECCION ############################################################  
        
        # self.dlg_export_titular_feature.btn_guardar_prop.clicked.connect(self.guardar_titular_feature)
        # self.dlg_export_titular_feature.btn_guardar_prop.clicked.connect(self.abrir_dialogo_exportbbdd_feature)
        # self.dlg_export_titular_feature.btn_guardar_prop.clicked.connect(self.cerrar_dialogo_exportartitular_feature)
   
      
        # self.dlg_export_titular_feature.btn_cancelar_prop.clicked.connect(self.cerrar_dialogo_exportartitular_feature)
 


        ##################################################### TERCER BOTON SELCCIONA CONSTRUCCION Y GUARDA ####################################################
        
        
        self.dlg_guardar_feature_construccion.btn_guardar.clicked.connect(self.abrir_dialogo_exportbbdd_feature_construccion)
        self.dlg_guardar_feature_construccion.btn_guardar.clicked.connect(self.cargar_tablabbdd_construccion)
        self.dlg_guardar_feature_construccion.btn_guardar.clicked.connect(self.cerrar_dialogo_guardarfeature_construccion)

                
        self.dlg_guardar_feature_construccion.btn_cancelar.clicked.connect(self.cerrar_dialogo_guardarfeature_construccion)
        self.dlg_guardar_feature_construccion.btn_cancelar.clicked.connect(self.desactiva_seleccion)
        
        
        self.dlg_export_feature_construccion.btn_exportdb.clicked.connect(self.cerrar_dialogo_exportbbdd_feature_construccion)
        self.dlg_export_feature_construccion.btn_exportdb.clicked.connect(self.selecciona_construccion)
        
        self.dlg_export_feature_construccion.btn_exportdb_esp.clicked.connect(self.abrir_dialogo_exportbbdd_especiales)
        self.dlg_export_feature_construccion.btn_exportdb_esp.clicked.connect(self.cargar_tablabbdd_especial)
        
        
        
        self.dlg_export_feature_construccion.btn_exportdb_mejora.clicked.connect(self.abrir_dialogo_exportbbdd_mejoras)
        self.dlg_export_feature_construccion.btn_exportdb_mejora.clicked.connect(self.cargar_tablabbdd_mejora)
 

        self.dlg_export_especial.btn_cancelar.clicked.connect(self.cerrar_dialogo_exportbbdd_especiales)
        
        self.dlg_export_especial.btn_guardar.clicked.connect(self.cerrar_dialogo_exportbbdd_especiales)
        self.dlg_export_especial.btn_guardar.clicked.connect(self.guardar_feature_bbdd_especial)  


        self.dlg_export_mejora.btn_cancelar.clicked.connect(self.cerrar_dialogo_exportbbdd_mejoras)
        
        self.dlg_export_mejora.btn_guardar.clicked.connect(self.cerrar_dialogo_exportbbdd_mejoras)
        self.dlg_export_mejora.btn_guardar.clicked.connect(self.guardar_feature_bbdd_mejora)         
        
        
        ###################################################    BOTON PLANTAS Y MATERIALES       ########################################################
        
        
        self.dlg_listar_construccion_plantas.btn_informe.clicked.connect(self.abrir_dialogo_exportbbdd_planta)
        self.dlg_listar_construccion_plantas.btn_informe.clicked.connect(self.cerrar_dialogo_listarconstruccion_plantas)
        
        
        self.dlg_listar_construccion_plantas.btn_const_selec_ref.clicked.connect(self.abrir_dialogo_select_construccion_planta_busca_ref)
        self.dlg_listar_construccion_plantas.btn_const_limpiar.clicked.connect(self.cargar_tablaconstruccionbd_plantas)
        
        
        self.dlg_select_construccion_planta_busca_ref.btn_busca.clicked.connect(self.planta_busca_ref)
        self.dlg_select_construccion_planta_busca_ref.btn_busca.clicked.connect(self.cerrar_dialogo_select_construccion_planta_busca_ref)
        
        self.dlg_select_construccion_planta_busca_ref.btn_cancelar.clicked.connect(self.cerrar_dialogo_select_construccion_planta_busca_ref)
        self.dlg_select_construccion_planta_busca_ref.btn_aceptar.clicked.connect(self.cerrar_dialogo_select_construccion_planta_busca_ref)
        
        
        self.dlg_export_planta.btn_guardar.clicked.connect(self.guardar_planta)
        self.dlg_export_planta.btn_guardar.clicked.connect(self.cerrar_dialogo_exportbbdd_planta)
        
        
      
        
        self.dlg_export_planta.btn_cancelar.clicked.connect(self.cerrar_dialogo_exportbbdd_planta)
        
        
        
        
        ##################################################### CUARTO BOTON DIBUJA LAYOUT ####################################################


               
        self.dlg_layout.btn_layout.clicked.connect(self.mostrar_layout)
        self.dlg_layout.btn_layout.clicked.connect(self.cerrar_dialogo_layout)
        
        self.dlg_layout.btn_selec_ref.clicked.connect(self.abrir_select_terreno_layout_busca_ref)
        self.dlg_layout.btn_selec_nombre.clicked.connect(self.abrir_select_terreno_layout_busca_nombre)
        self.dlg_layout.btn_limpiar.clicked.connect(self.cargar_tablabbdd)
        
        
        self.dlg_select_terreno_layout_busca_ref.btn_busca.clicked.connect(self.listar_layer_busca_ref)
        self.dlg_select_terreno_layout_busca_ref.btn_busca.clicked.connect(self.cerrar_select_terreno_layout_busca_ref)
        
        self.dlg_select_terreno_layout_busca_ref.btn_aceptar.clicked.connect(self.cerrar_select_terreno_layout_busca_ref)
        self.dlg_select_terreno_layout_busca_ref.btn_cancelar.clicked.connect(self.cerrar_select_terreno_layout_busca_ref)
        
        
        self.dlg_select_terreno_layout_busca_nombre.btn_busca.clicked.connect(self.listar_layer_busca_nombre)
        self.dlg_select_terreno_layout_busca_nombre.btn_busca.clicked.connect(self.cerrar_select_terreno_layout_busca_nombre)
        
        self.dlg_select_terreno_layout_busca_nombre.btn_aceptar.clicked.connect(self.cerrar_select_terreno_layout_busca_nombre)
        self.dlg_select_terreno_layout_busca_nombre.btn_cancelar.clicked.connect(self.cerrar_select_terreno_layout_busca_nombre)
    
        

        ##################################################### QUINTO BOTON PRIMER CERTIFICADO ####################################################

        
        self.dlg_informe.btn_informe.clicked.connect(self.mostrar_informe)
        self.dlg_informe.btn_informe.clicked.connect(self.cerrar_dialogo_informe)
        
        self.dlg_informe.btn_selec_ref.clicked.connect(self.abrir_dialogo_select_terreno_informe_busca_ref)
        self.dlg_informe.btn_selec_nombre.clicked.connect(self.abrir_dialogo_select_terreno_informe_busca_nombre)
        self.dlg_informe.btn_limpiar.clicked.connect(self.cargar_tablabbdd2)
        

        self.dlg_select_terreno_informe_busca_ref.btn_busca.clicked.connect(self.listar_layer_informe_busca_ref)
        self.dlg_select_terreno_informe_busca_ref.btn_busca.clicked.connect(self.cerrar_dialogo_select_terreno_informe_busca_ref)
 

        self.dlg_select_terreno_informe_busca_ref.btn_aceptar.clicked.connect(self.cerrar_dialogo_select_terreno_informe_busca_ref)
        self.dlg_select_terreno_informe_busca_ref.btn_cancelar.clicked.connect(self.cerrar_dialogo_select_terreno_informe_busca_ref)


        self.dlg_select_terreno_informe_busca_nombre.btn_busca.clicked.connect(self.listar_layer_informe_busca_nombre)
        self.dlg_select_terreno_informe_busca_nombre.btn_busca.clicked.connect(self.cerrar_dialogo_select_terreno_informe_busca_nombre)

        self.dlg_select_terreno_informe_busca_nombre.btn_aceptar.clicked.connect(self.cerrar_dialogo_select_terreno_informe_busca_nombre)
        self.dlg_select_terreno_informe_busca_nombre.btn_cancelar.clicked.connect(self.cerrar_dialogo_select_terreno_informe_busca_nombre)       
       
        ##################################################### SEXTO BOTON SEGUNDO CERTIFICADO ####################################################
        #BOTON DE CERTIFICADO CATASTRAL
        
        
        self.dlg_informe2.btn_informe.clicked.connect(self.mostrar_informe2)
        self.dlg_informe2.btn_informe.clicked.connect(self.cerrar_dialogo_informe2)
        
        self.dlg_informe2.btn_selec_ref.clicked.connect(self.abrir_dialogo_select_terreno_informe2_busca_ref)
        self.dlg_informe2.btn_selec_nombre.clicked.connect(self.abrir_dialogo_select_terreno_informe2_busca_nombre)
        self.dlg_informe2.btn_limpiar.clicked.connect(self.cargar_tablabbdd3)
        

        self.dlg_select_terreno_informe2_busca_ref.btn_busca.clicked.connect(self.listar_layer_informe3_busca_ref)
        self.dlg_select_terreno_informe2_busca_ref.btn_busca.clicked.connect(self.cerrar_dialogo_select_terreno_informe2_busca_ref)
 

        self.dlg_select_terreno_informe2_busca_ref.btn_aceptar.clicked.connect(self.cerrar_dialogo_select_terreno_informe2_busca_ref)
        self.dlg_select_terreno_informe2_busca_ref.btn_cancelar.clicked.connect(self.cerrar_dialogo_select_terreno_informe2_busca_ref)


        self.dlg_select_terreno_informe2_busca_nombre.btn_busca.clicked.connect(self.listar_layer_informe3_busca_nombre)
        self.dlg_select_terreno_informe2_busca_nombre.btn_busca.clicked.connect(self.cerrar_dialogo_select_terreno_informe2_busca_nombre)

        self.dlg_select_terreno_informe2_busca_nombre.btn_aceptar.clicked.connect(self.cerrar_dialogo_select_terreno_informe2_busca_nombre)
        self.dlg_select_terreno_informe2_busca_nombre.btn_cancelar.clicked.connect(self.cerrar_dialogo_select_terreno_informe2_busca_nombre)  
       
        ##################################################### SEPTIMO BOTON TERCER CERTIFICADO ####################################################
        #BOTON DE CERTIFICADO AVALUO
        
        
        self.dlg_informe3.btn_informe.clicked.connect(self.abrir_dialogo_listarconstruccion)
        self.dlg_informe3.btn_informe.clicked.connect(self.cargar_construccion)
        self.dlg_informe3.btn_informe.clicked.connect(self.cerrar_dialogo_informe3)
 


        self.dlg_informe3.btn_selec_ref.clicked.connect(self.abrir_dialogo_select_terreno_informe3_busca_ref)
        self.dlg_informe3.btn_selec_nombre.clicked.connect(self.abrir_dialogo_select_terreno_informe3_busca_nombre)
        self.dlg_informe3.btn_limpiar.clicked.connect(self.cargar_tablabbdd4)
        

        self.dlg_select_terreno_informe3_busca_ref.btn_busca.clicked.connect(self.listar_layer_informe4_busca_ref)
        self.dlg_select_terreno_informe3_busca_ref.btn_busca.clicked.connect(self.cerrar_dialogo_select_terreno_informe3_busca_ref)
 

        self.dlg_select_terreno_informe3_busca_ref.btn_aceptar.clicked.connect(self.cerrar_dialogo_select_terreno_informe3_busca_ref)
        self.dlg_select_terreno_informe3_busca_ref.btn_cancelar.clicked.connect(self.cerrar_dialogo_select_terreno_informe3_busca_ref)


        self.dlg_select_terreno_informe3_busca_nombre.btn_busca.clicked.connect(self.listar_layer_informe4_busca_nombre)
        self.dlg_select_terreno_informe3_busca_nombre.btn_busca.clicked.connect(self.cerrar_dialogo_select_terreno_informe3_busca_nombre)

        self.dlg_select_terreno_informe3_busca_nombre.btn_aceptar.clicked.connect(self.cerrar_dialogo_select_terreno_informe3_busca_nombre)
        self.dlg_select_terreno_informe3_busca_nombre.btn_cancelar.clicked.connect(self.cerrar_dialogo_select_terreno_informe3_busca_nombre) 


 
        self.dlg_listar_construccion.btn_informe.clicked.connect(self.mostrar_informe3)
        self.dlg_listar_construccion.btn_informe.clicked.connect(self.cerrar_dialogo_listarconstruccion)
        
        
        ##################################################### CAMBIO DE TITULAR ####################################################
        
        self.dlg_guardar_feature_cambiar_titular.btn_guardar.clicked.connect(self.cerrar_dialogo_guardarfeature_cambiarTitular)
        self.dlg_guardar_feature_cambiar_titular.btn_guardar.clicked.connect(self.abrir_select_titular_cambio_titular)
        self.dlg_guardar_feature_cambiar_titular.btn_guardar.clicked.connect(self.cargar_titular_cambiar_titular)
        
        self.dlg_guardar_feature_cambiar_titular.btn_cancelar.clicked.connect(self.cerrar_dialogo_guardarfeature_cambiarTitular)
        
        
        self.dlg_select_titular_cambio_titular.btn_titular_selec_nombre.clicked.connect(self.abrir_select_titular_cambio_titular_busca_nombre)
        self.dlg_select_titular_cambio_titular.btn_titular_selec_ref.clicked.connect(self.abrir_select_titular_cambio_titular_busca_ref)
        self.dlg_select_titular_cambio_titular.btn_titular_limpiar.clicked.connect(self.cargar_titular_cambiar_titular)
        self.dlg_select_titular_cambio_titular.btn_select_titular.clicked.connect(self.abrir_confirmar_guardar_titular)
        self.dlg_select_titular_cambio_titular.btn_select_titular.clicked.connect(self.cerrar_select_titular_cambio_titular)
        
                      
        self.dlg_select_titular_cambio_titular_busca_nombre.btn_cancelar.clicked.connect(self.cerrar_select_titular_cambio_titular_busca_nombre)
        self.dlg_select_titular_cambio_titular_busca_nombre.btn_aceptar.clicked.connect(self.cerrar_select_titular_cambio_titular_busca_nombre)
        self.dlg_select_titular_cambio_titular_busca_nombre.btn_busca.clicked.connect(self.titular_titular_cambiar_busca_nombre)
        
        
        self.dlg_select_titular_cambio_titular_busca_ref.btn_cancelar.clicked.connect(self.cerrar_select_titular_cambio_titular_busca_ref)
        self.dlg_select_titular_cambio_titular_busca_ref.btn_aceptar.clicked.connect(self.cerrar_select_titular_cambio_titular_busca_ref)
        self.dlg_select_titular_cambio_titular_busca_ref.btn_busca.clicked.connect(self.titular_titular_cambiar_busca_ref)
        
                
        self.confirmar_guardar_titular.btn_cancelar.clicked.connect(self.cerrar_confirmar_guardar_titular)
        self.confirmar_guardar_titular.btn_cancelar.clicked.connect(self.abrir_select_titular_cambio_titular)
    
        self.confirmar_guardar_titular.btn_guardar.clicked.connect(self.cerrar_confirmar_guardar_titular)
        self.confirmar_guardar_titular.btn_guardar.clicked.connect(self.cambia_titular)
        
        
        
    #####################################################################UNIÓN DE DOS PARCELAS####################################################################

        self.dlg_guardar_feature_union.btn_guardar.clicked.connect(self.cerrar_guardar_feature_union)
        self.dlg_guardar_feature_union.btn_guardar.clicked.connect(self.abrir_select_titular_union)
        self.dlg_guardar_feature_union.btn_guardar.clicked.connect(self.cargar_titular_union)
        
        self.dlg_guardar_feature_union.btn_cancelar.clicked.connect(self.cerrar_guardar_feature_union)
        
        
        self.dlg_select_titular_union.btn_titular_selec_nombre.clicked.connect(self.abrir_select_titular_union_busca_nombre)
        self.dlg_select_titular_union.btn_titular_selec_ref.clicked.connect(self.abrir_select_titular_union_busca_ref)
        self.dlg_select_titular_union.btn_titular_limpiar.clicked.connect(self.cargar_titular_union)
        self.dlg_select_titular_union.btn_select_titular.clicked.connect(self.abrir_dlg_info_codigo_union_union)
        self.dlg_select_titular_union.btn_select_titular.clicked.connect(self.cerrar_select_titular_union)
        
        
        self.dlg_select_titular_union_busca_nombre.btn_cancelar.clicked.connect(self.cerrar_select_titular_union_busca_nombre)
        self.dlg_select_titular_union_busca_nombre.btn_aceptar.clicked.connect(self.cerrar_select_titular_union_busca_nombre)
        self.dlg_select_titular_union_busca_nombre.btn_busca.clicked.connect(self.titular_union_busca_nombre)
        
        
        self.dlg_select_titular_union_busca_ref.btn_cancelar.clicked.connect(self.cerrar_select_titular_union_busca_ref)
        self.dlg_select_titular_union_busca_ref.btn_aceptar.clicked.connect(self.cerrar_select_titular_union_busca_ref)
        self.dlg_select_titular_union_busca_ref.btn_busca.clicked.connect(self.titular_union_busca_ref)
        
        
        self.dlg_info_codigo_union.btn_guardar.clicked.connect(self.abrir_confirmar_union)
        self.dlg_info_codigo_union.btn_guardar.clicked.connect(self.cerrar_dlg_info_codigo_union_union)
        self.dlg_info_codigo_union.btn_cancelar.clicked.connect(self.cerrar_dlg_info_codigo_union_union)
        
        
        self.dlg_confirmar_union.btn_cancelar.clicked.connect(self.cerrar_confirmar_union)
        self.dlg_confirmar_union.btn_cancelar.clicked.connect(self.abrir_select_titular_union)
        self.dlg_confirmar_union.btn_guardar.clicked.connect(self.cerrar_confirmar_union)
        self.dlg_confirmar_union.btn_guardar.clicked.connect(self.union_titular)

#####################################################################DIVIDIR  PARCELA####################################################################



   
        self.dlg_guardar_feature_divide.btn_guardar.clicked.connect(self.cerrar_guardar_feature_divide)
        self.dlg_guardar_feature_divide.btn_guardar.clicked.connect(self.abrir_guardar_linea_divide)
        self.dlg_guardar_feature_divide.btn_guardar.clicked.connect(self.guardar_terreno)
        self.dlg_guardar_feature_divide.btn_cancelar.clicked.connect(self.cerrar_guardar_feature_union)
        
        self.dlg_guardar_linea_divide.btn_guardar.clicked.connect(self.cerrar_guardar_linea_divide)
        self.dlg_guardar_linea_divide.btn_guardar.clicked.connect(self.cerrar_guardar_linea_divide)
        self.dlg_guardar_linea_divide.btn_guardar.clicked.connect(self.abrir_select_titular_divide1)
        self.dlg_guardar_linea_divide.btn_guardar.clicked.connect(self.cargar_titular_divide1)
        self.dlg_guardar_linea_divide.btn_guardar.clicked.connect(self.guardar_linea)
        self.dlg_guardar_linea_divide.btn_cancelar.clicked.connect(self.cerrar_guardar_linea_divide)
        
        
        self.dlg_select_titular_divide1.btn_titular_selec_nombre.clicked.connect(self.abrir_select_titular_divide1_buscar_nombre)
        self.dlg_select_titular_divide1.btn_titular_selec_ref.clicked.connect(self.abrir_select_titular_divide1_buscar_ref)
        self.dlg_select_titular_divide1.btn_titular_limpiar.clicked.connect(self.cargar_titular_divide1)
        self.dlg_select_titular_divide1.btn_select_titular.clicked.connect(self.abrir_dlg_info_codigo_divide1)
        self.dlg_select_titular_divide1.btn_select_titular.clicked.connect(self.cerrar_select_titular_divide1)
        
        
        self.dlg_select_titular_divide1_buscar_nombre.btn_cancelar.clicked.connect(self.cerrar_select_titular_divide1_buscar_nombre)
        self.dlg_select_titular_divide1_buscar_nombre.btn_aceptar.clicked.connect(self.cerrar_select_titular_divide1_buscar_nombre)
        self.dlg_select_titular_divide1_buscar_nombre.btn_busca.clicked.connect(self.titular_divide1_busca_nombre)
        
        
        self.dlg_select_titular_divide1_buscar_ref.btn_cancelar.clicked.connect(self.cerrar_select_titular_divide1_buscar_ref)
        self.dlg_select_titular_divide1_buscar_ref.btn_aceptar.clicked.connect(self.cerrar_select_titular_divide1_buscar_ref)
        self.dlg_select_titular_union_busca_ref.btn_busca.clicked.connect(self.titular_divide1_busca_ref)
        
        

        self.dlg_info_codigo_divide1.btn_guardar.clicked.connect(self.abrir_select_titular_divide2)
        self.dlg_info_codigo_divide1.btn_guardar.clicked.connect(self.cargar_titular_divide2)
        self.dlg_info_codigo_divide1.btn_guardar.clicked.connect(self.cerrar_dlg_info_codigo_divide1)
        self.dlg_info_codigo_divide1.btn_cancelar.clicked.connect(self.cerrar_dlg_info_codigo_divide1)



        self.dlg_select_titular_divide2.btn_titular_selec_nombre.clicked.connect(self.abrir_select_titular_divide2_buscar_nombre)
        self.dlg_select_titular_divide2.btn_titular_selec_ref.clicked.connect(self.abrir_select_titular_divide2_buscar_ref)
        self.dlg_select_titular_divide2.btn_titular_limpiar.clicked.connect(self.cargar_titular_divide2)
        self.dlg_select_titular_divide2.btn_select_titular.clicked.connect(self.abrir_dlg_info_codigo_divide2)
        self.dlg_select_titular_divide2.btn_select_titular.clicked.connect(self.cerrar_select_titular_divide2)
        
        
        self.dlg_select_titular_divide2_buscar_nombre.btn_cancelar.clicked.connect(self.cerrar_select_titular_divide2_buscar_nombre)
        self.dlg_select_titular_divide2_buscar_nombre.btn_aceptar.clicked.connect(self.cerrar_select_titular_divide2_buscar_nombre)
        self.dlg_select_titular_divide2_buscar_nombre.btn_busca.clicked.connect(self.titular_divide2_busca_nombre)
        
        
        self.dlg_select_titular_divide2_buscar_ref.btn_cancelar.clicked.connect(self.cerrar_select_titular_divide1_buscar_ref)
        self.dlg_select_titular_divide2_buscar_ref.btn_aceptar.clicked.connect(self.cerrar_select_titular_divide1_buscar_ref)
        self.dlg_select_titular_divide2_buscar_ref.btn_busca.clicked.connect(self.titular_divide2_busca_ref)


        self.dlg_info_codigo_divide2.btn_guardar.clicked.connect(self.abrir_confirmar_divide)
        self.dlg_info_codigo_divide2.btn_guardar.clicked.connect(self.cerrar_dlg_info_codigo_divide2)
        self.dlg_info_codigo_divide2.btn_cancelar.clicked.connect(self.cerrar_dlg_info_codigo_divide2)


        
                   
        self.dlg_confirmar_divide.btn_guardar.clicked.connect(self.cerrar_confirmar_divide)
        self.dlg_confirmar_divide.btn_guardar.clicked.connect(self.divide_titular)




        # self.dlg_info_codigo_divide1
        # self.dlg_info_codigo_divide2
        
        
            # def abrir_dlg_info_codigo_divide2(self):
        # self.dlg_info_codigo_divide2.show()
 
    # def cerrar_dlg_info_codigo_divide2(self):
        # self.dlg_info_codigo_divide2.close() 



#################################################################################################################################################################
##############################################################FUNCIONES DE  ABRIR Y CERRAR DIALOGOS################################################################   
    
    def abrir_dialogo_titular(self):
        self.dlg_export_titular.show()
        
    
    def abrir_dialogo_listar_titular(self):
        self.dlg_select_titular.show()
 
    def cerrar_dialogo_listar_titular(self):
        self.dlg_select_titular.close()
        



    def abrir_dialogo_listar_titular_buscar_ref(self):
        self.dlg_select_titular_busca_ref.show()
 
    def cerrar_dialogo_listar_titular_buscar_ref(self):
        self.dlg_select_titular_busca_ref.close()

    def abrir_dialogo_listar_titular_buscar_nombre(self):
        self.dlg_select_titular_busca_nombre.show()

    def cerrar_dialogo_listar_titular_buscar_nombre(self):
        self.dlg_select_titular_busca_nombre.close()




    def abrir_dialogo_listar_titular_feature(self):
        self.dlg_select_titular_feature.show()
 
    def cerrar_dialogo_listar_titular_feature(self):
        self.dlg_select_titular_feature.close()        
        
        
        
    def abrir_dialogo_cargacsv(self):
        self.dlg.show()
        
    def cerrar_dialogo_cargacsv(self):
        self.dlg.close()
        
        
        
                
    def abrir_dialogo_exportbbdd(self):
        self.dlg_export.show()
        
    def cerrar_dialogo_exportbbdd(self):
        self.dlg_export.close()
        
    
    def abrir_dialogo_exportartitular(self):
        self.dlg_export_titular.show()
        
    def cerrar_dialogo_exportartitular(self):
        self.dlg_export_titular.close()
        

    def abrir_dialogo_exportartitular_feature(self):
        self.dlg_export_titular_feature.show()
        
    def cerrar_dialogo_exportartitular_feature(self):
        self.dlg_export_titular_feature.close()
        
        
    def abrir_dialogo_listar_titular_feature_buscar_ref(self):
        self.dlg_select_titular_feature_busca_ref.show()
 
    def cerrar_dialogo_listar_titular_feature_buscar_ref(self):
        self.dlg_select_titular_feature_busca_ref.close()

    def abrir_dialogo_listar_titular_feature_buscar_nombre(self):
        self.dlg_select_titular_feature_busca_nombre.show()

    def cerrar_dialogo_listar_titular_feature_buscar_nombre(self):
        self.dlg_select_titular_feature_busca_nombre.close()
     
     
     

        
        
    #FUNCIONES DE DIALOGOS DE CONSTRUCCION
    
    def abrir_dialogo_guardarfeature_construccion(self):
        self.dlg_guardar_feature_construccion.show()
        iface.actionSelect().trigger()

    def cerrar_dialogo_guardarfeature_construccion(self):
        self.dlg_guardar_feature_construccion.close()
             
    
    def abrir_dialogo_exportbbdd_feature_construccion(self):
        self.dlg_export_feature_construccion.show()
        
    def cerrar_dialogo_exportbbdd_feature_construccion(self):
        self.dlg_export_feature_construccion.close()
        
    
    def abrir_dialogo_export_plantas(self):
        self.dlg_export_plantas.show()
              
        
    def cerrar_dialogo_export_plantas(self):
        self.dlg_export_plantas.close() 
     
     
    def abrir_dialogo_layout(self):
        self.dlg_layout.show()
        
        self.cargar_tablabbdd()
               
        
    def cerrar_dialogo_layout(self):
        self.dlg_layout.close()
        
  



  
    def abrir_dialogo_informe(self):
        self.dlg_informe.show()
        self.cargar_tablabbdd2()
        
    def cerrar_dialogo_informe(self):
        self.dlg_informe.close()
               


    
    def abrir_dialogo_select_terreno_informe_busca_ref(self):
        self.dlg_select_terreno_informe_busca_ref.show()
    
    def cerrar_dialogo_select_terreno_informe_busca_ref(self):
        self.dlg_select_terreno_informe_busca_ref.close()


    def abrir_dialogo_select_terreno_informe_busca_nombre(self):
        self.dlg_select_terreno_informe_busca_nombre.show()
    
    def cerrar_dialogo_select_terreno_informe_busca_nombre(self):
        self.dlg_select_terreno_informe_busca_nombre.close()


     
    def abrir_dialogo_guardarfeature(self):
        self.dlg_guardar_feature.show()
        
        iface.actionSelect().trigger()


    def cerrar_dialogo_guardarfeature(self):
        self.dlg_guardar_feature.close()
        
       
        
    
    def abrir_dialogo_exportbbdd_feature(self):
        self.dlg_export_feature.show()
        
    def cerrar_dialogo_exportbbdd_feature(self):
        self.dlg_export_feature.close()    
        
         
       
    def activa_seleccion(self):
        iface.actionSelect().trigger()
      
    def desactiva_seleccion(self):
        iface.mainWindow().findChild(QAction, 'mActionDeselectAll').trigger()
        
    
    
    def abrir_dialogo_exportbbdd_especiales(self):
        self.dlg_export_especial.show()
        
    def cerrar_dialogo_exportbbdd_especiales(self):
        self.dlg_export_especial.close() 

    
    def abrir_dialogo_exportbbdd_mejoras(self):
        self.dlg_export_mejora.show()
        
    def cerrar_dialogo_exportbbdd_mejoras(self):
        self.dlg_export_mejora.close()    


    def abrir_dialogo_exportbbdd_plantas(self):
        self.dlg_export_planta.show()
        
    def cerrar_dialogo_exportbbdd_plantas(self):
        self.dlg_export_planta.close() 



#BOTON MATERIALES Y PLANTAS

    def abrir_dialogo_exportbbdd_planta(self):
        self.cargar_plantas()
        self.dlg_export_planta.show()
        
    def cerrar_dialogo_exportbbdd_planta(self):
        self.dlg_export_planta.close() 
       

    def abrir_dialogo_listarconstruccion_plantas(self):
        self.dlg_listar_construccion_plantas.show()
        self.cargar_tablaconstruccionbd_plantas()
        
    def cerrar_dialogo_listarconstruccion_plantas(self):
        self.dlg_listar_construccion_plantas.close() 
        
        
    
    def abrir_dialogo_select_construccion_planta_busca_ref(self):    
        self.dlg_select_construccion_planta_busca_ref.show()
 
    def cerrar_dialogo_select_construccion_planta_busca_ref(self):    
        self.dlg_select_construccion_planta_busca_ref.close() 
        
    

#BOTON CERTIFICADO CATASTRAL


    def abrir_dialogo_informe2(self):
        self.dlg_informe2.show()
        self.cargar_tablabbdd3()
        
    def cerrar_dialogo_informe2(self):
        self.dlg_informe2.close()
        
    
    def abrir_select_terreno_layout_busca_ref(self):
        self.dlg_select_terreno_layout_busca_ref.show()
        
    def cerrar_select_terreno_layout_busca_ref(self):
        self.dlg_select_terreno_layout_busca_ref.close()
        
        
    def abrir_select_terreno_layout_busca_nombre(self):
        self.dlg_select_terreno_layout_busca_nombre.show()
        
    def cerrar_select_terreno_layout_busca_nombre(self):
        self.dlg_select_terreno_layout_busca_nombre.close()
    


    
        
    def abrir_dialogo_select_terreno_informe2_busca_ref(self):
        self.dlg_select_terreno_informe2_busca_ref.show()
    
    def cerrar_dialogo_select_terreno_informe2_busca_ref(self):
        self.dlg_select_terreno_informe2_busca_ref.close()


    def abrir_dialogo_select_terreno_informe2_busca_nombre(self):
        self.dlg_select_terreno_informe2_busca_nombre.show()
    
    def cerrar_dialogo_select_terreno_informe2_busca_nombre(self):
        self.dlg_select_terreno_informe2_busca_nombre.close()
            
 

#BOTON CERTIFICADO AVALUO


    def abrir_dialogo_informe3(self):
        self.dlg_informe3.show()
        self.cargar_tablabbdd4()
        
        
    def cerrar_dialogo_informe3(self):
        self.dlg_informe3.close() 
    
    def abrir_dialogo_listarconstruccion(self):
        self.dlg_listar_construccion.show()
        self.cargar_construccion()
        
    def cerrar_dialogo_listarconstruccion(self):
        self.dlg_listar_construccion.close() 
    
    
    
    def abrir_dialogo_select_terreno_informe3_busca_ref(self):
        self.dlg_select_terreno_informe3_busca_ref.show()
    
    def cerrar_dialogo_select_terreno_informe3_busca_ref(self):
        self.dlg_select_terreno_informe3_busca_ref.close()


    def abrir_dialogo_select_terreno_informe3_busca_nombre(self):
        self.dlg_select_terreno_informe3_busca_nombre.show()
    
    def cerrar_dialogo_select_terreno_informe3_busca_nombre(self):
        self.dlg_select_terreno_informe3_busca_nombre.close()   
        
        
        
    # BOTON CAMBIAR TITULAR
    
    #abro y cierro  
    
    def abrir_dialogo_guardarfeature_cambiarTitular(self):
        self.dlg_guardar_feature_cambiar_titular.show()
        
        iface.actionSelect().trigger()


    def cerrar_dialogo_guardarfeature_cambiarTitular(self):
        self.dlg_guardar_feature_cambiar_titular.close()
        
        
        
    def abrir_select_titular_cambio_titular(self):
        self.dlg_select_titular_cambio_titular.show()
    

    def cerrar_select_titular_cambio_titular(self):
        self.dlg_select_titular_cambio_titular.close()    
        
        
        
    def abrir_select_titular_cambio_titular_busca_ref(self):    
       self.dlg_select_titular_cambio_titular_busca_ref.show()
       

    def cerrar_select_titular_cambio_titular_busca_ref(self):    
       self.dlg_select_titular_cambio_titular_busca_ref.close()      


    def abrir_select_titular_cambio_titular_busca_nombre(self):    
       self.dlg_select_titular_cambio_titular_busca_nombre.show()
       

    def cerrar_select_titular_cambio_titular_busca_nombre(self):    
       self.dlg_select_titular_cambio_titular_busca_nombre.close()         
       
       
       
    def abrir_confirmar_guardar_titular(self):
        self.confirmar_guardar_titular.show()
    
    
    def cerrar_confirmar_guardar_titular(self):
        self.confirmar_guardar_titular.close()
        
        
        
        
    #######################UNION DE PARCELAS####################################################################
    
    
    def abrir_guardar_feature_union(self):
        self.dlg_guardar_feature_union.show()
        iface.actionSelect().trigger()
        
    def cerrar_guardar_feature_union(self):
        self.dlg_guardar_feature_union.close()       
        
        
    def abrir_select_titular_union(self):
        self.dlg_select_titular_union.show()
 
    def cerrar_select_titular_union(self):
        self.dlg_select_titular_union.close() 
       
 
    def abrir_select_titular_union_busca_ref(self):
        self.dlg_select_titular_union_busca_ref.show()
 
    def cerrar_select_titular_union_busca_ref(self):
        self.dlg_select_titular_union_busca_ref.close()

        
    def abrir_select_titular_union_busca_nombre(self):
        self.dlg_select_titular_union_busca_nombre.show()
 
    def cerrar_select_titular_union_busca_nombre(self):
        self.dlg_select_titular_union_busca_nombre.close()  
  

    def abrir_confirmar_union(self):
        self.dlg_confirmar_union.show()
 
    def cerrar_confirmar_union(self):
        self.dlg_confirmar_union.close() 
        
 
 

    def abrir_dlg_info_codigo_union_union(self):
        self.dlg_info_codigo_union.show()
 
    def cerrar_dlg_info_codigo_union_union(self):
        self.dlg_info_codigo_union.close() 


        
        
    def abrir_info_forma_union(self):
        self.dlg_info_forma_union.show()
 
    def cerrar_info_forma_union(self):
        self.dlg_info_forma_union.close()   


    def abrir_info_inclinacion_union(self):
        self.dlg_info_inclinacion_union.show()
 
    def cerrar_info_inclinacion_union(self):
        self.dlg_info_inclinacion_union.close()         
  

    def abrir_material_calzada_union(self):
        self.dlg_info_material_calzada_union.show()
 
    def cerrar_material_calzada_union(self):
        self.dlg_info_material_calzada_union.close()  
  

    def abrir_tipo_calzada_union(self):
        self.dlg_info_tipo_calzada_union.show()
 
    def cerrar_tipo_calzada_union(self):
        self.dlg_info_tipo_calzada_union.close() 
        

    def abrir_dlg_info_ubicacion_union_union(self):
        self.dlg_info_ubicacion_union.show()
 
    def cerrar_dlg_info_ubicacion_union_union(self):
        self.dlg_info_ubicacion_union.close() 
        

    def abrir_dlg_info_zona_union_union(self):
        self.dlg_info_zona_union.show()
 
    def cerrar_dlg_info_zona_union_union(self):
        self.dlg_info_zona_union.close()         
        


   
    
    
    ##########################################DIVIDIR PARCELA############################################
    
    def abrir_guardar_feature_divide(self):
        self.dlg_guardar_feature_divide.show()
        iface.actionSelect().trigger()
        
    def cerrar_guardar_feature_divide(self):
        self.dlg_guardar_feature_divide.close()       
        
    
    def abrir_guardar_linea_divide(self):
        self.dlg_guardar_linea_divide.show()
        iface.actionSelect().trigger()
        
    def cerrar_guardar_linea_divide(self):
        self.dlg_guardar_linea_divide.close()

        
    def abrir_select_titular_divide1(self):
        self.dlg_select_titular_divide1.show()
        
    def cerrar_select_titular_divide1(self):
        self.dlg_select_titular_divide1.close()
        

    def abrir_select_titular_divide2(self):
        self.dlg_select_titular_divide2.show()
        
    def cerrar_select_titular_divide2(self):
        self.dlg_select_titular_divide2.close()        
        
        
    def abrir_select_titular_divide1_buscar_ref(self):
        self.dlg_select_titular_divide1_buscar_ref.show()
        
    def cerrar_select_titular_divide1_buscar_ref(self):
        self.dlg_select_titular_divide1_buscar_ref.close()        
 
 
    def abrir_select_titular_divide2_buscar_ref(self):
        self.dlg_select_titular_divide2_buscar_ref.show()
        
    def cerrar_select_titular_divide2_buscar_ref(self):
        self.dlg_select_titular_divide2_buscar_ref.close()          
        

    def abrir_select_titular_divide1_buscar_nombre(self):
        self.dlg_select_titular_divide1_buscar_nombre.show()
        
    def cerrar_select_titular_divide1_buscar_nombre(self):
        self.dlg_select_titular_divide1_buscar_nombre.close()        
 
 
    def abrir_select_titular_divide2_buscar_nombre(self):
        self.dlg_select_titular_divide2_buscar_nombre.show()
        
    def cerrar_select_titular_divide2_buscar_nombre(self):
        self.dlg_select_titular_divide2_buscar_nombre.close()   
 

    def abrir_confirmar_divide(self):
        self.dlg_confirmar_divide.show()
    
    def cerrar_confirmar_divide(self):
        self.dlg_confirmar_divide.close() 


    def abrir_dlg_info_codigo_divide1(self):
        self.dlg_info_codigo_divide1.show()
 
    def cerrar_dlg_info_codigo_divide1(self):
        self.dlg_info_codigo_divide1.close() 
    
 
    def abrir_dlg_info_codigo_divide2(self):
        self.dlg_info_codigo_divide2.show()
 
    def cerrar_dlg_info_codigo_divide2(self):
        self.dlg_info_codigo_divide2.close() 
        


    
    #######################################  FUNCIONES DE FUNCIONAMIENTO DE BOTONES#########################################################
    #########################################################################################################################################
    #########################################################################################################################################
    
    
    
    
    ############################################################################################################################################
    ############################################################BOTON GUARDA TITULAR##########################################################
    ############################################################################################################################################
    
    
    nombre_apellidos = ''
    id_titular_archivo = 0
    
    def guardar_titular(self):
    
        ####POST A TITULAR ####
    
        text_apellidos = self.dlg_export_titular.txt_apellidos
        valor_apellidos = text_apellidos.toPlainText()
    
        text_nombre = self.dlg_export_titular.txt_nombre
        valor_nombre = text_nombre.toPlainText()
        
        text_documento = self.dlg_export_titular.txt_documento
        valor_documento = text_documento.toPlainText()
    
        tipo_documento = self.dlg_export_titular.comboBox_tipo_prop.currentIndex()
        titularidad = self.dlg_export_titular.comboBox_titularidad_prop.currentIndex()
        documento_propiedad = self.dlg_export_titular.comboBox_doc_prop.currentIndex()
        adquisicion = self.dlg_export_titular.comboBox_adquisicion_prop.currentIndex()
          
        urlTitular = "http://192.168.0.150:8080/apiCatastro/titular"
        
        datos = {'apellidos': valor_apellidos, 'documento' : valor_documento, 'nombre': valor_nombre, "adquisicionBean": {"id": adquisicion}, "caracterTitular": {"id": titularidad},
        "documentoPropiedad": {"id": documento_propiedad}, "tipoDocumento": {"id": tipo_documento}}
        
        
        response = requests.post(urlTitular, json=datos)
        
        print("POSTEANDO")
        print(response)
        
        if response.status_code == 201:
            print(response.content)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'Información Guardada en la Base de Datos Correctamente')
        else:
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'No se pude cargar la información en la Base de Datos')
         
        
        self.dlg_export_titular.txt_apellidos.clear()
        self.dlg_export_titular.txt_nombre.clear()
        self.dlg_export_titular.txt_documento.clear()
        
        self.dlg_export_titular.comboBox_tipo_prop.setCurrentIndex(0)
        self.dlg_export_titular.comboBox_titularidad_prop.setCurrentIndex(0)
        self.dlg_export_titular.comboBox_doc_prop.setCurrentIndex(0)
        self.dlg_export_titular.comboBox_adquisicion_prop.setCurrentIndex(0)
            
    
    ############################################################################################################################################
    ############################################################BOTON CARGA ARCHIVO SHP o CSV###################################################
    ############################################################################################################################################
    
    titulares_cargados = ""
    
    
    def cargar_titular(self):
    
        urlTitular = "http://192.168.0.150:8080/apiCatastro/titular"
        
        response = requests.get(urlTitular)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_select_titular.list_titular
        
        for i in range(list_widget.count()):
        
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:
            lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        
        self.titulares_cargados = response_json
       
            
    
    def titular_busca_ref(self):
        
        list_widget = self.dlg_select_titular.list_titular
        
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        # features = list(self.titulares_cargados.getFeatures())
        
        text_busqueda  = self.dlg_select_titular_busca_ref.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
  
        lista = []
              
        for item in self.titulares_cargados:      
            if valor_busqueda == str(item["documento"]):
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))

        list_widget.addItems(lista)
    
    
                
    def titular_busca_nombre(self):
    
        list_widget = self.dlg_select_titular.list_titular
               
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_titular_busca_nombre.text_titular
        valor_busqueda = text_busqueda.toPlainText().lower()
              
        lista = []
        
        for item in self.titulares_cargados:     
            nombreyapellidos = str(item["nombre"]).lower() + " " + str(item["apellidos"]).lower()
      
            if valor_busqueda in nombreyapellidos:
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        

        
    #CARGAR ARCHIVO
        
    def cargar_csv(self):
        """ Carrgando archivos de tipo CSV """
        
        file_widget = self.dlg.carga_archivo
        
        file_src = file_widget.filePath()
        
        file_src_end = file_src[-3:]
        
        if file_src_end == 'shp':      
            #creo un vectorlayer a partir de mi archivo
            vector_layer = QgsVectorLayer(file_src, 'pedro', 'ogr')
            
        if file_src_end == 'csv':
            #uri =  'file:///' + file_src + '?delimiter=%s&xField=%s&yField=%s" % (";", "XCOORD", "YCOORD")'
            uri = 'file:///' + file_src + '?delimiter=;&yField=ycoord&xField=xcoord'
            vector_layer = QgsVectorLayer(uri, 'pedro3', 'delimitedtext')
            
            features_puntuales = list(vector_layer.getFeatures())
            
            lista_puntos = []
            lista_puntos_api = []
            
            for f in features_puntuales:
                point_x = f["xcoord"]
                point_y = f["ycoord"]
                
                # lista_puntos_api.append([point_x, point_y])
                
                point = QgsPointXY(point_x, point_y)
                lista_puntos.append(point)
                
                
            point_x_0 = features_puntuales[0]["xcoord"]
            point_y_0 = features_puntuales[0]["ycoord"]
            point_0 = QgsPointXY(point_x_0, point_y_0)
            lista_puntos.append(point_0)

                
            #Set feature
            nueva_feature = QgsFeature()
 
            #Set geometry
            nueva_feature.setGeometry(QgsGeometry.fromPolygonXY([lista_puntos]))
            
            vector_layer = QgsVectorLayer("MULTIPOLYGON?crs=EPSG:32719", "poligono_csv", "memory")
            
            vector_layer.dataProvider().addFeatures([nueva_feature])
                
                    
        
        features_del_archivo = list(vector_layer.getFeatures())
        feture_uno = features_del_archivo[0]
        
        geometria_del_archivo = feture_uno.geometry()
 
  
        
        listPointsToExport = []
        
        for listPointsGeometry in geometria_del_archivo.asPolygon():
            for listPoints in listPointsGeometry:
                listPointsToExport.append([listPoints.x(), listPoints.y()])

        
        print(listPointsToExport)

        
        
        list_widget = self.dlg_select_titular.list_titular
        current = list_widget.currentItem()
        
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name = current.text()
        
        titular_tuple = list_widget_name.split()
        
 
        
        #Añado datos a los campos que se crean en el plugin y paso la feature llena
        text_codigo = self.dlg_export.txt_referencia
        valor_codigo = text_codigo.toPlainText()
        
        text_direccion = self.dlg_export.txt_calle
        valor_direccion = text_direccion.toPlainText()

        text_manzano = self.dlg_export.txt_manzano
        valor_manzano = text_manzano.toPlainText()
        
        text_predio = self.dlg_export.txt_predio 
        valor_predio  = text_predio.toPlainText()
        
        text_subpredio = self.dlg_export.txt_sub
        valor_subpredio = text_subpredio.toPlainText()       
        
        text_zona = self.dlg_export.txt_zona
        valor_zona = text_zona.toPlainText()
        

        text_suptest = self.dlg_export.txt_suptest
        valor_suptest = text_suptest.toPlainText()       

        
        
        text_frente = self.dlg_export.txt_frente
        valor_frente = text_frente.toPlainText()       
                
        text_fondo = self.dlg_export.txt_fondo
        valor_fondo = text_fondo.toPlainText()
        
        

        agua = self.dlg_export.checkBox_agua.isChecked()
        telefono = self.dlg_export.checkBox_telefono.isChecked()
        alcantarillado = self.dlg_export.checkBox_alcantarilla.isChecked()
        energia = self.dlg_export.checkBox_energia.isChecked()
        internet = self.dlg_export.checkBox_internet.isChecked()
        transporte = self.dlg_export.checkBox_transporte.isChecked()        
        
        
        
        text_norte = "norte"        
        text_sur = "sur" 
        text_este = "este"
        text_oeste = "oeste"

        
        
        text_base = self.dlg_export.txt_base
        valor_base = text_base.toPlainText()
        
        
        zona = self.dlg_export.comboBox_zona.currentIndex()
        material_via = self.dlg_export.comboBox_calzada.currentIndex()
        inclinacion = self.dlg_export.comboBox_inclinacion.currentIndex()
        ubicacion = self.dlg_export.comboBox_ubicacion.currentIndex()
        calzada = self.dlg_export.comboBox_tipocalzada.currentIndex()
        forma = self.dlg_export.comboBox_forma.currentIndex()
        

        cur_area = (geometria_del_archivo.area())
        
 
        
        #######################################añadir el id del titular ####################################
        titular = titular_tuple[0]
        
        

 
  
    
        urlTerrenos19 = "http://192.168.0.150:8080/apiCatastro/terrenos19"
                
        datos = {'codigo': valor_codigo, 'agua': agua, 'alcantarillado': alcantarillado, 'barrio': valor_zona, 'base': valor_base, 'direccion': valor_direccion, 
        'energia': energia, 'este': " ", 'fondo': valor_fondo, 'frente': valor_frente, 'internet': internet, 'manzano': valor_manzano, 'norte': " ", 'oeste': " ", 
        'predio': valor_predio, 'subpredio': valor_subpredio, 'superficie': cur_area, 'suptest': valor_suptest, 'sur': " ",  'telefono': telefono,  'transporte': transporte,
        'formaBean': {'id': forma}, 'materialViaBean': {'id': material_via}, 'tipoVia': {'id': calzada}, 'titularBean': {'id': titular}, 'topografiaBean': {'id': inclinacion}, 
        'ubicacionBean': {'id': ubicacion}, 'zonaBean': {'id': zona}, "geom": {"type": "MultiPolygon","coordinates": [[listPointsToExport]]}}
        
        
        response = requests.post(urlTerrenos19, json=datos)
        
        print(response.status_code)
        
        if response.status_code == 201:
            print(response.content)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'Información Guardada en la Base de Datos Correctamente')
        else:
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'No se pude cargar la información en la Base de Datos')
         
        
        self.dlg_export.txt_referencia.clear()
        self.dlg_export.txt_calle.clear()
        self.dlg_export.txt_manzano.clear()
        self.dlg_export.txt_predio.clear() 
        self.dlg_export.txt_sub.clear()
        self.dlg_export.txt_zona.clear()
        self.dlg_export.txt_suptest.clear()
        self.dlg_export.txt_frente.clear()        
        self.dlg_export.txt_fondo.clear()
        
        self.dlg_export.checkBox_agua.setChecked(False)
        self.dlg_export.checkBox_telefono.setChecked(False)
        self.dlg_export.checkBox_alcantarilla.setChecked(False)
        self.dlg_export.checkBox_energia.setChecked(False)
        self.dlg_export.checkBox_internet.setChecked(False)
        self.dlg_export.checkBox_transporte.setChecked(False)
        
        self.dlg_export.txt_base.clear() 
        
        self.dlg_export.comboBox_zona.setCurrentIndex(0)
        self.dlg_export.comboBox_calzada.setCurrentIndex(0)
        self.dlg_export.comboBox_inclinacion.setCurrentIndex(0)
        self.dlg_export.comboBox_ubicacion.setCurrentIndex(0) 
        self.dlg_export.comboBox_tipocalzada.setCurrentIndex(0)
        self.dlg_export.comboBox_forma.setCurrentIndex(0)

 
    
    
     
    
    ############################################################################################################################################
    ############################################################BOTON SELECCIONA POLIGONO##########################################################
    ############################################################################################################################################
    
                    
  
    titulares_feature_cargados = ""
   
    def cargar_titular_feature(self):
    
        urlTitular = "http://192.168.0.150:8080/apiCatastro/titular"
        
        response = requests.get(urlTitular)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_select_titular_feature.list_titular
        
        for i in range(list_widget.count()):
        
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:
            lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        
        self.titulares_feature_cargados = response_json     
       
    
 
    def titular_feature_busca_ref(self):
        
        list_widget = self.dlg_select_titular_feature.list_titular
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        # features = list(self.titulares_cargados.getFeatures())
        
        text_busqueda  = self.dlg_select_titular_busca_ref.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
  
        lista = []
              
        for item in self.titulares_feature_cargados:      
            if valor_busqueda == str(item["documento"]):
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))

        list_widget.addItems(lista)
        
        
       
    def titular_feature_busca_nombre(self):
    
        list_widget = self.dlg_select_titular_feature.list_titular
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_titular_busca_nombre.text_titular
        valor_busqueda = text_busqueda.toPlainText().lower()
              
        lista = []
        
        for item in self.titulares_feature_cargados:     
            nombreyapellidos = str(item["nombre"]).lower() + " " + str(item["apellidos"]).lower()
      
            if valor_busqueda in nombreyapellidos:
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        
        
        
        
    
    def selecciona_feature(self):    
        
        layer = iface.activeLayer()
        
        features = layer.selectedFeatures()
        
        geometria = features[0].geometry()
        
                               
        n = 0
        ver = geometria.vertexAt(0)
        puntos = []
        
        while(ver.isEmpty() != True):
            ver = geometria.vertexAt(n)
            n +=1
            ver_xy = QgsPointXY(ver)
            puntos.append(ver_xy)
        
        puntos.pop()
        
        
        listPointsToExport = []
        
        for point in puntos:
            listPointsToExport.append([point.x(), point.y()])
        
        print(listPointsToExport)
    
        
        
        list_widget = self.dlg_select_titular_feature.list_titular
        current = list_widget.currentItem()
        
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name = current.text()
        
        titular_tuple = list_widget_name.split()
        
        
    #Añado datos a los campos que se crean en el plugin y paso la feature llena
        text_codigo = self.dlg_export_feature.txt_referencia
        valor_codigo = text_codigo.toPlainText()
        
        text_direccion = self.dlg_export_feature.txt_calle
        valor_direccion = text_direccion.toPlainText()

        text_manzano = self.dlg_export_feature.txt_manzano
        valor_manzano = text_manzano.toPlainText()
        
        text_predio = self.dlg_export_feature.txt_predio 
        valor_predio  = text_predio.toPlainText()
        
        text_subpredio = self.dlg_export_feature.txt_sub
        valor_subpredio = text_subpredio.toPlainText()       
        
        text_zona = self.dlg_export_feature.txt_zona
        valor_zona = text_zona.toPlainText()
        

        text_suptest = self.dlg_export_feature.txt_suptest
        valor_suptest = text_suptest.toPlainText()       

        
        text_frente = self.dlg_export_feature.txt_frente
        valor_frente = text_frente.toPlainText()       
                
        text_fondo = self.dlg_export_feature.txt_fondo
        valor_fondo = text_fondo.toPlainText()
        
        
        agua = self.dlg_export_feature.checkBox_agua.isChecked()
        telefono = self.dlg_export_feature.checkBox_telefono.isChecked()
        alcantarillado = self.dlg_export_feature.checkBox_alcantarilla.isChecked()
        energia = self.dlg_export_feature.checkBox_energia.isChecked()
        internet = self.dlg_export_feature.checkBox_internet.isChecked()
        transporte = self.dlg_export_feature.checkBox_transporte.isChecked()        
        
        
        text_norte = "norte"        
        text_sur = "sur"         
        text_este = "este"
        text_oeste = "oeste"
 
        
        text_base = self.dlg_export_feature.txt_base
        valor_base = text_base.toPlainText()
        
        
        zona = self.dlg_export_feature.comboBox_zona.currentIndex()
        material_via = self.dlg_export_feature.comboBox_calzada.currentIndex()
        inclinacion = self.dlg_export_feature.comboBox_inclinacion.currentIndex()
        ubicacion = self.dlg_export_feature.comboBox_ubicacion.currentIndex()
        calzada = self.dlg_export_feature.comboBox_tipocalzada.currentIndex()
        forma = self.dlg_export_feature.comboBox_forma.currentIndex()
        

        cur_area = (geometria.area())
        
        #######################################añadir el id del titular ####################################
        titular = titular_tuple[0]
        
        
        urlTerrenos19 = "http://192.168.0.150:8080/apiCatastro/terrenos19"
                
        datos = {'codigo': valor_codigo, 'agua': agua, 'alcantarillado': alcantarillado, 'barrio': valor_zona, 'base': valor_base, 'direccion': valor_direccion, 
        'energia': energia, 'este': " ", 'fondo': valor_fondo, 'frente': valor_frente, 'internet': internet, 'manzano': valor_manzano, 'norte': " ", 'oeste': " ", 
        'predio': valor_predio, 'subpredio': valor_subpredio, 'superficie': cur_area, 'suptest': valor_suptest, 'sur': " ",  'telefono': telefono,  'transporte': transporte,
        'formaBean': {'id': forma}, 'materialViaBean': {'id': material_via}, 'tipoVia': {'id': calzada}, 'titularBean': {'id': titular}, 'topografiaBean': {'id': inclinacion}, 
        'ubicacionBean': {'id': ubicacion}, 'zonaBean': {'id': zona}, "geom": {"type": "MultiPolygon","coordinates": [[listPointsToExport]]}}
        
        
        # , "geom": {"type": "MultiPolygon","coordinates": [[listPointsToExport]]}
        
        
        response = requests.post(urlTerrenos19, json=datos)
        
        
        if response.status_code == 201:
            print(response.content)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'Información Guardada en la Base de Datos Correctamente')
        else:
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'No se pude cargar la información en la Base de Datos')
          
        
        self.dlg_export_feature.txt_referencia.clear()
        self.dlg_export_feature.txt_calle.clear()
        self.dlg_export_feature.txt_manzano.clear()
        self.dlg_export_feature.txt_predio.clear() 
        self.dlg_export_feature.txt_sub.clear()
        self.dlg_export_feature.txt_zona.clear()
        self.dlg_export_feature.txt_suptest.clear()
        self.dlg_export_feature.txt_frente.clear()        
        self.dlg_export_feature.txt_fondo.clear()
        
        self.dlg_export_feature.checkBox_agua.setChecked(False)
        self.dlg_export_feature.checkBox_telefono.setChecked(False)
        self.dlg_export_feature.checkBox_alcantarilla.setChecked(False)
        self.dlg_export_feature.checkBox_energia.setChecked(False)
        self.dlg_export_feature.checkBox_internet.setChecked(False)
        self.dlg_export_feature.checkBox_transporte.setChecked(False)
        
        self.dlg_export.txt_base.clear() 
        
        self.dlg_export_feature.comboBox_zona.setCurrentIndex(0)
        self.dlg_export_feature.comboBox_calzada.setCurrentIndex(0)
        self.dlg_export_feature.comboBox_inclinacion.setCurrentIndex(0)
        self.dlg_export_feature.comboBox_ubicacion.setCurrentIndex(0)
        self.dlg_export_feature.comboBox_tipocalzada.setCurrentIndex(0)
        self.dlg_export_feature.comboBox_forma.setCurrentIndex(0)




    ############################################################################################################################################
    ############################################################TERCER BOTON SELECCIONA CONSTRUCCION##########################################################
    ############################################################################################################################################   



    #Selecciona Construccion
    
    def selecciona_construccion(self):    
    
        #guardo feature seleccionado
        
        layer = iface.activeLayer()
        
        features = layer.selectedFeatures()
        
        geometria = features[0].geometry()
                 
        n = 0
        ver = geometria.vertexAt(0)
        puntos = []
        
        while(ver.isEmpty() != True):
            ver = geometria.vertexAt(n)
            n +=1
            ver_xy = QgsPointXY(ver)
            puntos.append(ver_xy)
        
        puntos.pop()
        
        listPointsToExport = []
        
        for point in puntos:
            listPointsToExport.append([point.x(), point.y()])
        
        print("prueba construccion")
        print(listPointsToExport)
        
        
        #añado valores a lo campos creados
        list_widget = self.dlg_export_feature_construccion.list_bbdd
        current = list_widget.currentItem()
        
 
        cod = self.dlg_export_feature_construccion.cod
        valor_cod = cod.toPlainText()
        

        
        currentText = current.text()
        list_widget_name_ref = ""
        
        currentTextSplit = currentText.split()
        currentTextSplitCodigo = currentTextSplit[0]
        
        print("prueba construccion2")
        print(currentTextSplitCodigo)
               
               
        cur_area = (features[0].geometry().area())
               
        anyo = self.dlg_export_feature_construccion.anyo
        valor_anyo = anyo.toPlainText()
        
        plantas = self.dlg_export_feature_construccion.plantas
        valor_plantas = plantas.toPlainText()
        
        dorm = self.dlg_export_feature_construccion.dormitorios
        valor_dorm = dorm.toPlainText()
        
        banyos = self.dlg_export_feature_construccion.banyos
        valor_banyos = cod.toPlainText()

           
        conservacion = self.dlg_export_feature_construccion.comboBox_conservacion.currentIndex()           
        uso = self.dlg_export_feature_construccion.comboBox_uso.currentIndex()
        tipo = self.dlg_export_feature_construccion.comboBox_tipo.currentIndex()       
        revestimiento = self.dlg_export_feature_construccion.comboBox_revestimiento.currentIndex()
        

        ascensor = self.dlg_export_feature_construccion.checkBox_ascensor.isChecked()
        calefaccion = self.dlg_export_feature_construccion.checkBox_calefaccion.isChecked()
        sanitarios = self.dlg_export_feature_construccion.checkBox_sanitarios.isChecked()
        escalera = self.dlg_export_feature_construccion.checkBox_escalera.isChecked()
        
        aire = self.dlg_export_feature_construccion.checkBox_aire.isChecked()
        lavanderia = self.dlg_export_feature_construccion.checkBox_lavandera.isChecked()
        agua = self.dlg_export_feature_construccion.checkBox_agua.isChecked()
        area = self.dlg_export_feature_construccion.checkBox_area.isChecked()
        


        urlConstrucciones19 = "http://192.168.0.150:8080/apiCatastro/construcciones19"
                
        datos = {'aire': aire, 'anyo': valor_anyo, 'ascensores': ascensor, 'banyos': valor_banyos, 'calefaccion': calefaccion, 'cod': valor_cod, 'dormitorios': valor_dorm, 
        'escalera': escalera, 'lavanderia': lavanderia, 'plantas': valor_plantas,  'sanitarios': sanitarios, 'servicio': area, 'superficie': cur_area,'tanque': agua, 
        'conservacionBean': {'id': conservacion }, 'revestimientoBean': {'id': revestimiento }, 'tipoConstruccion': {'id': tipo }, 'usoBean': {'id': uso }, 
        'terrenos19': {'codigo': currentTextSplitCodigo}, "geom": {"type": "MultiPolygon","coordinates": [[listPointsToExport]]}}
        
        response = requests.post(urlConstrucciones19, json=datos)
        
        
        if response.status_code == 201:
            print(response.content)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'Información Guardada en la Base de Datos Correctamente')
        else:
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'No se pude cargar la información en la Base de Datos')        
        
        
                
        self.dlg_export_feature_construccion.cod.clear()
        self.dlg_export_feature_construccion.anyo.clear()      
        self.dlg_export_feature_construccion.plantas.clear()       
        self.dlg_export_feature_construccion.dormitorios.clear()

        self.dlg_export_feature_construccion.banyos.clear()           
        self.dlg_export_feature_construccion.comboBox_conservacion.setCurrentIndex(0)        
        self.dlg_export_feature_construccion.comboBox_uso.setCurrentIndex(0)
        self.dlg_export_feature_construccion.comboBox_tipo.setCurrentIndex(0)   
        self.dlg_export_feature_construccion.comboBox_revestimiento.setCurrentIndex(0)
        

        self.dlg_export_feature_construccion.checkBox_ascensor.setChecked(False)
        self.dlg_export_feature_construccion.checkBox_calefaccion.setChecked(False)
        self.dlg_export_feature_construccion.checkBox_sanitarios.setChecked(False)
        escalera = self.dlg_export_feature_construccion.checkBox_escalera.setChecked(False)
        
        self.dlg_export_feature_construccion.checkBox_aire.setChecked(False)
        self.dlg_export_feature_construccion.checkBox_lavandera.setChecked(False)
        self.dlg_export_feature_construccion.checkBox_agua.setChecked(False)
        self.dlg_export_feature_construccion.checkBox_area.setChecked(False)
        
   
        
    def cargar_tablabbdd_construccion(self):
    
    #GET A TERRENOS#############################################################################################################################################
    
        
        urlTerrenos19 = "http://192.168.0.150:8080/apiCatastro/terrenos19"
        
        response = requests.get(urlTerrenos19)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_export_feature_construccion.list_bbdd
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:
            lista.append(str(item["codigo"]) + "   " + str(item["direccion"]))
       
        list_widget.addItems(lista)
          
        
        
               
 #######################################AÑADIR EDIFICACION ESPECIAL##############################################################
               
               
    def cargar_tablabbdd_especial(self):
    
        
        urlTerrenosEspeciales19 = "http://192.168.0.150:8080/apiCatastro/terrenosespeciales19"
        
        response = requests.get(urlTerrenosEspeciales19)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget_especial = self.dlg_export_especial.list_bbdd
        
        list_widget = self.dlg_export_feature_construccion.list_bbdd
        current = list_widget.currentItem()
        
        for i in range(list_widget_especial.count()):
            list_widget_especial.takeItem(0)
        
        lista = []
           
        currentText = current.text()
        currentTextSplit = currentText.split()
        currentTextSplitCodigo = currentTextSplit[0]
                
        for item in response_json:
            if(currentTextSplitCodigo == str(item["terrenos19"]["codigo"])):
                lista.append(str(item["especiale"]["nombre"]) +"    "+ str(item["terrenos19"]["codigo"]))
       
        list_widget_especial.addItems(lista)
          

    
    def guardar_feature_bbdd_especial(self,feature):
            
        list_widget = self.dlg_export_feature_construccion.list_bbdd
        current = list_widget.currentItem()
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name = current.text()
        currentTextSplit = list_widget_name.split()
        currentTextSplitCodigo = currentTextSplit[0]
        
        tipo = self.dlg_export_especial.comboBox_tipo_edi.currentIndex() 
        
        anyo = self.dlg_export_especial.anyo
        valor_anyo = anyo.toPlainText()
        
        sup = self.dlg_export_especial.superficie
        valor_superficie = sup.toPlainText()
       
        conservacion = self.dlg_export_especial.comboBox_conservacion.currentIndex()  
        
        cimientos = self.dlg_export_especial.comboBox_cimientos.currentIndex()  
        estructura = self.dlg_export_especial.comboBox_estructura.currentIndex()  
        muros = self.dlg_export_especial.comboBox_muros.currentIndex()  
        externos = self.dlg_export_especial.comboBox_externos.currentIndex()  
        interiores = self.dlg_export_especial.comboBox_interiores.currentIndex()  
        techos = self.dlg_export_especial.comboBox_techos.currentIndex()  
        pisos = self.dlg_export_especial.comboBox_pisos.currentIndex()  
        ventanas = self.dlg_export_especial.comboBox_ventanas.currentIndex() 
        
        
        urlTerrenosEspeciales19 = "http://192.168.0.150:8080/apiCatastro/terrenosespeciales19"
                
        
        datos = {'anyo': valor_anyo, 'superficie': valor_superficie, 'conservacionBean': {'id': conservacion}, 'ediCarpinteria': {'id': ventanas},
        'ediCimiento':{'id': cimientos}, 'ediCubierta':{'id': techos}, 'ediEstructura': {'id': estructura},'ediMuro': {'id': muros},'ediMurosExt': {'id': externos},
        'ediMurosInt': {'id': interiores}, 'ediPiso': {'id': pisos}, 'especiale':{'id': tipo}, 'terrenos19': {'codigo': currentTextSplitCodigo}}
        
        response = requests.post(urlTerrenosEspeciales19, json=datos)
        
        
        if response.status_code == 201:
            print(response.content)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'Información Guardada en la Base de Datos Correctamente')
        else:
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'No se pude cargar la información en la Base de Datos') 
            
        
        self.dlg_export_especial.comboBox_tipo_edi.setCurrentIndex(0)
        self.dlg_export_especial.anyo.clear()         
        sup = self.dlg_export_especial.superficie.clear() 
        self.dlg_export_especial.comboBox_conservacion.setCurrentIndex(0)
        
        self.dlg_export_especial.comboBox_cimientos.setCurrentIndex(0) 
        self.dlg_export_especial.comboBox_estructura.setCurrentIndex(0) 
        self.dlg_export_especial.comboBox_muros.setCurrentIndex(0)
        self.dlg_export_especial.comboBox_externos.setCurrentIndex(0)  
        self.dlg_export_especial.comboBox_interiores.setCurrentIndex(0)
        self.dlg_export_especial.comboBox_techos.setCurrentIndex(0) 
        self.dlg_export_especial.comboBox_pisos.setCurrentIndex(0)  
        self.dlg_export_especial.comboBox_ventanas.setCurrentIndex(0)
    
                 
               
               
               ######################################AÑADIR MEJORA#########################################################################
                             
        
    def cargar_tablabbdd_mejora(self):
    
   
        urlTerrenosMejoras19 = "http://192.168.0.150:8080/apiCatastro/terrenosmejoras19"
        
        response = requests.get(urlTerrenosMejoras19)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget_mejora = self.dlg_export_mejora.list_bbdd
        
        list_widget = self.dlg_export_feature_construccion.list_bbdd
        current = list_widget.currentItem()
        list_widget_name = current.text()
        
        
        for i in range(list_widget_mejora.count()):
            list_widget_mejora.takeItem(0)
        
        lista = []
        
        print("CURRENTE")
        currentText = current.text()
        currentTextSplit = currentText.split()
        currentTextSplitCodigo = currentTextSplit[0]
        print(currentTextSplitCodigo)
        
        
        for item in response_json:
            if(currentTextSplitCodigo == str(item["terrenos19"]["codigo"])):
                lista.append(str(item["mejora"]["nombre"]) +"    "+ str(item["terrenos19"]["codigo"]))
       
        list_widget_mejora.addItems(lista)
 
               
    
    def guardar_feature_bbdd_mejora(self,feature):
    
    
        list_widget = self.dlg_export_feature_construccion.list_bbdd
        current = list_widget.currentItem()
        
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name = current.text()
        currentTextSplit = list_widget_name.split()
        currentTextSplitCodigo = currentTextSplit[0]
        
    
        tipo = self.dlg_export_mejora.comboBox_tipo_mejora.currentIndex() 
        
        anyo = self.dlg_export_mejora.anyo
        valor_anyo = anyo.toPlainText()
        
        sup = self.dlg_export_mejora.superficie
        valor_superficie = sup.toPlainText()
       
        conservacion = self.dlg_export_mejora.comboBox_conservacion.currentIndex()  
        
        cimientos = self.dlg_export_mejora.comboBox_cimientos.currentIndex()  
        estructura = self.dlg_export_mejora.comboBox_estructura.currentIndex()  
        muros = self.dlg_export_mejora.comboBox_muros.currentIndex()  
        externos = self.dlg_export_mejora.comboBox_externos.currentIndex()  
        interiores = self.dlg_export_mejora.comboBox_interiores.currentIndex()  
        techos = self.dlg_export_mejora.comboBox_techos.currentIndex()  
        pisos = self.dlg_export_mejora.comboBox_pisos.currentIndex()  
        ventanas = self.dlg_export_mejora.comboBox_ventanas.currentIndex()
        
  
  
        urlTerrenosMejoras19 = "http://192.168.0.150:8080/apiCatastro/terrenosmejoras19"
                
        datos = {'anyo': valor_anyo, 'superficie': valor_superficie, 'conservacionBean': {'id': conservacion}, 'ediCarpinteria': {'id': ventanas},
        'ediCimiento':{'id': cimientos}, 'ediCubierta':{'id': techos}, 'ediEstructura': {'id': estructura},'ediMuro': {'id': muros},'ediMurosExt': {'id': externos},
        'ediMurosInt': {'id': interiores}, 'ediPiso': {'id': pisos}, 'mejora':{'id': tipo}, 'terrenos19': {'codigo': currentTextSplitCodigo}}
        
        response = requests.post(urlTerrenosMejoras19, json=datos)
        
        
        if response.status_code == 201:
            print(response.content)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'Información Guardada en la Base de Datos Correctamente')
        else:
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'No se pude cargar la información en la Base de Datos') 
  
        
        
        self.dlg_export_mejora.comboBox_tipo_mejora.setCurrentIndex(0)
        self.dlg_export_mejora.anyo.clear() 
        self.dlg_export_mejora.superficie.clear() 

        self.dlg_export_mejora.comboBox_conservacion.setCurrentIndex(0)
        
        self.dlg_export_mejora.comboBox_cimientos.setCurrentIndex(0)
        self.dlg_export_mejora.comboBox_estructura.setCurrentIndex(0) 
        self.dlg_export_mejora.comboBox_muros.setCurrentIndex(0) 
        self.dlg_export_mejora.comboBox_externos.setCurrentIndex(0) 
        self.dlg_export_mejora.comboBox_interiores.setCurrentIndex(0)
        self.dlg_export_mejora.comboBox_techos.setCurrentIndex(0)
        self.dlg_export_mejora.comboBox_pisos.setCurrentIndex(0)  
        self.dlg_export_mejora.comboBox_ventanas.setCurrentIndex(0)
    
               
        
 
        ################################################################################################################################################
        #################################################################################################################################################
        ######################################################     AÑADIR PLANTA      ####################################################################
        #################################################################################################################################################
        #################################################################################################################################################
            
            
            
    construcciones_cargadas = ""
 
    def cargar_tablaconstruccionbd_plantas(self):
        
       
        urlConstrucciones19 = "http://192.168.0.150:8080/apiCatastro/construcciones19"
        
        response = requests.get(urlConstrucciones19)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_listar_construccion_plantas.list_bbdd
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:
            lista.append(str(item["id"]) + "    " + str(item["cod"]) + "    " + str(item["terrenos19"]["codigo"]) + "    " + str(item["usoBean"]["uso"]))
            
       
        list_widget.addItems(lista)
        
        self.construcciones_cargadas = response_json
        
        
        
    def planta_busca_ref(self):
             
        list_widget = self.dlg_listar_construccion_plantas.list_titular
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        
        text_busqueda  = self.dlg_select_construccion_planta_busca_ref.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
  
        lista = []
              
        for item in self.construcciones_cargadas:      
            if valor_busqueda == str(item["terrenos19"]["codigo"]):
                lista.append(str(item["id"]) + "    " + str(item["cod"]) + "    " + str(item["terrenos19"]["codigo"]) + "    " + str(item["usoBean"]["uso"]))

        list_widget.addItems(lista)
              
    

    def cargar_plantas(self):
    
        list_widget = self.dlg_listar_construccion_plantas.list_bbdd
    
        current = list_widget.currentItem()
        
        list_widget_name_construccion = current.text()
    
        
        list_widget_name_ref = ""
        
        for asa in range(len(list_widget_name_construccion)):
            if list_widget_name_construccion[asa] == " ":
                ran = asa
                break
        
        list_widget_name_ref = list_widget_name_construccion[0:ran]  
        
        
        list_widget_const = self.dlg_listar_construccion.list_bbdd
 
        for i in range(list_widget_const.count()):
           
            list_widget_const.takeItem(0)
            
       
        urlPlantas19 = "http://192.168.0.150:8080/apiCatastro/construccionesplantas19"
        
        response = requests.get(urlPlantas19)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_export_planta.list_bbdd
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
        
        lista = []
        
                 
        for item in response_json:      
            if str(item["construcciones19"]["id"]) == list_widget_name_ref:
                lista.append(str(item["id"]) + "    "  + str(item["planta"]["id"]) )
  
        list_widget.addItems(lista)    
        self.construcciones_cargadas = response_json
        
        
        
    def guardar_planta(self):
    
        list_widget = self.dlg_listar_construccion_plantas.list_bbdd
        current = list_widget.currentItem()
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name = current.text()
        list_widget_name_list = list_widget_name.split()
        list_widget_name_id = int(list_widget_name_list[0])
        
        print("probando construccion")
        print(list_widget_name_id)
        
        
        self.cargar_plantas()
    
        planta = self.dlg_export_planta.comboBox_planta.currentIndex()
    
        anyo = self.dlg_export_planta.anyo
        valor_anyo = anyo.toPlainText()
        
        sup = self.dlg_export_planta.superficie
        valor_superficie = sup.toPlainText()
       
        
        ventanas = self.dlg_export_planta.comboBox_ventanas.currentIndex() 
        cimientos = self.dlg_export_planta.comboBox_cimientos.currentIndex()  
        techos = self.dlg_export_planta.comboBox_techos.currentIndex()  
        estructura = self.dlg_export_planta.comboBox_estructura.currentIndex()  
        muros = self.dlg_export_planta.comboBox_muros.currentIndex()  
        interiores = self.dlg_export_planta.comboBox_interiores.currentIndex()  
        externos = self.dlg_export_planta.comboBox_externos.currentIndex()  
        pisos = self.dlg_export_planta.comboBox_pisos.currentIndex()  
        
        
        

        urConstruccionesPlantas19 = "http://192.168.0.150:8080/apiCatastro/construccionesplantas19"
                
        datos = {'anyo':valor_anyo, 'superficie':valor_superficie, 'ediCarpinteria': {'id':ventanas},'ediCimiento': {'id':cimientos},'ediCubierta': {'id':techos},'ediEstructura': {'id':estructura},
        'ediMuro': {'id':muros},'ediMurosInt': {'id':interiores},'ediMurosExt': {'id':externos},'ediPiso': {'id':pisos},'planta': {'id':planta},
        'construcciones19': {'id': list_widget_name_id} }
        
        response = requests.post(urConstruccionesPlantas19, json=datos)
        
        
        if response.status_code == 201:
            print(response.content)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'Información Guardada en la Base de Datos Correctamente')
        else:
            print(response.content)
            print(response.status_code)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'No se pude cargar la información en la Base de Datos') 


        
        
        self.dlg_export_planta.comboBox_planta.setCurrentIndex(0)
        self.dlg_export_planta.anyo.clear()
        self.dlg_export_planta.superficie.clear()
       
        self.dlg_export_planta.comboBox_cimientos.setCurrentIndex(0)
        self.dlg_export_planta.comboBox_estructura.setCurrentIndex(0)
        self.dlg_export_planta.comboBox_muros.setCurrentIndex(0)
        self.dlg_export_planta.comboBox_externos.setCurrentIndex(0) 
        self.dlg_export_planta.comboBox_interiores.setCurrentIndex(0)
        self.dlg_export_planta.comboBox_techos.setCurrentIndex(0) 
        self.dlg_export_planta.comboBox_pisos.setCurrentIndex(0)
        self.dlg_export_planta.comboBox_ventanas.setCurrentIndex(0)
        
     
     
     
     
   
    ############################################################################################################################################
    ############################################################CUARTO BOTON DIBUJA LAYOUT##########################################################
    ############################################################################################################################################ 






    
    terrenos_cargados_layout = ""

                
    def cargar_tablabbdd(self):
            
        urlTerrenos19 = "http://192.168.0.150:8080/apiCatastro/terrenos19"
        
        response = requests.get(urlTerrenos19)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_layout.list_bbdd
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:

            if item["titularBean"]:
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"])  + "   " + str(item["titularBean"]["apellidos"]))
            else:
                lista.append(str(item["codigo"]))
       
        list_widget.addItems(lista)
        
        self.terrenos_cargados_layout = response_json
          
        
    
    def listar_layer_busca_ref(self):
                        
        list_widget = self.dlg_layout.list_bbdd
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_terreno_layout_busca_ref.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
        lista = []
              
        for item in self.terrenos_cargados_layout:      
            if valor_busqueda == str(item["codigo"]):
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"]))

        list_widget.addItems(lista)
        
            
    
    def listar_layer_busca_nombre(self):
            
        list_widget = self.dlg_layout.list_bbdd
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_terreno_layout_busca_nombre.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
        lista = []
              
        for item in self.terrenos_cargados_layout: 
        
            nombreyapellidos = str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"])
        
            if valor_busqueda in nombreyapellidos:
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"]))

        list_widget.addItems(lista)
        
        
    
    
     
    def mostrar_layout(self):
    
        
        QgsProject.instance().removeAllMapLayers()
        
        list_widget = self.dlg_layout.list_bbdd
        
        current = list_widget.currentItem()
        
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name = current.text()
        list_widget_name_ref = ""
        
        for asa in range(len(list_widget_name)):
            ran = len(list_widget_name) -1
            if list_widget_name[asa] == " ":
                ran = asa
                break
        
        print()
        list_widget_name_ref = list_widget_name[0:ran]
        
        
        
        
        urlTerreno19 = "http://192.168.0.150:8080/apiCatastro/terrenos19/" + list_widget_name_ref
        
        response_terreno = requests.get(urlTerreno19)
        
        
        if response_terreno.status_code == 200:
            response_json_terreno = response_terreno.json()
            
                
        
        layer_terreno = QgsVectorLayer("Polygon?crs=EPSG:32719","terreno","memory")
        layer_terreno_provider = layer_terreno.dataProvider()
        
        
        campo_codigo = QgsField("codigo",QVariant.String)
        campo_direccion = QgsField("direccion",QVariant.String)
        campo_superficie = QgsField("superficie",QVariant.Double)
        
        campo_barrio = QgsField("barrio",QVariant.String)
        
        
        campo_agua = QgsField("agua", QVariant.Bool)
        campo_energia = QgsField("energia", QVariant.Bool)
        campo_alcantarillado = QgsField("alcantarillado", QVariant.Bool)
        campo_telefono = QgsField("telefono", QVariant.Bool)
        campo_internet = QgsField("internet", QVariant.Bool)
        campo_transporte = QgsField("transporte", QVariant.Bool)
        
        campo_frente = QgsField("frente",QVariant.String)
        campo_fondo = QgsField("fondo",QVariant.String)
        campo_suptest = QgsField("suptest",QVariant.String)

        campo_manzano = QgsField("manzano",QVariant.String)
        campo_predio = QgsField("predio",QVariant.String)
        campo_sub = QgsField("subpredio",QVariant.String)
        campo_base = QgsField("base",QVariant.String)
        
        campo_nombre = QgsField("nombre",QVariant.String)
        campo_apellidos = QgsField("apellidos",QVariant.String)
        campo_documento = QgsField("documento",QVariant.String)
        
        campo_tipo_doc = QgsField("tipo_doc",QVariant.String)
        campo_caracter = QgsField("caracter",QVariant.String)
        campo_documento_prop = QgsField("documento_prop",QVariant.String)
        campo_adquisicion = QgsField("adquisicion",QVariant.String)
        
        campo_tipovia = QgsField("tipovia",QVariant.String)
        campo_valorvia = QgsField("valorvia",QVariant.Double)
        
        campo_nombretopo = QgsField("nombretopo",QVariant.String)
        campo_descrtopo = QgsField("descrtopo",QVariant.String) 
        campo_valortopo = QgsField("valortopo",QVariant.Double)        
        
        
        
        terreno_fields = [campo_codigo,campo_direccion,campo_superficie,campo_barrio,campo_energia,campo_agua,campo_alcantarillado,campo_telefono,campo_internet,
        campo_transporte,campo_frente,campo_fondo,campo_suptest,campo_manzano,campo_predio,campo_sub,campo_base,
        campo_nombre,campo_apellidos, campo_documento,campo_tipo_doc,campo_caracter,campo_documento_prop,campo_adquisicion,campo_tipovia,campo_valorvia,campo_nombretopo,
        campo_descrtopo,campo_valortopo]
        
        
        layer_terreno_provider.addAttributes(terreno_fields)
        layer_terreno.updateFields()
        

        
        feature_terreno = QgsFeature()
        
        feature_terreno.setFields(layer_terreno.fields())
        
              
        feature_terreno.setAttribute("codigo", response_json_terreno["codigo"])
        
        feature_terreno.setAttribute("direccion", response_json_terreno["direccion"])
        feature_terreno.setAttribute("superficie", response_json_terreno["superficie"])
        feature_terreno.setAttribute("barrio", response_json_terreno["barrio"])
        
        feature_terreno.setAttribute("energia", response_json_terreno["energia"])
        feature_terreno.setAttribute("agua", response_json_terreno["agua"])
        feature_terreno.setAttribute("alcantarillado", response_json_terreno["alcantarillado"])
        feature_terreno.setAttribute("telefono", response_json_terreno["telefono"])
        feature_terreno.setAttribute("internet", response_json_terreno["internet"])
        feature_terreno.setAttribute("transporte", response_json_terreno["transporte"])
                
        feature_terreno.setAttribute("frente", response_json_terreno["frente"])
        feature_terreno.setAttribute("fondo", response_json_terreno["fondo"])
        feature_terreno.setAttribute("suptest", response_json_terreno["suptest"])
        
        feature_terreno.setAttribute("manzano", response_json_terreno["frente"])
        feature_terreno.setAttribute("predio", response_json_terreno["fondo"])
        feature_terreno.setAttribute("subpredio", response_json_terreno["suptest"])
        feature_terreno.setAttribute("base", response_json_terreno["suptest"])

        if (response_json_terreno["titularBean"]):
            feature_terreno.setAttribute("nombre", response_json_terreno["titularBean"]["nombre"])
            feature_terreno.setAttribute("apellidos", response_json_terreno["titularBean"]["apellidos"])
            feature_terreno.setAttribute("documento", response_json_terreno["titularBean"]["documento"])        
            
            feature_terreno.setAttribute("tipo_doc", response_json_terreno["titularBean"]["tipoDocumento"]["tipo"])
            feature_terreno.setAttribute("caracter", response_json_terreno["titularBean"]["caracterTitular"]["caracter"])
            feature_terreno.setAttribute("documento_prop", response_json_terreno["titularBean"]["documentoPropiedad"]["documento"])
            feature_terreno.setAttribute("adquisicion", response_json_terreno["titularBean"]["adquisicionBean"]["adquisicion"])

            feature_terreno.setAttribute("tipovia", response_json_terreno["tipoVia"]["tipo"])
            feature_terreno.setAttribute("valorvia", response_json_terreno["tipoVia"]["valor"])
            
            feature_terreno.setAttribute("nombretopo", response_json_terreno["topografiaBean"]["nombre"])        
            feature_terreno.setAttribute("descrtopo", response_json_terreno["topografiaBean"]["descripcion"])
            feature_terreno.setAttribute("valortopo", response_json_terreno["topografiaBean"]["valor"])


        
        arrayCoordenadasTerreno = response_json_terreno["geom"]["coordinates"]
        
        arrayCoordenadasTerrenoGeometria = []
        
        for coordenadasTerreno in arrayCoordenadasTerreno:
            for coords in coordenadasTerreno:
                for i in coords:
                    arrayCoordenadasTerrenoGeometria.append(QgsPointXY(i[0],i[1]))

        
        terreno_geometria = QgsGeometry.fromPolygonXY([arrayCoordenadasTerrenoGeometria])
               
        
        #feature_terreno.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(10,10)))
        feature_terreno.setGeometry(terreno_geometria)
        
        
        
        
        layer_terreno_provider.addFeatures([feature_terreno])
        
        layer_terreno.updateExtents()

        symbol_terreno = QgsFillSymbol.createSimple({'color':'#ffffff', 
                                              'color_border':'#0F0290',
                                              'width_border':'1'})

        layer_terreno.renderer().setSymbol(symbol_terreno)

        layer_terreno.triggerRepaint()
        
        
        
        layer_settings_superficie  = QgsPalLayerSettings()
        text_format_superficie = QgsTextFormat()

        text_format_superficie.setFont(QFont("Arial", 8))
        text_format_superficie.setSize(10)

        buffer_settings_superficie = QgsTextBufferSettings()
        buffer_settings_superficie.setEnabled(True)
        buffer_settings_superficie.setSize(0.10)
        # layer_settings_superficie.setColor(QColor("blue"))
        
        text_format_superficie.setBuffer(buffer_settings_superficie)
        layer_settings_superficie.setFormat(text_format_superficie)

        layer_settings_superficie.fieldName = "superficie"
        # layer_settings_superficie.placement = 0
        layer_settings_superficie.centroidInside = True

        
        layer_settings_superficie.enabled = True

        layer_settings_superficie = QgsVectorLayerSimpleLabeling(layer_settings_superficie)
        layer_terreno.setLabelsEnabled(True)
        layer_terreno.setLabeling(layer_settings_superficie)
        layer_terreno.triggerRepaint()

         



        urlConstrucciones19 = "http://192.168.0.150:8080/apiCatastro/construcciones19"
        
        response_construcciones = requests.get(urlConstrucciones19)
                
        if response_construcciones.status_code == 200:
            response_json_construcciones = response_construcciones.json()
                
        jsonConstruccionesArray = []
        
        for itemConstruccion in response_json_construcciones:          
                
            if itemConstruccion["terrenos19"] and itemConstruccion["terrenos19"]["codigo"] == response_json_terreno["codigo"]:
         
                jsonConstruccionesArray.append(itemConstruccion);
        
        
        
        
        layer_construcciones = QgsVectorLayer("MultiPolygon?crs=32719","construcciones","memory")
        
        campo_id = QgsField("id",QVariant.Int)
        campo_cod = QgsField("cod",QVariant.Int)
        campo_aire = QgsField("aire",QVariant.String)
        
        construccion_fields = [campo_id, campo_cod, campo_aire]
           
        layer_construcciones.dataProvider().addAttributes(construccion_fields)
        layer_construcciones.updateFields()
        
        
        arrayCoordenadasConstruccionGeometria = []
        listFeaturesConstruccion = []
        
        for jsonConstruccionArrayItem in jsonConstruccionesArray:
        
            feature_construccion = QgsFeature()
            feature_construccion.setFields(layer_construcciones.fields())
            
            
            feature_construccion.setAttribute("id", jsonConstruccionArrayItem["id"])
            feature_construccion.setAttribute("cod", jsonConstruccionArrayItem["cod"])
            feature_construccion.setAttribute("aire", jsonConstruccionArrayItem["aire"])
            
            arrayCoordenadasConstruccion = jsonConstruccionArrayItem["geom"]["coordinates"]
            
            for coordenadasConstruccion in arrayCoordenadasConstruccion:             
                for coordCons in coordenadasConstruccion:                
                    for j in coordCons:
                        arrayCoordenadasConstruccionGeometria.append(QgsPointXY(j[0],j[1]))

            construccion_geometria = QgsGeometry.fromPolygonXY([arrayCoordenadasConstruccionGeometria])
            feature_construccion.setGeometry(construccion_geometria)
            
            listFeaturesConstruccion.append(feature_construccion)
            arrayCoordenadasConstruccionGeometria = []

        
        layer_construcciones.dataProvider().addFeatures(listFeaturesConstruccion)
       
        symbol_cons = QgsFillSymbol.createSimple({'color':'#ffffff', 
                                              'color_border':'#B22B1B',
                                              'width_border':'0.5',
                                              "outline_style": "dashed",})

        layer_construcciones.renderer().setSymbol(symbol_cons)

 
        layer_construcciones.triggerRepaint()         
  

        
        
        layer_settings_cod_cons  = QgsPalLayerSettings()
        text_format_cod_cons = QgsTextFormat()

        text_format_cod_cons.setFont(QFont("Arial", 8))
        text_format_cod_cons.setSize(10)

        buffer_settings_cod_cons = QgsTextBufferSettings()
        buffer_settings_cod_cons.setEnabled(True)
        buffer_settings_cod_cons.setSize(0.10)
        # layer_settings_superficie.setColor(QColor("blue"))
        
        text_format_cod_cons.setBuffer(buffer_settings_superficie)
        layer_settings_cod_cons.setFormat(text_format_superficie)

        layer_settings_cod_cons.fieldName = "cod"
        # layer_settings_cod_cons.placement = 0
        layer_settings_cod_cons.centroidInside = True

        
        layer_settings_cod_cons.enabled = True

        layer_settings_cod_cons = QgsVectorLayerSimpleLabeling(layer_settings_cod_cons)
        layer_construcciones.setLabelsEnabled(True)
        layer_construcciones.setLabeling(layer_settings_cod_cons)
        layer_construcciones.triggerRepaint()
        
        
        
        
        
        
        urlTodosTerrenos19 = "http://192.168.0.150:8080/apiCatastro/terrenos19/"
        response_todos_terrenos19 = requests.get(urlTodosTerrenos19)
        
        if response_todos_terrenos19.status_code == 200:
            response_json_todos_terrenos19 = response_todos_terrenos19.json()
            
        layer_todos_terrenos19 = QgsVectorLayer("Polygon?crs=EPSG:32719","terreno","memory")
        layer_todos_terrenos19_provider = layer_todos_terrenos19.dataProvider()
        
        campo_codigo = QgsField("codigo",QVariant.String)
        campo_nombre = QgsField("nombre",QVariant.String)

        todos_terrenos19_fields = [campo_codigo, campo_nombre]
        
        layer_todos_terrenos19_provider.addAttributes(todos_terrenos19_fields)
        layer_todos_terrenos19.updateFields()
        
        arrayCoordenadasTodosTerrenoGeometria = []
        listFeaturesTodosTerrenos = []
        
        for response_json_todos_terrenos19_item in response_json_todos_terrenos19:
        
            if response_json_todos_terrenos19_item["codigo"] != response_json_terreno["codigo"]:
            
                feature_todos_terrenos19 = QgsFeature()
                feature_todos_terrenos19.setFields(layer_todos_terrenos19.fields())
                
                
                feature_todos_terrenos19.setAttribute("codigo", response_json_todos_terrenos19_item["codigo"])
                
                if response_json_todos_terrenos19_item["titularBean"]:
                    feature_todos_terrenos19.setAttribute("nombre", response_json_todos_terrenos19_item["titularBean"]["nombre"] + " " +response_json_todos_terrenos19_item["titularBean"]["apellidos"])
       
                
                arrayCoordenadasTodosTerrenos = response_json_todos_terrenos19_item["geom"]["coordinates"]
                
                for coordenadasTodosTerrenos in arrayCoordenadasTodosTerrenos:             
                    for coordTodTerrenos in coordenadasTodosTerrenos:                
                        for k in coordTodTerrenos:
                            arrayCoordenadasTodosTerrenoGeometria.append(QgsPointXY(k[0],k[1]))

                todos_terrenos_geometria = QgsGeometry.fromPolygonXY([arrayCoordenadasTodosTerrenoGeometria])
                feature_todos_terrenos19.setGeometry(todos_terrenos_geometria)
                
                listFeaturesTodosTerrenos.append(feature_todos_terrenos19)
                arrayCoordenadasTodosTerrenoGeometria = []

        
        layer_todos_terrenos19.dataProvider().addFeatures(listFeaturesTodosTerrenos)
        


        symbol_todos_terrenos = QgsFillSymbol.createSimple({'color':'#ffffff', 
                                              'color_border':'#0F0290',
                                              'width_border':'0.2',
                                              'outline_style': 'dash',
                                              })

        layer_todos_terrenos19.renderer().setSymbol(symbol_todos_terrenos)
        layer_todos_terrenos19.triggerRepaint()         
  

        
        layer_settings_todos_terrenos19  = QgsPalLayerSettings()
        text_format_todos_terrenos19 = QgsTextFormat()

        text_format_todos_terrenos19.setFont(QFont("Arial", 8))
        text_format_todos_terrenos19.setSize(10)

        buffer_settings_todos_terrenos19 = QgsTextBufferSettings()
        buffer_settings_todos_terrenos19.setEnabled(True)
        buffer_settings_todos_terrenos19.setSize(0.10)
  
        
        text_format_todos_terrenos19.setBuffer(buffer_settings_superficie)
        layer_settings_todos_terrenos19.setFormat(text_format_superficie)

        layer_settings_todos_terrenos19.fieldName = "nombre"
        # layer_settings_todos_terrenos19.placement = 0
        layer_settings_todos_terrenos19.centroidInside = True

        layer_settings_todos_terrenos19.enabled = True

        layer_settings_todos_terrenos19 = QgsVectorLayerSimpleLabeling(layer_settings_todos_terrenos19)
        layer_todos_terrenos19.setLabelsEnabled(True)
        layer_todos_terrenos19.setLabeling(layer_settings_todos_terrenos19)
        layer_todos_terrenos19.triggerRepaint()
        
            


    

        urlWithParams = 'type=xyz&url=http://ecn.t3.tiles.virtualearth.net/tiles/a{q}.jpeg?g=1&zmax=19&zmin=0&crs=EPSG32719'
        rlayer = QgsRasterLayer(urlWithParams, 'Satelite', 'wms')  

        
        
        
        
        
        
       
        vertexLayer = QgsVectorLayer("POINT?crs=EPSG:32719", feature_terreno["codigo"] + '_Vertices', "memory")
    
        vertex_nombre = QgsField("nombre",QVariant.String)
        vertexLayer.dataProvider().addAttributes([vertex_nombre])
        vertexLayer.updateFields()
        
        
        geom = feature_terreno.geometry()
        ver = geom.vertexAt(0)
                
        points=[]
        pointsxy = []
        coordenadas = []
        n = 0
        
        featureVertices = QgsFeature()
        featureVertices.setFields(vertexLayer.fields())
 
  
        while(ver.isEmpty() != True):
            n +=1
            points.append(ver)
            ver=geom.vertexAt(n)
            ver_xy = QgsPointXY(ver)
            pointsxy.append(ver_xy)
            x = ver_xy.x()
            y = ver_xy.y()
            coordenadas.append(x)
            coordenadas.append(y)
            geomVertex = QgsGeometry.fromPointXY(ver_xy)
            featureVertices.setGeometry(geomVertex)
            featureVertices.setAttribute("Nombre", "V"+str(n))
            vertexLayer.dataProvider().addFeatures([featureVertices])
        


        # Añado etiqueta a la layer de vertices
        layer_settings  = QgsPalLayerSettings()
        text_format = QgsTextFormat()

        text_format.setFont(QFont("Arial", 8))
        text_format.setSize(8)

        buffer_settings = QgsTextBufferSettings()
        buffer_settings.setEnabled(True)
        buffer_settings.setSize(0.10)
        buffer_settings.setColor(QColor("black"))

        text_format.setBuffer(buffer_settings)
        layer_settings.setFormat(text_format)

        layer_settings.fieldName = "Nombre"
        #layer_settings.placement = 3
        
        layer_settings.centroidWhole = False
        layer_settings.centroidInside = True
     
        layer_settings.enabled = True

        layer_settings = QgsVectorLayerSimpleLabeling(layer_settings)
        vertexLayer.setLabelsEnabled(True)
        vertexLayer.setLabeling(layer_settings)
        vertexLayer.triggerRepaint()
        


        
        
        layerLineas = QgsVectorLayer("Linestring?crs=EPSG:32719", feature_terreno["codigo"] + '_Lineas', "memory") 
        
        layerLineas_nombre = QgsField("nombre",QVariant.String)
        layerLineas_distancia = QgsField("distancia",QVariant.String)
        layerLineas_orientacion = QgsField("orientacion",QVariant.String)
        layerLineas_vecino = QgsField("vecino",QVariant.String)
        layerLineas.dataProvider().addAttributes([layerLineas_nombre, layerLineas_distancia, layerLineas_orientacion, layerLineas_vecino])
        layerLineas.updateFields()
        
        puntos = []
        pointsxy.pop()

        for i in range(len(pointsxy) -1):
            featurelines = QgsFeature()
            
            p1 = pointsxy[i]
            p2 = pointsxy[i + 1]
            
            puntos = [p1, p2]

            geomLine = QgsGeometry.fromPolylineXY(puntos)
            featurelines.setGeometry(geomLine)
            distancia = round(geomLine.length(),2)
                        
            camposlineas = layerLineas.dataProvider().fields()
            featurelines.setFields(camposlineas)
            
            featurelines.setAttribute('nombre', str(i+1))
            featurelines.setAttribute('distancia', distancia)
            
            layerLineas.dataProvider().addFeatures([featurelines])
        
        
        p_inicio = pointsxy[0]
        p_final = pointsxy[-1]
        
        p_inicio_lista = [p_final, p_inicio]
        
        p_inicio_feature = QgsFeature()
        p_inicio_geometria = QgsGeometry.fromPolylineXY(p_inicio_lista)
        p_inicio_feature.setGeometry(p_inicio_geometria)
        
        p_inicio_distancia = round(p_inicio_geometria.length(),2)
        p_inicio_campos = layerLineas.dataProvider().fields()
        p_inicio_feature.setFields(p_inicio_campos)
        
        p_inicio_feature.setAttribute('nombre', str(len(pointsxy) + 1 ))
        p_inicio_feature.setAttribute('distancia', p_inicio_distancia)
        
        layerLineas.dataProvider().addFeatures([p_inicio_feature])

        
        featsCopiaLine = [feat for feat in layerLineas.getFeatures()]
        
        
        
        layerLineasUbicacion = QgsVectorLayer("Linestring?crs=EPSG:32719", feature_terreno["codigo"] + '_LineasUbicacion', "memory")
     
        mem_layer_data = layerLineasUbicacion.dataProvider()
        attr = layerLineas.dataProvider().fields().toList()
        mem_layer_data.addAttributes(attr)
        layerLineasUbicacion.updateFields()
        mem_layer_data.addFeatures(featsCopiaLine)
        
        n = 1
        distanciaArray = []
        
        for i in points:
            if n < len(points):
                distance = i.distance(points[n])
                n = n+1
                distanciaArray.append(distance)
            else:
                n = 0
                distance = i.distance(points[n])
                distanciaArray.append(distance)
               
        symbol_l =QgsLineSymbol.createSimple ({'color':'yellow', 'width':'0.8', 'line_style':'solid'})    
        layerLineasUbicacion.renderer().setSymbol(symbol_l)
        layerLineasUbicacion.triggerRepaint()
        
        
 
 
 
        
        # añadir etiqueta de distancias al mapa
        
        layer_settings_distance  = QgsPalLayerSettings()
        text_format_distance = QgsTextFormat()

        text_format_distance.setFont(QFont("Arial", 8))
        text_format_distance.setSize(8)

        buffer_settings_line = QgsTextBufferSettings()
        buffer_settings_line.setEnabled(True)
        buffer_settings_line.setSize(0.10)
        buffer_settings_line.setColor(QColor("blue"))
        
        text_format_distance.setBuffer(buffer_settings_line)
        layer_settings_distance.setFormat(text_format_distance)

        layer_settings_distance.fieldName = "Distancia"
        #layer_settings_distance.placement = 3
        layer_settings_distance.placementFlags = QgsPalLayerSettings.AboveLine

        
        layer_settings_distance.enabled = True

        layer_settings_distance = QgsVectorLayerSimpleLabeling(layer_settings_distance)
        layerLineas.setLabelsEnabled(True)
        layerLineas.setLabeling(layer_settings_distance)
        layerLineas.triggerRepaint()
        
   
        
    
        project = QgsProject.instance()         
        
        manager = project.layoutManager()       
        
        layout = QgsPrintLayout(project)        
        
        layoutName = "Prueba4"
        
        layouts_list = manager.printLayouts()

        for layout in layouts_list:
            if layout.name() == layoutName:
                manager.removeLayout(layout)
                
        
        layout = QgsPrintLayout(project)
        
        layout.initializeDefaults()                 
        
        layout.setName(layoutName)
        
        manager.addLayout(layout)
        
        

        tmpfile = self.plugin_dir + "/riberaltalayout2.qpt"
   

        with open(tmpfile) as f:
            template_content = f.read()
        
        doc = QDomDocument()
        doc.setContent(template_content)
        
        

        items, ok = layout.loadFromTemplate(doc, QgsReadWriteContext(), False)
        
 
        
        items[0].setText(str(feature_terreno["nombre"]) + " " + str(feature_terreno["apellidos"]))
        items[1].setText(str(feature_terreno["documento"]))
        
        suptest2 = 0
        
        # if feature_terreno["suptest"] == "":
            # suptest2 = 0
        # else:
        
            # suptest = float(feature_terreno["suptest"])
            # suptest2 = round(suptest, 2)
        
        resta = suptest2 - float(feature_terreno["superficie"])
        resta2 = round(resta,2)
        
        sup = 0
        if feature_terreno["superficie"]:
            sup = feature_terreno["superficie"]
        sup2 = round(sup, 2)
        
        items[2].setText(str(resta2))
        items[3].setText(str(sup2))
        items[4].setText(str(suptest2))
        
   
        items[5].setText("La Pampa")
        items[6].setText("Municipio de Reyes")
        items[7].setText(str(feature_terreno["barrio"]))
        items[8].setText(str(feature_terreno["direccion"]))
        items[9].setText(str(feature_terreno["subpredio"]))
        items[10].setText(str(feature_terreno["predio"]))
        items[11].setText(str(feature_terreno["manzano"]))
 
       
        
        sup_total = sup + resta
        items[17].setText(str(sup_total))
        
        items[23].setText(str(round(coordenadas[0],3)))
        items[24].setText(str(round(coordenadas[1],3)))
        
        items[25].setText(str(round(coordenadas[2],3)))
        items[26].setText(str(round(coordenadas[3],3)))
        
        items[27].setText(str(round(coordenadas[4],3)))
        items[28].setText(str(round(coordenadas[5],3)))
        
        items[29].setText(str(round(coordenadas[6],3)))
        items[30].setText(str(round(coordenadas[7],3)))
        
        items[31].setText(str(round(coordenadas[8],3)))
        items[32].setText(str(round(coordenadas[9],3)))
        
        items[33].setText(str(feature_terreno["codigo"]))
        items[34].setText(str(feature_terreno["base"]))
        
        now = datetime.now()
        
        items[35].setText("{}/{}/{}".format(now.day, now.month, now.year))

  
        items[36].setText("19")
            
        

      
        
        project = QgsProject.instance()
 
        mapas = []

        for i in items: 
            if i.type() == 65639:
                mapas.append(i)
                       
        mapa1 = mapas[0]
        mapa2 = mapas[1]
        
        nombre = ""
        
        for id, layer in project.mapLayers().items():
            if layer.name() == "Satelite":
                nombre = "Satelite"
        
        if nombre == "":
            QgsProject.instance().addMapLayer(rlayer)
        
        QgsProject.instance().addMapLayer(layerLineasUbicacion)        
        QgsProject.instance().addMapLayer(vertexLayer)
        QgsProject.instance().addMapLayer(layer_terreno)
        QgsProject.instance().addMapLayer(layerLineas)
        QgsProject.instance().addMapLayer(layer_todos_terrenos19)

 
        # if feature_construccion != []: 
        QgsProject.instance().addMapLayer(layer_construcciones)
       
        
        map_settings = iface.mapCanvas().mapSettings() 
        
                
        mapa1.setRect(20, 20, 20, 20)
        
        ms1 = QgsMapSettings()
        ms1.setLayers([layer_terreno])
        
        # if feature_construccion != []: 
            # mapa1.setLayers([layerConstruccion, vertexLayer, layer, layerLineas])
        # else:
        mapa1.setLayers([layer_construcciones,layer_terreno,layer_todos_terrenos19, vertexLayer, layerLineas])
        
        rect1 = QgsRectangle(ms1.fullExtent())
        rect1.scale(2.2)
        ms1.setExtent(rect1)
        mapa1.setExtent(rect1)
        mapa1.setBackgroundColor(QColor(255, 0, 0, 0))
                
        mapa1.attemptResize(QgsLayoutSize(207, 144, QgsUnitTypes.LayoutMillimeters))
        
 
        
        mapa2.setRect(20, 20, 20, 20) 
        ms2 = QgsMapSettings()
        ms2.setLayers([layer_terreno])
        mapa2.setLayers([layerLineasUbicacion, rlayer])
        
        rect2 = QgsRectangle(ms2.fullExtent())
        rect2.scale(1.8)
        ms2.setExtent(rect2)
        mapa2.setExtent(rect2)
        
        
        mapa2.attemptResize(QgsLayoutSize(73, 62, QgsUnitTypes.LayoutMillimeters))


        iface.openLayoutDesigner(layout)
        exporter = QgsLayoutExporter(layout)    
        exporter.exportToPdf(self.plugin_dir + "/Layout.pdf", QgsLayoutExporter.PdfExportSettings()) 
        
        
        # QgsProject.instance().removeMapLayer(layerLineasUbicacion)        
        # QgsProject.instance().removeMapLayer(vertexLayer)
        # QgsProject.instance().removeMapLayer(layer_terreno)
        # QgsProject.instance().removeMapLayer(layerLineas)
        # QgsProject.instance().removeMapLayer(layer_todos_terrenos19)
     
                        
        
       ############################################################################################################################################
    ############################################################QUINTO BOTON PRIMER CERTIFICADO##########################################################
    ############################################################################################################################################ 
    
    
    lista_terreno_informe = ""
    
    def cargar_tablabbdd2(self):
    
            
        urlTerrenos19 = "http://192.168.0.150:8080/apiCatastro/terrenos19"       
                
        response = requests.get(urlTerrenos19)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_informe.list_bbdd
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:
            if item["titularBean"]:
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"])  + "   " + str(item["titularBean"]["nombre"]))
            else:
                lista.append(str(item["codigo"]))
       
        list_widget.addItems(lista)
        
        self.lista_terreno_informe = response_json
        
       
          
    
    def listar_layer_informe_busca_ref(self):
        
        list_widget = self.dlg_informe.list_bbdd
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_terreno_informe_busca_ref.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
        lista = []
              
        for item in self.lista_terreno_informe:      
            if valor_busqueda == str(item["codigo"]):
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"]))

        list_widget.addItems(lista)
        
            
    
    def listar_layer_informe_busca_nombre(self):
    
        list_widget = self.dlg_informe.list_bbdd
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_terreno_informe_busca_nombre.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
        lista = []
              
        for item in self.lista_terreno_informe: 
        
            nombreyapellidos = str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"])
        
            if valor_busqueda in nombreyapellidos:
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"]))

        list_widget.addItems(lista)
        
        
         
        
        
    def mostrar_informe(self):
    
    
    
        QgsProject.instance().removeAllMapLayers()
        
        list_widget = self.dlg_informe.list_bbdd
        
        current = list_widget.currentItem()
        
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name = current.text()
        list_widget_name_ref = ""
        
        for asa in range(len(list_widget_name)):
            if list_widget_name[asa] == " ":
                ran = asa
                break
        
        
        list_widget_name_ref = list_widget_name[0:ran]
        
        
        
        
        urlTerreno19 = "http://192.168.0.150:8080/apiCatastro/terrenos19/" + list_widget_name_ref
        
        response_terreno = requests.get(urlTerreno19)
        
        
        if response_terreno.status_code == 200:
            response_json_terreno = response_terreno.json()
            
                
        
        layer_terreno = QgsVectorLayer("Polygon?crs=EPSG:32719","terreno","memory")
        layer_terreno_provider = layer_terreno.dataProvider()
        
        
        campo_codigo = QgsField("codigo",QVariant.String)
        campo_direccion = QgsField("direccion",QVariant.String)
        campo_superficie = QgsField("superficie",QVariant.Double)
        
        campo_barrio = QgsField("barrio",QVariant.String)
        
        
        campo_agua = QgsField("agua", QVariant.Bool)
        campo_energia = QgsField("energia", QVariant.Bool)
        campo_alcantarillado = QgsField("alcantarillado", QVariant.Bool)
        campo_telefono = QgsField("telefono", QVariant.Bool)
        campo_internet = QgsField("internet", QVariant.Bool)
        campo_transporte = QgsField("transporte", QVariant.Bool)
        
        campo_frente = QgsField("frente",QVariant.String)
        campo_fondo = QgsField("fondo",QVariant.String)
        campo_suptest = QgsField("suptest",QVariant.String)

        campo_manzano = QgsField("manzano",QVariant.String)
        campo_predio = QgsField("predio",QVariant.String)
        campo_sub = QgsField("subpredio",QVariant.String)
        campo_base = QgsField("base",QVariant.String)
        
        campo_nombre = QgsField("nombre",QVariant.String)
        campo_apellidos = QgsField("apellidos",QVariant.String)
        campo_documento = QgsField("documento",QVariant.String)
        
        campo_tipo_doc = QgsField("tipo_doc",QVariant.String)
        campo_caracter = QgsField("caracter",QVariant.String)
        campo_documento_prop = QgsField("documento_prop",QVariant.String)
        campo_adquisicion = QgsField("adquisicion",QVariant.String)
        
        campo_tipovia = QgsField("tipovia",QVariant.String)
        campo_valorvia = QgsField("valorvia",QVariant.Double)
        
        campo_nombretopo = QgsField("nombretopo",QVariant.String)
        campo_descrtopo = QgsField("descrtopo",QVariant.String) 
        campo_valortopo = QgsField("valortopo",QVariant.Double)        
        
        
        
        terreno_fields = [campo_codigo,campo_direccion,campo_superficie,campo_barrio,campo_energia,campo_agua,campo_alcantarillado,campo_telefono,campo_internet,
        campo_transporte,campo_frente,campo_fondo,campo_suptest,campo_manzano,campo_predio,campo_sub,campo_base,
        campo_nombre,campo_apellidos, campo_documento,campo_tipo_doc,campo_caracter,campo_documento_prop,campo_adquisicion,campo_tipovia,campo_valorvia,campo_nombretopo,
        campo_descrtopo,campo_valortopo]
        
        
        layer_terreno_provider.addAttributes(terreno_fields)
        layer_terreno.updateFields()
        

        
        feature_terreno = QgsFeature()
        
        feature_terreno.setFields(layer_terreno.fields())
        
              
        feature_terreno.setAttribute("codigo", response_json_terreno["codigo"])
        
        feature_terreno.setAttribute("direccion", response_json_terreno["direccion"])
        feature_terreno.setAttribute("superficie", response_json_terreno["superficie"])
        feature_terreno.setAttribute("barrio", response_json_terreno["barrio"])
        
        feature_terreno.setAttribute("energia", response_json_terreno["energia"])
        feature_terreno.setAttribute("agua", response_json_terreno["agua"])
        feature_terreno.setAttribute("alcantarillado", response_json_terreno["alcantarillado"])
        feature_terreno.setAttribute("telefono", response_json_terreno["telefono"])
        feature_terreno.setAttribute("internet", response_json_terreno["internet"])
        feature_terreno.setAttribute("transporte", response_json_terreno["transporte"])
                
        feature_terreno.setAttribute("frente", response_json_terreno["frente"])
        feature_terreno.setAttribute("fondo", response_json_terreno["fondo"])
        feature_terreno.setAttribute("suptest", response_json_terreno["suptest"])
        
        feature_terreno.setAttribute("manzano", response_json_terreno["frente"])
        feature_terreno.setAttribute("predio", response_json_terreno["fondo"])
        feature_terreno.setAttribute("subpredio", response_json_terreno["suptest"])
        feature_terreno.setAttribute("base", response_json_terreno["suptest"])

        feature_terreno.setAttribute("nombre", response_json_terreno["titularBean"]["nombre"])
        feature_terreno.setAttribute("apellidos", response_json_terreno["titularBean"]["apellidos"])
        feature_terreno.setAttribute("documento", response_json_terreno["titularBean"]["documento"])        
        
        feature_terreno.setAttribute("tipo_doc", response_json_terreno["titularBean"]["tipoDocumento"]["tipo"])
        feature_terreno.setAttribute("caracter", response_json_terreno["titularBean"]["caracterTitular"]["caracter"])
        feature_terreno.setAttribute("documento_prop", response_json_terreno["titularBean"]["documentoPropiedad"]["documento"])
        feature_terreno.setAttribute("adquisicion", response_json_terreno["titularBean"]["adquisicionBean"]["adquisicion"])

        feature_terreno.setAttribute("tipovia", response_json_terreno["tipoVia"]["tipo"])
        feature_terreno.setAttribute("valorvia", response_json_terreno["tipoVia"]["valor"])
        
        feature_terreno.setAttribute("nombretopo", response_json_terreno["topografiaBean"]["nombre"])        
        feature_terreno.setAttribute("descrtopo", response_json_terreno["topografiaBean"]["descripcion"])
        feature_terreno.setAttribute("valortopo", response_json_terreno["topografiaBean"]["valor"])

       
        
        layer_terreno_provider.addFeatures([feature_terreno])
        
        
        
        print("PRIMER INFORME")
        print(list(layer_terreno.getFeatures()))

        
      
        
        
        #Creo un layout vacio
        project = QgsProject.instance()         
        manager = project.layoutManager()       
        layout = QgsPrintLayout(project)        
        layoutName = "Prueba4"
        
        layouts_list = manager.printLayouts()

        for layout in layouts_list:
            if layout.name() == layoutName:
                manager.removeLayout(layout)
                
        
        layout = QgsPrintLayout(project)
        layout.initializeDefaults()                 #create default map canvas
        layout.setName(layoutName)
        manager.addLayout(layout)
        
        # change first page orientation to portrait
        pc = layout.pageCollection()
        pc.page(0).setPageSize('A4', QgsLayoutItemPage.Orientation.Portrait)
        
        
        #Cargo un archivo de plantilla del layout
        tmpfile = self.plugin_dir + '/riberaltainforme1.qpt'
        
        
        with open(tmpfile) as f:
            template_content = f.read()
        
        doc = QDomDocument()
        doc.setContent(template_content)
        
        print(doc)
        
        # adding to existing items
        #En items se guarda una lista de los elementos del layout, Ver como hacer para ir editando estos elementos y que se muestre el layout
        items, ok = layout.loadFromTemplate(doc, QgsReadWriteContext(), False)
        
 
        
        #añado texto a las labels que quiero
        
        
        
        items[0].setText("")
        items[1].setText("")
        items[2].setText(feature_terreno["fondo"])
        items[3].setText(feature_terreno["frente"])
        
        items[4].setText(str(round(feature_terreno["superficie"],2)))
        
        items[5].setText(feature_terreno["direccion"])
        items[6].setText(feature_terreno["barrio"])
        #items[7].setText(feature["distrito"])
        items[8].setText("Municipio de Reyes")
        items[9].setText("La Pampa")
        
        
        items[10].setText(str(feature_terreno["nombre"]) + " " + str(feature_terreno["apellidos"]))
        
        now = datetime.now()
        
        items[11].setText("{}/{}/{}".format(now.day, now.month, now.year))
        items[12].setText("{}/{}/{}".format(now.day, now.month, now.year))
       
        items[13].setText(str(feature_terreno["nombre"]) + " " + str(feature_terreno["apellidos"]))
        items[14].setText(feature_terreno["predio"])
             
        
        iface.openLayoutDesigner(layout)
        
        #iface.showLayoutManager ()
        
        #this creates a QgsLayoutExporter object
        exporter = QgsLayoutExporter(layout)       

        print(exporter)

        #this exports a pdf of the layout object
        exporter.exportToPdf(self.plugin_dir + '/Informe.pdf', QgsLayoutExporter.PdfExportSettings()) 
        
     
       
    def current_date_format(date):
        months = ("Enero", "Febrero", "Marzo", "Abri", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre")
        day = date.day
        month = months[date.month - 1]
        year = date.year
        messsage = "{} de {} del {}".format(day, month, year)

        return messsage

  

       
       
       
   
   
       
       ############################################################################################################################################
    ############################################################SEXTO BOTON SEGUNDO CERTIFICADO (CATASTRAL)##########################################################
    ############################################################################################################################################ 
    
    lista_terreno_informe2 = ""
    
    def cargar_tablabbdd3(self):
        
        urlTerrenos19 = "http://192.168.0.150:8080/apiCatastro/terrenos19"       
                
        response = requests.get(urlTerrenos19)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_informe2.list_bbdd
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:
            if item["titularBean"]:
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"])  + "   " + str(item["titularBean"]["nombre"]))
            else:
                lista.append(str(item["codigo"]))
       
        list_widget.addItems(lista)
        
        self.lista_terreno_informe2 = response_json

        
    
    def listar_layer_informe3_busca_ref(self):
        
        list_widget = self.dlg_informe2.list_bbdd
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_terreno_informe2_busca_ref.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
        lista = []
              
        for item in self.lista_terreno_informe2:      
            if valor_busqueda == str(item["codigo"]):
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"]))

        list_widget.addItems(lista)
        
        
    
    
    def listar_layer_informe3_busca_nombre(self):
            
        list_widget = self.dlg_informe2.list_bbdd
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_terreno_informe2_busca_nombre.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
        lista = []
              
        for item in self.lista_terreno_informe2: 
        
            nombreyapellidos = str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"])
        
            if valor_busqueda in nombreyapellidos:
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"]))

        list_widget.addItems(lista)
        
                
        
        
        
    def mostrar_informe2(self, feature):
    
        QgsProject.instance().removeAllMapLayers()
        
        list_widget = self.dlg_informe2.list_bbdd
        
        current = list_widget.currentItem()
        
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name = current.text()
        list_widget_name_ref = ""
        
        for asa in range(len(list_widget_name)):
            if list_widget_name[asa] == " ":
                ran = asa
                break
        
        
        list_widget_name_ref = list_widget_name[0:ran]
        
        
        
        
        urlTerreno19 = "http://192.168.0.150:8080/apiCatastro/terrenos19/" + list_widget_name_ref
        
        response_terreno = requests.get(urlTerreno19)
        
        
        if response_terreno.status_code == 200:
            response_json_terreno = response_terreno.json()
            
                
        
        layer_terreno = QgsVectorLayer("Polygon?crs=EPSG:32719","terreno","memory")
        layer_terreno_provider = layer_terreno.dataProvider()
        
        
        campo_codigo = QgsField("codigo",QVariant.String)
        campo_direccion = QgsField("direccion",QVariant.String)
        campo_superficie = QgsField("superficie",QVariant.Double)
        
        campo_barrio = QgsField("barrio",QVariant.String)
        
        
        campo_agua = QgsField("agua", QVariant.Bool)
        campo_energia = QgsField("energia", QVariant.Bool)
        campo_alcantarillado = QgsField("alcantarillado", QVariant.Bool)
        campo_telefono = QgsField("telefono", QVariant.Bool)
        campo_internet = QgsField("internet", QVariant.Bool)
        campo_transporte = QgsField("transporte", QVariant.Bool)
        
        campo_frente = QgsField("frente",QVariant.String)
        campo_fondo = QgsField("fondo",QVariant.String)
        campo_suptest = QgsField("suptest",QVariant.String)

        campo_manzano = QgsField("manzano",QVariant.String)
        campo_predio = QgsField("predio",QVariant.String)
        campo_sub = QgsField("subpredio",QVariant.String)
        campo_base = QgsField("base",QVariant.String)
        
        campo_nombre = QgsField("nombre",QVariant.String)
        campo_apellidos = QgsField("apellidos",QVariant.String)
        campo_documento = QgsField("documento",QVariant.String)
        
        campo_tipo_doc = QgsField("tipo_doc",QVariant.String)
        campo_caracter = QgsField("caracter",QVariant.String)
        campo_documento_prop = QgsField("documento_prop",QVariant.String)
        campo_adquisicion = QgsField("adquisicion",QVariant.String)
        
        campo_tipovia = QgsField("tipovia",QVariant.String)
        campo_valorvia = QgsField("valorvia",QVariant.Double)
        
        campo_nombretopo = QgsField("nombretopo",QVariant.String)
        campo_descrtopo = QgsField("descrtopo",QVariant.String) 
        campo_valortopo = QgsField("valortopo",QVariant.Double)        
        
        campo_valorzona = QgsField("valorzona",QVariant.Double)  
        campo_valorubicacion = QgsField("valorubicacion",QVariant.Double)  
        campo_valormaterialvia = QgsField("valormaterialvia",QVariant.Double)  
        campo_valorforma = QgsField("valorforma",QVariant.Double) 
        
        terreno_fields = [campo_codigo,campo_direccion,campo_superficie,campo_barrio,campo_energia,campo_agua,campo_alcantarillado,campo_telefono,campo_internet,
        campo_transporte,campo_frente,campo_fondo,campo_suptest,campo_manzano,campo_predio,campo_sub,campo_base,
        campo_nombre,campo_apellidos, campo_documento,campo_tipo_doc,campo_caracter,campo_documento_prop,campo_adquisicion,campo_tipovia,campo_valorvia,campo_nombretopo,
        campo_descrtopo,campo_valortopo, campo_valorzona, campo_valorubicacion, campo_valormaterialvia, campo_valorforma]
        
        
        layer_terreno_provider.addAttributes(terreno_fields)
        layer_terreno.updateFields()
        

        
        feature_terreno = QgsFeature()
        
        feature_terreno.setFields(layer_terreno.fields())
        
              
        feature_terreno.setAttribute("codigo", response_json_terreno["codigo"])
        
        feature_terreno.setAttribute("direccion", response_json_terreno["direccion"])
        feature_terreno.setAttribute("superficie", response_json_terreno["superficie"])
        feature_terreno.setAttribute("barrio", response_json_terreno["barrio"])
        
        feature_terreno.setAttribute("energia", response_json_terreno["energia"])
        feature_terreno.setAttribute("agua", response_json_terreno["agua"])
        feature_terreno.setAttribute("alcantarillado", response_json_terreno["alcantarillado"])
        feature_terreno.setAttribute("telefono", response_json_terreno["telefono"])
        feature_terreno.setAttribute("internet", response_json_terreno["internet"])
        feature_terreno.setAttribute("transporte", response_json_terreno["transporte"])
                
        feature_terreno.setAttribute("frente", response_json_terreno["frente"])
        feature_terreno.setAttribute("fondo", response_json_terreno["fondo"])
        feature_terreno.setAttribute("suptest", response_json_terreno["suptest"])
        
        feature_terreno.setAttribute("manzano", response_json_terreno["frente"])
        feature_terreno.setAttribute("predio", response_json_terreno["fondo"])
        feature_terreno.setAttribute("subpredio", response_json_terreno["suptest"])
        feature_terreno.setAttribute("base", response_json_terreno["suptest"])

        feature_terreno.setAttribute("nombre", response_json_terreno["titularBean"]["nombre"])
        feature_terreno.setAttribute("apellidos", response_json_terreno["titularBean"]["apellidos"])
        feature_terreno.setAttribute("documento", response_json_terreno["titularBean"]["documento"])        
        
        feature_terreno.setAttribute("tipo_doc", response_json_terreno["titularBean"]["tipoDocumento"]["tipo"])
        feature_terreno.setAttribute("caracter", response_json_terreno["titularBean"]["caracterTitular"]["caracter"])
        feature_terreno.setAttribute("documento_prop", response_json_terreno["titularBean"]["documentoPropiedad"]["documento"])
        feature_terreno.setAttribute("adquisicion", response_json_terreno["titularBean"]["adquisicionBean"]["adquisicion"])

        feature_terreno.setAttribute("tipovia", response_json_terreno["tipoVia"]["tipo"])
        feature_terreno.setAttribute("valorvia", response_json_terreno["tipoVia"]["valor"])
        
        feature_terreno.setAttribute("nombretopo", response_json_terreno["topografiaBean"]["nombre"])        
        feature_terreno.setAttribute("descrtopo", response_json_terreno["topografiaBean"]["descripcion"])
        feature_terreno.setAttribute("valortopo", response_json_terreno["topografiaBean"]["valor"])
        
        feature_terreno.setAttribute("valorzona", response_json_terreno["zonaBean"]["valorCatastral"])
        feature_terreno.setAttribute("valorubicacion", response_json_terreno["ubicacionBean"]["valor"])
        feature_terreno.setAttribute("valormaterialvia", response_json_terreno["materialViaBean"]["valor"])
        feature_terreno.setAttribute("valorforma", response_json_terreno["formaBean"]["valor"])
  
        
        layer_terreno_provider.addFeatures([feature_terreno])        
        
        
        
        
        # if feature_cons != 0:        

            # layer_construccion = QgsVectorLayer("MULTIPOLYGON?crs=EPSG:32719", "capa", "memory")
        
            # campo_referencia_const = QgsField("codigo",QVariant.String)
            # campo_superficie_const = QgsField("superficie",QVariant.Double)
            # campo_tipo_const = QgsField("uso",QVariant.Double)

            # layer_construccion.dataProvider().addAttributes([campo_referencia_const, campo_superficie_const, campo_tipo_const])
            # layer_construccion.updateFields()
            # layer_construccion.dataProvider().addFeatures([feature_cons])
        
      
        
        
        #Creo un layout vacio
        project = QgsProject.instance()         
        manager = project.layoutManager()       
        layout = QgsPrintLayout(project)        
        layoutName = "Catastral"
        
        layouts_list = manager.printLayouts()

        for layout in layouts_list:
            if layout.name() == layoutName:
                manager.removeLayout(layout)
                
        
        layout = QgsPrintLayout(project)
        layout.initializeDefaults()                 #create default map canvas
        layout.setName(layoutName)
        manager.addLayout(layout)
        
        # change first page orientation to portrait
        pc = layout.pageCollection()
        pc.page(0).setPageSize('A4', QgsLayoutItemPage.Orientation.Portrait)
        
        
        #Cargo un archivo de plantilla del layout
        tmpfile = self.plugin_dir + '/riberaltacatastral.qpt'
        
        
        with open(tmpfile) as f:
            template_content = f.read()
        
        doc = QDomDocument()
        doc.setContent(template_content)
        
        print(doc)
        
        # adding to existing items
        #En items se guarda una lista de los elementos del layout, Ver como hacer para ir editando estos elementos y que se muestre el layout
        items, ok = layout.loadFromTemplate(doc, QgsReadWriteContext(), False)
        
 
        
        #añado texto a las labels que quiero
        
        items[0].setText(str(feature_terreno["nombre"]) + " " + str(feature_terreno["apellidos"]))
        items[1].setText("La Pampa")
        items[2].setText("Municipio de Reyes")
        items[3].setText("Distrito")
        items[4].setText(feature_terreno["barrio"])
        items[5].setText(feature_terreno["direccion"])
        
        items[6].setText(feature_terreno["manzano"])
        items[7].setText(feature_terreno["predio"])
        items[8].setText(feature_terreno["subpredio"])
        
        items[9].setText(str(round(feature_terreno["superficie"],2)))
        
        items[10].setText("")
        items[11].setText("")
        items[12].setText("")
        items[13].setText("")
        
        now = datetime.now()
        items[14].setText("{}/{}/{}".format(now.day, now.month, now.year))
        
        coeficiente_servicios = 1
        
        if feature_terreno["energia"] == True:
            items[15].setText("Si")   
        else:
            items[15].setText(" - ")
            coeficiente_servicios = coeficiente_servicios - 0.1
        
        if feature_terreno["agua"] == True:
            items[16].setText("Si")    
        else:
            items[16].setText(" - ")
            coeficiente_servicios = coeficiente_servicios - 0.15
            
        if feature_terreno["telefono"] == True:
            items[17].setText("Si")
        else:
            items[17].setText(" - ")
            coeficiente_servicios = coeficiente_servicios - 0.05
  
        if feature_terreno["alcantarillado"] == True:
            items[18].setText("Si")  
        else:
            items[18].setText(" - ")
            coeficiente_servicios = coeficiente_servicios - 0.1
            
        if feature_terreno["transporte"] == False:
            coeficiente_servicios = coeficiente_servicios - 0.1
        
            
        
        items[20].setText(str(round(feature_terreno["superficie"],2)))
        
        items[21].setText(feature_terreno["suptest"])
        
        
        items[19].setText(" - ")
        items[22].setText(" - ")
        items[23].setText(" - ")
        
        # if feature_cons != 0: 
            # items[19].setText(str(feature_cons["nombreuso"]))
            # items[22].setText(str(round(feature_cons["superficie"],2)))
            # items[23].setText(str(feature_cons["anyo"]))
        # else:
            # items[19].setText(" - ")
            # items[22].setText(" - ")
            # items[23].setText(" - ")
            
        
        kfrentefondo = float(feature_terreno["frente"]) / float(feature_terreno["fondo"])
        
        

        
        # if feature_terreno["formaBean"]["valor"] == null:        
        items[24].setText(str(round(feature_terreno["valorzona"] * feature_terreno["superficie"] * coeficiente_servicios * 
        feature_terreno["valorubicacion"] * feature_terreno["valortopo"] * feature_terreno["valormaterialvia"] * 
        kfrentefondo,2)))

        # else:
            # items[24].setText(str(round(feature_terreno["zonaBean"]["valorCatastral"] * round(feature_terreno["superficie"],2) * coeficiente_servicios * 
            # feature_terreno["ubicacionBean"]["valor"] * feature_terreno["topografiaBean"]["valor"] * feature_terreno["materialViaBean"]["valor"] * 
            # kfrentefondo * feature_terreno["valorforma"],2)))
       
             
        
        iface.openLayoutDesigner(layout)
        
        #iface.showLayoutManager ()
        
        #this creates a QgsLayoutExporter object
        exporter = QgsLayoutExporter(layout)       

        print(exporter)

        #this exports a pdf of the layout object
        exporter.exportToPdf(self.plugin_dir + '/CertificadoCatastral.pdf', QgsLayoutExporter.PdfExportSettings()) 
     
    
    
    
    
    ############################################################################################################################################
    ############################################################SEPTIMO BOTON TERCER CERTIFICADO (AVALUO)##########################################################
    ############################################################################################################################################ 
    
    
    lista_terreno_informe3 = ""
    list_widget_name_terreno = ""
    
    def cargar_tablabbdd4(self):
    
        urlTerrenos19 = "http://192.168.0.150:8080/apiCatastro/terrenos19"       
                
        response = requests.get(urlTerrenos19)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_informe3.list_bbdd
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:
            if item["titularBean"]:
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"])  + "   " + str(item["titularBean"]["nombre"]))
            else:
                lista.append(str(item["codigo"]))
       
        list_widget.addItems(lista)
        
        self.lista_terreno_informe3 = response_json
        

        
                
        
    
    def listar_layer_informe4_busca_ref(self):
        
        list_widget = self.dlg_informe3.list_bbdd
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_terreno_informe3_busca_ref.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
        lista = []
              
        for item in self.lista_terreno_informe3:      
            if valor_busqueda == str(item["codigo"]):
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"]))

        list_widget.addItems(lista)
        

        
        
    
    
    def listar_layer_informe4_busca_nombre(self):
    
        list_widget = self.dlg_informe3.list_bbdd
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_terreno_informe3_busca_nombre.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
        lista = []
              
        for item in self.lista_terreno_informe3: 
        
            nombreyapellidos = str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"])
        
            if valor_busqueda in nombreyapellidos:
                lista.append(str(item["codigo"]) + "   " + str(item["titularBean"]["nombre"]) + " " + str(item["titularBean"]["apellidos"]))

        list_widget.addItems(lista)
        
                
        
            
    
    def cargar_construccion(self):
    
        list_widget = self.dlg_informe3.list_bbdd
    
        current = list_widget.currentItem()
        
        list_widget_name_terreno = current.text()
    
        
        
        list_widget_name_ref = ""
        
        for asa in range(len(list_widget_name_terreno)):
            if list_widget_name_terreno[asa] == " ":
                ran = asa
                break
        
        list_widget_name_ref = list_widget_name_terreno[0:ran]  
                
        
        
        list_widget_const = self.dlg_listar_construccion.list_bbdd
 
        for i in range(list_widget_const.count()):
           
            list_widget_const.takeItem(0)
 
        
        urlConstrucciones19 = "http://192.168.0.150:8080/apiCatastro/construcciones19"       
                
        response = requests.get(urlConstrucciones19)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
        

        lista = []
        
       
        for feature_contruccion in response_json:
            if feature_contruccion["terrenos19"]["codigo"] == list_widget_name_ref:
                lista.append(str(feature_contruccion["terrenos19"]["codigo"]) + "   " + str(feature_contruccion["cod"]) + "   " + str(feature_contruccion["conservacionBean"]["estado"])
                + "   " + str(feature_contruccion["revestimientoBean"]["revestimiento"]))

        list_widget_const.addItems(lista)
        

        
        
    def mostrar_informe3(self, feature):
    
        QgsProject.instance().removeAllMapLayers()
    
        list_widget = self.dlg_informe3.list_bbdd
        
        current = list_widget.currentItem()
        
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name = current.text()
        
        list_widget_name_ref = ""
        
        for asa in range(len(list_widget_name)):
            if list_widget_name[asa] == " ":
                ran = asa
                break
        
        
        list_widget_name_ref = list_widget_name[0:ran]
        
        #guardo las features del layer creado de la bbdd
        # features = self.layercargado.getFeatures()
        
        # features_construccion = self.construccioncargado.getFeatures()
        
        # features_plantas = self.plantascargado.getFeatures()
        
        # features_plan = []
        
      
        # Obtengo la feature del mismo nombre que el QListWidgetItem
        # for f in features:
            # if list_widget_name_ref == f["codigo"]:
                # feature = f
                
        # for g in features_construccion:
            # if list_widget_name_ref == g["codigo"]:
                # feature_cons = g
                
        # print("COMOOO")
        # print(feature_cons)
        # print(list(features_plantas))
        # print(feature_cons["id"])
        
        # feature_baja = None
        # feature_primer = None
        # feature_segundo = None
        # feature_tercer = None
        # feature_cuarto = None
        # feature_quinto = None
        # feature_sexto = None
        # feature_septimo = None
        
        
        # for h in features_plantas:
            # if feature_cons["id"] == h["id_construccion"] and h["id_planta"] == 1:
                # feature_baja = h
            # if feature_cons["id"] == h["id_construccion"] and h["id_planta"] == 2:
                # feature_primer = h
            # if feature_cons["id"] == h["id_construccion"] and h["id_planta"] == 3:
                # feature_segundo = h
            # if feature_cons["id"] == h["id_construccion"] and h["id_planta"] == 4:
                # feature_tercer = h
            # if feature_cons["id"] == h["id_construccion"] and h["id_planta"] == 5:
                # feature_cuarto = h
            # if feature_cons["id"] == h["id_construccion"] and h["id_planta"] == 6:
                # feature_quinto = h
            # if feature_cons["id"] == h["id_construccion"] and h["id_planta"] == 7:
                # feature_sexto = h
            # if feature_cons["id"] == h["id_construccion"] and h["id_planta"] == 8:
                # feature_septimo = h
        
        
        # print(list(features_plan))
                


                
        
        
        urlTerreno19 = "http://192.168.0.150:8080/apiCatastro/terrenos19/" + list_widget_name_ref
        
        response_terreno = requests.get(urlTerreno19)
        
        
        if response_terreno.status_code == 200:
            response_json_terreno = response_terreno.json()
            
                
        
        layer_terreno = QgsVectorLayer("Polygon?crs=EPSG:32719","terreno","memory")
        layer_terreno_provider = layer_terreno.dataProvider()
        
        
        campo_codigo = QgsField("codigo",QVariant.String)
        campo_direccion = QgsField("direccion",QVariant.String)
        campo_superficie = QgsField("superficie",QVariant.Double)
        
        campo_barrio = QgsField("barrio",QVariant.String)
        
        
        campo_agua = QgsField("agua", QVariant.Bool)
        campo_energia = QgsField("energia", QVariant.Bool)
        campo_alcantarillado = QgsField("alcantarillado", QVariant.Bool)
        campo_telefono = QgsField("telefono", QVariant.Bool)
        campo_internet = QgsField("internet", QVariant.Bool)
        campo_transporte = QgsField("transporte", QVariant.Bool)
        
        campo_frente = QgsField("frente",QVariant.String)
        campo_fondo = QgsField("fondo",QVariant.String)
        campo_suptest = QgsField("suptest",QVariant.String)

        campo_manzano = QgsField("manzano",QVariant.String)
        campo_predio = QgsField("predio",QVariant.String)
        campo_sub = QgsField("subpredio",QVariant.String)
        campo_base = QgsField("base",QVariant.String)
        
        campo_nombre = QgsField("nombre",QVariant.String)
        campo_apellidos = QgsField("apellidos",QVariant.String)
        campo_documento = QgsField("documento",QVariant.String)
        
        campo_tipo_doc = QgsField("tipo_doc",QVariant.String)
        campo_caracter = QgsField("caracter",QVariant.String)
        campo_documento_prop = QgsField("documento_prop",QVariant.String)
        campo_adquisicion = QgsField("adquisicion",QVariant.String)
        
        campo_tipovia = QgsField("tipovia",QVariant.String)
        campo_valorvia = QgsField("valorvia",QVariant.Double)
        
        campo_nombretopo = QgsField("nombretopo",QVariant.String)
        campo_descrtopo = QgsField("descrtopo",QVariant.String) 
        campo_valortopo = QgsField("valortopo",QVariant.Double)        
        
        campo_valorzona = QgsField("valorzona",QVariant.Double)  
        campo_valorubicacion = QgsField("valorubicacion",QVariant.Double)  
        campo_valormaterialvia = QgsField("valormaterialvia",QVariant.Double)
        campo_valorforma = QgsField("valorforma",QVariant.Double)                 
        
        terreno_fields = [campo_codigo,campo_direccion,campo_superficie,campo_barrio,campo_energia,campo_agua,campo_alcantarillado,campo_telefono,campo_internet,
        campo_transporte,campo_frente,campo_fondo,campo_suptest,campo_manzano,campo_predio,campo_sub,campo_base,
        campo_nombre,campo_apellidos, campo_documento,campo_tipo_doc,campo_caracter,campo_documento_prop,campo_adquisicion,campo_tipovia,campo_valorvia,campo_nombretopo,
        campo_descrtopo,campo_valortopo, campo_valorzona, campo_valorubicacion, campo_valormaterialvia, campo_valorforma]
        
        
        layer_terreno_provider.addAttributes(terreno_fields)
        layer_terreno.updateFields()
        

        
        feature_terreno = QgsFeature()
        
        feature_terreno.setFields(layer_terreno.fields())
        
              
        feature_terreno.setAttribute("codigo", response_json_terreno["codigo"])
        
        feature_terreno.setAttribute("direccion", response_json_terreno["direccion"])
        feature_terreno.setAttribute("superficie", response_json_terreno["superficie"])
        feature_terreno.setAttribute("barrio", response_json_terreno["barrio"])
        
        feature_terreno.setAttribute("energia", response_json_terreno["energia"])
        feature_terreno.setAttribute("agua", response_json_terreno["agua"])
        feature_terreno.setAttribute("alcantarillado", response_json_terreno["alcantarillado"])
        feature_terreno.setAttribute("telefono", response_json_terreno["telefono"])
        feature_terreno.setAttribute("internet", response_json_terreno["internet"])
        feature_terreno.setAttribute("transporte", response_json_terreno["transporte"])
                
        feature_terreno.setAttribute("frente", response_json_terreno["frente"])
        feature_terreno.setAttribute("fondo", response_json_terreno["fondo"])
        feature_terreno.setAttribute("suptest", response_json_terreno["suptest"])
        
        feature_terreno.setAttribute("manzano", response_json_terreno["frente"])
        feature_terreno.setAttribute("predio", response_json_terreno["fondo"])
        feature_terreno.setAttribute("subpredio", response_json_terreno["suptest"])
        feature_terreno.setAttribute("base", response_json_terreno["suptest"])

        feature_terreno.setAttribute("nombre", response_json_terreno["titularBean"]["nombre"])
        feature_terreno.setAttribute("apellidos", response_json_terreno["titularBean"]["apellidos"])
        feature_terreno.setAttribute("documento", response_json_terreno["titularBean"]["documento"])        
        
        feature_terreno.setAttribute("tipo_doc", response_json_terreno["titularBean"]["tipoDocumento"]["tipo"])
        feature_terreno.setAttribute("caracter", response_json_terreno["titularBean"]["caracterTitular"]["caracter"])
        feature_terreno.setAttribute("documento_prop", response_json_terreno["titularBean"]["documentoPropiedad"]["documento"])
        feature_terreno.setAttribute("adquisicion", response_json_terreno["titularBean"]["adquisicionBean"]["adquisicion"])

        feature_terreno.setAttribute("tipovia", response_json_terreno["tipoVia"]["tipo"])
        feature_terreno.setAttribute("valorvia", response_json_terreno["tipoVia"]["valor"])
        
        feature_terreno.setAttribute("nombretopo", response_json_terreno["topografiaBean"]["nombre"])        
        feature_terreno.setAttribute("descrtopo", response_json_terreno["topografiaBean"]["descripcion"])
        feature_terreno.setAttribute("valortopo", response_json_terreno["topografiaBean"]["valor"])
        
        feature_terreno.setAttribute("valorzona", response_json_terreno["zonaBean"]["valorCatastral"])
        feature_terreno.setAttribute("valorubicacion", response_json_terreno["ubicacionBean"]["valor"])
        feature_terreno.setAttribute("valormaterialvia", response_json_terreno["materialViaBean"]["valor"])
        feature_terreno.setAttribute("valorforma", response_json_terreno["formaBean"]["valor"])
        
        
        layer_terreno_provider.addFeatures([feature_terreno]) 
        
        
        
        
        
        urlConstrucciones19 = "http://192.168.0.150:8080/apiCatastro/construcciones19"
        
        response_construcciones = requests.get(urlConstrucciones19)
                
        if response_construcciones.status_code == 200:
            response_json_construcciones = response_construcciones.json()
                
        jsonConstruccionesArray = []
        
        for itemConstruccion in response_json_construcciones:          
                
            if itemConstruccion["terrenos19"] and itemConstruccion["terrenos19"]["codigo"] == response_json_terreno["codigo"]:
         
                jsonConstruccionesArray.append(itemConstruccion);
        
        
        layer_construcciones = QgsVectorLayer("MultiPolygon?crs=32719","construcciones","memory")
        
        campo_id = QgsField("id",QVariant.Int)
        campo_cod = QgsField("cod",QVariant.Int)
        campo_aire = QgsField("aire",QVariant.Bool)
        campo_anyo = QgsField("anyo",QVariant.String)
        campo_ascensores = QgsField("ascensores",QVariant.Bool)
        campo_superfice = QgsField("superficie",QVariant.Double)
        campo_conservacionEstado = QgsField("conservacionestado",QVariant.String)
        campo_conservacionValor = QgsField("conservacionvalor",QVariant.Double)
        campo_revestimiento = QgsField("revestimiento",QVariant.String)
        campo_usoNombre  = QgsField("usonombre",QVariant.String)
        campo_usoValor  = QgsField("usovalor",QVariant.Double)
        
          
        construccion_fields = [campo_id, campo_cod, campo_aire, campo_anyo, campo_ascensores, campo_superfice, campo_conservacionEstado, campo_conservacionValor, campo_revestimiento,
        campo_usoNombre, campo_usoValor]
           
        layer_construcciones.dataProvider().addAttributes(construccion_fields)
        layer_construcciones.updateFields()
        
        
        arrayCoordenadasConstruccionGeometria = []
        listFeaturesConstruccion = []
        
        for jsonConstruccionArrayItem in jsonConstruccionesArray:
        
            feature_construccion = QgsFeature()
            feature_construccion.setFields(layer_construcciones.fields())
            
            
            feature_construccion.setAttribute("id", jsonConstruccionArrayItem["id"])
            feature_construccion.setAttribute("cod", jsonConstruccionArrayItem["cod"])
            feature_construccion.setAttribute("aire", jsonConstruccionArrayItem["aire"])
            feature_construccion.setAttribute("anyo", jsonConstruccionArrayItem["anyo"])
            feature_construccion.setAttribute("ascensores", jsonConstruccionArrayItem["ascensores"])
            feature_construccion.setAttribute("superficie", jsonConstruccionArrayItem["superficie"])
            feature_construccion.setAttribute("conservacionestado", jsonConstruccionArrayItem["conservacionBean"]["estado"])
            feature_construccion.setAttribute("conservacionvalor", jsonConstruccionArrayItem["conservacionBean"]["valor"])
            feature_construccion.setAttribute("revestimiento", jsonConstruccionArrayItem["revestimientoBean"]["revestimiento"])
            feature_construccion.setAttribute("usonombre", jsonConstruccionArrayItem["usoBean"]["uso"])
            feature_construccion.setAttribute("usovalor", jsonConstruccionArrayItem["usoBean"]["valor"])
            
        
        layer_construcciones.dataProvider().addFeatures(listFeaturesConstruccion)
        
        
 
        
        
        
        #Creo un layout vacio
        project = QgsProject.instance()         
        manager = project.layoutManager()       
        layout = QgsPrintLayout(project)        
        layoutName = "Avaluo"
        
        layouts_list = manager.printLayouts()

        for layout in layouts_list:
            if layout.name() == layoutName:
                manager.removeLayout(layout)
                
        
        layout = QgsPrintLayout(project)
        layout.initializeDefaults()                 #create default map canvas
        layout.setName(layoutName)
        manager.addLayout(layout)
        
        # change first page orientation to portrait
        pc = layout.pageCollection()
        pc.page(0).setPageSize('A4', QgsLayoutItemPage.Orientation.Portrait)
        
        
        #Cargo un archivo de plantilla del layout
        tmpfile = self.plugin_dir + '/riberaltaavaluo.qpt'
        
        
        with open(tmpfile) as f:
            template_content = f.read()
        
        doc = QDomDocument()
        doc.setContent(template_content)
        
        print(doc)
        
        # adding to existing items
        #En items se guarda una lista de los elementos del layout, Ver como hacer para ir editando estos elementos y que se muestre el layout
        items, ok = layout.loadFromTemplate(doc, QgsReadWriteContext(), False)
        
 
        
        #añado texto a las labels que quiero
        
        items[0].setText(str(feature_terreno["apellidos"]) + " " + str(feature_terreno["nombre"]))
        items[1].setText(feature_terreno["direccion"])
        items[2].setText(feature_terreno["barrio"])
        
        items[3].setText(feature_terreno["codigo"])
        
        items[4].setText(str(round(feature_terreno["superficie"],2)))
        
        coeficiente_servicios = 1
        
        if feature_terreno["energia"] == True:
            items[5].setText("Si")
        else:
            coeficiente_servicios = coeficiente_servicios - 0.2
            items[5].setText(" - ")
        
        
        if feature_terreno["agua"] == True:
            items[6].setText("Si")    
        else:
            coeficiente_servicios = coeficiente_servicios - 0.2
            items[6].setText(" - ")
        
        
        if feature_terreno["alcantarillado"] == True:
            items[7].setText("Si")
        else:
            coeficiente_servicios = coeficiente_servicios - 0.2
            items[7].setText(" - ")
    
    
        if feature_terreno["telefono"] == True:
            items[8].setText("Si")
        else:
            coeficiente_servicios = coeficiente_servicios - 0.2
            items[8].setText(" - ")
            
        if feature_terreno["transporte"] == False:
            coeficiente_servicios = coeficiente_servicios - 0.2
             
        
        items[9].setText("")
        items[10].setText("")
        items[11].setText("")
        items[12].setText("")
        
        
        items[13].setText(str(feature_terreno["tipovia"]))
        items[14].setText(str(feature_terreno["nombretopo"]))
        
        
        now = datetime.now()
        items[15].setText("{}/{}/{}".format(now.day, now.month, now.year))
        
        # if feature_baja is not None:
            # if feature_baja["cimiento"] != NULL:
                # items[16].setText(str(feature_baja["cimiento"]))
            # else:
                # items[16].setText(" - ")
        
            # if feature_baja["estructura"] != NULL:        
                # items[17].setText(str(feature_baja["estr"]))
            # else:
                # items[17].setText(" - ")
            
            # if feature_baja["cubierta"] != NULL:          
                # items[18].setText(str(feature_baja["cubierta"]))
            # else:
                # items[18].setText(" - ") 
                
            # if feature_baja["pisos"] != NULL:          
                # items[19].setText(str(feature_baja["pisos"]))
            # else:
                # items[19].setText(" - ") 
        
        # else:
            # items[16].setText(" - ")
            # items[17].setText(" - ")
            # items[18].setText(" - ")
            # items[19].setText(" - ")

            
        items[20].setText(str(round(feature_construccion["superficie"],2)))
        
        items[25].setText(str(2022 - int(feature_construccion["anyo"])))
        
        # items[30].setText(str(feature_cons["tipoconstruccion"]))
        
        # if feature_primer is not None:
            # items[21].setText(str(round(feature_cons["superficie"],2)))
            # items[26].setText(str(feature_cons["anyo"]))
            # items[31].setText(str(feature_cons["tipoconstruccion"]))
            # items[39].setText(str(round(feature["valorcatastralzona"] * coeficiente_servicios * feature["valorubicacion"] * feature["valortopo"] * feature["valormaterialvial"],2)))
            # items[43].setText(str(round(feature["valorcatastralzona"] * round(feature["superficie"],2) * coeficiente_servicios * feature["valorubicacion"] * feature["valortopo"],2))) 


        # else:
            # items[21].setText(" - ")
            # items[26].setText(" - ")
            # items[31].setText(" - ")
            # items[39].setText(" - ")
            # items[43].setText(" - ")      
             
        # if feature_segundo is not None:
            # items[22].setText(str(round(feature_cons["superficie"],2)))
            # items[27].setText(str(feature_cons["anyo"]))
            # items[32].setText(str(feature_cons["tipoconstruccion"]))
            # items[40].setText(str(round(feature["valorcatastralzona"] * coeficiente_servicios * feature["valorubicacion"] * feature["valortopo"] * feature["valormaterialvial"],2)))
            # items[44].setText(str(round(feature["valorcatastralzona"] * round(feature["superficie"],2) * coeficiente_servicios * feature["valorubicacion"] * feature["valortopo"],2))) 

        # else:
            # items[22].setText(" - ")
            # items[27].setText(" - ")
            # items[32].setText(" - ")
            # items[40].setText(" - ")
            # items[44].setText(" - ")
        
        # if feature_tercer is not None:
            # items[23].setText(str(round(feature_cons["superficie"],2)))
            # items[28].setText(str(feature_cons["anyo"]))
            # items[33].setText(str(feature_cons["tipoconstruccion"]))
            # items[41].setText(str(round(feature["valorcatastralzona"] * coeficiente_servicios * feature["valorubicacion"] * feature["valortopo"] * feature["valormaterialvial"],2)))
            # items[45].setText(str(round(feature["valorcatastralzona"] * round(feature["superficie"],2) * coeficiente_servicios * feature["valorubicacion"] * feature["valortopo"],2))) 

        # else:
            # items[23].setText(" - ")
            # items[28].setText(" - ")
            # items[33].setText(" - ")
            # items[41].setText(" - ")
            # items[45].setText(" - ")
            
        # if feature_cuarto is not None:
            # items[24].setText(str(round(feature_cons["superficie"],2)))
            # items[29].setText(str(feature_cons["anyo"]))
            # items[34].setText(str(feature_cons["tipoconstruccion"]))
            # items[42].setText(str(round(feature["valorcatastralzona"] * coeficiente_servicios * feature["valorubicacion"] * feature["valortopo"] * feature["valormaterialvial"],2)))
            # items[46].setText(str(round(feature["valorcatastralzona"] * round(feature["superficie"],2) * coeficiente_servicios * feature["valorubicacion"] * feature["valortopo"],2))) 

        # else:
            # items[24].setText(" - ")
            # items[29].setText(" - ")
            # items[34].setText(" - ")
            # items[42].setText(" - ")
            # items[46].setText(" - ")

        
         
        kfrentefondo = float(feature["frente"]) / float(feature["fondo"])
        
        items[35].setText(str(round(feature_terreno["valorzona"] * feature_terreno["superficie"] * coeficiente_servicios * 
        feature_terreno["valorubicacion"] * feature_terreno["valortopo"] * feature_terreno["valormaterialvia"] * 
        kfrentefondo / feature_terreno["superficie"],2)))
        
        
        items[36].setText(str(round(feature_terreno["valorzona"] * feature_terreno["superficie"] * coeficiente_servicios * 
        feature_terreno["valorubicacion"] * feature_terreno["valortopo"] * feature_terreno["valormaterialvia"] * 
        kfrentefondo,2)))
        


        #items[37].setText(str(round(float(feature_cons["valortipoconstruccion"]) * float(feature_cons["valoruso"],2))))
        #items[38].setText(str(round(feature_cons["superficie"] * feature_cons["tipovalor"] * feature_cons["usovalor"],2)))
     

        # if feature_cons["ant1valor"] != NULL:
            # items[39].setText(str(round(feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant1valor"],2)))
        # else:
            # items[39].setText(" - ")
        
        # if feature_cons["ant2valor"] != NULL:        
            # items[40].setText(str(round(feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant2valor"],2)))
        # else:
            # items[40].setText(" - ")           
        
        # if feature_cons["ant3valor"] != NULL:         
            # items[41].setText(str(round(feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant3valor"],2)))
        # else:
            # items[41].setText(" - ")  
            
        # if feature_cons["ant4valor"] != NULL:     
            # items[42].setText(str(round(feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant4valor"],2)))
        # else:
            # items[42].setText(" - ")  
        
        
        
        # if feature_cons["ant1valor"] != NULL:
            # items[43].setText(str(round(float(feature_cons["superficie1"]) * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant1valor"],2)))
        # else:
            # items[43].setText(" - ")  
            
        # if feature_cons["ant2valor"] != NULL:
            # items[44].setText(str(round(float(feature_cons["superficie2"]) * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant2valor"],2)))
        # else:
            # items[44].setText(" - ")      
            
        # if feature_cons["ant3valor"] != NULL:
            # items[45].setText(str(round(float(feature_cons["superficie3"]) * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant2valor"],2)))
        # else:
            # items[45].setText(" - ")    
            
        # if feature_cons["ant4valor"] != NULL:
            # items[46].setText(str(round(float(feature_cons["superficie4"]) * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant3valor"],2)))
        # else:
            # items[46].setText(" - ") 
            
        
        
        # if feature_cons["superficie1"] == "":
            # feature_cons["superficie1"] = 0
        # else:
            # feature_cons["superficie1"] = float(feature_cons["superficie1"])
            
        # if feature_cons["superficie2"] == "":
            # feature_cons["superficie2"] = 0
        # else:
            # feature_cons["superficie2"] = float(feature_cons["superficie2"])           
                        
        # if feature_cons["superficie3"] == "":
            # feature_cons["superficie3"] = 0 
        # else:
            # feature_cons["superficie3"] = float(feature_cons["superficie3"])              
                      
        # if feature_cons["superficie4"] == "":
            # feature_cons["superficie4"] = 0  
        # else:
            # feature_cons["superficie4"] = float(feature_cons["superficie4"])   
  
  
        # if feature_cons["ant1valor"] == None:
            # feature_cons["ant1valor"] = 0
        # if feature_cons["ant2valor"] == None:
            # feature_cons["ant2valor"] = 0
        # if feature_cons["ant3valor"] == None:
            # feature_cons["ant3valor"] = 0
        # if feature_cons["ant4valor"] ==  None:
            # feature_cons["ant4valor"] = 0
            
        
        # items[47].setText(str(round((feature_cons["superficie"] * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant0valor"]) +
                               # (feature_cons["superficie1"] * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant1valor"]) +
                               # (feature_cons["superficie2"] * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant2valor"]) +
                               # (feature_cons["superficie3"] * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant3valor"]) +
                               # (feature_cons["superficie4"] * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant4valor"]),2)))

        # items[48].setText(str(round((feature_cons["superficie"] * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant0valor"]) +
                               # (feature_cons["superficie1"] * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant1valor"]) +
                               # (feature_cons["superficie2"] * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant2valor"]) +
                               # (feature_cons["superficie3"] * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant3valor"]) +
                               # (feature_cons["superficie4"] * feature_cons["tipovalor"] * feature_cons["usovalor"] * feature_cons["ant4valor"]) +
                               # (feature["Valor"] * feature["Superficie"] * coeficiente_servicios * feature["ubicfactor"] * feature["inclfactor"] * feature["calzvalor"] * feature["formafactor"] * kfrentefondo),2)))
        
        
        # items[47].setText(str(round(feature["valorcatastralzona"] * round(feature["superficie"],2) * coeficiente_servicios * feature["valorubicacion"] * feature["valortopo"],2))) 
        # items[48].setText(str(round(feature["valorcatastralzona"] * round(feature["superficie"],2) * coeficiente_servicios * feature["valorubicacion"] * feature["valortopo"],2)))
        
       
        
        iface.openLayoutDesigner(layout)
        

        exporter = QgsLayoutExporter(layout)       


        exporter.exportToPdf(self.plugin_dir + '/CertificadoCatastral.pdf', QgsLayoutExporter.PdfExportSettings()) 
     
    
    
       
       #############################################################################################################################################################################
       #################################################################BOTON CAMBIAR TITULAR DEL TERRENO##########################################################################
       ############################################################################################################################################################################


    titulares_cargar_titular_cargados = ""
   
    def cargar_titular_cambiar_titular(self):
    
        urlTitular = "http://192.168.0.150:8080/apiCatastro/titular"
        
        response = requests.get(urlTitular)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_select_titular_cambio_titular.list_titular
        
        for i in range(list_widget.count()):
        
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:
            lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        
        self.titulares_cargar_titular_cargados = response_json     
       
    
 
    def titular_titular_cambiar_busca_ref(self):
        
        list_widget = self.dlg_select_titular_cambio_titular.list_titular
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        # features = list(self.titulares_cargados.getFeatures())
        
        text_busqueda  = self.dlg_select_titular_cambio_titular_busca_ref.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
  
        lista = []
              
        for item in self.titulares_cargar_titular_cargados:      
            if valor_busqueda == str(item["documento"]):
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))

        list_widget.addItems(lista)
        
        
       
    def titular_titular_cambiar_busca_nombre(self):
    
        list_widget = self.dlg_select_titular_cambio_titular.list_titular
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_titular_cambio_titular_busca_nombre.text_titular
        valor_busqueda = text_busqueda.toPlainText().lower()
              
        lista = []
        
        for item in self.titulares_cargar_titular_cargados:     
            nombreyapellidos = str(item["nombre"]).lower() + " " + str(item["apellidos"]).lower()
      
            if valor_busqueda in nombreyapellidos:
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        
        
        
        
        
        
    def cambia_titular(self):    
        
        layer = iface.activeLayer()
        
        features = layer.selectedFeatures()
        
        feature = features[0]
        
        
        list_widget = self.dlg_select_titular_cambio_titular.list_titular
        current = list_widget.currentItem()
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name = current.text()      
        titular_tuple = list_widget_name.split()
           
        id_titular = titular_tuple[0]
        
 

        urlTerreno = "http://192.168.0.150:8080/apiCatastro/terrenos19/" + feature["codigo"]
        
        responseTerreno = requests.get(urlTerreno)
        responseTerrenoJson = responseTerreno.json()
        
        responseTerrenoJson["titularBean"]["id"] = id_titular
        
        print("TERRENO SELECCIONADO")
        print(responseTerrenoJson)
        
        response = requests.put(urlTerreno, json=responseTerrenoJson)
        
        
        print("PUTEANDO")
        print(response)
        
        if response.status_code == 200:
            print(response.content)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'Información Guardada en la Base de Datos Correctamente')
        else:
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'No se pude cargar la información en la Base de Datos')
         
        
 


        ##########################################################################################################################################################################
        #################################################################BOTON UNIR DOS TERRENOS##############################################################################################################################################
       ##########################################################################################################################################################################
       
       
    titulares_cargar_union = ""
   
    def cargar_titular_union(self):
    
        urlTitular = "http://192.168.0.150:8080/apiCatastro/titular"
        
        response = requests.get(urlTitular)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_select_titular_union.list_titular
        
        for i in range(list_widget.count()):
        
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:
            lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        
        self.titulares_cargar_union = response_json     
       
    
 
    def titular_union_busca_ref(self):
        
        list_widget = self.dlg_select_titular_union.list_titular
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        # features = list(self.titulares_cargados.getFeatures())
        
        text_busqueda  = self.dlg_select_titular_union_busca_ref.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
  
        lista = []
              
        for item in self.titulares_cargar_union:      
            if valor_busqueda == str(item["documento"]):
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))

        list_widget.addItems(lista)
        
        
       
    def titular_union_busca_nombre(self):
    
        list_widget = self.dlg_select_titular_union.list_titular
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_titular_union_busca_nombre.text_titular
        valor_busqueda = text_busqueda.toPlainText().lower()
              
        lista = []
        
        for item in self.titulares_cargar_union:     
            nombreyapellidos = str(item["nombre"]).lower() + " " + str(item["apellidos"]).lower()
      
            if valor_busqueda in nombreyapellidos:
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        
        
        
        
        
        
    def union_titular(self):    
        
        layer = iface.activeLayer()
        
        features = layer.selectedFeatures()
        
        feature_primera = features[0]
        feature_segunda = features[1]
        
        geom = None
        for feat in features:
            if geom == None:
                geom = feat.geometry()
            else:
                geom = geom.combine(feat.geometry())

               
        ver = geom.vertexAt(0)
        
        points=[]
        pointsxy = []
        coordenadas = []
        coordenadasArray =[]
        n = 0
        
        while(ver.isEmpty() != True):
            n +=1
            points.append(ver)
            ver=geom.vertexAt(n)
            ver_xy = QgsPointXY(ver)
            pointsxy.append(ver_xy)
            x = ver_xy.x()
            y = ver_xy.y()
            coordenadas.append(x)
            coordenadas.append(y)
            
            coordenadasArray.append(coordenadas)
            
            coordenadas = []
        
        coordenadasArray.pop()
        
        primera_coordenada = coordenadasArray[0]
        coordenadasArray.append(primera_coordenada)
   

        
        urlTerreno_primero = "http://192.168.0.150:8080/apiCatastro/terrenos19/" + feature_primera["codigo"]
        
        responseTerrenoPrimero = requests.get(urlTerreno_primero)
        responseTerrenoPrimeroJson = responseTerrenoPrimero.json()
        
        
        

        urlTerreno_segundo = "http://192.168.0.150:8080/apiCatastro/terrenos19/" + feature_segunda["codigo"]
        
        responseTerrenoSegundo = requests.get(urlTerreno_segundo)
        responseTerrenoSegundoJson = responseTerrenoSegundo.json()
        
        

        
        list_widget = self.dlg_select_titular_union.list_titular
        current = list_widget.currentItem()
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name = current.text()      
        titular_tuple = list_widget_name.split()
        
        id_titular = titular_tuple[0]
        


        agua_union = False
        if responseTerrenoPrimeroJson['agua'] or responseTerrenoSegundoJson['agua']:
            agua_union = True
        
        alcantarillado_union = False
        if responseTerrenoPrimeroJson['alcantarillado'] or responseTerrenoSegundoJson['alcantarillado']:
            alcantarillado_union = True
                       
        internet_union = False
        if responseTerrenoPrimeroJson['internet'] or responseTerrenoSegundoJson['internet']:
            alcantarillado_union = True
            
        energia_union = False
        if responseTerrenoPrimeroJson['energia'] or responseTerrenoSegundoJson['energia']:
            energia_union = True

        telefono_union = False
        if responseTerrenoPrimeroJson['telefono'] or responseTerrenoSegundoJson['telefono']:
            telefono_union = True

        transporte_union = False
        if responseTerrenoPrimeroJson['transporte'] or responseTerrenoSegundoJson['transporte']:
            transporte_union = True
            
        
      
        nuevo_codigo = self.dlg_info_codigo_union.txt_codigo.toPlainText()
        nueva_direccion = self.dlg_info_codigo_union.txt_direccion.toPlainText()
        
        fondo_primero = float(responseTerrenoPrimeroJson["fondo"])
        fondo_segundo = float(responseTerrenoSegundoJson["fondo"])
        
        fondo_union = 0
        if fondo_primero >= fondo_segundo:
            fondo_union = fondo_primero
        else:
            fondo_union = fondo_segundo
        
        
        frente_primero = float(responseTerrenoPrimeroJson["frente"])
        frente_segundo = float(responseTerrenoSegundoJson["frente"])
        
        frente_union = frente_primero + frente_segundo
        
        
        suptest_primero = float(responseTerrenoPrimeroJson["suptest"])
        suptest_segundo = float(responseTerrenoSegundoJson["suptest"])
        
        suptest_union = suptest_primero + suptest_segundo
        
        
        
        superficie_union = responseTerrenoPrimeroJson["superficie"] + responseTerrenoSegundoJson["superficie"]

                 
        datos = {'codigo': nuevo_codigo , 'agua': agua_union, 'alcantarillado': alcantarillado_union, 'barrio': responseTerrenoPrimeroJson["barrio"], 'base': responseTerrenoPrimeroJson["base"],
        'direccion': nueva_direccion, 'energia': energia_union, 'este': " ", 'fondo': fondo_primero, 'frente': frente_union, 'internet': internet_union, 'manzano': responseTerrenoPrimeroJson["manzano"], 
        'norte': " ", 'oeste': " ",'predio': responseTerrenoPrimeroJson["predio"],'subpredio': responseTerrenoPrimeroJson["subpredio"], 'superficie': superficie_union, 'suptest': suptest_union, 
        'sur': " ",  'telefono': telefono_union, 'transporte': transporte_union, 'formaBean': {'id': responseTerrenoPrimeroJson['formaBean']['id']}, 
        'materialViaBean': {'id': responseTerrenoPrimeroJson['materialViaBean']['id']}, 'tipoVia': {'id': responseTerrenoPrimeroJson['materialViaBean']['id']}, 
        'titularBean': {'id': id_titular}, 'topografiaBean': {'id': responseTerrenoPrimeroJson['topografiaBean']['id']}, 
        'ubicacionBean': {'id': responseTerrenoPrimeroJson['ubicacionBean']['id']}, 'zonaBean': {'id': responseTerrenoPrimeroJson['zonaBean']['id']},
        "geom": {"type": "MultiPolygon","coordinates": [[coordenadasArray]]}}
     
        
        
         
        urlTerrenos = "http://192.168.0.150:8080/apiCatastro/terrenos19"
        response = requests.post(urlTerrenos, json=datos)  


        if response.status_code == 201:
            print(response.content)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'Información Guardada en la Base de Datos Correctamente')
        else:
            print(response.content)
            print(response.status_code)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'No se pude cargar la información en la Base de Datos') 




        ##########################################################################################################################################################################
        #################################################################BOTON DIVIDIR TERRENOS##############################################################################################################################################
       ##########################################################################################################################################################################  
       
       
    terreno_seleccionado_division = "" 
    linea_seleccionada_division = ""
     
       
    def guardar_terreno(self):
        
        layer_terreno = iface.activeLayer()
        
        features = layer_terreno.selectedFeatures()
        
        feature = features[0]
        


        self.terreno_seleccionado_division = feature
        
       

    def guardar_linea(self):
        
        layer_linea_division = iface.activeLayer()
        
        features = layer_linea_division.selectedFeatures()
        
        feature = features[0]
 

        self.linea_seleccionada_division = feature       
    
        
   

    titular1_cargar_division = ""
   
    def cargar_titular_divide1(self):
    
        urlTitular = "http://192.168.0.150:8080/apiCatastro/titular"
        
        response = requests.get(urlTitular)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_select_titular_divide1.list_titular
        
        for i in range(list_widget.count()):
        
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:
            lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        
        self.titular1_cargar_division = response_json     
       
    
 
    def titular_divide1_busca_ref(self):
        
        list_widget = self.dlg_select_titular_divide1.list_titular
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        # features = list(self.titulares_cargados.getFeatures())
        
        text_busqueda  = self.dlg_select_titular_divide1_buscar_ref.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
  
        lista = []
              
        for item in self.titular1_cargar_division:      
            if valor_busqueda == str(item["documento"]):
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))

        list_widget.addItems(lista)
        
        
       
    def titular_divide1_busca_nombre(self):
    
        list_widget = self.dlg_select_titular_divide1.list_titular
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_titular_divide1_buscar_nombre.text_titular
        valor_busqueda = text_busqueda.toPlainText().lower()
              
        lista = []
        
        for item in self.titular1_cargar_division:     
            nombreyapellidos = str(item["nombre"]).lower() + " " + str(item["apellidos"]).lower()
      
            if valor_busqueda in nombreyapellidos:
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        
        
 


    titular2_cargar_division = ""
   
    def cargar_titular_divide2(self):
    
        urlTitular = "http://192.168.0.150:8080/apiCatastro/titular"
        
        response = requests.get(urlTitular)
        
        responseArray = []
        
        if response.status_code == 200:
            response_json = response.json()
            
        list_widget = self.dlg_select_titular_divide2.list_titular
        
        for i in range(list_widget.count()):
        
            list_widget.takeItem(0)
        
        lista = []
                
        for item in response_json:
            lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        
        self.titular2_cargar_division = response_json     
       
    
 
    def titular_divide2_busca_ref(self):
        
        list_widget = self.dlg_select_titular_divide2.list_titular
            
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        # features = list(self.titulares_cargados.getFeatures())
        
        text_busqueda  = self.dlg_select_titular_divide2_buscar_ref.text_titular
        valor_busqueda = text_busqueda.toPlainText()
            
  
        lista = []
              
        for item in self.titular2_cargar_division:      
            if valor_busqueda == str(item["documento"]):
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))

        list_widget.addItems(lista)
        
        
       
    def titular_divide2_busca_nombre(self):
    
        list_widget = self.dlg_select_titular_divide2.list_titular
        
        for i in range(list_widget.count()):
            list_widget.takeItem(0)
            
        text_busqueda  = self.dlg_select_titular_divide2_buscar_nombre.text_titular
        valor_busqueda = text_busqueda.toPlainText().lower()
              
        lista = []
        
        for item in self.titular2_cargar_division:     
            nombreyapellidos = str(item["nombre"]).lower() + " " + str(item["apellidos"]).lower()
      
            if valor_busqueda in nombreyapellidos:
                lista.append(str(item["id"]) + "    " + str(item["nombre"]) + " " + str(item["apellidos"]) + " " + str(item["documento"]))
       
        list_widget.addItems(lista)
        
        
 



    def divide_titular(self):
    
    
        terreno = self.terreno_seleccionado_division
        linea = self.linea_seleccionada_division
        
        
        verTerreno = terreno.geometry().vertexAt(0)
        
        pointsTerreno=[]
        pointsxyTerreno = []
        coordenadasTerreno = []
        coordenadasArrayTerreno = []
        n = 0       
        
        while(verTerreno.isEmpty() != True):
            verTerreno=terreno.geometry().vertexAt(n)
            n +=1
            pointsTerreno.append(verTerreno)
        
            ver_xyTerreno = QgsPointXY(verTerreno)
            pointsxyTerreno.append(ver_xyTerreno)
            xterreno = ver_xyTerreno.x()
            yterreno = ver_xyTerreno.y()
            
            pointTerreno = QgsPointXY(xterreno, yterreno)
            

            coordenadasArrayTerreno.append(pointTerreno)
            
            coordenadasTerreno = []
        
        coordenadasArrayTerreno.pop()


        geometriaTerreno = QgsGeometry.fromPolygonXY([coordenadasArrayTerreno])



        
        ver = linea.geometry().vertexAt(0)
 
        
        points=[]
        pointsxy = []
        coordenadas = []
        coordenadasArray =[]
        n = 0
        
        while(ver.isEmpty() != True):
            ver=linea.geometry().vertexAt(n)
            n +=1
            points.append(ver)

            ver_xy = QgsPointXY(ver)
            
            pointsxy.append(ver_xy)
            x = ver_xy.x()
            y = ver_xy.y()
            
            point = QgsPointXY(x, y)
            

            coordenadasArray.append(ver_xy)
            
            coordenadas = []
        
        coordenadasArray.pop()
            
        geometriaLinea = QgsLineString(coordenadasArray)
        
  
      
        
        line = QgsLineString([QgsPoint(1, 1), QgsPoint(2, 2)])
        

        layerTerreno = QgsVectorLayer("Polygon?crs=32719","terreno","memory")
        provider = layerTerreno.dataProvider()
        layerTerreno.dataProvider().addAttributes([QgsField("id",QVariant.Int)])
        layerTerreno.updateFields()
        
        featureTerreno = QgsFeature()
        featureTerreno.setFields(layerTerreno.fields())
        featureTerreno.setAttribute('id', 1)
        featureTerreno.setGeometry(geometriaTerreno)
        features = []
        features.append(featureTerreno)
        
        layerTerreno.dataProvider().addFeatures(features)
        
        iterator = layerTerreno.getFeatures()
        featuresIterador = list(iterator)
        
        featureIterador = featuresIterador[0]
        
        
        
        t = 15

        feats_to_update=[]
        geomIterador = featureIterador.geometry()
        t = geomIterador.reshapeGeometry(geometriaLinea)
        feats_to_update.append([featureIterador.id(),geomIterador])
        
        diff = QgsFeature()
      # Calculate the difference between the original geometry and the first half of the split
        diff.setGeometry( geomIterador.difference(featureIterador.geometry()))
        
        
       
        
        verIzqda = geomIterador.vertexAt(0)

        coordenadasIzqda = []
        coordenadasArrayIzqda =[]
        nIzqda = 0
        
        while(verIzqda.isEmpty() != True):
            
            verIzqda=geomIterador.vertexAt(nIzqda)
      
            xIzqda = verIzqda.x()
            yIzqda = verIzqda.y()
            coordenadasIzqda.append(xIzqda)
            coordenadasIzqda.append(yIzqda)
            
            coordenadasArrayIzqda.append(coordenadasIzqda)
            
            coordenadasIzqda = []
            
            nIzqda +=1
            
        
        coordenadasArrayIzqda.pop()
        coordenadasArrayIzqda.append(coordenadasArrayIzqda[0])
        

        
        

        verDerecha = diff.geometry().vertexAt(0)

        coordenadasDerecha = []
        coordenadasArrayDerecha =[]
        nDerecha = 0
        
        while(verDerecha.isEmpty() != True):
            
            verDerecha=diff.geometry().vertexAt(nDerecha)
      
            xDerecha = verDerecha.x()
            yDerecha = verDerecha.y()
            coordenadasDerecha.append(xDerecha)
            coordenadasDerecha.append(yDerecha)
            
            coordenadasArrayDerecha.append(coordenadasDerecha)
            
            coordenadasDerecha = []
            
            nDerecha +=1
            
        
        coordenadasArrayDerecha.pop()
        coordenadasArrayDerecha.append(coordenadasArrayDerecha[0])
        
    

        
        urlTerreno = "https://riberaltaweb.mapearte.com/apiriberalta/terrenos19/" + terreno["codigo"]
        
        responseTerreno = requests.get(urlTerreno)
        
        responseTerrenoJson = responseTerreno.json()
        
               
  
        list_widget1 = self.dlg_select_titular_divide1.list_titular
        current1 = list_widget1.currentItem()
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name1 = current1.text()   

        
        titular_tuple1 = list_widget_name1.split()
        
        id_titular1 = titular_tuple1[0]
        
        
        urlTitular1 = "http://192.168.0.150:8080/apiCatastro/titular/" + id_titular1
        
        responseTitular1 = requests.get(urlTitular1)
        responseTitular1Json = responseTitular1.json()       
        
  
        codigo_izqda = self.dlg_info_codigo_divide1.txt_codigo.toPlainText()
        direccion_izqda = self.dlg_info_codigo_divide1.txt_direccion.toPlainText()
        fondo_izqda = self.dlg_info_codigo_divide1.txt_fondo.toPlainText()
        frente_izqda = self.dlg_info_codigo_divide1.txt_frente.toPlainText()
        
        
        datos_izqda = {'codigo': codigo_izqda , 'agua': responseTerrenoJson['agua'], 'alcantarillado': responseTerrenoJson['alcantarillado'], 
        'barrio': responseTerrenoJson["barrio"], 'base': responseTerrenoJson["base"],
        'direccion': direccion_izqda, 'energia': responseTerrenoJson["energia"], 'este': " ", 'fondo': fondo_izqda, 'frente': frente_izqda, 
        'internet': responseTerrenoJson["internet"], 'manzano': responseTerrenoJson["manzano"], 
        'norte': " ", 'oeste': " ",'predio': responseTerrenoJson["predio"],'subpredio': responseTerrenoJson["subpredio"], 
        'superficie': '', 'suptest': '', 'sur': " ",  'telefono': responseTerrenoJson["telefono"], 'transporte': responseTerrenoJson["transporte"], 
        'formaBean': {'id': responseTerrenoJson['formaBean']['id']}, 'materialViaBean': {'id': responseTerrenoJson['materialViaBean']['id']}, 
        'tipoVia': {'id': responseTerrenoJson['materialViaBean']['id']}, 'titularBean': {'id': id_titular1}, 'topografiaBean': {'id': responseTerrenoJson['topografiaBean']['id']}, 
        'ubicacionBean': {'id': responseTerrenoJson['ubicacionBean']['id']}, 'zonaBean': {'id': responseTerrenoJson['zonaBean']['id']},
        "geom": {"type": "MultiPolygon","coordinates": [[coordenadasArrayIzqda]]}}



        urlTerrenos = "http://192.168.0.150:8080/apiCatastro/terrenos19"
        responseIzqda = requests.post(urlTerrenos, json=datos_izqda)  


        if responseIzqda.status_code == 201:
            print(responseIzqda.content)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'Información del primer Terreno Guardada en la Base de Datos Correctamente')
        else:
            print(responseIzqda.content)
            print(responseIzqda.status_code)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", ' Información del primer Terreno No se pude cargar la información en la Base de Datos')   
        
      

        list_widget2 = self.dlg_select_titular_divide2.list_titular
        current2 = list_widget2.currentItem()
        
        
        #Obtengo el texto del QListWidgetItem
        list_widget_name2 = current2.text()      
        titular_tuple2 = list_widget_name2.split()
        
        id_titular2 = titular_tuple2[0]
        
        urlTitular2 = "http://192.168.0.150:8080/apiCatastro/titular/" + id_titular2

        responseTitular2 = requests.get(urlTitular2)
        responseTitular2Json = responseTitular2.json()   
        
        
 
        codigo_derecha = self.dlg_info_codigo_divide2.txt_codigo.toPlainText()
        direccion_derecha = self.dlg_info_codigo_divide2.txt_direccion.toPlainText()
        fondo_derecha = self.dlg_info_codigo_divide2.txt_fondo.toPlainText()
        frente_derecha = self.dlg_info_codigo_divide2.txt_frente.toPlainText()
        
        
        datos_derecha = {'codigo': codigo_derecha , 'agua': responseTerrenoJson['agua'], 'alcantarillado': responseTerrenoJson['alcantarillado'], 
        'barrio': responseTerrenoJson["barrio"], 'base': responseTerrenoJson["base"],
        'direccion': direccion_derecha, 'energia': responseTerrenoJson["energia"], 'este': " ", 'fondo': fondo_derecha, 'frente': frente_derecha, 
        'internet': responseTerrenoJson["internet"], 'manzano': responseTerrenoJson["manzano"], 
        'norte': " ", 'oeste': " ",'predio': responseTerrenoJson["predio"],'subpredio': responseTerrenoJson["subpredio"], 
        'superficie': '', 'suptest': '', 'sur': " ",  'telefono': responseTerrenoJson["telefono"], 'transporte': responseTerrenoJson["transporte"], 
        'formaBean': {'id': responseTerrenoJson['formaBean']['id']}, 'materialViaBean': {'id': responseTerrenoJson['materialViaBean']['id']}, 
        'tipoVia': {'id': responseTerrenoJson['materialViaBean']['id']}, 'titularBean': {'id': id_titular1}, 'topografiaBean': {'id': responseTerrenoJson['topografiaBean']['id']}, 
        'ubicacionBean': {'id': responseTerrenoJson['ubicacionBean']['id']}, 'zonaBean': {'id': responseTerrenoJson['zonaBean']['id']},
        "geom": {"type": "MultiPolygon","coordinates": [[coordenadasArrayDerecha]]}}




        responseDerecha = requests.post(urlTerrenos, json=datos_derecha)  


        if responseDerecha.status_code == 201:
            print(responseDerecha.content)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", 'Información del segundo Terreno Guardada en la Base de Datos Correctamente')
        else:
            print(responseDerecha.content)
            print(responseDerecha.status_code)
            QMessageBox.information(iface.mainWindow(), "Base de Datos", ' Información del segundo Terreno No se pude cargar la información en la Base de Datos')   
        
      
 

