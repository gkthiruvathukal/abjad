from copy import copy
from abjad.tools.abctools import AbjadObject
from abjad.tools.datastructuretools.ImmutableDictionary import ImmutableDictionary
from abjad.tools.sequencetools import all_are_pairs


class Digraph(AbjadObject):
    '''A digraph, built out of edges - pairs of hashable objects:

    ::

        abjad> from abjad.tools.datastructuretools import Digraph

    ::

        abjad> edges = [('a', 'b'), ('a', 'c'), ('a', 'f'), ('c', 'd'), ('d', 'e'), ('e', 'c')]
        abjad> digraph = Digraph(edges)
        abjad> digraph.root_nodes
        ('a',)
        abjad> digraph.terminal_nodes
        ('b', 'f')
        abjad> digraph.cyclic_nodes
        ('c', 'd', 'e')
        abjad> digraph.is_cyclic
        True

    Return `Digraph` instance.
    '''

    ### CLASS ATTRIBUTES ###

    __slots__ = ('_child_graph', '_cyclic_nodes', '_parent_graph', '_root_nodes', '_terminal_nodes')

    ### INITIALIZER ###

    def __init__(self, edges=None):
        if edges is not None:
            assert all_are_pairs(edges)

        parent_graph = { }
        child_graph = { }

        for parent, child in edges:
            # populate parent-wise graph
            if parent not in parent_graph:
                parent_graph[parent] = set([child])
            else:
                parent_graph[parent].add(child)
            if child not in parent_graph:
                parent_graph[child] = set([])

            # populate child-wise graph
            if child not in child_graph:
                child_graph[child] = set([parent])
            else:
                child_graph[child].add(parent)
            if parent not in child_graph:
                child_graph[parent] = set([])

        self._parent_graph = ImmutableDictionary(parent_graph)
        self._child_graph = ImmutableDictionary(child_graph)
        self._cyclic_nodes = self._find_cyclic_nodes()
        self._root_nodes = tuple(sorted([child for child in child_graph if not child_graph[child]]))
        self._terminal_nodes = tuple(sorted([parent for parent in parent_graph if not parent_graph[parent]]))

    ### PRIVATE METHODS ###

    def _find_cyclic_nodes(self):

        parent_graph = { }
        for k, v in self.parent_graph.iteritems():
            parent_graph[k] = copy(v)

        child_graph = { }
        for k, v in self.child_graph.iteritems():
            child_graph[k] = copy(v)

        roots = [child for child in child_graph if not child_graph[child]]
        terminals = [parent for parent in parent_graph if not parent_graph[parent]]

        while roots or terminals:
            for terminal in terminals:
                parents = child_graph[terminal]
                for parent in parents:
                    parent_graph[parent].remove(terminal)
                if terminal in roots:
                    roots.remove(terminal)
                del(parent_graph[terminal])
                del(child_graph[terminal])

            for root in roots:
                children = parent_graph[root]
                for child in children:
                    child_graph[child].remove(root)
                del(parent_graph[root])
                del(child_graph[root])

            roots = [child for child in child_graph if not child_graph[child]]
            terminals = [parent for parent in parent_graph if not parent_graph[parent]]
            
            if not roots and not terminals and parent_graph:
                return tuple(sorted(parent_graph.keys()))

        return ()

    ### PUBLIC ATTRIBUTES ###

    @property
    def child_graph(self):
        return self._child_graph

    @property
    def cyclic_nodes(self):
        return self._cyclic_nodes

    @property
    def is_cyclic(self):
        if self.cyclic_nodes:
            return True
        return False

    @property
    def parent_graph(self):
        return self._parent_graph

    @property
    def root_nodes(self):
        return self._root_nodes

    @property
    def terminal_nodes(self):
        return self._terminal_nodes
