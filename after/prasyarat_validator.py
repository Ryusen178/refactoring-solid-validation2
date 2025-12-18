import logging
from validation_rule import ValidationRule

class PrasyaratValidator(ValidationRule):
    """
    Validasi kelulusan mata kuliah prasyarat.
    """

    def validate(self, data):
        """
        Mengecek kelulusan prasyarat.

        Args:
            data (dict): Data mahasiswa

        Returns:
            str | None
        """
        if not data["lulus_prasyarat"]:
            logging.warning("Validasi prasyarat gagal")
            return "Registrasi ditolak: Prasyarat belum lulus"

        logging.info("Validasi prasyarat berhasil")
        return None
