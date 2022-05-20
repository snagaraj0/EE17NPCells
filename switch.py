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
        a,b,c,d = self.center_size_to_points(0 - (beam_width / 2) - gap_width - 9.5 / (2 * dbu), 2.5/dbu , 9.5 / dbu, (beam_length - (3.5 / dbu)))
        self.cell.shapes(self.poly_layer).insert(pya.Box(a,b,c,d))
        #Right Gate
        a,b,c,d = self.center_size_to_points(0 + (beam_width / 2) + gap_width + 9.5 / (2 * dbu), 2.5/dbu, 9.5 / dbu, (beam_length - (3.5 / dbu)))
        self.cell.shapes(self.poly_layer).insert(pya.Box(a,b,c,d))
        #Beam Left Prong
        a,b,c,d = self.center_size_to_points(0 - (10.5 / dbu) +  (1 / (2 * dbu)), 0 + (beam_length / 2) + (1) / (2 * dbu) + (2.5) / (2 * dbu), 1/ dbu, 2.5 / dbu)
        self.cell.shapes(self.poly_layer).insert(pya.Box(a,b,c,d))
        #Beam Right Prong

        #Source Left Prong

        #Source Right Prong

        #Drain Left Prong

        #Drain Right Prong


        #self.cell.shapes(self.poly_layer).insert(pya.Box(self.center_size_to_points))
        #self.cell.shapes(self.poly_layer).insert()