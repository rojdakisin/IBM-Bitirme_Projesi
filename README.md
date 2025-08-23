# IBM Applied Data Science Capstone Project - SpaceX Launch Predicition

Bu proje, SpaceX'in fırlatma verilerini kullanarak roketin başarılı bir şekilde iniş yapıp yapmayacağını tahmin etmeye yönelik bir veri analizi ve modelleme çalışmasıdır.

### Proje Süreci
1. SpaceX'in fırlatma verilerini sağlamak için bir web API kullanıldı.
2. Wikipedia'daki "List of Falcon 9 and Falcon Heavy launches" sayfasından Falcon 9’a ait tarihsel fırlatma kayıtlarını toplamak amacıyla web scraping (web kazıma) işlemi gerçekleştirildi.
3. Toplanan veriler temizlenip düzenlendi.
4. SQL sorguları ile verinin temel özellikleri ve dağılımları incelendi.
5. Pandas ve Matplotlib kullanarak Keşifsel Veri Analizi (EDA) ve Özellik Mühendisliği (Feature Engineering) yapıldı.
6. Folium ile etkileşimli harita analizi gerçekleştirildi. Böylece veriler dinamik ve görsel olarak keşfedilebilir hale getirildi.
7. Plotly Dash kullanılarak ekip için görsel panolar (dashboard) oluşturuldu. Bu panolar, karar verme süreçlerinde kullanılabilir.
8.  Falcon 9'un ilk aşamasının başarılı bir şekilde iniş yapıp yapmayacağını tahmin etmek için bir makine öğrenimi boru hattı (pipeline) geliştirildi. Bu, SpaceX ile rekabet eden bir startup için daha bilinçli kararlar alınmasına yardımcı olabilir.


### Kullanılan Makine Öğrenimi Modelleri
* Logistic Regression
* Support Vector Machines (SVM)
* Decision Tree Classifier
* K-nearest neighbors (KNN)
  
Ayrıca, farklı hiperparametre kombinasyonlarını deneyerek en iyi performansı bulmak için Grid Search (Izgara Arama) kullanıldı. Bu adım, modelin doğruluğunu artırmak için kritik öneme sahiptir.

### Not
* Folium ile oluşturulan interaktif haritalar GitHub'da doğrudan görünmez.
* Görmek için notebook'u lokal ortamda çalıştırın.(Jupyter Notebook/ JupyterLab)
