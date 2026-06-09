# Third-party MHC binding tools

NeoTCR-Scout can call locally provided MHC binding predictors, but it does not
redistribute or license them.

## NetMHCpan

Place your licensed NetMHCpan executable in one of these locations:

- `tools/netMHCpan`
- `tools/netMHCpan/netMHCpan`
- a custom path exported as `NEOTCR_SCOUT_NETMHCPAN`

NeoTCR-Scout also checks `netMHCpan` / `netmhcpan` on `PATH`.

## MHCflurry

MHCflurry is available from the OpenVax repository:

- https://github.com/openvax/mhcflurry

Recommended local layout:

```bash
git clone https://github.com/openvax/mhcflurry tools/mhcflurry
python -m pip install -e tools/mhcflurry
```

NeoTCR-Scout checks `NEOTCR_SCOUT_MHCFLURRY_PREDICT`, common local
`tools/mhcflurry/.../mhcflurry-predict` paths, and `mhcflurry-predict` on
`PATH`.

## License notice

This repository is for academic research workflows only. Before using NetMHCpan
or MHCflurry, contact the original authors and comply with their license,
citation, and redistribution requirements.
