class Singer:
    def __init__(self, nameSinger):
        self.nameSinger = nameSinger
        self.appearanceDates = ["01/02/2020", "01/05/2020", "02/05/2020", "06/08/2020"]

    def addAppearance(self, date):
        """add date Appearance to the list if not full"""
        for i in self.appearanceDates:
            if i == date:
                return False
        self.appearanceDates.append(date)
        return True

    def printAppearance(self):
        """print the Appearance for the singer"""
        for i in self.appearanceDates:
            print(i)
