<<<<<<< HEAD
import logging
from validation_rule import ValidationRule

class SKSValidator(ValidationRule):
    """
    Validasi jumlah SKS mahasiswa.
    """

    def validate(self, data):
        """
        Mengecek batas maksimal SKS.

        Args:
            data (dict): Data mahasiswa

        Returns:
            str | None
        """
        if data["sks"] > 24:
            logging.warning("Validasi SKS gagal")
            return "Registrasi ditolak: SKS melebihi batas"

        logging.info("Validasi SKS berhasil")
        return None
=======
import logging
from validation_rule import ValidationRule

class SKSValidator(ValidationRule):
    """
    Validasi jumlah SKS mahasiswa.
    """

    def validate(self, data):
        """
        Mengecek batas maksimal SKS.

        Args:
            data (dict): Data mahasiswa

        Returns:
            str | None
        """
        if data["sks"] > 24:
            logging.warning("Validasi SKS gagal")
            return "Registrasi ditolak: SKS melebihi batas"

        logging.info("Validasi SKS berhasil")
        return None
>>>>>>> a47044d8648da51e150e0b03232ff5d25ba31f20
