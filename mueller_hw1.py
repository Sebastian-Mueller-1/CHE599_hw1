import marimo

__generated_with = "0.8.22"
app = marimo.App(width="medium")


@app.cell
def __():
    import marimo as mo 
    import math as mt
    import matplotlib.pyplot as plt
    import numpy as np
    import re
    return mo, mt, np, plt, re


@app.cell
def __(mo):
    mo.md(r"""# Part 1""")
    return


@app.cell
def __(mt, np, plt):
    # Build class Projectile

    class Projectile:
        '''This class represents and instance of a projectile that can return information about the velocity and location.  '''
        
        def __init__(self, magnitude, direction):
            '''Initalize class projectile with magnitude of initial velocity, direction of its initial velocity vector, and time = 0'''

            self.magnitude = magnitude
            self.direction = direction

        def compute_x_pos(self, t):
            '''This method computes the x position of the projectile at arbitrary time t and returns the value'''
            return self.magnitude * t * mt.cos(self.direction)

        def compute_y_pos(self, t):
            '''This method computes the y position of the projectile at arbitrary time t and returns the value'''
            return self.magnitude * t * mt.sin(self.direction) - .5 * 9.81 * t**2

        def compute_time_of_flight(self):
            '''This method computes the time of flight for the projectile'''
            return (2 * self.magnitude * mt.sin(self.direction)) / 9.8

        def compute_horizontal_range(self):
            '''This method compute the horizontal range of the projectile and returns the value'''
            time_of_flight = self.compute_time_of_flight()
            return self.magnitude * time_of_flight * mt.cos(self.direction)

        def compute_max_height(self):
            '''This method calculates the max height achieved and returns the value'''
            t_h = (self.magnitude * mt.sin(self.direction)) / 9.81
            return self.magnitude * t_h * mt.sin(self.direction) - 0.5 * 9.81 * t_h ** 2

            
        def produce_historic_path_and_loc_plot(self, t):
            '''This method will make a plot for historic path and current position of projectile instence'''

            height_max = self.compute_max_height()
            flight_time = self.compute_time_of_flight()
            horizontal_range = self.compute_horizontal_range()

            times = np.linspace(0, min(t,flight_time),500)

            y_values = [self.compute_y_pos(time) for time in times]
            X_values = [self.compute_x_pos(time) for time in times]

            plt.figure(figsize=(10,6))
            plt.plot(X_values, y_values, label = "Historic Projectil Path")

            current_y_loc = self.compute_y_pos(t)
            current_x_loc = self.compute_x_pos(t)
            plt.scatter(current_x_loc, current_y_loc, color='orange', label = f"Current Position at t={t:.2f}s")

            plt.xlim(0,1.1*horizontal_range)
            plt.ylim(0,1.1*height_max)

            plt.gca().set_aspect('equal', adjustable='box')

            plt.ylabel('Vertical Distance (meters)')
            plt.xlabel('Horizontal Distance (meters)')
            plt.title('Historic Project Path and Current Location')
            plt.legend()
            plt.show()
    return (Projectile,)


@app.cell
def __(mo):
    mo.md(r"""## Q1""")
    return


@app.cell
def __(Projectile, mt):
    foobar_projectile = Projectile(20,(4/9)*mt.pi)
    return (foobar_projectile,)


@app.cell
def __(mo):
    mo.md(r"""## Q2""")
    return


@app.cell
def __(foobar_projectile):
    y_cord = foobar_projectile.compute_y_pos(t=1)
    x_cord = foobar_projectile.compute_x_pos(t=1)

    print(f'x cordinate at t=1s is {x_cord:.2f}, y cordinate at t=1s is {y_cord:.2f}')
    return x_cord, y_cord


@app.cell
def __(mo):
    mo.md(r"""## Q3""")
    return


@app.cell
def __(foobar_projectile):
    flight_time = foobar_projectile.compute_time_of_flight()
    max_height = foobar_projectile.compute_max_height()
    horizontal_range = foobar_projectile.compute_horizontal_range()

    print(f'For the projectile, time of flight is {flight_time:.2f}s, horizonatal range is {horizontal_range:.2f}m, and max height is {max_height:.2f}m')
    return flight_time, horizontal_range, max_height


@app.cell
def __(mo):
    mo.md(r"""## Q4""")
    return


@app.cell
def __(foobar_projectile):
    foobar_projectile.produce_historic_path_and_loc_plot(1)
    return


@app.cell
def __(mo):
    mo.md(r"""##Q5""")
    return


@app.cell
def __(flight_time, mo):
    slider = mo.ui.slider(0, flight_time, 0.01)
    return (slider,)


@app.cell
def __(foobar_projectile, mo, slider):
    mo.hstack([slider,foobar_projectile.produce_historic_path_and_loc_plot(slider.value)])
    return


@app.cell
def __(mo):
    mo.md(r"""#Part 2""")
    return


@app.cell
def __(mt, re):
    class Crystal:
        '''This class will store information about a crystal's physical information. It contains two methods, one for computing volume and the other for printing the MOF name'''

        def __init__(self, i):
            '''This will init the class and provide which txt file to read discriptor info from'''
            
            with open (f"sample_{i}.txt", 'r') as f:
                for line in f:
                    if 'MOF' in line:
                        match= re.search(r'(?<=MOF-)\d+', line)
                        self.mof = float(match.group())
                    
                    if 'a/Å' in line:
                        match = re.search(r'(?<=\s)\d+(\.\d+)?(?=\s*\(?)', line)
                        self.a_len = float(match.group())
                        
                    elif 'b/Å' in line:
                        match = re.search(r'(?<=\s)\d+(\.\d+)?(?=\s*\(?)', line)
                        self.b_len= float(match.group())
                        
                    elif 'c/Å' in line:
                        match = re.search(r'(?<=\s)\d+(\.\d+)?(?=\s*\(?)', line)
                        self.c_len = float(match.group())
                    
                    elif 'α/°' in line:
                       match = re.search(r'(?<=\s)\d+(\.\d+)?(?=\s*\(?)', line)
                       self.alpha = float(match.group())
                    
                    elif 'β/°' in line:
                        match = re.search(r'(?<=\s)\d+(\.\d+)?(?=\s*\(?)', line)
                        self.beta = float(match.group())
                    
                    elif 'γ/°' in line:
                        match = re.search(r'(?<=\s)\d+(\.\d+)?(?=\s*\(?)', line)
                        self.gamma= float(match.group())
                        

            
            
        def calc_triclinic_vol(self):
            '''This method calculates the triclinic volume and returns the value'''

            alpha_radians = mt.radians(self.alpha)
            beta_radians = mt.radians(self.beta)
            gamma_radians = mt.radians(self.gamma)
            
            return self.a_len * self.b_len * self.c_len * mt.sqrt(1 - (mt.cos(alpha_radians))**2 - (mt.cos(beta_radians))**2 - (mt.cos(gamma_radians))**2 +  mt.cos(alpha_radians) * mt.cos(beta_radians) - mt.cos(gamma_radians))

        def print_info(self):
            '''This method will print name of the MOF and lattic parameters, and volume of lattice'''

            print(f'The MOF name is: {self.mof}, length a is {self.a_len} Å, length b is {self.b_len} Å, length c is {self.c_len} Å, angle alpha is {self.alpha} degrees, angle of beta id {self.beta} degrees, angle of gamma is {self.gamma} degrees, and the volume of lattice is {self.calc_triclinic_vol()} Å³')

    return (Crystal,)


@app.cell
def __(mo):
    mo.md(r"""## Q1""")
    return


@app.cell
def __(Crystal):
    text5read = Crystal(5)
    text5read.print_info()

    return (text5read,)


if __name__ == "__main__":
    app.run()