

import igraph, random
import matplotlib.pyplot as plt

# Helper function for auto-display of graphs in Jupyter notebooks
def format_igraph(g : igraph.Graph, **kwargs):

    if g.vcount() > 200 or g.ecount() > 1000:
        print(repr(g))
        return
    
    # Always show vertex labels
    if 'vertex_label' not in kwargs:
        if 'label' in g.vs.attribute_names():
            kwargs['vertex_label'] = g.vs['label']
        elif 'name' in g.vs.attribute_names():
            kwargs['vertex_label'] = g.vs['name']
        else:
            kwargs['vertex_label'] = range(g.vcount())

    # If no layout was specified, compute a "nice" layout
    if 'layout' not in kwargs:
        rng_state = random.getstate()
        random.seed(42)
        if g.is_tree() and g.vcount() <= 50 and g.diameter() <= 10:
            kwargs['layout'] = g.layout_reingold_tilford()
        else:
            kwargs['layout'] = g.layout_fruchterman_reingold()
        random.setstate(rng_state)

    ax = plt.subplot()
    ax.invert_yaxis()
    plt.axis('equal')
    return igraph.plot(g, target=ax, **kwargs)
