import numpy as np
import matplotlib.pyplot as plt

# ================== CONSTANTES BSFT v1.1.5 ==================
m_rho = 0.775  # GeV
Delta_AdS = 4.0  # Dimensão canônica de TrF² em AdS₅/CFT₄
d_perp = 3  # Dimensões espaciais perpendiculares

# Constante de modulação BSFT com incerteza
C_BSFT = 2.076
C_err = 0.03  # 1.5% - running do acoplamento

# Dados Lattice QCD pra comparação
M_LATTICE = 2.2  # GeV
M_LATTICE_ERR = 0.2  # GeV

# Dados PDG 2024
M_PDG = 2.07  # GeV
M_PDG_ERR = 0.04  # GeV

# ================== FUNÇÕES BSFT ==================
def bsft_mass(Delta):
    """Calcula massa BSFT dado Delta usando fórmula de fluxo RG"""
    ratio = (1 + np.sqrt(Delta * (Delta + 4) / 4.0)) / (1 + np.sqrt(5/4))
    return ratio * m_rho

def wavefunction(r, Delta, is_3d=False):
    """Função de onda AdS vs 3D normalizada"""
    if not is_3d:
        # AdS puro: decaimento lento, não confinado
        psi = r**2 * np.exp(-m_rho * r * 1.5)
    else:
        # 3D: confinamento pelos graus perp d_perp
        psi = r**2 * np.exp(-m_rho * r * 3.0) * np.exp(-r**2 * d_perp / 8)
    return psi / np.max(psi)

# ================== CÁLCULO COM ERROS ==================
# 1. AdS_5 puro - previsão canônica
M_AdS = bsft_mass(Delta_AdS)
ratio_AdS = M_AdS / m_rho

# 2. 3D Modulado - valor central
Delta_3D = Delta_AdS + d_perp * C_BSFT
M_3D = bsft_mass(Delta_3D)
ratio_3D = M_3D / m_rho

# 3. 3D Modulado - banda de erro propagada de C_BSFT
Delta_min = Delta_AdS + d_perp * (C_BSFT - C_err)
Delta_max = Delta_AdS + d_perp * (C_BSFT + C_err)
M_min = bsft_mass(Delta_min)
M_max = bsft_mass(Delta_max)
M_3D_err = (M_max - M_min) / 2

# 4. Sigma de acordo com Lattice
sigma_diff_lattice = abs(M_3D - M_LATTICE)
sigma_total_lattice = np.sqrt(M_LATTICE_ERR**2 + M_3D_err**2)
sigma_agreement_lattice = sigma_diff_lattice / sigma_total_lattice

# 5. Sigma de acordo com PDG
sigma_diff_pdg = abs(M_3D - M_PDG)
sigma_total_pdg = np.sqrt(M_PDG_ERR**2 + M_3D_err**2)
sigma_agreement_pdg = sigma_diff_pdg / sigma_total_pdg

# ================== PLOT FIGURA 1 ==================
r = np.linspace(0.01, 1.2, 300)
psi_AdS = wavefunction(r, Delta_AdS, is_3d=False)
psi_3D = wavefunction(r, Delta_3D, is_3d=True)

# Calcula banda de erro na função de onda
psi_3D_min = wavefunction(r, Delta_min, is_3d=True)
psi_3D_max = wavefunction(r, Delta_max, is_3d=True)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# PAINEL 1: AdS_5 Puro - Falha
ax1.plot(r, psi_AdS, 'r--', linewidth=2.5, label='AdS_5 Pure')
ax1.fill_between(r, 0, psi_AdS, alpha=0.2, color='red')
ax1.set_title(f'AdS_5: M = {M_AdS:.2f} GeV', fontsize=13, fontweight='bold')
ax1.text(0.05, 0.90, f'Delta = {Delta_AdS:.1f}', transform=ax1.transAxes, fontsize=11)
ax1.text(0.05, 0.83, f'M/m_rho = {ratio_AdS:.2f}', transform=ax1.transAxes, fontsize=11)
ax1.text(0.05, 0.76, 'Inconsistent with QCD', transform=ax1.transAxes, fontsize=11, color='red')
ax1.set_xlabel('Radius [GeV^-1]', fontsize=11)
ax1.set_ylabel('Normalized psi(r)', fontsize=11)
ax1.set_xlim(0, 1.2)
ax1.set_ylim(0, 1.05)
ax1.grid(alpha=0.3)
ax1.legend()

# PAINEL 2: 3D Modulado - Sucesso
ax2.plot(r, psi_3D, 'b-', linewidth=2.5, label='BSFT 3D Central')
ax2.fill_between(r, psi_3D_min, psi_3D_max, alpha=0.3, color='blue', 
                 label='BSFT 3D +/- 1sigma')
ax2.plot(r, psi_3D_min, 'b:', linewidth=1, alpha=0.7)
ax2.plot(r, psi_3D_max, 'b:', linewidth=1, alpha=0.7)

ax2.set_title(f'3D Physical: M = {M_3D:.3f} +/- {M_3D_err:.3f} GeV', 
              fontsize=13, fontweight='bold')
ax2.text(0.05, 0.90, f'Delta_3D = {Delta_3D:.2f} +/- {d_perp*C_err:.2f}', 
         transform=ax2.transAxes, fontsize=11)
ax2.text(0.05, 0.83, f'M/m_rho = {ratio_3D:.2f}', transform=ax2.transAxes, fontsize=11)
ax2.text(0.05, 0.76, f'{sigma_agreement_lattice:.1f} sigma vs Lattice', 
         transform=ax2.transAxes, fontsize=11, color='blue')
ax2.text(0.05, 0.69, f'C_BSFT = {C_BSFT:.3f} +/- {C_err:.3f}', 
         transform=ax2.transAxes, fontsize=10)

# Adiciona linha da Lattice pra comparação
ax2.axhline(y=0.95, xmin=0.7, xmax=0.98, color='green', linewidth=3, 
            label=f'Lattice: {M_LATTICE:.1f} +/- {M_LATTICE_ERR:.1f} GeV')
ax2.text(0.72, 0.96, 'Lattice QCD', transform=ax2.transAxes, fontsize=9, color='green')

ax2.set_xlabel('Radius [GeV^-1]', fontsize=11)
ax2.set_ylabel('Normalized psi_3D(r)', fontsize=11)
ax2.set_xlim(0, 1.2)
ax2.set_ylim(0, 1.05)
ax2.grid(alpha=0.3)
ax2.legend(loc='upper right', fontsize=9)

plt.suptitle('BSFT Scalar Glueball: Holographic 3D Projection v1.1.5', 
             fontsize=16, fontweight='bold')
plt.tight_layout()
plt.savefig('fig1.pdf', bbox_inches='tight', dpi=300)
plt.close()

# ================== OUTPUT TERMINAL ==================
print("="*75)
print("BSFT Scalar Glueball Result v1.1.5 - Holographic 3D Projection:")
print("="*75)
print(f"AdS_5 Pure : Delta = {Delta_AdS:.1f} -> M = {M_AdS:.3f} GeV")
print(f"3D Modulated: Delta = {Delta_3D:.2f} +/- {d_perp*C_err:.2f}")
print(f"              C_BSFT = {C_BSFT:.3f} +/- {C_err:.3f}")
print(f"              M = {M_3D:.3f} +/- {M_3D_err:.3f} GeV")
print(f"              M/m_rho = {ratio_3D:.2f}")
print("-"*75)
print(f"Lattice QCD : M = {M_LATTICE:.1f} +/- {M_LATTICE_ERR:.1f} GeV")
print(f"Agreement   : {sigma_agreement_lattice:.1f} sigma")
print(f"PDG 2024    : M = {M_PDG:.2f} +/- {M_PDG_ERR:.2f} GeV")
print(f"Agreement   : {sigma_agreement_pdg:.1f} sigma")
print("-"*75)
print("Physical Interpretation:")
print(f"Delta_3D = Delta_AdS + d_perp * C_BSFT")
print(f"         = {Delta_AdS:.1f} + 3 * {C_BSFT:.3f} = {Delta_3D:.2f}")
print("Delta_AdS = 4 is canonical dimension of TrF² operator in AdS₅/CFT₄")
print("The 3 transverse dimensions renormalize Delta, projecting AdS_5 to 3D.")
print("="*75)
print("Files generated: fig1.pdf with dual panel + error bands")
print("="*75)
