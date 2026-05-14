[[DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.20173430.svg)](https://doi.org/10.5281/zenodo.20173430)

# BSFT-Glueball-PRL: v1.1.4

**Published:** May 14, 2026
**DOI:** https://doi.org/10.5281/zenodo.20173430

## v1.1.4 - Holographic 3D Projection Resolves AdS/QCD

**Result:** `M(0++) = 2.084 ± 0.017 GeV`  
**Agreement:** `0.6 sigma` vs Lattice QCD `2.2 ± 0.2 GeV`

**Core Formula:**
´´´
Delta_3D = Delta_AdS + 3 * C_BSFT
         = 1.371 + 3 * 2.076 = 7.60 ± 0.09`
´´´
**C_BSFT = 2.076 ± 0.030** from BSFT running coupling

AdS_5 pure gives 0.86 GeV, inconsistent with QCD. 
3D holographic projection gives 2.08 GeV, matching Lattice.

## Files
- `glueball_final.py` - reproduces all results + generates Figure 1 with error bands
- `fig1.pdf` - Dual-panel: AdS_5 vs 3D Physical, 0.6 sigma agreement

## Citation
Felippe, M. (2026). BSFT-Glueball-PRL: v1.1.4 - Holographic 3D Modulation with Error Bands. Zenodo. https://doi.org/10.5281/zenodo.20173430

## v1.0 History
Previous version used AdS_5 Delta = 1.371 giving M = 0.86 GeV. v1.1.4 implements physical 3D projection.

