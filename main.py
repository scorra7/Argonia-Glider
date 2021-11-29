# Code from:    https://learn.adafruit.com/adafruit-ultimate-gps-on-the-raspberry-pi?view=all


class Fly:
    gps_position_of_target = [0,0,0]
    # This gives us the longitude, latitude, and elevation of the target
    # (we might need elevation since our location might be either above or below sea level)

    def open_wings(self):
        pass
        # Turns on the servos

    def move_over_target(self):
        while True:
            gps_position_of_glider = [gps.longitude, gps.latitude, gps.altitude]
            # Need to find out which exact gps sensor we are using because different sensors will have different
            # modules and ways of installing it

            height = 0
            # We need to find a equation for the barometer in order to find our altitude

            angle_of_attack = 0
            # Use gyroscope in order to find our angle of attack

            # Calculate the new angle of attack

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
