# -*- coding: utf-8 -*-
import os
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets

# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'colegio_riberalta_dialog_base.ui'))
class ColegioRiberaltaDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ColegioRiberaltaDialog, self).__init__(parent)
        self.setupUi(self)
        

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'export_titular.ui'))
class ExportTitular(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ExportTitular, self).__init__(parent)
        self.setupUi(self)
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'export_titular_feature.ui'))
class ExportTitularFeature(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ExportTitularFeature, self).__init__(parent)
        self.setupUi(self)


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'export_database.ui'))
class ExportDatabase(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ExportDatabase, self).__init__(parent)
        self.setupUi(self)
        

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'export_database_feature.ui'))
class ExportDatabaseFeature(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ExportDatabaseFeature, self).__init__(parent)
        self.setupUi(self)
        
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'generar_layout.ui'))
class GenerarLayout(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GenerarLayout, self).__init__(parent)
        self.setupUi(self)
        
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'generar_informe.ui'))
class GenerarInforme(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GenerarInforme, self).__init__(parent)
        self.setupUi(self)
        
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_huso.ui'))
class SeleccionarHuso(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SeleccionarHuso, self).__init__(parent)
        self.setupUi(self)
  
  
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_huso_layout.ui'))
class SeleccionarHusoLayout(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SeleccionarHusoLayout, self).__init__(parent)
        self.setupUi(self)
        
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_huso_informe.ui'))
class SeleccionarHusoInforme(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SeleccionarHusoInforme, self).__init__(parent)
        self.setupUi(self)
        
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'guardar_feature.ui'))
class GuardarFeature(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GuardarFeature, self).__init__(parent)
        self.setupUi(self)
        
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'export_database_feature.ui'))
class ExportDatabaseFeature(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ExportDatabaseFeature, self).__init__(parent)
        self.setupUi(self)
        
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_huso_feature.ui'))
class SeleccionarHusoFeature(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SeleccionarHusoFeature, self).__init__(parent)
        self.setupUi(self)


#BOTON CONSTRUCCION        
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'guardar_feature_construccion.ui'))
class GuardarFeatureConstruccion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GuardarFeatureConstruccion, self).__init__(parent)
        self.setupUi(self)
        
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'export_database_feature_construccion.ui'))
class ExportDatabaseFeatureConstruccion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ExportDatabaseFeatureConstruccion, self).__init__(parent)
        self.setupUi(self)
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_huso_feature_construccion.ui'))
class SeleccionarHusoFeatureConstruccion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SeleccionarHusoFeatureConstruccion, self).__init__(parent)
        self.setupUi(self)
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'export_plantas.ui'))
class ExportPlantas(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ExportPlantas, self).__init__(parent)
        self.setupUi(self)
        

###INFORMES 2 y 3

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_huso_informe2.ui'))
class SeleccionarHusoInforme2(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SeleccionarHusoInforme2, self).__init__(parent)
        self.setupUi(self)


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_huso_informe3.ui'))
class SeleccionarHusoInforme3(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SeleccionarHusoInforme3, self).__init__(parent)
        self.setupUi(self)        
        
        

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'generar_informe2.ui'))
class GenerarInforme2(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GenerarInforme2, self).__init__(parent)
        self.setupUi(self)


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'generar_informe3.ui'))
class GenerarInforme3(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GenerarInforme3, self).__init__(parent)
        self.setupUi(self) 

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'listar_construccion.ui'))
class ListarConstruccion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ListarConstruccion, self).__init__(parent)
        self.setupUi(self)  


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'listar_construccion_plantas.ui'))
class ListarConstruccionPlantas(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ListarConstruccionPlantas, self).__init__(parent)
        self.setupUi(self) 

      


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'export_database_especial.ui'))
class ExportDatabaseEspecial(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ExportDatabaseEspecial, self).__init__(parent)
        self.setupUi(self)

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'export_database_mejoras.ui'))
class ExportDatabaseMejoras(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ExportDatabaseMejoras, self).__init__(parent)
        self.setupUi(self)

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'export_database_plantas.ui'))
class ExportDatabasePlantas(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ExportDatabasePlantas, self).__init__(parent)
        self.setupUi(self) 





FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_titular.ui'))
class SelectTitular(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitular, self).__init__(parent)
        self.setupUi(self)  


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_titular_feature.ui'))
class SelectTitularFeature(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularFeature, self).__init__(parent)
        self.setupUi(self)   





FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_busca_ref.ui'))
class SelectTitularBuscaRef(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularBuscaRef, self).__init__(parent)
        self.setupUi(self)  


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_busca_nombre.ui'))
class SelectTitularBuscaNombre(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularBuscaNombre, self).__init__(parent)
        self.setupUi(self) 




FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_feature_busca_ref.ui'))
class SelectTitularFeatureBuscaRef(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularFeatureBuscaRef, self).__init__(parent)
        self.setupUi(self)  


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_feature_busca_nombre.ui'))
class SelectTitularFeatureBuscaNombre(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularFeatureBuscaNombre, self).__init__(parent)
        self.setupUi(self)    




FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_construccion_planta_busca_ref.ui'))
class SelectConstruccionPlantaBuscaRef(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectConstruccionPlantaBuscaRef, self).__init__(parent)
        self.setupUi(self)  



FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_terreno_layout_busca_ref.ui'))
class SelectTerrenoLayoutBuscaRef(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTerrenoLayoutBuscaRef, self).__init__(parent)
        self.setupUi(self)  


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_terreno_layout_busca_nombre.ui'))
class SelectTerrenoLayoutBuscaNombre(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTerrenoLayoutBuscaNombre, self).__init__(parent)
        self.setupUi(self)  



FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_terreno_informe_busca_ref.ui'))
class SelectTerrenoInformeBuscaRef(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTerrenoInformeBuscaRef, self).__init__(parent)
        self.setupUi(self)  


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_terreno_informe_busca_nombre.ui'))
class SelectTerrenoInformeBuscaNombre(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTerrenoInformeBuscaNombre, self).__init__(parent)
        self.setupUi(self)         





FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_terreno_informe2_busca_ref.ui'))
class SelectTerrenoInforme2BuscaRef(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTerrenoInforme2BuscaRef, self).__init__(parent)
        self.setupUi(self)  


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_terreno_informe2_busca_nombre.ui'))
class SelectTerrenoInforme2BuscaNombre(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTerrenoInforme2BuscaNombre, self).__init__(parent)
        self.setupUi(self) 




FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_terreno_informe3_busca_ref.ui'))
class SelectTerrenoInforme3BuscaRef(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTerrenoInforme3BuscaRef, self).__init__(parent)
        self.setupUi(self)  


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_terreno_informe3_busca_nombre.ui'))
class SelectTerrenoInforme3BuscaNombre(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTerrenoInforme3BuscaNombre, self).__init__(parent)
        self.setupUi(self)         
        
        
####################################################        

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'guardar_feature_cambiar_titular.ui'))
class GuardarFeatureCambioTitular(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GuardarFeatureCambioTitular, self).__init__(parent)
        self.setupUi(self)
 


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_titular_cambio_titular.ui'))
class SelecTitularCambioTitular(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelecTitularCambioTitular, self).__init__(parent)
        self.setupUi(self)
 

         
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_cambio_titular_busca_ref.ui'))
class SelectTitularCambioTitularBuscaRef(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularCambioTitularBuscaRef, self).__init__(parent)
        self.setupUi(self)  


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_cambio_titular_busca_nombre.ui'))
class SelectTitularCambioTitularBuscaNombre(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularCambioTitularBuscaNombre, self).__init__(parent)
        self.setupUi(self) 
        

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'confirmar_cambiar_titular.ui'))
class ConfirmarGuardarTitular(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ConfirmarGuardarTitular, self).__init__(parent)
        self.setupUi(self)
        

###########################################################################################################################


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'guardar_feature_union.ui'))
class GuardarFeatureUnion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GuardarFeatureUnion, self).__init__(parent)
        self.setupUi(self)
 

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_titular_union.ui'))
class SelecTitularUnion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelecTitularUnion, self).__init__(parent)
        self.setupUi(self)
 
         
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_union_busca_ref.ui'))
class SelectTitularUnionBuscaRef(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularUnionBuscaRef, self).__init__(parent)
        self.setupUi(self)  


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_union_busca_nombre.ui'))
class SelectTitularUnionBuscaNombre(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularUnionBuscaNombre, self).__init__(parent)
        self.setupUi(self) 
        

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'confirmar_union.ui'))
class ConfirmarUnion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ConfirmarUnion, self).__init__(parent)
        self.setupUi(self)
        
        
        
        


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'info_forma_union.ui'))
class InfoFormaUnion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(InfoFormaUnion, self).__init__(parent)
        self.setupUi(self)

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'info_inclinacion_union.ui'))
class InfoInclinacionUnion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(InfoInclinacionUnion, self).__init__(parent)
        self.setupUi(self)

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'info_material_calzada_union.ui'))
class InfoMaterialCalzadaUnion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(InfoMaterialCalzadaUnion, self).__init__(parent)
        self.setupUi(self)

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'info_tipo_calzada_union.ui'))
class InfoTipoCalzadaUnion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(InfoTipoCalzadaUnion, self).__init__(parent)
        self.setupUi(self)

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'info_ubicacion_union.ui'))
class InfoUbicacionUnion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(InfoUbicacionUnion, self).__init__(parent)
        self.setupUi(self)

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'info_union.ui'))
class InfoCodigoUnion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(InfoCodigoUnion, self).__init__(parent)
        self.setupUi(self)

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'info_zona_union.ui'))
class InfoZonaUnion(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(InfoZonaUnion, self).__init__(parent)
        self.setupUi(self)        
        
        
        
        
        
        
        
        
        
        
        
        
#############################################################################################################################################




FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'guardar_feature_divide.ui'))
class GuardarFeatureDivide(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GuardarFeatureDivide, self).__init__(parent)
        self.setupUi(self)
 

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'guardar_linea_divide.ui'))
class GuardarLineaDivide(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(GuardarLineaDivide, self).__init__(parent)
        self.setupUi(self)


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_titular_dividir1.ui'))
class SelecTitularDivide1(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelecTitularDivide1, self).__init__(parent)
        self.setupUi(self)
        
        
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'selec_titular_dividir2.ui'))
class SelecTitularDivide2(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelecTitularDivide2, self).__init__(parent)
        self.setupUi(self)
 
         
FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_divide1_busca_ref.ui'))
class SelectTitularDivide1BuscaRef(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularDivide1BuscaRef, self).__init__(parent)
        self.setupUi(self)  

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_divide2_busca_ref.ui'))
class SelectTitularDivide2BuscaRef(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularDivide2BuscaRef, self).__init__(parent)
        self.setupUi(self) 
        


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_divide1_busca_nombre.ui'))
class SelectTitularDivide1BuscaNombre(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularDivide1BuscaNombre, self).__init__(parent)
        self.setupUi(self) 

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'select_titular_divide2_busca_nombre.ui'))
class SelectTitularDivide2BuscaNombre(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(SelectTitularDivide2BuscaNombre, self).__init__(parent)
        self.setupUi(self)   
        

FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'confirmar_divide.ui'))
class ConfirmarDivide(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(ConfirmarDivide, self).__init__(parent)
        self.setupUi(self) 



FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'info_divide1.ui'))
class InfoCodigoDivide1(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(InfoCodigoDivide1, self).__init__(parent)
        self.setupUi(self)
        


FORM_CLASS, _ = uic.loadUiType(os.path.join(os.path.dirname(__file__), 'info_divide2.ui'))
class InfoCodigoDivide2(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(InfoCodigoDivide2, self).__init__(parent)
        self.setupUi(self)