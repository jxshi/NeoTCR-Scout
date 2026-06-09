"""Tiny built-in protein reference snippets for demos.

Production workflows should provide explicit protein_sequence values or configure
versioned reference FASTA files. Built-ins are only for v0.1 examples and CLI
quick starts.
"""

from __future__ import annotations

REFERENCE_SEQUENCES = {
    "KRAS": "MTEYKLVVVGAGGVGKSALTIQLIQNHFVDEYDPTIEDSYRKQV",
}


def get_reference_sequence(gene: str) -> str | None:
    """Return a built-in demo reference sequence if one is available."""

    return REFERENCE_SEQUENCES.get(gene.upper())
