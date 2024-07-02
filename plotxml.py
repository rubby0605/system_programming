from lxml import etree
from bs4 import BeautifulSoup
import graphviz 
xml = '''\

    <incdepgraph>
      <node id="44">
        <label>IDimensionScale.h</label>
        <link refid="IDimensionScale_8h_source"/>
      </node>
      <node id="26">
        <label>MObjCalLine.h</label>
        <link refid="MObjCalLine_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
      </node>
      <node id="54">
        <label>EProMoveRecipe.h</label>
        <link refid="EProMoveRecipe_8h_source"/>
      </node>
      <node id="3">
        <label>AutoStitchInput.h</label>
        <link refid="AutoStitchInput_8h_source"/>
        <childnode refid="4" relation="include">
        </childnode>
        <childnode refid="13" relation="include">
        </childnode>
      </node>
      <node id="58">
        <label>BifConverter.h</label>
        <link refid="BifConverter_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
        <childnode refid="15" relation="include">
        </childnode>
      </node>
      <node id="5">
        <label>GlobalVariable.h</label>
        <link refid="GlobalVariable_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
        <childnode refid="10" relation="include">
        </childnode>
        <childnode refid="11" relation="include">
        </childnode>
        <childnode refid="9" relation="include">
        </childnode>
        <childnode refid="12" relation="include">
        </childnode>
      </node>
      <node id="29">
        <label>MObjPropertyForm.h</label>
        <link refid="MObjPropertyForm_8h_source"/>
      </node>
      <node id="10">
        <label>MessageForm.h</label>
        <link refid="MessageForm_8h_source"/>
      </node>
      <node id="33">
        <label>DataTag.h</label>
        <link refid="DataTag_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
        <childnode refid="5" relation="include">
        </childnode>
        <childnode refid="15" relation="include">
        </childnode>
      </node>
      <node id="8">
        <label>stdlib.h</label>
      </node>
      <node id="18">
        <label>MObjLine.h</label>
        <link refid="MObjLine_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
        <childnode refid="19" relation="include">
        </childnode>
      </node>
      <node id="20">
        <label>MObjEllipse.h</label>
        <link refid="MObjEllipse_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
      </node>
      <node id="32">
        <label>ColorMap.h</label>
        <link refid="ColorMap_8h_source"/>
      </node>
      <node id="36">
        <label>ImageFFT.h</label>
        <link refid="ImageFFT_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
      </node>
      <node id="12">
        <label>cmath</label>
      </node>
      <node id="49">
        <label>opencv2/core/core.hpp</label>
      </node>
      <node id="1">
        <label>AutoStitchFlow.cpp</label>
        <link refid="AutoStitchFlow_8cpp"/>
        <childnode refid="2" relation="include">
        </childnode>
        <childnode refid="58" relation="include">
        </childnode>
      </node>
      <node id="17">
        <label>MObjAngler.h</label>
        <link refid="MObjAngler_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
      </node>
      <node id="42">
        <label>CropRectangleTool.h</label>
        <link refid="CropRectangleTool_8h_source"/>
        <childnode refid="43" relation="include">
        </childnode>
      </node>
      <node id="30">
        <label>FilterForm.h</label>
        <link refid="FilterForm_8h_source"/>
      </node>
      <node id="56">
        <label>StitchFlowBase.h</label>
        <link refid="StitchFlowBase_8h_source"/>
      </node>
      <node id="25">
        <label>MObjCrossLine.h</label>
        <link refid="MObjCrossLine_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
      </node>
      <node id="23">
        <label>MObjRuler.h</label>
        <link refid="MObjRuler_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
      </node>
      <node id="16">
        <label>ChildForm.h</label>
        <link refid="ChildForm_8h_source"/>
        <childnode refid="5" relation="include">
        </childnode>
        <childnode refid="14" relation="include">
        </childnode>
        <childnode refid="17" relation="include">
        </childnode>
        <childnode refid="18" relation="include">
        </childnode>
        <childnode refid="20" relation="include">
        </childnode>
        <childnode refid="21" relation="include">
        </childnode>
        <childnode refid="22" relation="include">
        </childnode>
        <childnode refid="23" relation="include">
        </childnode>
        <childnode refid="24" relation="include">
        </childnode>
        <childnode refid="25" relation="include">
        </childnode>
        <childnode refid="26" relation="include">
        </childnode>
        <childnode refid="27" relation="include">
        </childnode>
        <childnode refid="28" relation="include">
        </childnode>
        <childnode refid="29" relation="include">
        </childnode>
        <childnode refid="30" relation="include">
        </childnode>
        <childnode refid="31" relation="include">
        </childnode>
        <childnode refid="33" relation="include">
        </childnode>
        <childnode refid="34" relation="include">
        </childnode>
        <childnode refid="15" relation="include">
        </childnode>
        <childnode refid="36" relation="include">
        </childnode>
        <childnode refid="37" relation="include">
        </childnode>
        <childnode refid="38" relation="include">
        </childnode>
        <childnode refid="40" relation="include">
        </childnode>
        <childnode refid="41" relation="include">
        </childnode>
        <childnode refid="42" relation="include">
        </childnode>
        <childnode refid="46" relation="include">
        </childnode>
        <childnode refid="47" relation="include">
        </childnode>
        <childnode refid="49" relation="include">
        </childnode>
        <childnode refid="50" relation="include">
        </childnode>
        <childnode refid="51" relation="include">
        </childnode>
      </node>
      <node id="37">
        <label>FFTForm.h</label>
        <link refid="FFTForm_8h_source"/>
      </node>
      <node id="19">
        <label>ShadowLabel.h</label>
        <link refid="ShadowLabel_8h_source"/>
      </node>
      <node id="55">
        <label>OmeMoveRecipe.h</label>
        <link refid="OmeMoveRecipe_8h_source"/>
      </node>
      <node id="46">
        <label>PosTransformor.h</label>
        <link refid="PosTransformor_8h_source"/>
        <childnode refid="5" relation="include">
        </childnode>
      </node>
      <node id="35">
        <label>MyGridListControl.h</label>
        <link refid="MyGridListControl_8h_source"/>
      </node>
      <node id="27">
        <label>MObjProfLine.h</label>
        <link refid="MObjProfLine_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
      </node>
      <node id="7">
        <label>string.h</label>
      </node>
      <node id="13">
        <label>DataCenter.h</label>
        <link refid="DataCenter_8h_source"/>
        <childnode refid="9" relation="include">
        </childnode>
        <childnode refid="5" relation="include">
        </childnode>
        <childnode refid="14" relation="include">
        </childnode>
        <childnode refid="16" relation="include">
        </childnode>
        <childnode refid="52" relation="include">
        </childnode>
      </node>
      <node id="50">
        <label>opencv2/imgproc/imgproc.hpp</label>
      </node>
      <node id="52">
        <label>AvgImage.h</label>
        <link refid="AvgImage_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
        <childnode refid="5" relation="include">
        </childnode>
      </node>
      <node id="2">
        <label>AutoStitchFlow.h</label>
        <link refid="AutoStitchFlow_8h_source"/>
        <childnode refid="3" relation="include">
        </childnode>
        <childnode refid="13" relation="include">
        </childnode>
        <childnode refid="5" relation="include">
        </childnode>
        <childnode refid="53" relation="include">
        </childnode>
        <childnode refid="54" relation="include">
        </childnode>
        <childnode refid="55" relation="include">
        </childnode>
        <childnode refid="56" relation="include">
        </childnode>
        <childnode refid="57" relation="include">
        </childnode>
      </node>
      <node id="43">
        <label>CropRectangle.h</label>
        <link refid="CropRectangle_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
        <childnode refid="44" relation="include">
        </childnode>
        <childnode refid="45" relation="include">
        </childnode>
      </node>
      <node id="31">
        <label>ColorMapForm.h</label>
        <link refid="ColorMapForm_8h_source"/>
        <childnode refid="32" relation="include">
        </childnode>
        <childnode refid="5" relation="include">
        </childnode>
      </node>
      <node id="24">
        <label>MObjMatrix.h</label>
        <link refid="MObjMatrix_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
      </node>
      <node id="11">
        <label>WaitForm.h</label>
        <link refid="WaitForm_8h_source"/>
      </node>
      <node id="14">
        <label>ImageData.h</label>
        <link refid="ImageData_8h_source"/>
        <childnode refid="15" relation="include">
        </childnode>
        <childnode refid="5" relation="include">
        </childnode>
        <childnode refid="7" relation="include">
        </childnode>
        <childnode refid="8" relation="include">
        </childnode>
      </node>
      <node id="4">
        <label>StitchRegionParams.h</label>
        <link refid="StitchRegionParams_8h_source"/>
        <childnode refid="5" relation="include">
        </childnode>
      </node>
      <node id="45">
        <label>LocalizedDisplayNameAttribute.h</label>
        <link refid="LocalizedDisplayNameAttribute_8h_source"/>
        <childnode refid="5" relation="include">
        </childnode>
      </node>
      <node id="53">
        <label>ImageWalker.h</label>
        <link refid="ImageWalker_8h_source"/>
      </node>
      <node id="57">
        <label>NavGenInput.h</label>
        <link refid="NavGenInput_8h_source"/>
      </node>
      <node id="28">
        <label>DiagramDocument.h</label>
        <link refid="DiagramDocument_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
      </node>
      <node id="9">
        <label>time.h</label>
      </node>
      <node id="6">
        <label>Parameter.h</label>
        <link refid="Parameter_8h"/>
        <childnode refid="7" relation="include">
        </childnode>
        <childnode refid="8" relation="include">
        </childnode>
        <childnode refid="9" relation="include">
        </childnode>
      </node>
      <node id="51">
        <label>opencv2/highgui/highgui.hpp</label>
      </node>
      <node id="39">
        <label>CustomLabel.h</label>
        <link refid="CustomLabel_8h_source"/>
      </node>
      <node id="34">
        <label>ImageInfoForm.h</label>
        <link refid="ImageInfoForm_8h_source"/>
        <childnode refid="33" relation="include">
        </childnode>
        <childnode refid="35" relation="include">
        </childnode>
      </node>
      <node id="48">
        <label>CropEllipse.h</label>
        <link refid="CropEllipse_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
        <childnode refid="44" relation="include">
        </childnode>
        <childnode refid="45" relation="include">
        </childnode>
      </node>
      <node id="21">
        <label>MObjRectangle.h</label>
        <link refid="MObjRectangle_8h_source"/>
        <childnode refid="6" relation="include">
        </childnode>
      </node>
      <node id="38">
        <label>CustomInplaceEditor.h</label>
        <link refid="CustomInplaceEditor_8h_source"/>
        <childnode refid="39" relation="include">
        </childnode>
      </node>
      <node id="40">
        <label>IDigitalZoomIn.h</label>
        <link refid="IDigitalZoomIn_8h_source"/>
      </node>
      <node id="41">
        <label>CustomDiaController.h</label>
        <link refid="CustomDiaController_8h_source"/>
      </node>
      <node id="47">
        <label>CropEllipseTool.h</label>
        <link refid="CropEllipseTool_8h_source"/>
        <childnode refid="48" relation="include">
        </childnode>
      </node>
      <node id="15">
        <label>stdio.h</label>
      </node>
      <node id="22">
        <label>MObjText.h</label>
        <link refid="MObjText_8h_source"/>
      </node>
    </incdepgraph>
'''
 
root = etree.fromstring(xml)
soup = BeautifulSoup(xml, 'lxml')
 
# lxml
for node in root.iter('*'):
    print(node.tag)
 
# BS
for tag in soup.findChildren():
    print(tag.name)
# Function to recursively add nodes to the graph
def add_nodes(graph, parent, element):
    node_label = element.tag
    graph.node(node_label, node_label)

    if parent is not None:
        graph.edge(parent, node_label)

    for child in element:
        add_nodes(graph, node_label, child)

# Create a directed graph
graph = graphviz.Digraph()

# Add nodes and edges recursively
add_nodes(graph, None, root)

# Save the graph to a file (e.g., PNG format)
graph.render('xml_structure', format='png', view=True)
