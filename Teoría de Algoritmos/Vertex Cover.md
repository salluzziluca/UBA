El vertex cover en un grafo es un subconjunto de vertices tal que podemos llegar a todas las aristas del grafo. 
![[Pasted image 20240915144558.png]]
Aca el minimmum vertex cover es de 2- Con esos dos tengo todos los vertices cubiertos


minimmum vertex cover en python utilizando [[Backtracking]]

```python
def obtener_aristas(grafo):
    aristas = []
    for v in grafo.obtener_vertices():
        for u in grafo.adyacentes(v):
            if (u, v) not in aristas and (v, u) not in aristas:
                aristas.append((v, u))
    return aristas

def backtracking(grafo, aristas, indice, current_vertex_cover, best_vertex_cover):
    if all(esta_cubierta(u, v, current_vertex_cover) for u, v in aristas):
        if len(best_vertex_cover) == 0 or len(current_vertex_cover) < len(best_vertex_cover):
            best_vertex_cover.clear()
            best_vertex_cover.extend(current_vertex_cover)
        return

    if indice == len(aristas):
        return

    u, v = aristas[indice]

    # Opción 1: incluimos el vértice u en el Vertex Cover
    if u not in current_vertex_cover:
        current_vertex_cover.append(u)
        backtracking(grafo, aristas, indice + 1, current_vertex_cover, best_vertex_cover)
        current_vertex_cover.pop()  # Retrocedemos
    else:
        backtracking(grafo, aristas, indice + 1, current_vertex_cover, best_vertex_cover)

    # Opción 2: incluimos el vértice v en el Vertex Cover
    if v not in current_vertex_cover:
        current_vertex_cover.append(v)
        backtracking(grafo, aristas, indice + 1, current_vertex_cover, best_vertex_cover)
        current_vertex_cover.pop()  # Retrocedemos
    else:
        backtracking(grafo, aristas, indice + 1, current_vertex_cover, best_vertex_cover)
   
def esta_cubierta(u, v, current_vertex_cover):
    return u in current_vertex_cover or v in current_vertex_cover

def vertex_cover_min(grafo):
    aristas = obtener_aristas(grafo)
    best_vertex_cover = []
    current_vertex_cover = []
    backtracking(grafo, aristas, 0, current_vertex_cover, best_vertex_cover)
    return best_vertex_cover
```