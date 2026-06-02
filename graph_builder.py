import networkx as nx
import matplotlib.pyplot as plt
import re


def create_graph(case_text):

    G = nx.Graph()

    # Extract entities

    suspects = re.findall(
        r"Suspect[:\s]+([A-Za-z ]+)",
        case_text,
        re.IGNORECASE
    )

    witnesses = re.findall(
        r"Witness[:\s]+([A-Za-z ]+)",
        case_text,
        re.IGNORECASE
    )

    vehicles = re.findall(
        r"(Red Car|Black Motorcycle|White Van|Blue Car)",
        case_text,
        re.IGNORECASE
    )

    locations = re.findall(
        r"Location[:\s]+([A-Za-z ]+)",
        case_text,
        re.IGNORECASE
    )
    # Remove duplicates and clean text

    suspects = list(set([s.strip() for s in suspects]))
    witnesses = list(set([w.strip() for w in witnesses]))
    vehicles = list(set([v.title().strip() for v in vehicles]))
    locations = list(set([l.strip() for l in locations]))

    # Remove very long extracted sentences

    suspects = [
        s for s in suspects
        if len(s.split()) <= 3
    ]

    witnesses = [
        w for w in witnesses
        if len(w.split()) <= 4
    ]

    evidence = []

    if "fingerprint" in case_text.lower():
        evidence.append("Fingerprints")

    if "cctv" in case_text.lower():
        evidence.append("CCTV Footage")

    if "dna" in case_text.lower():
        evidence.append("DNA Evidence")

    # Defaults

    if not suspects:
        suspects = ["Unknown Suspect"]

    if not locations:
        locations = ["Crime Scene"]

    # Build graph

    for suspect in suspects:

        for location in locations:
            G.add_edge(suspect, location)

        for vehicle in vehicles:
            G.add_edge(suspect, vehicle)

        for ev in evidence:
            G.add_edge(suspect, ev)

    for witness in witnesses:

        for suspect in suspects:
            G.add_edge(witness, suspect)

    # Layout

    pos = nx.spring_layout(
        G,
        k=4,
        iterations=100,
        seed=42
    )

    node_colors = []

    for node in G.nodes():

        if node in suspects:
            node_colors.append("red")

        elif node in witnesses:
            node_colors.append("green")

        elif node in vehicles:
            node_colors.append("purple")

        elif node in evidence:
            node_colors.append("orange")

        else:
            node_colors.append("skyblue")

    fig, ax = plt.subplots(figsize=(14, 8))

    nx.draw_networkx_nodes(
        G,
        pos,
        node_color=node_colors,
        node_size=3000,
        ax=ax
    )

    nx.draw_networkx_edges(
        G,
        pos,
        width=2,
        ax=ax
    )

    nx.draw_networkx_labels(
        G,
        pos,
        font_size=9,
        font_weight="bold",
        ax=ax
    )

    ax.axis("off")

    return fig