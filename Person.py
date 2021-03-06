class Person:

    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
        self.coords_history = []
        self.direction = None
        self.attemps = 20
        self.delete = False

    def time_to_delete(self):
        # Person has 20 frames to cross any line
        self.attemps -= 1
        if self.attemps == 0:
            self.delete = True

    def update_coords(self, x, y):
        self.coords_history.append([self.x,self.y])
        self.x = x
        self.y = y

    def specify_direction(self, line_in_x, line_out_x):
        # If person has at least 2 tracking points
        if len(self.coords_history) >= 2:
            # If direction of the person is unknown specify direction
            if self.direction is None:
                last_coords_x = self.coords_history[-1][0]
                pre_last_coords_x = self.coords_history[-2][0]
                if last_coords_x > line_in_x and pre_last_coords_x <= line_in_x:
                    self.direction = 'in'
                    print "Someone just walked %s" % (self.direction)
                    return True
                elif last_coords_x < line_out_x and pre_last_coords_x >= line_out_x:
                    self.direction = 'out'
                    print "Someone just walked %s" % (self.direction)
                    return True
            else:
                return False
        else:
            return False
