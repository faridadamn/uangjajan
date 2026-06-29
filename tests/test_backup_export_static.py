import unittest
from pathlib import Path

HTML = Path(__file__).resolve().parents[1] / "index.html"
text = HTML.read_text(encoding="utf-8")


class BackupExportStaticTests(unittest.TestCase):
    def test_profile_has_backup_export_import_actions(self):
        self.assertIn("downloadBackupData()", text)
        self.assertIn("exportTransaksiCSV()", text)
        self.assertIn("triggerImportBackup()", text)
        self.assertIn("backup-file-input", text)

    def test_backup_export_import_functions_exist(self):
        for fn in [
            "function buildBackupPayload()",
            "function downloadBackupData()",
            "function exportTransaksiCSV()",
            "function triggerImportBackup()",
            "function handleBackupImport(",
            "function restoreBackupPayload(",
        ]:
            with self.subTest(fn=fn):
                self.assertIn(fn, text)

    def test_backup_payload_contains_version_and_storage_key(self):
        self.assertIn("schemaVersion", text)
        self.assertIn("STORAGE_KEY", text)
        self.assertIn("uangjajan-backup", text)
        self.assertIn("text/csv", text)


if __name__ == "__main__":
    unittest.main()
