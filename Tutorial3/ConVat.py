class ConVat:
    def __init__(self):
        self.Ho = ""
        self.NamSinh = ""
        self.MoiTruongSong = ""

    def NhapThongTin(self):
        self.Ho = input("Moi ban nhap Ho: ")
        self.NamSinh = input("Moi ban nhap nam sinh: ")
        self.MoiTruongSong = input("Nhap moi truong song: ")

    def __str__(self):
        return "{:^10}{:^10}{:<20}".format(self.Ho, self.NamSinh, self.MoiTruongSong)
