import logging
from validation_rule import ValidationRule

class IPKValidator(ValidationRule):
    """
    Validasi IPK mahasiswa.
    """

    def validate(self, data):
        """
        Mengecek apakah IPK memenuhi syarat minimal.

        Args:
            data (dict): Data mahasiswa

        Returns:
            str | None
        """
        if data["ipk"] < 2.5:
            logging.warning("Validasi IPK gagal")
            return "Registrasi ditolak: IPK kurang dari 2.5"

        logging.info("Validasi IPK berhasil")
        return None
