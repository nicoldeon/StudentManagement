from CalculationMark import CalculationMark


class Mark(CalculationMark):
    def __init__(self,
                 math_mark=0,
                 physics_mark=0,
                 chemistry_mark=0):
        self.math_mark = math_mark
        self.physics_mark = physics_mark
        self.chemistry_mark = chemistry_mark

    def get_math_mark(self):
        return self.math_mark

    def set_math_mark(self):
        math = input("Input student's math mark:")
        try:
            math = float(math)
            if (Mark.check_mark(math)):
                self.physics_mark = math
        except:
            raise ValueError("Math mark data type doesn't valid!")

    def get_physics_mark(self):
        return self.physics_mark

    def set_physics_mark(self):
        physics = input("Input student's physics mark:")
        try:
            physics = float(physics)
            if (Mark.check_mark(physics)):
                self.physics_mark = physics
        except:
            raise ValueError("Physics mark data type doesn't valid!")

    def get_chemistry_mark(self):
        return self.chemistry_mark

    def set_chemistry_mark(self):
        chemistry = input("Input student's chemistry mark:")
        try:
            chemistry = float(chemistry)
            if (Mark.check_mark(chemistry)):
                self.c = chemistry
        except:
            raise ValueError("Chemistry mark data type doesn't valid!")

    @staticmethod
    def check_mark(mark):
        if 0 <= mark <= 10:
            return True
        return False

    def __repr__(self):
        return f"Mark('{self.math_mark}', '{self.physics_mark}', '{self.chemistry_mark}')"

    def calc_ave_mark(self):
        """ Method to calculate the average mark of student """
        ls_mark = [self.math_mark, self.physics_mark, self.chemistry_mark]
        sum_mark = sum(ls_mark)
        return float(sum_mark / len(ls_mark))
