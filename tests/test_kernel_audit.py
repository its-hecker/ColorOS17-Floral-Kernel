import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "kernel_audit", ROOT / "tools/audit_kernel.py")
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


class KernelAuditTests(unittest.TestCase):
    def test_config_missing_fails(self):
        with tempfile.TemporaryDirectory() as td:
            self.assertFalse(m.audit(Path(td))["pass"])
    def test_expected_features_pass_source_audit(self):
        with tempfile.TemporaryDirectory() as td:
            root = Path(td)
            (root / "arch/arm64/configs").mkdir(parents=True)
            (root / "drivers").mkdir()
            (root / "build.config.floral").write_text("BUILD_CONFIG=floral\n")
            (root / "Makefile").write_text("VERSION = 4\nPATCHLEVEL = 14\n")
            (root / "arch/arm64/configs/floral_defconfig").write_text(
                "\n".join(k + "=y" for k in m.BOOT_CONFIG_FLAGS) + "\n")
            report = m.audit(root)
            self.assertTrue(report["pass"])
            self.assertEqual(report["kernel_series"], "4.14")

if __name__ == "__main__":
    unittest.main()
