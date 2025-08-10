# IBM - Uygulamalı Veri Bilimi Bitirme Projesi

Bu proje, SpaceX'in fırlatma verilerini kullanarak roketin başarılı bir şekilde iniş yapıp yapmayacağını tahmin etmeye yönelik bir veri analizi ve modelleme çalışmasıdır.

* 1. SpaceX'in fırlatma verilerini sağlamak için kullanılan bir web API'sinden verileri topladık.
* 2. Wikipedia sayfasındaki "List of Falcon 9 and Falcon Heavy launches" başlıklı içerikten Falcon 9’a ait tarihsel fırlatma kayıtlarını toplamak için web scraping işlemi gerçekleştirdik.
* 3. Verileri düzenledik.
* 4. SQL sorguları ile verinin temel özellikleri ve dağılımları incelendi.
* 5. Pandas ve Matplotlib kullanarak Keşifsel Veri Analizi (EDA) ve Özellik Mühendisliği (Feature Engineering) yaptık.
* 6. Folium ile etkileşimli harita analizi yapıldı. Böylelikle veriler etkileşimli ve gerçek zamanlı bir şekilde keşfedilebilir.
* 7.  Python Plotly Dash kullanılarak, ekip için görsel panolar (dashboard) oluşturuldu. Bu panolar, karar verme süreçlerinde kullanılabilir.
* 8.  Falcon 9'un ilk aşamasının başarılı bir şekilde iniş yapıp yapmayacağını tahmin etmek için bir makine öğrenimi boru hattı oluşturuldu. Bu, SpaceX ile rekabet eden bir startup için daha bilinçli kararlar alınmasına yardımcı olacaktır


### Kullanılan Makine Öğrenmesi Modelleri
* Logistic Regression
* Support Vector Machines (SVM)
* Decision Tree Classifier
* K-nearest neighbors (KNN)
* ** Grid Search: Farklı hiperparametre kombinasyonlarını deneyerek en iyi performansı sağlayan parametreleri bulmak için kullanılır. Bu, modelin doğruluğunu artırmak için kritik bir adımdır.**
