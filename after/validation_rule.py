from abc import ABC, abstractmethod

class ValidationRule(ABC):
    """
    Interface untuk semua aturan validasi registrasi mahasiswa.
    Setiap rule harus mengimplementasikan method validate().
    """

    @abstractmethod
    def validate(self, data):
        """
        Melakukan validasi terhadap data mahasiswa.

        Args:
            data (dict): Data mahasiswa (ipk, sks, prasyarat, dll)

        Returns:
            str | None: Pesan error jika validasi gagal, None jika lolos
        """
        pass

