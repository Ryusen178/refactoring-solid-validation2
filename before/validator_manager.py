class ValidatorManager:
    def validate(self, ipk, sks, lulus_prasyarat):
        if ipk < 2.5:
            return "Registrasi ditolak: IPK kurang"
        elif sks > 24:
            return "Registrasi ditolak: SKS melebihi batas"
        elif not lulus_prasyarat:
            return "Registrasi ditolak: Prasyarat belum lulus"
        else:
            return "Registrasi diterima"


# Main program
if __name__ == "__main__":
    vm = ValidatorManager()
    hasil = vm.validate(ipk=3.0, sks=22, lulus_prasyarat=True)
    print(hasil)