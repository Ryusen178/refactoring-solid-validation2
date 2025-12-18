import logging
from validation_rule import ValidationRule

class SemesterValidator(ValidationRule):
    """
    Validasi semester aktif mahasiswa.
    """

    def validate(self, data):
        """
        Mengecek apakah semester memenuhi syarat.

        Args:
            data (dict): Data mahasiswa

        Returns:
            str | None
        """
        if data["semester"] < 2:
            logging.warning("Validasi semester gagal")
            return "Registrasi ditolak: Semester belum memenuhi"

        logging.info("Validasi semester berhasil")
        return None
