import copy
from collections import Counter
class Database(object):


	def __init__(self ,  node_parent ):

		node = Nodes((node_parent , None))
		self.tree = {node_parent : None}
		self.root = node


	def add_nodes(self , list_tuple):
		self.before_update = copy.deepcopy(self.tree)

		for i in set(list_tuple):
			Nodes.add_child(self.root, i[0])
			self.tree[i[0]] = i[1]

		edit = set(self.tree.keys()) - set(self.before_update.keys())
		self.edits = dict()
		for key in edit:
			self.edits[key] = self.tree.get(key)

		self.graph = list_tuple

		list_child = []

		for i , j  in self.graph :
			list_child.append(self.recursive_dfs(self.graph , i))
		self.enfant = list_child[0]


	def recursive_dfs(self, tree, node , find =[] , neighbour = None):

		if node not in find:
			find.append(node)
			if node not in tree:
				return find
			for neighbour in tree[node]:
				find = self.recursive_dfs(tree, neighbour, find)
		return find , neighbour


	def add_extract(self , dict):

		{i: j for i, j in dict.items()}
		self.dico = dict


	def get_extract_status(self):
		self.status = {}
		for i , j   in self.dico.items():
			key = i
			self.status[key] = 'Valid'

			for e in j :

				if e not in self.enfant :
					self.stat = 'Invalid'


				for  k ,l in self.before_update.items():
					for m , n  in self.edits.items():
						if k == n == e:

							self.stat = 'Granularity_Stage'
						if  l == n and e == k  :
							self.stat = 'Covery_stage'


			self.status.update({key: self.stat})
		return self.status


class Nodes:

	def __init__(self , nodes_tuple  , list = [] ):
		self.nodesnew= nodes_tuple[0]
		self.nodesparent = nodes_tuple[1]
		self.list = list



	def add_child(self , nodeschildinsert):
		self.nodes_child =  Nodes((nodeschildinsert, self.nodesnew))

		if self.nodesparent == None:
			self.nodesparent == self.nodesnew

		self.list.append(self.nodes_child)
























