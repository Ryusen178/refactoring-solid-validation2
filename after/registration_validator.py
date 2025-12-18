<<<<<<< HEAD
import logging
from ipk_validator import IPKValidator
from sks_validator import SKSValidator
from prasyarat_validator import PrasyaratValidator
from semester_validator import SemesterValidator

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

class RegistrationValidator:
    """
    Service utama untuk menjalankan seluruh aturan validasi registrasi.
    """

    def __init__(self, rules):
        """
        Inisialisasi service dengan kumpulan validation rule.

        Args:
            rules (list): List object ValidationRule
        """
        self.rules = rules

    def validate(self, data):
        """
        Menjalankan semua aturan validasi.

        Args:
            data (dict): Data mahasiswa

        Returns:
            str: Hasil validasi akhir
        """
        logging.info("Proses validasi registrasi dimulai")

        for rule in self.rules:
            result = rule.validate(data)
            if result:
                logging.warning("Registrasi ditolak")
                return result

        logging.info("Registrasi diterima")
        return "Registrasi diterima"


if __name__ == "__main__":
    rules = [
        IPKValidator(),
        SKSValidator(),
        PrasyaratValidator(),
        SemesterValidator()
    ]

    mahasiswa = {
        "ipk": 3.2,
        "sks": 22,
        "lulus_prasyarat": True,
        "semester": 3
    }

    service = RegistrationValidator(rules)
    print(service.validate(mahasiswa))
=======
import logging
from ipk_validator import IPKValidator
from sks_validator import SKSValidator
from prasyarat_validator import PrasyaratValidator
from semester_validator import SemesterValidator

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s"
)

class RegistrationValidator:
    """
    Service utama untuk menjalankan seluruh aturan validasi registrasi.
    """

    def __init__(self, rules):
        """
        Inisialisasi service dengan kumpulan validation rule.

        Args:
            rules (list): List object ValidationRule
        """
        self.rules = rules

    def validate(self, data):
        """
        Menjalankan semua aturan validasi.

        Args:
            data (dict): Data mahasiswa

        Returns:
            str: Hasil validasi akhir
        """
        logging.info("Proses validasi registrasi dimulai")

        for rule in self.rules:
            result = rule.validate(data)
            if result:
                logging.warning("Registrasi ditolak")
                return result

        logging.info("Registrasi diterima")
        return "Registrasi diterima"


if __name__ == "__main__":
    rules = [
        IPKValidator(),
        SKSValidator(),
        PrasyaratValidator(),
        SemesterValidator()
    ]

    mahasiswa = {
        "ipk": 3.2,
        "sks": 22,
        "lulus_prasyarat": True,
        "semester": 3
    }

    service = RegistrationValidator(rules)
    print(service.validate(mahasiswa))
>>>>>>> a47044d8648da51e150e0b03232ff5d25ba31f20
