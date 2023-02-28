# Password-Generator-in-python

Bu bir şifre oluşturma programıdır. Şifre oluşturduktan sonra kullanıcının tercihine göre bu şifreleri bir database'de depolar. Program 'main.py' dosyası üzerinden çalışır. 

![Şifre Oluşturucu 1 03 2023 00_04_27](https://user-images.githubusercontent.com/119891602/221979904-5a11dc93-0acb-41b7-9479-6262c714166b.png)

## Arayüz Tanıtımı ve Fonksiyonları

İlk olarak kullanıcıdan istenilen "Oluşturulacak Şifre Sayısı" ve "Karakter Sayısı" girdilerine bakalım. Bu iki girdi de kendilerine sayı alırlar. Eğer ki program sayı dışında bir ifade ile karşılaşırsa arayüzün alt kısmından uyarı verecektir. Bunun dışında "Oluşturulacak Şifre Sayısı" girdisi minimum 1 maksimum 100 değerini almaktadır, aynı şekilde "Karakter Sayısı" girdiside minimum 4 ve maksimum 30 olmak üzere sınırlandırılmıştır. 

İkincil olarak kullanıcıdan seçilmesi istenen "Büyük Harf", "Özel Karakter" ve "Sadece Rakam" seçeneklerine bakalım. Öncelikle şunu belirtmek isterim, eğer ki herhangi bir seçeneği seçmeden "Şifre Oluştur" butonuna basılırsa, program default olarak sadece rakam ve küçük harflerden oluşan bir şifre oluşturacaktır. Bunun dışında kullanıcı "Büyük Harf" seçeneğine tıkladığında, program küçük harf, büyük harf ve rakamdan oluşan bir şifre oluşturacaktır. Aynı şekilde sadece
"Özel Karakter" seçeneği seçilirse kullanıcıya küçük harf, özel karakter ve rakamdan oluşan bir şifre oluşturacaktır. Son seçeneğe bakıldığında "Sadece Rakam", isminden anlaşılacağı üzere sadece rakamlarda oluşan bir şifre program tarafından oluşturulmaktadır.

Butonlara geldiğimizde ise karşımıza 3 tane buton çıkıyor: "Şifre Oluştur", "Şeçili Şifreleri Kaydet" ve "Tümünü Seç". Burada özellikle "Şeçili Şifreleri Kaydet" ve "Tümünü Seç" butonlarının üzerinde durulması gerekir. Program gerekli girdileri aldıktan sonra kullanıcıya şifreler sunar. Kullanıcı bu şifreler arasından istediklerini seçebilmesi için butonların altında "Şifreleri Seç" sütununda şifreleri seçer. Eğer tüm şifreleri seçmek isterse "Tümünü Seç" butonuna tıklar. Şifreler seçildikten sonra kullanıcı "Şeçili Şifreleri Kaydet" tuşuna basar ve şifreler database'e yollanır. Fakat bu butonun çalışması için kullanıcının aşağıda bulunan tabloda yapması gereken bir işlem daha vardır. Bu yüzden tablo kısmına geçelim. 

Tabloyu genel olarak incelediğimizde karşımıza 4 sütun çıkıyor: "Şifre Etiketi", "Şifre", "Oluşturulma Tarihi" ve "Şifreni Seç". Bunlardan ilk sütunu olan "Şifre Etiketi"ne baktığımızda, burada oluşturulan şifreler default olarak "Şifre 1", "Şifre 2", ...  gibi etiketle gösteriliyor.  "Şifre" sütununda adından anlaşılacağı gibi şifreler tutulmaktadır. Aynı durum "Oluşturulma Tarihi" içinde geçerlidir. Son sütuna olan "Şifreni Seç"e baktığımız zaman kullanıcı program tarafından oluşturulan şifreler arasından istediğini seçebilmesi için içersinde CheckBox'lar bulunmaktadır. Bu aşamada kullanıcı şifre oluşturduktan sonra ilk olarak "Şifre Etiketi" altında bulunan satırların değerlerini değiştirmeli, ama bütün değerleri değiştirmesine gerek yok sadece seçtiği şifrelerin değerlerini değiştirmesi yeterli olacaktır. Bu işlemlerin ardından kullanıcı "Şeçili Şifreleri Kaydet" butonuna tıklayarak şifrelerini database'e kaydeder. 

![Şifre Oluşturucu 1 03 2023 00_47_24](https://user-images.githubusercontent.com/119891602/221988947-a5227c61-336b-4eaf-96af-9881c538a89b.png)

Burada örnek olarak yapılmış birkaç tane işlem görmektesiniz, şifre sütununa dikkatli bakıldığında 3 farkı şifre oluşturma işlemi yapıldığını anlayabilirsiniz. Kullanıcı bu şifrelerin arasından kullanacaklarının ilk önce Şifre Etiketi değerini değiştirip ardından Şifreni Şeç sütununda işaretlemiştir. Bu işlemden sonra kullanıcı "Şeçili Şifreleri Kaydet" butonuna basacaktır. Bu işlemin ardından programın altında "Şifreler Parola Kayıt Defterine Kaydedildi" şeklinde bir mesaj yazacaktır. Kullanıcı bu sayfada Sol Üst köşede bulunan şifrelerim seçeneğinin içersinden "Parola Kayıt Defteri" adında bir arayüze ulaşabilir. Bu sayfanın amacı kişinin mevcut şifrelerini tutmaktır. İçersindeki veriyi database'den almaktadır. 

![MainWindow 1 03 2023 00_53_31](https://user-images.githubusercontent.com/119891602/221991964-d8804634-b088-4711-b944-d4ec127c2066.png)

Bu sayfada genel olarak görüntüleme işlemi yapılmaktadır. Kullanıcı "Ara" butonu sayersinde şifre ismini yazarak ilgili satırdaki şifresini bulabilir. Kullanım ömrünü tamamlamış şifresini seçip database'den "SİL" butonunun yardımıyla kaldırabilir. Yine aynı zamanda şifrelerini "A'dan Z'ye", "Z'den A'ya" ve "Tarih" kategorilerine göre sılama seçeneği mevcuttur. 

