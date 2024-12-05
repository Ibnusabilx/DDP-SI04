class Gempa:
    # Konstruktor Inisial atribut
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala
    
    #Method Penentu Gempa
    def dampak(self):
        #Logika/Statment
        if self.skala < 2:
            print('Gempa Tidak Berasa')
        elif 2 <= self.skala <= 4:
            print('Gempa Berdampak Bangunan Retak-retak')
        elif 4 <= self.skala <= 6:
            print('Gempa Berdampak Bangunan Roboh')
        elif self.skala > 6:
            print('Gempa Besar Berpotensi Roboh Dan Tsunami')
        
        # # Menampilkan Lokasi Dan Skala Gempa
        # print('Lokasi Gempa:',self.lokasi)
        # print('Skala Gempa:',self.skala)

        #cara print yang lain
        print(f'Lokasi Gempa:{self.lokasi}')
        print(f'Skala Gempa:{self.skala}')
