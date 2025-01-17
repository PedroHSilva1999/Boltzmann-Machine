from typing import List, Tuple
import io
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
from fastapi import FastAPI, HTTPException
from fastapi.responses import StreamingResponse
from PIL import Image

app = FastAPI()

VISIBLE_UNITS = 4
HIDDEN_UNITS = 3
FRAMES = 20
DURATION = 500
TEMPERATURE = 1.0

def create_boltzmann_graph() -> nx.Graph:
    bm_graph = nx.Graph()

    for i in range(VISIBLE_UNITS):
        bm_graph.add_node(f"V{i+1}", layer="Visible", state=np.random.choice([0, 1]))

    for j in range(HIDDEN_UNITS):
        bm_graph.add_node(f"H{j+1}", layer="Hidden", state=np.random.choice([0, 1]))

    for i in range(VISIBLE_UNITS):
        for j in range(HIDDEN_UNITS):
            bm_graph.add_edge(f"V{i+1}", f"H{j+1}")

    return bm_graph

def update_states(bm_graph: nx.Graph, temperature: float = TEMPERATURE) -> None:
    for node in bm_graph.nodes:
        
        neighbors = list(bm_graph.neighbors(node))
        energy_diff = sum(bm_graph.nodes[neighbor]["state"] for neighbor in neighbors)
        
        probability = 1 / (1 + np.exp(-energy_diff / temperature))
        new_state = np.random.choice([0, 1], p=[1-probability, probability])
        bm_graph.nodes[node]["state"] = new_state

def generate_boltzmann_image(bm_graph: nx.Graph) -> io.BytesIO:
    try:
        update_states(bm_graph)

        fig, ax = plt.subplots(figsize=(8, 6))
        pos = nx.multipartite_layout(bm_graph, subset_key="layer")

        node_colors = [bm_graph.nodes[node]["state"] for node in bm_graph.nodes]
        nx.draw(
            bm_graph,
            pos,
            with_labels=True,
            node_size=2000,
            node_color=node_colors,
            cmap=plt.cm.Blues,
            font_size=10,
            font_color="black",
            font_weight="bold",
            edge_color="gray",
            ax=ax
        )

        ax.set_title("Visualização Dinâmica da Boltzmann Machine", fontsize=14)

        buf = io.BytesIO()
        plt.savefig(buf, format="png")
        buf.seek(0)
        plt.close(fig)
        
        return buf
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar imagem: {str(e)}")

def generate_gif() -> io.BytesIO:
    try:
        bm_graph = create_boltzmann_graph()
        images = []
        
        for _ in range(FRAMES):
            image_buf = generate_boltzmann_image(bm_graph)
            img = Image.open(image_buf)
            images.append(img)

        gif_buf = io.BytesIO()
        images[0].save(
            gif_buf, 
            format="GIF", 
            save_all=True, 
            append_images=images[1:], 
            loop=0, 
            duration=DURATION
        )
        gif_buf.seek(0)
        return gif_buf
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao gerar GIF: {str(e)}")

@app.get("/boltzmann")
async def get_boltzmann_gif():
    try:
        gif_buf = generate_gif()
        return StreamingResponse(gif_buf, media_type="image/gif")
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro inesperado: {str(e)}")
