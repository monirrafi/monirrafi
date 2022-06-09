#!/usr/bin/python
# -*- coding: UTF-8 -*-
#***************************************************************************#
#                                                                           #
#                                 App.py                                    #
#                                                                           #
#***************************************************************************#
#                                                                           #
# Class App which contains application logic                                #
#                                                                           #
#                                                                           #
#                                                                           #
#***************************************************************************#
# Création     : 29.07.2015  T. Benoit       Version 1.0                    #
# Vérifié      : @@.@@.@@@@  T. Benoit                                      #
# Modification :                                                            #
#***************************************************************************#


from MainUI import MainUI
from PyQt4 import QtCore, QtGui



#---------------------------------------------------------------------------#

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

#---------------------------------------------------------------------------#

class App:

    gui = None
    app = None
    counter = 0

    def __init__(self, guiClass, appClass):
        self.gui = guiClass
        self.app = appClass
        self.counter = 0

    def setup(self):
        """ setup functionnality """
        
        self.gui.pushButton.clicked.connect(self.action)


    def main(self):
        """ Main execution for App """
        self.setup()
        self.gui.main()


    def action(self):
        """ action when I click the push Button """
        self.gui.textEdit.append("Hello world: "+str(self.counter))
        self.counter = self.counter + 1