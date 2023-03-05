import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from sifrelerim_2 import *
from PyQt5.QtGui import QIntValidator, QColor
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QDateTime
import sqlite3
from datetime import datetime
import os

class Sifrelerim(QMainWindow):
    def __init__(self):
        super().__init__()
        self.sifrelerim = Ui_sifrelerim_ui()
        self.sifrelerim.setupUi(self)
        self.sifrelerim.kayit_defteri.setHorizontalHeaderLabels(("Şifre Etiketi", "Şifre", "Tarih", "Sil"))
        self.sifrelerim.siralama.currentIndexChanged.connect(self.tablo_siralama)
        self.sifrelerim.ara_lineedit.returnPressed.connect(self.tablo_arama)
        self.sifrelerim.ara_push_but.clicked.connect(self.tablo_arama)
        self.sifrelerim.pushButton.clicked.connect(self.secili_sifre_sil)
        self.sifrelerim.tumunu_sec.clicked.connect(self.tumunu_sec_2)
       

    def closeEvent(self, event):
        self.sifrelerim.kayit_defteri.clearContents()
        self.sifrelerim.kayit_defteri.setRowCount(0)

    def db_baglanti_ac(self):
        try:
            # Veritabanı dosyasının tam yolu
            db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "veri_tabanı", "sifrelerim_db.db"))
            # Veritabanına bağlanma işlemi
            self.data_base = sqlite3.connect(db_path)
            self.islem= self.data_base.cursor()
        except:
            print("Veri Tabanı Bağlantı Hatası")
    
    def db_baglanti_off(self):
        self.data_base.close()

    def db_veri_cekmek(self):
        self.db_baglanti_ac()
        self.islem.execute("SELECT * FROM sifrelerim")
        rows= self.islem.fetchall()

        for row_index, row_data in enumerate(rows):
            self.sifrelerim.kayit_defteri.insertRow(row_index)
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.sifrelerim.kayit_defteri.setItem(row_index, col_index, item)
                self.sifrelerim.kayit_defteri.item(row_index, col_index).setFlags(self.sifrelerim.kayit_defteri.item(row_index, col_index).flags() & ~Qt.ItemIsEditable)

            check_box = QCheckBox()
            self.sifrelerim.kayit_defteri.setCellWidget(row_index, self.sifrelerim.kayit_defteri.columnCount()-1, check_box)
        self.db_baglanti_off()

        
    def db_sifre_ekle(self, liste): # main de şifre oluşturma durumlarının içerisine ekle
        self.db_baglanti_ac()
        for i in liste:
            sifre_etiketi, sifre = i
            tarih = datetime.now()
            
            self.islem.execute("INSERT INTO sifrelerim (\"Şifre Etiketi\", \"Şifre\", \"Tarih\") VALUES (?, ?, ?)", (sifre_etiketi, sifre, tarih))
            self.data_base.commit()
        self.db_baglanti_off()    


    def tablo_siralama (self, index): 
    # Kaydet checkbox durumları
        checkbox_durumlari = {}
        for row in range(self.sifrelerim.kayit_defteri.rowCount()):
            checkbox_durumlari[row] = self.sifrelerim.kayit_defteri.cellWidget(row, 3).isChecked()

        if index == 0:  
            self.sifrelerim.kayit_defteri.sortItems(-1, Qt.AscendingOrder)
        elif index == 1:  # Sort A-Z
            self.sifrelerim.kayit_defteri.sortItems(0, Qt.AscendingOrder)
        elif index == 2:  # Sort Z-A
            self.sifrelerim.kayit_defteri.sortItems(0, Qt.DescendingOrder)
        elif index == 3:  # Sort by Date
            self.sifrelerim.kayit_defteri.sortItems(2, Qt.DescendingOrder)

        # Yükle checkbox durumları
        for row in range(self.sifrelerim.kayit_defteri.rowCount()):
            checkbox = QCheckBox()
            if row in checkbox_durumlari and checkbox_durumlari[row]:
                checkbox.setChecked(True)
            self.sifrelerim.kayit_defteri.setCellWidget(row, 3, checkbox)


    def tablo_arama(self):
        #self.hucre_arkaplan_temizleme()
        search= self.sifrelerim.ara_lineedit.text().capitalize()
        table = self.sifrelerim.kayit_defteri
        for i in range(table.rowCount()):
            item = table.item(i, 0) # "Şifre Etiketi" sütunu
            if item is not None and search in item.text().capitalize():
                #item.setBackground(QColor("yellow"))
                #item.setForeground(QColor("black"))
                row = item.row() 
                table.selectRow(row)
            else:
                self.sifrelerim.statusbar.showMessage("Aramanız ile Eşleşme Bulunamadı, Tekrar Deneyiniz", 5000)
   


    def secili_sifre_sil(self):
        for row in range(self.sifrelerim.kayit_defteri.rowCount()-1, -1, -1):
            if self.sifrelerim.kayit_defteri.cellWidget(row, 3).isChecked():
                sifre_id = self.sifrelerim.kayit_defteri.item(row, 1).text() # sifre id sütununu al
                self.db_baglanti_ac()
                self.islem.execute("DELETE FROM sifrelerim WHERE \"Şifre\"=?", (sifre_id,))
                self.data_base.commit()
                self.db_baglanti_off()
                self.sifrelerim.kayit_defteri.removeRow(row)

            
    def tumunu_sec_2(self):
        for row in range(self.sifrelerim.kayit_defteri.rowCount()):
            checkbox = self.sifrelerim.kayit_defteri.cellWidget(row, 3)
            if checkbox.isChecked():
                checkbox.setChecked(False)
            else:
                checkbox.setChecked(True)
            


    

#app = QApplication(sys.argv)
#pencere1 = Sifrelerim()
#pencere1.show()
#sys.exit(app.exec_())
