get"""Calcul de la moyenne pondérée d'un élève."""
import csv


def moyenne_ponderee(notes):
    """Retourne la moyenne sur 20, arrondie à 2 décimales.

    notes : liste de tuples (note, coefficient).
    """
    if not notes:
        raise ValueError("La liste de notes est vide")
    total = sum(note * coef for note, coef in notes)
    somme_coefs = sum(coef for _, coef in notes)
    return round(total / somme_coefs, 2)


def lire_notes(chemin):
    """Lit un fichier CSV (matiere,note,coefficient) et retourne la liste des tuples."""
    with open(chemin, newline="", encoding="utf-8") as fichier:
        lecteur = csv.DictReader(fichier)
        return [(float(l["note"]), float(l["coefficient"])) for l in lecteur]


def mention(moyenne):
    """Renvoie la mention correspondant à une moyenne sur 20."""
    if moyenne >= 16:
        return "Très bien"
    if moyenne >= 14:
        return "Bien"
    if moyenne >= 12:
        return "Assez bien"
    if moyenne >= 10:
        return "Passable"
    return "Insuffisant"


def extremes(notes):
    """Renvoie (meilleure note, plus faible note) d'une liste de (note, coef)."""
    valeurs = [note for note, _ in notes]
    return max(valeurs), min(valeurs)


def tableau_html(lignes):
    """Construit un tableau HTML à partir de lignes (matière, note, coef)."""
    corps = "".join(
        f"<tr><td>{m}</td><td>{n}</td><td>{c}</td></tr>" for m, n, c in lignes
    )
    return f"<table>{corps}</table>"


if __name__ == "__main__":
    notes = lire_notes("donnees/notes.csv")
    print("Moyenne :", moyenne_ponderee(notes))
