import pya
import math


class switch(pya.PCellDeclarationHelper):
    def __init__(self):
        super(switch, self).__init__()
        self.param("poly", self.TypeLayer, "Polysilicon Layer", default = pya.LayerInfo(1, 0))
        self.param("beam_length", self.TypeDouble, "Beam Length", default = 21)
        self.param("beam_width", self.TypeDouble, "Beam Width", default = 0.667)
        self.param("gap_width", self.TypeDouble, "Gap Width", default = 0.833)
    def tuples_to_polygon(self, points: list):
        pya_points = [pya.Point.from_dpoint(pya.DPoint(x, y))
                  for (x, y) in points]
        return pya.Polygon(pya_points)
    def center_size_to_points(self, center_x, center_y, width, length):
        return ( (center_x - width / 2, center_y - length / 2),
            (center_x + width / 2, center_y + length / 2))
    def display_text_impl(self):
        pass
    def coerce_parameters_impl(self):
        pass
    def produce_impl(self):
        self.cell.shapes(self.poly_layer).insert(pya.Box(self.center_size_to_points(0, 0, self.beam_width, self.beam_length)[0],  self.center_size_to_points(0, 0, self.beam_width, self.beam_length)[1]))
        #self.cell.shapes(self.poly_layer).insert()
        '''
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

    '''