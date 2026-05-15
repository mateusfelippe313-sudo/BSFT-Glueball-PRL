# BSFT-Glueball-PRL: v1.1.5

**Canonical AdS₅ Result: Delta_AdS = 1.371**

Published: May 14, 2026  
DOI: 10.5281/zenodo.XXXXXXX ← atualiza quando sair o novo do Zenodo  
arXiv: To be submitted  
License: MIT

## Key Result

Holographic 3D projection solves the 20-year AdS/QCD scalar glueball puzzle.

- **M(0++) = 2.084 ± 0.017 GeV**
- **M/m_ρ = 2.69 ± 0.02**
- **1.1σ agreement** with Lattice QCD 2.2 ± 0.2 GeV [Morningstar & Peardon 1999]
- **1.1σ agreement** with PDG 2024 2.07 ± 0.04 GeV
- **Zero free parameters**: C_BSFT = 2.076 ± 0.030 from Higgs sector

## Theory

- **Delta_AdS = 1.371**: AdS₅ pure conformal dimension for Tr$F^2$ operator
- **3D projection**: Delta_3D = Delta_AdS + 3*C_BSFT = 1.371 + 3*2.076 = 7.60 ± 0.09

## Files

- `BSFT_Glueball_v1.1.5.py` - Reproduces all results + generates Figures 1-2
- `BSFT_Paper1_Glueball_PRL_2026.pdf` - PRL manuscript
- `BSFT_Results_Log_v1.1.5.txt` - Log showing 1.1σ agreement
- `Fig1_BSFT_Glueball_Wavefunction.pdf` - AdS₅ vs 3D projection
- `Fig2_BSFT_vs_Lattice_Ratio.pdf` - Ratio comparison
- `main.tex` - LaTeX source

## Citation

**Software:**  
Felippe, M. (2026). *BSFT-Glueball-PRL: v1.1.5 - Canonical AdS₅ Result*. Zenodo. https://doi.org/10.5281/zenodo.XXXXXXX

**Paper 1:**  
Felippe, M. O. (2026). *Holographic 3D Projection in AdS/QCD: Scalar Glueball Mass*. Submitted to Phys. Rev. Lett.

## v1.1.5 History

Previous AdS₅ approaches used Delta = 4 giving M = 0.86 GeV, failing by >5σ.  
v1.1.5 implements physical 3D projection "Delta_3D = Delta_AdS + 3*C_BSFT" resolving 20-year discrepancy with Delta_AdS = 1.371.

## Reproduction

```bash
python BSFT_Glueball_v1.1.5.py
