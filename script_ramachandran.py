#!/usr/bin/env python3

import os
import numpy as np
import matplotlib.pyplot as plt

# Dossier contenant les fichiers XVG
dossier_contenant_fichiers = '/home/paturel/Bureau/dossier_travail_bioinfo/ramachandran/candidats/total_graphs_heatmap'

# Liste tous les fichiers dans le dossier
fichiers_xvg = [f for f in os.listdir(dossier_contenant_fichiers) if f.endswith('.xvg')]

# Itération sur les fichiers
for fichier_xvg in fichiers_xvg:
    # Chemin complet du fichier
    chemin_fichier_xvg = os.path.join(dossier_contenant_fichiers, fichier_xvg)

    # Lire les données à partir du fichier XVG (seulement les deux premières colonnes)
    data = np.genfromtxt(chemin_fichier_xvg, skip_header=34, dtype=None, encoding=None, usecols=(0, 1))

    # Extraire les valeurs de phi et psi
    phi = data[:, 0].astype(float)
    psi = data[:, 1].astype(float)

    # Calculer la densité des points
    densite_points, xedges, yedges = np.histogram2d(phi, psi, bins=100)

    # Normaliser la densité des points
    densite_points_norm = densite_points / np.max(densite_points)

    # Créer le graphique de Ramachandran avec une couleur en fonction de la densité des points
    plt.figure(figsize=(8, 8))

    # Utiliser imshow pour le graphique de densité
    plt.imshow(densite_points_norm.T, origin='lower', extent=[-180, 180, -180, 180], cmap='coolwarm')

    # Ajouter la barre de couleur avec une police plus grande
    cbar = plt.colorbar(label='Density')
    cbar.ax.tick_params(labelsize=12)  # Taille de la police de la barre de couleur

    # Ajouter des étiquettes aux axes avec une police plus grande et en gras
    plt.xlabel('Phi', fontsize=14, fontweight='bold', color='black')
    plt.ylabel('Psi', fontsize=14, fontweight='bold', color='black')

    # Modifier l'épaisseur des axes
    plt.gca().spines['left'].set_linewidth(3)
    plt.gca().spines['bottom'].set_linewidth(3)
    plt.gca().spines['right'].set_linewidth(3)
    plt.gca().spines['top'].set_linewidth(3)

    # Modifier l'épaisseur des ticks
    plt.gca().xaxis.set_tick_params(width=3)
    plt.gca().yaxis.set_tick_params(width=3)

    # Modifier la couleur et l'épaisseur des ticks
    plt.xticks(fontsize=16, color='black')
    plt.yticks(fontsize=16, color='black')

    # Modifier la couleur et l'épaisseur de la grille
    plt.grid(True, color='black', linestyle='--', linewidth=0.5)

    # Modifier l'épaisseur du quadrillage en 0 (X et Y)
    plt.axhline(0, color='black', linewidth=2)  # Ligne horizontale à y=0
    plt.axvline(0, color='black', linewidth=2)  # Ligne verticale à x=0

    # Enregistrer l'image au format PNG avec le nom du fichier d'origine
    chemin_sauvegarde = os.path.join(dossier_contenant_fichiers, f"{os.path.splitext(fichier_xvg)[0]}_heatmap.png")
    plt.savefig(chemin_sauvegarde, dpi=300, bbox_inches='tight')

    # Effacer le graphique actuel pour en créer un nouveau pour le prochain fichier
    plt.clf()

# Fermer la fenêtre de l'interpréteur graphique après avoir traité tous les fichiers
plt.close('all')

