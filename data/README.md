# Data directory

This directory is reserved for pinned, versioned local database snapshots used by
NeoTCR-Scout workflows.

Recommended v0.1 data plan:

1. Download a dated VDJdb export and store it under `data/vdjdb/`.
2. Store any IEDB receptor query exports under `data/iedb/` with the query date.
3. Store TCR3D structural evidence tables under `data/tcr3d/`.
4. Record source URL, access date, checksum, and normalization script for every file.

The code currently ships only tiny seed records in Python/database fixtures so
the KRAS G12D demo remains lightweight and deterministic.
