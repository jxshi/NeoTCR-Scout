"""pMHC structure workflow placeholders and adapters."""

from __future__ import annotations

from pathlib import Path

from neotcr_scout.models import PMHCResult


class PlaceholderPMHCEngine:
    """Produce a transparent pMHC placeholder until Boltz/AF3 adapters are enabled."""

    def predict(self, peptide: str, hla: str, output_dir: Path | None = None) -> PMHCResult:
        pdb_path = None
        if output_dir:
            output_dir.mkdir(parents=True, exist_ok=True)
            pdb_path = output_dir / "pMHC.placeholder.pdb"
            pdb_path.write_text(
                "REMARK NeoTCR-Scout placeholder pMHC artifact\n"
                f"REMARK peptide={peptide} hla={hla}\n"
                "END\n",
                encoding="utf-8",
            )
        residues = {
            f"P{index + 1}": "exposed" if index in {3, 4, 6} else "unknown"
            for index, _ in enumerate(peptide)
        }
        return PMHCResult(pdb_path=pdb_path, tcr_facing_residues=residues, method="placeholder-v0.1")
