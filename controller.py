from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from view import *
import search as s


QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    """
    A class definition defines a controller object
    """
    def __init__(self, *args, **kwargs):
        """
        Contructor to create initial state of a controller object
        :param args:
        :param kwargs:
        """
        super().__init__(*args, **kwargs)
        self.setupUi(self)

        #Main button options
        self.button_warframe.clicked.connect(lambda: self.warframe())
        self.button_primary.clicked.connect(lambda: self.primary())
        self.button_secondary.clicked.connect(lambda: self.secondary())
        self.button_melee.clicked.connect(lambda: self.melee())

        #Clear options
        self.button_clearAll.clicked.connect(lambda: self.clearAll())
        self.button_clearPage.clicked.connect(lambda: self.clearPage())

        #Enter selection
        self.line_warframeSelect.returnPressed.connect(lambda: self.onReturn(option='f'))
        self.line_primarySelect.returnPressed.connect(lambda: self.onReturn(option='p'))
        self.line_secondarySelect.returnPressed.connect(lambda: self.onReturn(option='s'))
        self.line_meleeSelect.returnPressed.connect(lambda: self.onReturn(option='m'))
        
        #Show hidden lists
        self.radio_primary.clicked.connect(lambda: self.onChecked(option='p'))
        self.radio_secondary.clicked.connect(lambda: self.onChecked(option='s'))
        self.radio_melee.clicked.connect(lambda: self.onChecked(option='m'))

        #Find variant info
        self.button_primaryVariant.clicked.connect(lambda: self.onClicked(option='p'))
        self.button_secondaryVariant.clicked.connect(lambda: self.onClicked(option='s'))
        self.button_meleeVariant.clicked.connect(lambda: self.onClicked(option='m'))

    def warframe(self):
        """
        Method to change index on stacked widget
        :return: None
        """
        self.stackedWidget.setCurrentIndex(0)

    def primary(self):
        """
        Method to change index on stacked widget
        :return: None
        """
        self.stackedWidget.setCurrentIndex(1)

    def secondary(self):
        """
        Method to change index on stacked widget
        :return: None
        """
        self.stackedWidget.setCurrentIndex(2)

    def melee(self):
        """
        Method to change index on stacked widget
        :return: None
        """
        self.stackedWidget.setCurrentIndex(3)

    def onReturn(self, option):
        """
        Method to display information based on option (lineEdit) the return key is pressed
        :param option: Determines which lineEdit the return was pressed on
        :return: Display info based on input and lineEdit
        """

        #Warframe page
        if option == 'f':
            try:
                name,prime,prime_parts,normal,mastery = s.warframe(self.line_warframeSelect.text().strip().capitalize())
                self.line_warframeSelect.clear()
                self.label_warframe.setText(name)
                self.label_warframeLeft.setText(f'{name} Normal Variant\n'
                f'{normal}')
                self.label_warframeMiddle.setText(f'Prime parts needed for {name} Prime\n'
                f'{prime_parts}')
                self.label_warframeRight.setText(f'{name} Prime Variant\n'
                f'{prime}')
                self.label_warframeMastery.setText(f'{name} Mastery: {mastery}')
                
                self.warframe_normalPicture.show()
                self.warframe_primePicture.show()
                self.warframe_bpPicture.show()
                self.warframe_neuropticPicture.show()
                self.warframe_chassisPicture.show()
                self.warframe_systemPicture.show()
                
                if normal == 'Owned':
                    self.warframe_normalPicture.setStyleSheet('border: 5px solid green;')
                else:
                    self.warframe_normalPicture.setStyleSheet('border: 5px solid red;')
                
                if prime == 'Owned':
                    self.warframe_primePicture.setStyleSheet('border: 5px solid green;')
                else:
                    self.warframe_primePicture.setStyleSheet('border: 5px solid red;')

                if 'BP' in prime_parts:
                    self.warframe_bpPicture.setStyleSheet('border: 5px solid red;')
                else:
                    self.warframe_bpPicture.setStyleSheet('border: 5px solid green;')

                if 'Neuroptics' in prime_parts:
                    self.warframe_neuropticPicture.setStyleSheet('border: 5px solid red;')
                else:
                    self.warframe_neuropticPicture.setStyleSheet('border: 5px solid green;')
                
                if 'Chassis' in prime_parts:
                    self.warframe_chassisPicture.setStyleSheet('border: 5px solid red;')
                else:
                    self.warframe_chassisPicture.setStyleSheet('border: 5px solid green;')
                
                if 'Systems' in prime_parts:
                    self.warframe_systemPicture.setStyleSheet('border: 5px solid red;')
                else:
                    self.warframe_systemPicture.setStyleSheet('border: 5px solid green;')
            except TypeError:
                self.label_warframe.setText('Invalid Entry')
                self.label_warframeMiddle.setText(f'Entry was either mispelled or incorrect\n'
                f'Double check your entry\n'
                f'Your entry: {self.line_warframeSelect.text()}\n'
                f'Was not recognized as a warframe name')
                
                self.line_warframeSelect.clear()
                self.label_warframeLeft.clear()
                self.label_warframeRight.clear()
                self.label_warframeMastery.clear()
                self.warframe_normalPicture.clear()
                self.warframe_primePicture.clear()
                self.warframe_bpPicture.clear()
                self.warframe_neuropticPicture.clear()
                self.warframe_chassisPicture.clear()
                self.warframe_systemPicture.clear()

                self.warframe_normalPicture.setStyleSheet('border: none')
                self.warframe_bpPicture.setStyleSheet('border: none')
                self.warframe_neuropticPicture.setStyleSheet('border: none')
                self.warframe_chassisPicture.setStyleSheet('border: none')
                self.warframe_systemPicture.setStyleSheet('border: none')
                self.warframe_primePicture.setStyleSheet('border: none')
            except ValueError:
                self.label_warframe.setText('No Entry')
                self.label_warframeMiddle.setText(f'No entry was made\n'
                f'Please enter a warframe name to continue')

                self.line_warframeSelect.clear()
                self.label_warframeLeft.clear()
                self.label_warframeRight.clear()
                self.label_warframeMastery.clear()
                self.warframe_normalPicture.clear()
                self.warframe_primePicture.clear()
                self.warframe_bpPicture.clear()
                self.warframe_neuropticPicture.clear()
                self.warframe_chassisPicture.clear()
                self.warframe_systemPicture.clear()

                self.warframe_normalPicture.setStyleSheet('border: none')
                self.warframe_bpPicture.setStyleSheet('border: none')
                self.warframe_neuropticPicture.setStyleSheet('border: none')
                self.warframe_chassisPicture.setStyleSheet('border: none')
                self.warframe_systemPicture.setStyleSheet('border: none')
                self.warframe_primePicture.setStyleSheet('border: none')
        #Primary page
        elif option == 'p':
            try:
                name,normal,prime,prime_parts,mastery = s.primary(weapon = self.line_primarySelect.text().strip())
                self.label_primary.setText(name)
                self.label_primaryLeft.setText(f'{name} Normal Variant\n'
                f'{normal}')
                self.label_primaryMiddle.setText(f'Prime parts needed for {name} Prime\n'
                f'{prime_parts}')
                self.label_primaryRight.setText(f'{name} Prime Variant\n'
                f'{prime}')
                self.label_primaryMastery.setText(f'{name} Mastery: {mastery}')
                self.line_primarySelect.clear()

                #Normal colored borders
                self.primary_normalPic.show()
                if normal == 'Owned':
                    self.primary_normalPic.setStyleSheet('border: 5px solid green;')
                else:
                    self.primary_normalPic.setStyleSheet('border: 5px solid red;')
                
                #Check if primary has prime variant
                check = s.primary_checkPrime(name)

                if check is True:
                    self.primary_primePic.show()

                    if prime == 'Owned':
                        self.primary_primePic.setStyleSheet('border: 5px solid green;')
                    else:
                        self.primary_primePic.setStyleSheet('border: 5px solid red;')

                    info = s.primary_parts(name)
                    if len(info) == 4:
                        self.primary_fivePic_1.setHidden(True)
                        self.primary_fivePic_2.setHidden(True)
                        self.primary_fivePic_3.setHidden(True)
                        self.primary_fivePic_4.setHidden(True)
                        self.primary_fivePic_5.setHidden(True)

                        self.primary_fourPic_1.show()
                        self.primary_fourPic_2.show()
                        self.primary_fourPic_3.show()
                        self.primary_fourPic_4.show()

                        if info[0] in prime_parts:
                            self.primary_fourPic_1.setStyleSheet('border: 5px solid red;')
                        else:
                            self.primary_fourPic_1.setStyleSheet('border: 5px solid green;')
                        
                        if info[1] in prime_parts:
                            self.primary_fourPic_2.setStyleSheet('border: 5px solid red;')
                        else:
                            self.primary_fourPic_2.setStyleSheet('border: 5px solid green;')
                        
                        if info[2] in prime_parts:
                            self.primary_fourPic_3.setStyleSheet('border: 5px solid red;')
                        else:
                            self.primary_fourPic_3.setStyleSheet('border: 5px solid green;')
                        
                        if info[3] in prime_parts:
                            self.primary_fourPic_4.setStyleSheet('border: 5px solid red;')
                        else:
                            self.primary_fourPic_4.setStyleSheet('border: 5px solid green;')
                    
                    if len(info) == 5:
                        self.primary_fivePic_1.show()
                        self.primary_fivePic_2.show()
                        self.primary_fivePic_3.show()
                        self.primary_fivePic_4.show()
                        self.primary_fivePic_5.show()

                        self.primary_fourPic_1.setHidden(True)
                        self.primary_fourPic_2.setHidden(True)
                        self.primary_fourPic_3.setHidden(True)
                        self.primary_fourPic_4.setHidden(True)

                        if info[0] in prime_parts:
                            self.primary_fivePic_1.setStyleSheet('border: 5px solid red;')
                        else:
                            self.primary_fivePic_1.setStyleSheet('border: 5px solid green;')
                        
                        if info[1] in prime_parts:
                            self.primary_fivePic_2.setStyleSheet('border: 5px solid red;')
                        else:
                            self.primary_fivePic_2.setStyleSheet('border: 5px solid green;')
                        
                        if info[2] in prime_parts:
                            self.primary_fivePic_3.setStyleSheet('border: 5px solid red;')
                        else:
                            self.primary_fivePic_3.setStyleSheet('border: 5px solid green;')
                        
                        if info[3] in prime_parts:
                            self.primary_fivePic_4.setStyleSheet('border: 5px solid red;')
                        else:
                            self.primary_fivePic_4.setStyleSheet('border: 5px solid green;')
                        
                        if info[4] in prime_parts:
                            self.primary_fivePic_5.setStyleSheet('border: 5px solid red;')
                        else:
                            self.primary_fivePic_5.setStyleSheet('border: 5px solid green;')
                #If no prime variant hide prime picture labels
                else:
                    self.primary_fivePic_1.setHidden(True)
                    self.primary_fivePic_2.setHidden(True)
                    self.primary_fivePic_3.setHidden(True)
                    self.primary_fivePic_4.setHidden(True)
                    self.primary_fivePic_5.setHidden(True)
        
                    self.primary_fourPic_1.setHidden(True)
                    self.primary_fourPic_2.setHidden(True)
                    self.primary_fourPic_3.setHidden(True)
                    self.primary_fourPic_4.setHidden(True)

                    self.primary_primePic.setHidden(True)

            except TypeError:
                self.label_primary.setText('Invalid Entry')
                self.label_primaryMiddle.setText(f'Entry was either mispelled or incorrect\n'
                f'Double check your entry\n'
                f'Your entry: {self.line_primarySelect.text()}\n'
                f'Was not recognized as a primary weapon')

                self.line_primarySelect.clear()
                self.label_primaryLeft.clear()
                self.label_primaryRight.clear()
                self.label_primaryMastery.clear()

                self.primary_fivePic_1.setHidden(True)
                self.primary_fivePic_2.setHidden(True)
                self.primary_fivePic_3.setHidden(True)
                self.primary_fivePic_4.setHidden(True)
                self.primary_fivePic_5.setHidden(True)
    
                self.primary_fourPic_1.setHidden(True)
                self.primary_fourPic_2.setHidden(True)
                self.primary_fourPic_3.setHidden(True)
                self.primary_fourPic_4.setHidden(True)

                self.primary_normalPic.setHidden(True)
                self.primary_primePic.setHidden(True)
            except ValueError:
                self.label_primary.setText('No Entry')
                self.label_primaryMiddle.setText(f'No entry was made\n'
                f'Please enter a primary weapon to continue')

                self.line_primarySelect.clear()
                self.label_primaryLeft.clear()
                self.label_primaryRight.clear()
                self.label_primaryMastery.clear()

                self.primary_fivePic_1.setHidden(True)
                self.primary_fivePic_2.setHidden(True)
                self.primary_fivePic_3.setHidden(True)
                self.primary_fivePic_4.setHidden(True)
                self.primary_fivePic_5.setHidden(True)
    
                self.primary_fourPic_1.setHidden(True)
                self.primary_fourPic_2.setHidden(True)
                self.primary_fourPic_3.setHidden(True)
                self.primary_fourPic_4.setHidden(True)

                self.primary_normalPic.setHidden(True)
                self.primary_primePic.setHidden(True)
            
        #Secondary page
        elif option == 's':
            try:
                name,normal,prime,prime_parts,mastery = s.secondary(self.line_secondarySelect.text().strip().capitalize())
                self.label_secondary.setText(name)
                self.label_secondaryLeft.setText(f'{name} Normal Variant\n'
                f'{normal}')
                self.label_secondaryMiddle.setText(f'Prime parts needed for {name} Prime\n'
                f'{prime_parts}')
                self.label_secondaryRight.setText(f'{name} Prime Variant\n'
                f'{prime}')
                self.label_secondaryMastery.setText(f'{name} Mastery: {mastery}')
                self.line_secondarySelect.clear()

                #Normal colored borders
                self.secondary_normalPic.show()
                if normal == 'Owned':
                    self.secondary_normalPic.setStyleSheet('border: 5px solid green;')
                else:
                    self.secondary_normalPic.setStyleSheet('border: 5px solid red;')

                #Check if secondary has prime variant
                check = s.secondary_checkPrime(name)

                if check is True:
                    self.secondary_primePic.show()

                    if prime == 'Owned':
                        self.secondary_primePic.setStyleSheet('border: 5px solid green;')
                    else:
                        self.secondary_primePic.setStyleSheet('border: 5px solid red;')
            
                    #Check prime parts against total prime parts
                    #Sort prime part and their numbers
                    info = s.secondary_parts(name)

                    part_inv = s.secondary_partNum(prime_parts)
                    part_total = s.secondary_partNumTotal(info)

                    if len(info) == 3:
                        self.secondary_threePic_1.show()
                        self.secondary_threePic_2.show()
                        self.secondary_threePic_3.show()

                        self.secondary_fourPic_1.setHidden(True)
                        self.secondary_fourPic_2.setHidden(True)
                        self.secondary_fourPic_3.setHidden(True)
                        self.secondary_fourPic_4.setHidden(True)

                        self.secondary_fivePic_1.setHidden(True)
                        self.secondary_fivePic_2.setHidden(True)
                        self.secondary_fivePic_3.setHidden(True)
                        self.secondary_fivePic_4.setHidden(True)
                        self.secondary_fivePic_5.setHidden(True)

                        for a in part_total:
                            #Checks for item is list
                            if isinstance(a, list):
                                part_name = a[0]
                                if part_name in prime_parts:
                                    #Items here will be red or orange
                                    #Color depends on how much of item is needed
                                    for b in part_inv:
                                        if isinstance(b, list):
                                            if b[0] == 'Pouch':
                                                if b[1] == a[1]:
                                                    self.secondary_threePic_2.setStyleSheet('border: 5px solid red')
                                                else:
                                                    self.secondary_threePic_2.setStyleSheet('border: 5px solid orange')
                                            elif b[0] == 'Stars':
                                                if b[1] == a[1]:
                                                    self.secondary_threePic_3.setStyleSheet('border: 5px solid red')
                                                else:
                                                    self.secondary_threePic_3.setStyleSheet('border: 5px solid orange')
                                            elif b[0] == 'Blade':
                                                if b[1] == a[1]:
                                                    self.secondary_threePic_3.setStyleSheet('border: 5px solid red')
                                                else:
                                                    self.secondary_threePic_3.setStyleSheet('border: 5px solid orange')
                                else:
                                    #Items here will be green
                                    ###print(f'{part_name} is not in prime_parts')
                                    if part_name == 'Pouch':
                                        self.secondary_threePic_2.setStyleSheet('border: 5px solid green')
                                    elif part_name == 'Stars':
                                        self.secondary_threePic_3.setStyleSheet('border: 5px solid green')
                                    elif part_name == 'Blade':
                                        self.secondary_threePic_3.setStyleSheet('border: 5px solid green')

                            else:
                                if a in prime_parts:
                                    if a == 'BP':
                                        self.secondary_threePic_1.setStyleSheet('border: 5px solid red')
                                    elif a == 'Barrel':
                                        self.secondary_threePic_2.setStyleSheet('border: 5px solid red')
                                    elif a == 'Receiver':
                                        self.secondary_threePic_3.setStyleSheet('border: 5px solid red')
                                else:
                                    if a == 'BP':
                                        self.secondary_threePic_1.setStyleSheet('border: 5px solid green')
                                    elif a == 'Barrel':
                                        self.secondary_threePic_2.setStyleSheet('border: 5px solid green')
                                    elif a == 'Receiver':
                                        self.secondary_threePic_3.setStyleSheet('border: 5px solid green')

                    if len(info) == 4:
                        self.secondary_threePic_1.setHidden(True)
                        self.secondary_threePic_2.setHidden(True)
                        self.secondary_threePic_3.setHidden(True)

                        self.secondary_fourPic_1.show()
                        self.secondary_fourPic_2.show()
                        self.secondary_fourPic_3.show()
                        self.secondary_fourPic_4.show()

                        self.secondary_fivePic_1.setHidden(True)
                        self.secondary_fivePic_2.setHidden(True)
                        self.secondary_fivePic_3.setHidden(True)
                        self.secondary_fivePic_4.setHidden(True)
                        self.secondary_fivePic_5.setHidden(True)

                        for a in part_total:
                            #Checks for item is list
                            if isinstance(a, list):
                                part_name = a[0]
                                if part_name in prime_parts:
                                    #Items here will be red or orange
                                    #Color depends on how much of item is needed
                                    for b in part_inv:
                                        if isinstance(b, list):
                                            if b[0] == 'Barrel':
                                                if b[1] == a[1]:
                                                    self.secondary_fourPic_2.setStyleSheet('border: 5px solid red')
                                                else:
                                                    self.secondary_fourPic_2.setStyleSheet('border: 5px solid orange')
                                            elif b[0] == 'Receiver':
                                                if b[1] == a[1]:
                                                    self.secondary_fourPic_3.setStyleSheet('border: 5px solid red')
                                                else:
                                                    self.secondary_fourPic_3.setStyleSheet('border: 5px solid orange')
                                else:
                                    #Items here will be green
                                    ###print(f'{part_name} is not in prime_parts')
                                    if part_name == 'Barrel':
                                        self.secondary_fourPic_2.setStyleSheet('border: 5px solid green')
                                    elif part_name == 'Receiver':
                                        self.secondary_fourPic_3.setStyleSheet('border: 5px solid green')

                            else:
                                if a in prime_parts:
                                    if a == 'BP':
                                        self.secondary_fourPic_1.setStyleSheet('border: 5px solid red')
                                    elif a == 'Link':
                                        self.secondary_fourPic_2.setStyleSheet('border: 5px solid red')
                                    else:
                                        new_name = a.replace('Ak','').capitalize()
                                        self.secondary_fourPic_2.setStyleSheet('border: 5px solid red')
                                        self.secondary_fourPic_3.setStyleSheet('border: 5px solid red')
                                else:
                                    if a == 'BP':
                                        self.secondary_fourPic_1.setStyleSheet('border: 5px solid green')
                                    elif a == 'Link':
                                        self.secondary_fourPic_2.setStyleSheet('border: 5px solid green')
                                    else:
                                        new_name = a.replace('Ak','').capitalize()
                                        self.secondary_fourPic_2.setStyleSheet('border: 5px solid green')
                                        self.secondary_fourPic_3.setStyleSheet('border: 5px solid green')

                    if len(info) == 5:
                        self.secondary_threePic_1.setHidden(True)
                        self.secondary_threePic_2.setHidden(True)
                        self.secondary_threePic_3.setHidden(True)

                        self.secondary_fourPic_1.setHidden(True)
                        self.secondary_fourPic_2.setHidden(True)
                        self.secondary_fourPic_3.setHidden(True)
                        self.secondary_fourPic_4.setHidden(True)

                        self.secondary_fivePic_1.show()
                        self.secondary_fivePic_2.show()
                        self.secondary_fivePic_3.show()
                        self.secondary_fivePic_4.show()
                        self.secondary_fivePic_5.show()

                        if info[0] in prime_parts:
                            self.secondary_fivePic_1.setStyleSheet('border: 5px solid red;')
                        else:
                            self.secondary_fivePic_1.setStyleSheet('border: 5px solid green;')
                        
                        if info[1] in prime_parts:
                            self.secondary_fivePic_2.setStyleSheet('border: 5px solid red;')
                        else:
                            self.secondary_fivePic_2.setStyleSheet('border: 5px solid green;')
                        
                        if info[2] in prime_parts:
                            self.secondary_fivePic_3.setStyleSheet('border: 5px solid red;')
                        else:
                            self.secondary_fivePic_3.setStyleSheet('border: 5px solid green;')
                        
                        if info[3] in prime_parts:
                            self.secondary_fivePic_4.setStyleSheet('border: 5px solid red;')
                        else:
                            self.secondary_fivePic_4.setStyleSheet('border: 5px solid green;')
                        
                        if info[4] in prime_parts:
                            self.secondary_fivePic_5.setStyleSheet('border: 5px solid red;')
                        else:
                            self.secondary_fivePic_5.setStyleSheet('border: 5px solid green;')
                        
                #If no prime variant hide prime picture labels
                else:
                    self.secondary_fivePic_1.setHidden(True)
                    self.secondary_fivePic_2.setHidden(True)
                    self.secondary_fivePic_3.setHidden(True)
                    self.secondary_fivePic_4.setHidden(True)
                    self.secondary_fivePic_5.setHidden(True)
        
                    self.secondary_fourPic_1.setHidden(True)
                    self.secondary_fourPic_2.setHidden(True)
                    self.secondary_fourPic_3.setHidden(True)
                    self.secondary_fourPic_4.setHidden(True)

                    self.secondary_threePic_1.setHidden(True)
                    self.secondary_threePic_2.setHidden(True)
                    self.secondary_threePic_3.setHidden(True)

                    self.secondary_primePic.setHidden(True)



            except TypeError:
                self.label_secondary.setText('Invalid Entry')
                self.label_secondaryMiddle.setText(f'Entry was either mispelled or incorrect\n'
                f'Double check your entry\n'
                f'Your entry: {self.line_secondarySelect.text()}\n'
                f'Was not recognized as a secondary weapon')
                
                self.line_secondarySelect.clear()
                self.label_secondaryLeft.clear()
                self.label_secondaryRight.clear()
                self.label_secondaryMastery.clear()

                self.secondary_fivePic_1.setHidden(True)
                self.secondary_fivePic_2.setHidden(True)
                self.secondary_fivePic_3.setHidden(True)
                self.secondary_fivePic_4.setHidden(True)
                self.secondary_fivePic_5.setHidden(True)
        
                self.secondary_fourPic_1.setHidden(True)
                self.secondary_fourPic_2.setHidden(True)
                self.secondary_fourPic_3.setHidden(True)
                self.secondary_fourPic_4.setHidden(True)

                self.secondary_threePic_1.setHidden(True)
                self.secondary_threePic_2.setHidden(True)
                self.secondary_threePic_3.setHidden(True)

                self.secondary_normalPic.setHidden(True)
                self.secondary_primePic.setHidden(True)


            except ValueError:
                self.label_secondary.setText('No Entry')
                self.label_secondaryMiddle.setText(f'No entry was made\n'
                f'Please enter a secondary weapon to continue')

                self.line_secondarySelect.clear()
                self.label_secondaryLeft.clear()
                self.label_secondaryRight.clear()
                self.label_secondaryMastery.clear()

                self.secondary_fivePic_1.setHidden(True)
                self.secondary_fivePic_2.setHidden(True)
                self.secondary_fivePic_3.setHidden(True)
                self.secondary_fivePic_4.setHidden(True)
                self.secondary_fivePic_5.setHidden(True)
        
                self.secondary_fourPic_1.setHidden(True)
                self.secondary_fourPic_2.setHidden(True)
                self.secondary_fourPic_3.setHidden(True)
                self.secondary_fourPic_4.setHidden(True)

                self.secondary_threePic_1.setHidden(True)
                self.secondary_threePic_2.setHidden(True)
                self.secondary_threePic_3.setHidden(True)

                self.secondary_normalPic.setHidden(True)
                self.secondary_primePic.setHidden(True)

        #Melee page
        elif option == 'm':
            try:
                name,normal,prime,prime_parts,mastery = s.melee(self.line_meleeSelect.text().strip())
                self.label_melee.setText(name)
                self.label_meleeLeft.setText(f'{name} Normal Variant\n'
                f'{normal}')
                self.label_meleeMiddle.setText(f'Prime parts needed for {name} Prime\n'
                f'{prime_parts}')
                self.label_meleeRight.setText(f'{name} Prime Variant\n'
                f'{prime}')
                self.label_meleeMastery.setText(f'{name} Mastery: {mastery}')
                self.line_meleeSelect.clear()

                #Normal colored borders
                self.melee_normalPic.show()
                if normal == 'Owned':
                    self.melee_normalPic.setStyleSheet('border: 5px solid green;')
                else:
                    self.melee_normalPic.setStyleSheet('border: 5px solid red;')

                #Check if melee has prime variant
                check = s.melee_checkPrime(name)

                if check is True:
                    self.melee_primePic.show()

                    if prime == 'Owned':
                        self.melee_primePic.setStyleSheet('border: 5px solid green;')
                    else:
                        self.melee_primePic.setStyleSheet('border: 5px solid red;')

                    info = s.melee_parts(name)

                    part_inv = s.melee_partNum(prime_parts)
                    part_total = s.melee_partNumTotal(info)

                    if len(info) == 3:
                        self.melee_threePic_1.show()
                        self.melee_threePic_2.show()
                        self.melee_threePic_3.show()

                        self.melee_fourPic_1.setHidden(True)
                        self.melee_fourPic_2.setHidden(True)
                        self.melee_fourPic_3.setHidden(True)
                        self.melee_fourPic_4.setHidden(True)

                        for a in part_total:
                            #Checks for item is list
                            if isinstance(a, list):
                                part_name = a[0]
                                if part_name in prime_parts:
                                    #Items here will be red or orange
                                    #Color depends on how much of item is needed
                                    for b in part_inv:
                                        if isinstance(b, list):
                                            if b[0] == 'Blade':
                                                if b[1] == a[1]:
                                                    self.melee_threePic_2.setStyleSheet('border: 5px solid red')
                                                else:
                                                    self.melee_threePic_2.setStyleSheet('border: 5px solid orange')
                                            elif b[0] == 'Ornament':
                                                if b[1] == a[1]:
                                                    self.melee_threePic_2.setStyleSheet('border: 5px solid red')
                                                else:
                                                    self.melee_threePic_2.setStyleSheet('border: 5px solid orange')
                                            elif b[0] == 'Boot':
                                                if b[1] == a[1]:
                                                    self.melee_threePic_2.setStyleSheet('border: 5px solid red')
                                                else:
                                                    self.melee_threePic_2.setStyleSheet('border: 5px solid orange')
                                            elif b[0] == 'Gauntlet':
                                                if b[1] == a[1]:
                                                    self.melee_threePic_3.setStyleSheet('border: 5px solid red')
                                                else:
                                                    self.melee_threePic_3.setStyleSheet('border: 5px solid orange')
                                            elif b[0] == 'Handle':
                                                if b[1] == a[1]:
                                                    self.melee_threePic_3.setStyleSheet('border: 5px solid red')
                                                else:
                                                    self.melee_threePic_3.setStyleSheet('border: 5px solid orange')
                                else:
                                    #Items here will be green
                                    if part_name == 'Blade':
                                        self.melee_threePic_2.setStyleSheet('border: 5px solid green')
                                    elif part_name == 'Ornament':
                                        self.melee_threePic_2.setStyleSheet('border: 5px solid green')
                                    elif part_name == 'Boot':
                                        self.melee_threePic_2.setStyleSheet('border: 5px solid green')
                                    elif part_name == 'Gauntlet':
                                        self.melee_threePic_3.setStyleSheet('border: 5px solid green')
                                    elif part_name == 'Handle':
                                        self.melee_threePic_3.setStyleSheet('border: 5px solid green')

                            else:
                                if a in prime_parts:
                                    if a == 'BP':
                                        self.melee_threePic_1.setStyleSheet('border: 5px solid red')
                                    elif a == 'Head':
                                        self.melee_threePic_2.setStyleSheet('border: 5px solid red')
                                    elif a == 'Blade':
                                        self.melee_threePic_2.setStyleSheet('border: 5px solid red')
                                    elif a == 'Handle':
                                        self.melee_threePic_3.setStyleSheet('border: 5px solid red')
                                    elif a == 'Disc':
                                        self.melee_threePic_3.setStyleSheet('border: 5px solid red')
                                    elif a == 'Hilt':
                                        self.melee_threePic_3.setStyleSheet('border: 5px solid red')
                                    
                                else:
                                    if a == 'BP':
                                        self.melee_threePic_1.setStyleSheet('border: 5px solid green')
                                    elif a == 'Head':
                                        self.melee_threePic_2.setStyleSheet('border: 5px solid green')
                                    elif a == 'Blade':
                                        self.melee_threePic_2.setStyleSheet('border: 5px solid green')
                                    elif a == 'Handle':
                                        self.melee_threePic_3.setStyleSheet('border: 5px solid green')
                                    elif a == 'Disc':
                                        self.melee_threePic_3.setStyleSheet('border: 5px solid green')
                                    elif a == 'Hilt':
                                        self.melee_threePic_3.setStyleSheet('border: 5px solid green')
                    
                    if len(info) == 4:
                        self.melee_threePic_1.setHidden(True)
                        self.melee_threePic_2.setHidden(True)
                        self.melee_threePic_3.setHidden(True)

                        self.melee_fourPic_1.show()
                        self.melee_fourPic_2.show()
                        self.melee_fourPic_3.show()
                        self.melee_fourPic_4.show()

                        if info[0] in prime_parts:
                            self.melee_fourPic_1.setStyleSheet('border: 5px solid red;')
                        else:
                            self.melee_fourPic_1.setStyleSheet('border: 5px solid green;')
                        
                        if info[1] in prime_parts:
                            self.melee_fourPic_2.setStyleSheet('border: 5px solid red;')
                        else:
                            self.melee_fourPic_2.setStyleSheet('border: 5px solid green;')

                        if info[2] in prime_parts:
                            self.melee_fourPic_3.setStyleSheet('border: 5px solid red;')
                        else:
                            self.melee_fourPic_3.setStyleSheet('border: 5px solid green;')
                        
                        if info[3] in prime_parts:
                            self.melee_fourPic_4.setStyleSheet('border: 5px solid red;')
                        else:
                            self.melee_fourPic_4.setStyleSheet('border: 5px solid green;')
                    
                #If no prime variant hide prime picture labels
                else:
                    self.melee_fourPic_1.setHidden(True)
                    self.melee_fourPic_2.setHidden(True)
                    self.melee_fourPic_3.setHidden(True)
                    self.melee_fourPic_4.setHidden(True)

                    self.melee_threePic_1.setHidden(True)
                    self.melee_threePic_2.setHidden(True)
                    self.melee_threePic_3.setHidden(True)

                    self.melee_primePic.setHidden(True)

            except TypeError:
                self.label_melee.setText('Invalid Entry')
                self.label_meleeMiddle.setText(f'Entry was either mispelled or incorrect\n'
                f'Double check your entry\n'
                f'Your entry: {self.line_meleeSelect.text()}\n'
                f'Was not recognized as a melee weapon')
                
                self.line_meleeSelect.clear()
                self.label_meleeLeft.clear()
                self.label_meleeRight.clear()
                self.label_meleeMastery.clear()
        
                self.melee_fourPic_1.setHidden(True)
                self.melee_fourPic_2.setHidden(True)
                self.melee_fourPic_3.setHidden(True)
                self.melee_fourPic_4.setHidden(True)

                self.melee_threePic_1.setHidden(True)
                self.melee_threePic_2.setHidden(True)
                self.melee_threePic_3.setHidden(True)

                self.melee_normalPic.setHidden(True)
                self.melee_primePic.setHidden(True)

            except ValueError:
                self.label_melee.setText('No Entry')
                self.label_meleeMiddle.setText(f'No entry was made\n'
                f'Please enter a melee weapon to continue')

                self.line_meleeSelect.clear()
                self.label_meleeLeft.clear()
                self.label_meleeRight.clear()
                self.label_meleeMastery.clear()
        
                self.melee_fourPic_1.setHidden(True)
                self.melee_fourPic_2.setHidden(True)
                self.melee_fourPic_3.setHidden(True)
                self.melee_fourPic_4.setHidden(True)

                self.melee_threePic_1.setHidden(True)
                self.melee_threePic_2.setHidden(True)
                self.melee_threePic_3.setHidden(True)

                self.melee_normalPic.setHidden(True)
                self.melee_primePic.setHidden(True)


    def onChecked(self, option):
        """
        Method to display variant information when variant radio button is clicked
        :param option: Determines variant list based on option
        :return: Displays variant list based on option
        """
        if option == 'p':
            if self.radio_primary.isChecked():
                self.list_primaryVariant.show()
            else:
                self.list_primaryVariant.setHidden(True)
                self.list_primaryVariant.clearSelection()
                self.list_primaryVariant.collapseAll()
        if option == 's':
            if self.radio_secondary.isChecked():
                self.list_secondaryVariant.show()
            else:
                self.list_secondaryVariant.setHidden(True)
                self.list_secondaryVariant.clearSelection()
                self.list_secondaryVariant.collapseAll()
        if option== 'm':
            if self.radio_melee.isChecked():
                self.list_meleeVariant.show()
            else:
                self.list_meleeVariant.setHidden(True)
                self.list_meleeVariant.clearSelection()
                self.list_meleeVariant.collapseAll()


    def onClicked(self, option):
        """
        Method to show variant information based on selection
        :param option: Determines which variant list is accessed
        :return: Display variant info based on option
        """
        if option == 'p':
            try:
                variant = self.list_primaryVariant.currentItem().parent().text(0)
                name = self.list_primaryVariant.currentItem().text(0)
                owned,mastery=s.primary_variant(variant, name)
                self.label_primary.setText(name)
                self.label_primaryLeft.setText(f'{variant}\n'
                f'{name} is {owned}')
                self.label_primaryMastery.setText(f'{variant} {name} Mastery: {mastery}')

                self.line_primarySelect.clear()
                self.label_primaryMiddle.clear()
                self.label_primaryRight.clear()
                self.list_primaryVariant.clearSelection()
                self.list_primaryVariant.collapseAll()
                
                self.primary_normalPic.setStyleSheet('border: None')
                self.primary_primePic.setStyleSheet('border: None')
                self.primary_fourPic_1.setStyleSheet('border: None')
                self.primary_fourPic_2.setStyleSheet('border: None')
                self.primary_fourPic_3.setStyleSheet('border: None')
                self.primary_fourPic_4.setStyleSheet('border: None')
                self.primary_fivePic_1.setStyleSheet('border: None')
                self.primary_fivePic_2.setStyleSheet('border: None')
                self.primary_fivePic_3.setStyleSheet('border: None')
                self.primary_fivePic_4.setStyleSheet('border: None')
                self.primary_fivePic_5.setStyleSheet('border: None')

            except AttributeError:
                self.label_primary.setText('Variant Not Selected')
                self.label_primaryMiddle.setText(f'No primary variant was selected\n'
                f'Select a primary variant and try again')

                self.line_primarySelect.clear()
                self.label_primaryRight.clear()
                self.label_primaryLeft.clear()
                self.label_primaryMastery.clear()
                self.list_primaryVariant.clearSelection()
                self.list_primaryVariant.collapseAll() 

                self.primary_normalPic.setStyleSheet('border: None')
                self.primary_primePic.setStyleSheet('border: None')
                self.primary_fourPic_1.setStyleSheet('border: None')
                self.primary_fourPic_2.setStyleSheet('border: None')
                self.primary_fourPic_3.setStyleSheet('border: None')
                self.primary_fourPic_4.setStyleSheet('border: None')
                self.primary_fivePic_1.setStyleSheet('border: None')
                self.primary_fivePic_2.setStyleSheet('border: None')
                self.primary_fivePic_3.setStyleSheet('border: None')
                self.primary_fivePic_4.setStyleSheet('border: None')
                self.primary_fivePic_5.setStyleSheet('border: None')

        if option == 's':
            try:
                variant = self.list_secondaryVariant.currentItem().parent().text(0)
                name = self.list_secondaryVariant.currentItem().text(0)
                owned,mastery=s.secondary_variant(variant, name)
                self.label_secondary.setText(name)
                self.label_secondaryLeft.setText(f'{variant}\n'
                f'{name} is {owned}')
                self.label_secondaryMastery.setText(f'{variant} {name} Mastery: {mastery}')

                self.line_secondarySelect.clear()
                self.label_secondaryMiddle.clear()
                self.label_secondaryRight.clear()
                self.list_secondaryVariant.clearSelection()
                self.list_secondaryVariant.collapseAll()

                self.secondary_normalPic.setStyleSheet('border: None')
                self.secondary_primePic.setStyleSheet('border: None')
                self.secondary_threePic_1.setStyleSheet('border: None')
                self.secondary_threePic_2.setStyleSheet('border: None')
                self.secondary_threePic_3.setStyleSheet('border: None')
                self.secondary_fourPic_1.setStyleSheet('border: None')
                self.secondary_fourPic_2.setStyleSheet('border: None')
                self.secondary_fourPic_3.setStyleSheet('border: None')
                self.secondary_fourPic_4.setStyleSheet('border: None')
                self.secondary_fivePic_1.setStyleSheet('border: None')
                self.secondary_fivePic_2.setStyleSheet('border: None')
                self.secondary_fivePic_3.setStyleSheet('border: None')
                self.secondary_fivePic_4.setStyleSheet('border: None')
                self.secondary_fivePic_5.setStyleSheet('border: None')

            except AttributeError:
                self.label_secondary.setText('Variant Not Selected')
                self.label_secondaryMiddle.setText(f'No primary variant was selected\n'
                f'Select a primary variant and try again')

                self.line_secondarySelect.clear()
                self.label_secondaryRight.clear()
                self.label_secondaryLeft.clear()
                self.label_secondaryMastery.clear()
                self.list_secondaryVariant.clearSelection()
                self.list_secondaryVariant.collapseAll()

                self.secondary_normalPic.setStyleSheet('border: None')
                self.secondary_primePic.setStyleSheet('border: None')
                self.secondary_threePic_1.setStyleSheet('border: None')
                self.secondary_threePic_2.setStyleSheet('border: None')
                self.secondary_threePic_3.setStyleSheet('border: None')
                self.secondary_fourPic_1.setStyleSheet('border: None')
                self.secondary_fourPic_2.setStyleSheet('border: None')
                self.secondary_fourPic_3.setStyleSheet('border: None')
                self.secondary_fourPic_4.setStyleSheet('border: None')
                self.secondary_fivePic_1.setStyleSheet('border: None')
                self.secondary_fivePic_2.setStyleSheet('border: None')
                self.secondary_fivePic_3.setStyleSheet('border: None')
                self.secondary_fivePic_4.setStyleSheet('border: None')
                self.secondary_fivePic_5.setStyleSheet('border: None')

        if option == 'm':
            try:
                variant = self.list_meleeVariant.currentItem().parent().text(0)
                name = self.list_meleeVariant.currentItem().text(0)
                owned,mastery=s.melee_variant(variant, name)
                self.label_melee.setText(name)
                self.label_meleeLeft.setText(f'{variant}\n'
                f'{name} is {owned}')
                self.label_meleeMastery.setText(f'{variant} {name} Mastery: {mastery}')

                self.line_meleeSelect.clear()
                self.label_meleeMiddle.clear()
                self.label_meleeRight.clear()
                self.list_meleeVariant.clearSelection()
                self.list_meleeVariant.collapseAll()

                self.melee_normalPic.setStyleSheet('border: None')
                self.melee_primePic.setStyleSheet('border: None')
                self.melee_threePic_1.setStyleSheet('border: None')
                self.melee_threePic_2.setStyleSheet('border: None')
                self.melee_threePic_3.setStyleSheet('border: None')
                self.melee_fourPic_1.setStyleSheet('border: None')
                self.melee_fourPic_2.setStyleSheet('border: None')
                self.melee_fourPic_3.setStyleSheet('border: None')
                self.melee_fourPic_4.setStyleSheet('border: None')
            except AttributeError:
                self.label_melee.setText('Variant Not Selected')
                self.label_meleeMiddle.setText(f'No primary variant was selected\n'
                f'Select a primary variant and try again')

                self.line_meleeSelect.clear()
                self.label_meleeRight.clear()
                self.label_meleeLeft.clear()
                self.label_meleeMastery.clear()
                self.list_meleeVariant.clearSelection()
                self.list_meleeVariant.collapseAll()

                self.melee_normalPic.setStyleSheet('border: None')
                self.melee_primePic.setStyleSheet('border: None')
                self.melee_threePic_1.setStyleSheet('border: None')
                self.melee_threePic_2.setStyleSheet('border: None')
                self.melee_threePic_3.setStyleSheet('border: None')
                self.melee_fourPic_1.setStyleSheet('border: None')
                self.melee_fourPic_2.setStyleSheet('border: None')
                self.melee_fourPic_3.setStyleSheet('border: None')
                self.melee_fourPic_4.setStyleSheet('border: None')


    def clearPage(self):
        """
        Method to clear page based on current stackedWidget index
        :return: None
        """
        if self.stackedWidget.currentIndex() == 0:
            self.label_warframe.setText('Select your Warframe')
            self.label_warframeLeft.clear()
            self.label_warframeMiddle.clear()
            self.label_warframeRight.clear()
            self.label_warframeMastery.clear()
            self.line_warframeSelect.clear()

            self.warframe_normalPicture.setStyleSheet('border: None')
            self.warframe_primePicture.setStyleSheet('border: None')
            self.warframe_bpPicture.setStyleSheet('border: None')
            self.warframe_neuropticPicture.setStyleSheet('border: None')
            self.warframe_chassisPicture.setStyleSheet('border: None')
            self.warframe_systemPicture.setStyleSheet('border: None')

        elif self.stackedWidget.currentIndex() == 1:
            self.label_primary.setText('Select your Primary Weapon')
            self.label_primaryLeft.clear()
            self.label_primaryMiddle.clear()
            self.label_primaryRight.clear()
            self.label_primaryMastery.clear()
            self.line_primarySelect.clear()
            self.list_primaryVariant.setHidden(True)
            self.radio_primary.setChecked(False)

            self.primary_normalPic.setStyleSheet('border: None')
            self.primary_primePic.setStyleSheet('border: None')
            self.primary_fourPic_1.setStyleSheet('border: None')
            self.primary_fourPic_2.setStyleSheet('border: None')
            self.primary_fourPic_3.setStyleSheet('border: None')
            self.primary_fourPic_4.setStyleSheet('border: None')
            self.primary_fivePic_1.setStyleSheet('border: None')
            self.primary_fivePic_2.setStyleSheet('border: None')
            self.primary_fivePic_3.setStyleSheet('border: None')
            self.primary_fivePic_4.setStyleSheet('border: None')
            self.primary_fivePic_5.setStyleSheet('border: None')

        elif self.stackedWidget.currentIndex() == 2:
            self.label_secondary.setText('Select your Secondary Weapon')
            self.label_secondaryLeft.clear()
            self.label_secondaryMiddle.clear()
            self.label_secondaryRight.clear()
            self.label_secondaryMastery.clear()
            self.line_secondarySelect.clear()
            self.list_secondaryVariant.setHidden(True)
            self.radio_secondary.setChecked(False)

            self.secondary_normalPic.setStyleSheet('border: None')
            self.secondary_primePic.setStyleSheet('border: None')
            self.secondary_threePic_1.setStyleSheet('border: None')
            self.secondary_threePic_2.setStyleSheet('border: None')
            self.secondary_threePic_3.setStyleSheet('border: None')
            self.secondary_fourPic_1.setStyleSheet('border: None')
            self.secondary_fourPic_2.setStyleSheet('border: None')
            self.secondary_fourPic_3.setStyleSheet('border: None')
            self.secondary_fourPic_4.setStyleSheet('border: None')
            self.secondary_fivePic_1.setStyleSheet('border: None')
            self.secondary_fivePic_2.setStyleSheet('border: None')
            self.secondary_fivePic_3.setStyleSheet('border: None')
            self.secondary_fivePic_4.setStyleSheet('border: None')
            self.secondary_fivePic_5.setStyleSheet('border: None')

        elif self.stackedWidget.currentIndex() == 3:
            self.label_melee.setText('Select your Melee Weapon')
            self.label_meleeLeft.clear()
            self.label_meleeMiddle.clear()
            self.label_meleeRight.clear()
            self.label_meleeMastery.clear()
            self.line_meleeSelect.clear()
            self.list_meleeVariant.setHidden(True)
            self.radio_melee.setChecked(False)

            self.melee_normalPic.setStyleSheet('border: None')
            self.melee_primePic.setStyleSheet('border: None')
            self.melee_threePic_1.setStyleSheet('border: None')
            self.melee_threePic_2.setStyleSheet('border: None')
            self.melee_threePic_3.setStyleSheet('border: None')
            self.melee_fourPic_1.setStyleSheet('border: None')
            self.melee_fourPic_2.setStyleSheet('border: None')
            self.melee_fourPic_3.setStyleSheet('border: None')
            self.melee_fourPic_4.setStyleSheet('border: None')


    def clearAll(self):
        """
        Method to clear all pages
        :return: None
        """
        self.label_warframe.setText('Select your Warframe')
        self.label_warframeLeft.clear()
        self.label_warframeMiddle.clear()
        self.label_warframeRight.clear()
        self.label_warframeMastery.clear()
        self.line_warframeSelect.clear()
        self.warframe_normalPicture.setStyleSheet('border: None')
        self.warframe_primePicture.setStyleSheet('border: None')
        self.warframe_bpPicture.setStyleSheet('border: None')
        self.warframe_neuropticPicture.setStyleSheet('border: None')
        self.warframe_chassisPicture.setStyleSheet('border: None')
        self.warframe_systemPicture.setStyleSheet('border: None')

        self.label_primary.setText('Select your Primary Weapon')
        self.label_primaryLeft.clear()
        self.label_primaryMiddle.clear()
        self.label_primaryRight.clear()
        self.label_primaryMastery.clear()
        self.line_primarySelect.clear()
        self.list_primaryVariant.setHidden(True)
        self.radio_primary.setChecked(False)
        self.primary_normalPic.setStyleSheet('border: None')
        self.primary_primePic.setStyleSheet('border: None')
        self.primary_fourPic_1.setStyleSheet('border: None')
        self.primary_fourPic_2.setStyleSheet('border: None')
        self.primary_fourPic_3.setStyleSheet('border: None')
        self.primary_fourPic_4.setStyleSheet('border: None')
        self.primary_fivePic_1.setStyleSheet('border: None')
        self.primary_fivePic_2.setStyleSheet('border: None')
        self.primary_fivePic_3.setStyleSheet('border: None')
        self.primary_fivePic_4.setStyleSheet('border: None')
        self.primary_fivePic_5.setStyleSheet('border: None')

        self.label_secondary.setText('Select your Secondary Weapon')
        self.label_secondaryLeft.clear()
        self.label_secondaryMiddle.clear()
        self.label_secondaryRight.clear()
        self.label_secondaryMastery.clear()
        self.line_secondarySelect.clear()
        self.list_secondaryVariant.setHidden(True)
        self.radio_secondary.setChecked(False)
        self.secondary_normalPic.setStyleSheet('border: None')
        self.secondary_primePic.setStyleSheet('border: None')
        self.secondary_threePic_1.setStyleSheet('border: None')
        self.secondary_threePic_2.setStyleSheet('border: None')
        self.secondary_threePic_3.setStyleSheet('border: None')
        self.secondary_fourPic_1.setStyleSheet('border: None')
        self.secondary_fourPic_2.setStyleSheet('border: None')
        self.secondary_fourPic_3.setStyleSheet('border: None')
        self.secondary_fourPic_4.setStyleSheet('border: None')
        self.secondary_fivePic_1.setStyleSheet('border: None')
        self.secondary_fivePic_2.setStyleSheet('border: None')
        self.secondary_fivePic_3.setStyleSheet('border: None')
        self.secondary_fivePic_4.setStyleSheet('border: None')
        self.secondary_fivePic_5.setStyleSheet('border: None')

        self.label_melee.setText('Select your Melee Weapon')
        self.label_meleeLeft.clear()
        self.label_meleeMiddle.clear()
        self.label_meleeRight.clear()
        self.label_meleeMastery.clear()
        self.line_meleeSelect.clear()
        self.list_meleeVariant.setHidden(True)
        self.radio_melee.setChecked(False)
        self.melee_normalPic.setStyleSheet('border: None')
        self.melee_primePic.setStyleSheet('border: None')
        self.melee_threePic_1.setStyleSheet('border: None')
        self.melee_threePic_2.setStyleSheet('border: None')
        self.melee_threePic_3.setStyleSheet('border: None')
        self.melee_fourPic_1.setStyleSheet('border: None')
        self.melee_fourPic_2.setStyleSheet('border: None')
        self.melee_fourPic_3.setStyleSheet('border: None')
        self.melee_fourPic_4.setStyleSheet('border: None')