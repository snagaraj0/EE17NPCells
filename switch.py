import pya
import math


class switch(pya.PCellDeclarationHelper):
    def __init__(self):
        super(switch, self).__init__()
        self.param("Layer1", self.TypeLayer, "Polysilicon Layer", default = pya.LayerInfo(1,0))
        self.param("W", self.TypeDouble, "Width", default = 1500)
        self.param("H", self.TypeDouble, "Height", default = 1500)
        #Source Pad params
        self.param("source_pad_center_x", self.TypeDouble, "source_pad_center_x")
        self.param("source_pad_center_y", self.TypeDouble, "source_pad_center_y")
        self.param("source_pad_width", self.TypeDouble, "source_pad_width")
        self.param("source_pad_length", self.TypeDouble, "source_pad_length")
        #Label Pad params
        self.param("label_center_x", self.TypeDouble, "label_center_x")
        self.param("label_center_y", self.TypeDouble, "label_center_y")
        self.param("label_width", self.TypeDouble, "label_width")
        self.param("label_length", self.TypeDouble, "label_length")
        self.param("label_text", self.TypeString, "Switch Label")
        self.param("label_text_x", self.TypeDouble, "label_text_x")
        self.param("label_text_y", self.TypeDouble, "label_text_y")
        #Drain Pad params
        self.param("drain_pad_center_x", self.TypeDouble, "drain_pad_center_x")
        self.param("drain_pad_center_y", self.TypeDouble, "drain_pad_center_y")
        self.param("drain_pad_width", self.TypeDouble, "drain_pad_width")
        self.param("drain_pad_length", self.TypeDouble, "drain_pad_length")
        #Left Gate Pad params
        self.param("lgate_pad_center_x", self.TypeDouble, "lgate_pad_center_x")
        self.param("lgate_pad_center_y", self.TypeDouble, "lgate_pad_center_y")
        self.param("lgate_pad_width", self.TypeDouble, "lgate_pad_width")
        self.param("lgate_pad_length", self.TypeDouble, "lgate_pad_length")
        #Right Gate Pad params
        self.param("rgate_pad_center_x", self.TypeDouble, "rgate_pad_center_x")
        self.param("rgate_pad_center_y", self.TypeDouble, "rgate_pad_center_y")
        self.param("rgate_pad_width", self.TypeDouble, "rgate_pad_width")
        self.param("rgate_pad_length", self.TypeDouble, "rgate_pad_length")
        #Beam Pad params
        self.param("beam_center_x", self.TypeDouble, "beam_center_x")
        self.param("beam_center_y", self.TypeDouble, "beam_center_y")
        self.param("beam_width", self.TypeDouble, "beam_width")
        self.param("beam_length", self.TypeDouble, "beam_length")
        #Left Gate params
        self.param("lgate_center_x", self.TypeDouble, "lgate_center_x")
        self.param("lgate_center_y", self.TypeDouble, "lgate_center_y")
        self.param("lgate_width", self.TypeDouble, "lgate_width")
        self.param("lgate_length", self.TypeDouble, "lgate_length")
        #Right Gate params
        self.param("rgate_center_x", self.TypeDouble, "rgate_center_x")
        self.param("rgate_center_y", self.TypeDouble, "rgate_center_y")
        self.param("rgate_width", self.TypeDouble, "rgate_width")
        self.param("rgate_length", self.TypeDouble, "rgate_length")
        #Source params
        self.param("source_center_x", self.TypeDouble, "source_center_x")
        self.param("source_center_y", self.TypeDouble, "source_center_y")
        self.param("source_width", self.TypeDouble, "source_width")
        self.param("source_length", self.TypeDouble, "source_length")
        #Drain params
        self.param("drain_center_x", self.TypeDouble, "drain_center_x")
        self.param("drain_center_y", self.TypeDouble, "drain_center_y")
        self.param("drain_width", self.TypeDouble, "drain_width")
        self.param("drain_length", self.TypeDouble, "drain_length")
        #Source left prong params
        self.param("slprong_center_x", self.TypeDouble, "slprong_center_x")
        self.param("slprong_center_y", self.TypeDouble, "slprong_center_y")
        self.param("slprong_width", self.TypeDouble, "slprong_width")
        self.param("slprong_length", self.TypeDouble, "slprong_length")
        #Source right prong params
        self.param("srprong_center_x", self.TypeDouble, "srprong_center_x")
        self.param("srprong_center_y", self.TypeDouble, "srprong_center_y")
        self.param("srprong_width", self.TypeDouble, "srprong_width")
        self.param("srprong_length", self.TypeDouble, "srprong_length")
        #Drain left prong params
        self.param("dlprong_center_x", self.TypeDouble, "dlprong_center_x")
        self.param("dlprong_center_y", self.TypeDouble, "dlprong_center_y")
        self.param("dlprong_width", self.TypeDouble, "dlprong_width")
        self.param("dlprong_length", self.TypeDouble, "dlprong_length")
        #Drain right prong params
        self.param("drprong_center_x", self.TypeDouble, "drprong_center_x")
        self.param("drprong_center_y", self.TypeDouble, "drprong_center_y")
        self.param("drprong_width", self.TypeDouble, "drprong_width")
        self.param("drprong_length", self.TypeDouble, "drprong_length")
        #Beam base params
        self.param("bbase_center_x", self.TypeDouble, "bbase_center_x")
        self.param("bbase_center_y", self.TypeDouble, "bbase_center_y")
        self.param("bbase_width", self.TypeDouble, "bbase_width")
        self.param("bbase_length", self.TypeDouble, "bbase_length")
        #Beam params
        self.param("beam_center_x", self.TypeDouble, "beam_center_x")
        self.param("beam_center_y", self.TypeDouble, "beam_center_y")
        self.param("beam_width", self.TypeDouble, "beam_width")
        self.param("beam_length", self.TypeDouble, "beam_length")
        #Beam left prong params
        self.param("lprongbeam_center_x", self.TypeDouble, "lprongbeam_center_x")
        self.param("lprongbeam_center_y", self.TypeDouble, "lprongbeam_center_y")
        self.param("lprongbeam_width", self.TypeDouble, "lprongbeam_width")
        self.param("lprongbeam_length", self.TypeDouble, "lprongbeam_length")
        #Beam right prong params
        self.param("rprongbeam_center_x", self.TypeDouble, "rprongbeam_center_x")
        self.param("rprongbeam_center_y", self.TypeDouble, "rprongbeam_center_y")
        self.param("rprongbeam_width", self.TypeDouble, "rprongbeam_width")
        self.param("rprongbeam_length", self.TypeDouble, "rprongbeam_length")
    def display_text_impl(self):
        return f'Trans L={self.L} W={self.W}'
    def coerce_parameters_impl(self):
        pass
    def produce_impl(self):
        #Create pads 
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(source_pad_center_x, source_pad_center_y, source_pad_width, source_pad_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(label_center_x, label_center_y, label_width, label_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Text(label_text, label_text_x, label_text_y))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(drain_pad_center_x, drain_pad_center_y, drain_pad_width, drain_pad_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(beam_center_x, beam_center_y, beam_center_width, beam_center_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(lgate_pad_center_x, lgate_pad_center_y, lgate_pad_width, lgate_pad_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(rgate_pad_center_x, rgate_pad_center_y, rgate_pad_width, rgate_pad_length)))

        #Create main components
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(beam_center_x, beam_center_y, beam_width, beam_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(lgate_center_x, lgate_center_y, lgate_width, lgate_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(rgate_center_x, rgate_center_y, rgate_width, rgate_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(source_center_x, source_center_y, source_width, source_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(drain_center_x, drain_center_y, drain_width, drain_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(beam_center_x, beam_center_y, beam_width, beam_length)))
        
        #Create prongs
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(slprong_center_x, slprong_center_y, slprong_width, slprong_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(srprong_center_x, srprong_center_y, srprong_width, srprong_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(dlprong_center_x, dlprong_center_y, dlprong_width, dlprong_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(drprong_center_x, drprong_center_y, drprong_width, drprong_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(lprongbeam_center_x, lprongbeam_center_y, lprongbeam_width, lprongbeam_length)))
        self.cell.shapes(self.Layer1_layer).insert(pya.Box(center_size_to_points(rprongbeam_center_x, rprongbeam_center_y, rprongbeam_width, rprongbeam_length)))

        #Source pad to source
        self.cell.shapes(self.Layer1_layer).insert(tuples_to_polygon([ (source_pad_center_x + source_pad_width / 2, source_pad_center_y + source_pad_length/2), 
        (source_center_x + source_width / 2, source_center_y + source_length / 2), (source_center_x  - source_width / 2, source_center_y - source_length / 2), 
        (source_pad_center_x + source_pad_width / 2, source_pad_center_y - source_pad_length / 2) ]))

        #Drain pad to drain
        self.cell.shapes(self.Layer1_layer).insert(tuples_to_polygon([ (drain_pad_center_x - drain_pad_width / 2, drain_pad_center_y + drain_pad_length / 2), 
        (drain_pad_center_x - drain_pad_width / 2, drain_pad_center_y - drain_pad_length / 2), (drain_center_x + drain_pad_width / 2, drain_center_y - drain_pad_length / 2) 
        , (drain_center_x - drain_pad_width / 2, drain_center_y + drain_pad_length / 2) ]))

        #Left gate pad to left gate
        self.cell.shapes(self.Layer1_layer).insert(tuples_to_polygon([(lgate_pad_center_x + lgate_pad_width / 2, lgate_pad_center_y + lgate_pad_length / 2), 
        (lgate_center_x + lgate_width / 2, lgate_center_y + lgate_length / 2), (lgate_center_x + lgate_width / 2, lgate_center_y - lgate_length / 2), 
        (lgate_pad_center_x + lgate_pad_width / 2, lgate_pad_center_y - lgate_pad_length / 2)]))

        #Right gate pad to right gate
        self.cell.shapes(self.Layer1_layer).insert(tuples_to_polygon([(rgate_center__x + rgate_width / 2, rgate_center_y + rgate_length / 2), 
        (rgate_pad_center_x - rgate_pad_width / 2, rgate_pad_center_y + rgate_pad_length / 2), (rgate_pad_center_x - rgate_pad_width / 2, rgate_pad_center_y - rgate_pad_length / 2), 
        (rgate_center_x + rgate_width / 2, rgate_center_y - rgate_length / 2)]))

        #Beam pad to beam 
        
        self.cell.shapes(self.Layer1_layer).insert(tuples_to_polygon([ (bbase_center_x + bbase_width / 2, bbase_center_y - bbase_length / 2), (beam_center_x + beam_width / 2, beam_center_y + beam_length / 2), 
        (beam_center_x - beam_width / 2, beam_center_y + beam_length / 2), (bbase_center_x - bbase_width / 2, bbase_center_y - bbase_length / 2)]))

    def tuples_to_polygon(points: list):
        pya_points = [pya.Point.from_dpoint(pya.DPoint(x, y))
                  for (x, y) in points]
        return pya.Polygon(pya_points)

    def center_size_to_points(center_x, center_y, width, length):
        return (center_x - width / 2, center_y - length / 2,
            center_x + width / 2, center_y + length / 2)
