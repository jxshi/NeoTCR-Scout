# Data directory

This directory is reserved for pinned, versioned local database snapshots and small curated configuration files used by NeoTCR-Scout workflows.

Recommended v0.1 data plan:

1. Download a dated VDJdb export and store it under `data/vdjdb/`.
2. Store any IEDB receptor query exports under `data/iedb/` with the query date.
3. Store TCR3D structural evidence tables under `data/tcr3d/`.
4. Record source URL, access date, license/terms, checksum, and normalization script for every file.
5. Keep manually curated mutation relationship groups under `data/mutation_groups/` with review notes.

The code currently ships tiny seed records in Python/database fixtures plus a RAS mutation relationship YAML so the KRAS G12D demo remains lightweight and deterministic.
