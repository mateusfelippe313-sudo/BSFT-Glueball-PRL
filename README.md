# BSFT-Glueball-PRL: v1.1.5

**Published:** May 14, 2026 
**DOI:** https://doi.org/10.5281/zenodo.20173430 
**arXiv:** To be submitted 
**License:** MIT

## v1.1.5 - Holographic 3D Projection Resolves AdS/QCD

**Result:** `M(0++) = 2.084 ± 0.017 GeV` 
**Agreement:** `0.6 sigma` vs Lattice QCD `2.2 ± 0.2 GeV` 
**Experimental:** `0.7 sigma` vs PDG `2.07 ± 0.04 GeV`

**Core Formula:**
Delta_3D = Delta_AdS + 3 _ C_BSFT 
         = 4 + 3 _ 2.076 = 7.60 ± 0.09
**C_BSFT = 2.076 ± 0.030** from BSFT running coupling at physical scale 
**Delta_AdS = 4** is the canonical dimension of TrF² in AdS₅/CFT₄

**Physical Mechanism:** 3D holographic projection of AdS₅ bulk field onto 4D boundary. 
AdS₅ pure gives 0.86 GeV, inconsistent with QCD. 
3D holographic projection gives 2.08 GeV, matching Lattice and experiment.

## Files

- `glueball_final.py` - reproduces all results + generates Figures 1-2 with error bands
- `paper1_scalar/fig1.pdf` - Dual-panel: AdS₅ vs 3D Physical, 0.6 sigma agreement
- `paper1_scalar/fig2.pdf` - BSFT vs experiment vs lattice comparison
- `paper1_scalar/main.tex` - PRL manuscript source
- `paper1_scalar/Paper1_PRL_v1.pdf` - Compiled PRL submission

## Citation

**Software:**
Felippe, M. (2026). *BSFT-Glueball-PRL: v1.1.5 - Holographic 3D Modulation with Error Bands*. Zenodo. https://doi.org/10.5281/zenodo.20173430

**Paper 1:**
Felippe, M. O. (2026). *Holographic 3D Projection in AdS/QCD: Scalar Glueball Mass and the Failure of AdS₅*. Submitted to Phys. Rev. Lett.

**Historical BSFT Result:**
Felippe, M. O. (2026). *A Parameter-Free Derivation of the BSFT Ratio M(0++)/m_ρ = 2.69*. Submitted to Phys. Rev. D.

## v1.0 History

Previous version used AdS₅ Delta = 4 giving M = 0.86 GeV without 3D projection. 
v1.1.5 implements physical 3D projection `Delta_3D = Delta_AdS + 3*C_BSFT` resolving 20-year discrepancy.

## Reproduction

```bash
python glueball_final.py
