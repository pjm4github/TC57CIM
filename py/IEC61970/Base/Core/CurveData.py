class CurveData:
    """Multi-purpose data points for defining a curve.  The use of this generic class
    is discouraged if a more specific class  can be used to specify the x and y
    axis values along with their specific data types.
    """
    def __init__(self):
        self.xvalue = 0.0  # The data value of the X-axis variable, depending on the X-axis units.
        self.y1value = 0.0  # The data value of the first Y-axis variable, depending on the Y-axis units.
        self.y2value = 0.0  # The data value of the second Y-axis variable (if present), depending on the Y-axis units.
        self.y3value = 0.0  # The data value of the third Y-axis variable (if present), depending on the Y-axis units.
