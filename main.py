class Fly:
    __gps_positioning = []

    def open_wings(self):
        pass
        # Turns on the servos

    def move_over_target(self,new_gps_pos):
        while True:
            __gps_positioning = new_gps_pos
            # Calculate stuff
            # Adjust the glider to the new pos

    def drop(self):
        pass
        #

    def light_sensor(self):
        pass
    # Might need to remove from class since its already defined

    @staticmethod
    def light_delay_time():
        light_delay = 2
        return light_delay
    # Might just make this into a variable inside main()


if __name__ == '__main__':
    if Fly.light_sensor() == Fly.light_delay_time():
        Fly.open_wings()
        Fly.move_over_target()
        Fly.drop()
