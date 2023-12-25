# Converted by an OPENAI API call using model: gpt-3.5-turbo-1106
class OilAnalysisFluidDiscreteKind:
    def __init__(self, color_number=None,
                 color_number_platinum_cobalt_scale=None,
                 corrosive_sulphur_by_d1275=None,
                 corrosive_sulphur_by_62535=None,
                 corrosive_sulphur_by_51353=None,
                 tarnish_level=None,
                 sludge_precipitation=None):
        # Fluid color index number.  Color numbers are expressed in 0.5 intervals and
        # value specified is  "less-than". For example, a value of '2.5' means the color
        # index number is between 2.0 and 2.5.
        # Possible values: 0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.
        # 5, 7.0, 7.5, 8.0.
        self.color_number = color_number if color_number else 0.5
        # Fluid color index on the platinum cobalt scale.
        # Possible values: 5, 10, 15, 20, 25, 30, 35, 40, 50, 60, 70, 100, 150, 200, 250,
        # 300, 350, 400, 450.
        self.color_number_platinum_cobalt_scale = color_number_platinum_cobalt_scale if \
            color_number_platinum_cobalt_scale else 5
        # Corrosive sulphur test result using bare copper strip test.
        # Possible values: corrosive, nonCorrosive
        self.corrosive_sulphur_by_d1275 = corrosive_sulphur_by_d1275 if corrosive_sulphur_by_d1275 else "corrosive"
        # Corrosive sulphur test result using covered (copper) conductor deposition test.
        # Possible values: potentiallyCorrosive, nonCorrosive.
        self.corrosive_sulphur_by_62535 = corrosive_sulphur_by_62535 if \
            corrosive_sulphur_by_62535 else "potentiallyCorrosive"
        # Corrosive sulphur test result using silver strip test.
        # Possible values: absent, present.
        self.corrosive_sulphur_by_51353 = corrosive_sulphur_by_51353 if corrosive_sulphur_by_51353 else "absent"
        # Tarnish level indicated by corrosive sulphur test.
        # Possible values: 1A, 1B, 2A, 2B, 2C, 2D, 2E, 3A, 3B, 4A, 4B, 4C.
        self.tarnish_level = tarnish_level if tarnish_level else "1A"
        # Sludge precipitation test results.
        # Possible values: present, notPresent.
        self.sludge_precipitation = sludge_precipitation if sludge_precipitation else  "present"
