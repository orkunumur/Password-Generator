import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from sifre_olusturucu import *
from sifrelerim_python_baglanti import *
import random as rd
import string 
from PyQt5.QtGui import QIntValidator
from datetime import datetime

class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = UiMainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_sifre_olustur.clicked.connect(self.sifre_olustur)
        self.ui.rakam_check_box.stateChanged.connect(self.special_case)
        self.Sifrelerim_2= Sifrelerim()
        self.ui.parola_kayit_defteri.triggered.connect(self.on_sifrelerim)
        self.ui.parola_kayit_defteri.triggered.connect(self.Sifrelerim_2.db_veri_cekmek)
        self.ui.pushButton_sifre_kaydet.clicked.connect(self.onay_sifreler_yolla)
        self.ui.pushButton_tumunu_sec.clicked.connect(self.tumunu_sec)
        

    def on_sifrelerim(self):
        self.Sifrelerim_2.show()

    def SifrelerimiAc(self):
        app = QApplication(sys.argv)
        self.pencere1 = Sifrelerim()
        self.pencere1.show()
        sys.exit(app.exec_())


    def sifre_olustur(self):
        validator = QIntValidator(4,30)
        validator_2 = QIntValidator(1,100)
        self.ui.karakter_sayisi_2.setValidator(validator)
        self.ui.sifre_sayisi.setValidator(validator_2)
        for row in range(self.ui.sifre_olustur_table.rowCount()):
            if self.ui.sifre_olustur_table.cellWidget(row, 3).isChecked():
                self.ui.sifre_olustur_table.cellWidget(row, 3).setChecked(False)
            else:
                pass
        try:
            if self.ui.karakter_sayisi_2.hasAcceptableInput() and self.ui.sifre_sayisi.hasAcceptableInput():
                pass
            else:
                raise ValueError("Girilen değerlar sayı olup minimum 4 maksimum 30 olabilir")
        except ValueError as e:     
            self.ui.statusbar.showMessage(str(e), 5000)
            self.ui.karakter_sayisi_2.clear()
            self.ui.sifre_sayisi.clear()
            return 
        
        leng= int(self.ui.karakter_sayisi_2.text())
        nums= int(self.ui.sifre_sayisi.text())

      
        #self.sonuc_signal.emit(self.situation_control(leng, nums))                                  
        self.situation_control(leng, nums)
        #Sifrelerim.db_sifre_ekle()


    def special_case(self):
        if self.ui.rakam_check_box.isChecked():
            self.ui.ozel_karak_check.setChecked(False)
            self.ui.checkBox_buyuk_harf.setChecked(False)
            self.ui.ozel_karak_check.setEnabled(False)
            self.ui.checkBox_buyuk_harf.setEnabled(False)
        else:
            self.ui.ozel_karak_check.setEnabled(True)
            self.ui.checkBox_buyuk_harf.setEnabled(True)  

    def situation_control(self, pass_len, num_pass):
        if not self.ui.checkBox_buyuk_harf.isChecked() and not self.ui.ozel_karak_check.isChecked() and not self.ui.rakam_check_box.isChecked():
            self.default_sit(pass_len, num_pass)
        elif self.ui.rakam_check_box.isChecked() and not self.ui.checkBox_buyuk_harf.isChecked() and not self.ui.ozel_karak_check.isChecked():
            self.only_digit(pass_len, num_pass)
        elif self.ui.checkBox_buyuk_harf.isChecked() and not self.ui.ozel_karak_check.isChecked() and not self.ui.rakam_check_box.isChecked():
            self.upper_lower_digit(pass_len, num_pass)
        elif self.ui.checkBox_buyuk_harf.isChecked() and self.ui.ozel_karak_check.isChecked() and not self.ui.rakam_check_box.isChecked():
            self.upper_lower_digit_punc(pass_len, num_pass)
        elif not self.ui.checkBox_buyuk_harf.isChecked() and self.ui.ozel_karak_check.isChecked() and not self.ui.rakam_check_box.isChecked():
            self.lower_digit_punc(pass_len, num_pass)


    def default_sit(self, pass_len, num_pass):
        pass_list= []
        last_sifre_num = self.ui.sifre_olustur_table.rowCount()
        for i in range(num_pass):
            malzeme = string.ascii_lowercase+string.digits
            mix= rd.sample(malzeme, pass_len)
            pass_list.append(mix)
            
        
        self.table_widget_ekle(pass_list, num_pass, last_sifre_num)

    def only_digit(self, pass_len, num_pass):  
        pass_list = []
        last_sifre_num = self.ui.sifre_olustur_table.rowCount()
        for i in range(num_pass):
            mix = [str(rd.randint(0, 9)) for i in range(pass_len)]
            pass_list.append(mix)

         
        self.table_widget_ekle(pass_list, num_pass,last_sifre_num)

    def upper_lower_digit(self, pass_len, num_pass):  
        pass_list= []
        last_sifre_num = self.ui.sifre_olustur_table.rowCount()
        for i in range(num_pass):
            malzeme = string.ascii_uppercase+string.ascii_lowercase+string.digits
            mix= rd.sample(malzeme, pass_len)
            pass_list.append(mix)
          
        self.table_widget_ekle(pass_list, num_pass,last_sifre_num)

    def upper_lower_digit_punc(self, pass_len, num_pass):  
        pass_list= []
        last_sifre_num = self.ui.sifre_olustur_table.rowCount()
        for i in range(num_pass):
            malzeme = string.ascii_uppercase+string.ascii_lowercase+string.digits+string.punctuation
            mix= rd.sample(malzeme, pass_len)
            pass_list.append(mix)
        
        self.table_widget_ekle(pass_list, num_pass,last_sifre_num)

    def lower_digit_punc(self, pass_len, num_pass):  
        pass_list= []
        last_sifre_num = self.ui.sifre_olustur_table.rowCount()
        for i in range(num_pass): 
            malzeme = string.ascii_lowercase+string.digits+string.punctuation
            mix= rd.sample(malzeme, pass_len)
            pass_list.append(mix)

             
        self.table_widget_ekle(pass_list, num_pass,last_sifre_num)
    
    def table_widget_ekle(self, p_list, num_p,last_sifre_num):
        self.aranacak = [(f"Şifre {i+last_sifre_num+1}", "".join(p_list[i]), f"{datetime.now()}") for i in range(num_p)]
        baslangic_satiri= self.ui.sifre_olustur_table.rowCount()
        for rowData in self.aranacak:
            rowNumber = self.ui.sifre_olustur_table.rowCount()
            self.ui.sifre_olustur_table.insertRow(rowNumber) 
            self.ui.sifre_olustur_table.setCellWidget(rowNumber, 3, QCheckBox())   
            for colNumber, cellData in enumerate(rowData):
                cellWidget = QTableWidgetItem(str(cellData))
                self.ui.sifre_olustur_table.setItem(rowNumber, colNumber, cellWidget)
        
        bitis_satiri=self.ui.sifre_olustur_table.rowCount()
        rangeSelected = QTableWidgetSelectionRange(baslangic_satiri, 0, bitis_satiri-1, self.ui.sifre_olustur_table.columnCount()-1)
        self.ui.sifre_olustur_table.setRangeSelected(rangeSelected, True)
            

    def onay_sifreler_yolla (self):
        secili_satir= []
        for row in range(self.ui.sifre_olustur_table.rowCount()):
            if self.ui.sifre_olustur_table.cellWidget(row, 3).isChecked():
                satir_verisi =[]
                for col in range(self.ui.sifre_olustur_table.columnCount()):
                    veri= self.ui.sifre_olustur_table.item(row, col)
                    if veri is not None:
                        satir_verisi.append(veri.text())
                secili_satir.append(satir_verisi)

        self.sifreleri_degistirip_yollama(self.aranacak)
        # Verileri yollarken şifrelerim 2. ekranında tabloya checkBox ekleme

    def sifreleri_degistirip_yollama(self, liste):
            # Kontrol için mevcut etiketleri ve yeni etiketleri alalım
        yeni_etiketler= [self.ui.sifre_olustur_table.item(row, 0).text() for row in range(self.ui.sifre_olustur_table.rowCount())]
        #check_durumu = [self.ui.sifre_olustur_table.cellWidget(row, 3).isChecked() for row in range(self.ui.sifre_olustur_table.rowCount())]
        mevcut_etiketler = [satir[0] for satir in liste]

        # Eğer mevcut ve yeni etiketler farklı ise işleme devam edelim
        if mevcut_etiketler != yeni_etiketler:
            for row in range(self.ui.sifre_olustur_table.rowCount()):
                checkbox = self.ui.sifre_olustur_table.cellWidget(row, 3)
                if checkbox.isChecked():
                    self.Sifrelerim_2.db_sifre_ekle([(self.ui.sifre_olustur_table.item(row, 0).text(), self.ui.sifre_olustur_table.item(row, 1).text())]) # Veri tabanına ekle
            self.ui.statusbar.showMessage("Şifreler Parola Kayıt Defterine Kaydedildi", 5000)
        else:
            self.ui.statusbar.showMessage("Lütfen Şifre Etiketlerini Düzenleyin")


    def tumunu_sec(self):
        for row in range(self.ui.sifre_olustur_table.rowCount()):
            checkbox = self.ui.sifre_olustur_table.cellWidget(row, 3)
            if checkbox.isChecked():
                checkbox.setChecked(False)
            else:
                checkbox.setChecked(True)

            #şimdi sana bütün kodu veriyorum 2 farklı class'ım var ve bunların altında çeşitli metotlarım var, şimdi
              
#uyg = QApplication(sys.argv)
#pencere = MainPage()
#pencere.show()
#sys.exit(uyg.exec_())
