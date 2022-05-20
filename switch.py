import pya
import math


class switch(pya.PCellDeclarationHelper):
    def __init__(self):
        super(switch, self).__init__()
        self.param("poly", self.TypeLayer, "Polysilicon Layer", default = pya.LayerInfo(1, 0))
        self.param("beam_length", self.TypeDouble, "Beam Length", default = 31.5)
        self.param("beam_width", self.TypeDouble, "Beam Width", default = 1)
        self.param("gap_width", self.TypeDouble, "Gap Width", default = 1.25)
    def tuples_to_polygon(self, points: list):
        pya_points = [pya.Point.from_dpoint(pya.DPoint(x, y))
                  for (x, y) in points]
        return pya.Polygon(pya_points)
    def center_size_to_points(self, center_x, center_y, width, length):
        return (center_x - width / 2, center_y - length / 2,
            center_x + width / 2, center_y + length / 2)
    def display_text_impl(self):
        pass
    def coerce_parameters_impl(self):
        pass
    def produce_impl(self):

        dbu = self.layout.dbu

        beam_width = self.beam_width / dbu
        beam_length = self.beam_length / dbu
        gap_width = self.gap_width / dbu

        self.cell.shapes(self.poly_layer).insert(pya.Box(self.center_size_to_points(0, 0, beam_width, beam_length)[0], self.center_size_to_points(0, 0, beam_width, beam_length)[1], 
        self.center_size_to_points(0, 0, beam_width, beam_length)[2], self.center_size_to_points(0, 0, beam_width, beam_length)[3]))

        # Beam base
        a,b,c,d = self.center_size_to_points(0, 0 - (beam_length / 2) - (7.5 / (2 * dbu)), 15 / dbu , 7.5 / dbu)
        self.cell.shapes(self.poly_layer).insert(pya.Box(a, b, c,d ))
        # Beam top rectangle 
        a,b,c,d = self.center_size_to_points(0, 0 + (beam_length / 2) + (1) / (2 * dbu), 10.5 / dbu, 1 / dbu)
        self.cell.shapes(self.poly_layer).insert(pya.Box(a, b, c,d ))
        # Left Gate 
        a,b,c,d = self.center_size_to_points(0 - (beam_width / 2) - gap_width - 9.5 / (2 * dbu), 0.75 /dbu , 9.5 / dbu, (beam_length - (3.5 / dbu)))
        self.cell.shapes(self.poly_layer).insert(pya.Box(a,b,c,d))
        #Right Gate
        a,b,c,d = self.center_size_to_points(0 + (beam_width / 2) + gap_width + 9.5 / (2 * dbu), 0.75 /dbu, 9.5 / dbu, (beam_length - (3.5 / dbu)))
        self.cell.shapes(self.poly_layer).insert(pya.Box(a,b,c,d))
        #Beam Left Prong
        a,b,c,d = self.center_size_to_points(0 - (5.25 / dbu) +  (1 / (2 * dbu)), 0 + (beam_length / 2) + (1) / (dbu) + (2.5) / (2 * dbu), 1/ dbu, 2.5 / dbu)
        self.cell.shapes(self.poly_layer).insert(pya.Box(a,b,c,d))
        #Beam Right Prong
        a,b,c,d = self.center_size_to_points(0 + (5.25 / dbu) -  (1 / (2 * dbu)), 0 + (beam_length / 2) + (1) / (dbu) + (2.5) / (2 * dbu), 1/ dbu, 2.5 / dbu)
        self.cell.shapes(self.poly_layer).insert(pya.Box(a,b,c,d))

        source_drain_y_val = (beam_length / 2) + (1 / dbu) + (3.25 / dbu)
        sd_prong_height = 4.5 / dbu
        c1 = 2.16 / dbu
        c2 = 2.355 / dbu
        c3 = 2.625 / dbu
        #Source Left Prong
        a,b,c,d = self.center_size_to_points( (-0.5 * c1 - 1.5 * c2 - c3), source_drain_y_val, c2, sd_prong_height)
        self.cell.shapes(self.poly_layer).insert(pya.Box(a,b,c,d))
        #Source Right Prong
        a,b,c,d = self.center_size_to_points( (-0.5 * c1 - 0.5 * c2), source_drain_y_val, c2, sd_prong_height)
        self.cell.shapes(self.poly_layer).insert(pya.Box(a,b,c,d))
        #Drain Left Prong
        a,b,c,d = self.center_size_to_points( (0.5 * c1 + 0.5 * c2), source_drain_y_val, c2 , sd_prong_height)
        self.cell.shapes(self.poly_layer).insert(pya.Box(a,b,c,d))
        #Drain Right Prong
        a,b,c,d = self.center_size_to_points( (0.5 * c1 + 1.5 * c2 + c3), source_drain_y_val, c2, sd_prong_height)
        self.cell.shapes(self.poly_layer).insert(pya.Box(a,b,c,d))

        #Source Pad to Source
        source_center_x = -1 * (5.25 / dbu) + (1 / (2 * dbu))
        source_center_y = (beam_length / 2) + (1/ dbu) + (5.5 / dbu) + (10/dbu)
        
        source_top_right_x = source_center_x + (7.34 / (2 * dbu))
        source_top_right_y = source_center_y + (10 / dbu)
        source_bottom_right_x = source_center_x + (7.34 / (2 * dbu))
        source_bottom_right_y = source_center_y - (10 / (dbu))
        source_bottom_left_x = source_center_x - (7.34 / (2 * dbu))
        source_bottom_left_y = source_center_y - (10 / (dbu))
        self.cell.shapes(self.poly_layer).insert(self.tuples_to_polygon([ (-275/dbu, 675/dbu), (-125/dbu, 675/dbu), (source_top_right_x, source_top_right_y), 
        (source_bottom_right_x, source_bottom_right_y), (source_bottom_left_x, source_bottom_left_y), ( (-275 / dbu) , (525 / dbu)) ]))

        #Drain Pad to Drain
        drain_center_x = (5.25 / dbu) - (1 / (2 * dbu))
        drain_center_y = (beam_length / 2) + (1/ dbu) + (5.5 / dbu) + (10/dbu)

        drain_top_left_x = drain_center_x - (7.335 / (2 * dbu))
        drain_top_left_y = drain_center_y +  (10 / dbu)
        drain_bottom_right_x = drain_center_x + (7.335 / (2 * dbu))
        drain_bottom_right_y = drain_center_y - (10 / (dbu))
        drain_bottom_left_x = drain_center_x - (7.335 / (2 * dbu))
        drain_bottom_left_y = drain_center_y - (10 / (dbu))
        self.cell.shapes(self.poly_layer).insert(self.tuples_to_polygon([ (125/dbu, 675/dbu), (275/dbu, 675/dbu), ( (275 / dbu) , (525 / dbu)), (drain_bottom_right_x, drain_bottom_right_y), 
        (drain_bottom_left_x, drain_bottom_left_y), (drain_top_left_x, drain_top_left_y) ]))


        #Beam Pad to Beam
        beam_center_x = 0
        beam_center_y = 0 - (beam_length / 2) - (7.5 / (2 * dbu))
        beam_bottom_right_x = beam_center_x + (15 / (2* dbu))
        beam_bottom_right_y = beam_center_y - (7.5 / (2 * dbu))
        beam_bottom_left_x = beam_center_x - (15 / (2* dbu))
        beam_bottom_left_y = beam_center_y - (7.5 / (2 * dbu))

        self.cell.shapes(self.poly_layer).insert(self.tuples_to_polygon([ (beam_bottom_right_x, beam_bottom_right_y), (75/dbu, -525/dbu), ( (75 / dbu) , (-675 / dbu)), (-75 / dbu, -675 / dbu), 
        (-75 / dbu, -525 / dbu), (beam_bottom_left_x, beam_bottom_left_y)]))

        #Right Gate Pad to Right Gate
        rgate_center_x = 0 + (beam_width / 2) + gap_width + 9.5 / (2 * dbu)
        rgate_center_y = 0.75 /dbu
        rgate_top_right_x = rgate_center_x + (9.5 / (2 * dbu))
        rgate_top_right_y = rgate_center_y + ((beam_length - (3.5 / dbu)) / 2)
        rgate_bottom_right_x = rgate_center_x + (9.5 / (2 * dbu))
        rgate_bottom_right_y = rgate_center_y - ((beam_length - (3.5 / dbu)) / 2)


        self.cell.shapes(self.poly_layer).insert(self.tuples_to_polygon([(rgate_top_right_x, rgate_top_right_y), ( (275 / dbu) , (-525 / dbu)), (275/dbu, -675/dbu), 
        (125 / dbu, -675 / dbu), (rgate_bottom_right_x, rgate_bottom_right_y) ]))

        #Left Gate Pad to Left Gate
        lgate_center_x = 0 - (beam_width / 2) - gap_width - 9.5 / (2 * dbu)
        lgate_center_y = 0.75 / dbu

        lgate_top_left_x = lgate_center_x - (9.5 / (2 * dbu))
        lgate_top_left_y = lgate_center_y + ((beam_length - (3.5 / dbu)) / 2)
        lgate_bottom_left_x = lgate_center_x - (9.5 / (2 * dbu))
        lgate_bottom_left_y = lgate_center_y - ((beam_length - (3.5 / dbu)) / 2)

        self.cell.shapes(self.poly_layer).insert(self.tuples_to_polygon([(lgate_top_left_x, lgate_top_left_y), ( lgate_bottom_left_x , lgate_bottom_left_y), 
        (-125 / dbu, -675 / dbu), (-275/dbu, -675/dbu),  (-275 / dbu, -525 / dbu) ]))
