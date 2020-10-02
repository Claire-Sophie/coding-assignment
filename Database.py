

class Database(object):


	def __init__(self ,  node_parent ):

		node = Nodes((node_parent , None))
		self.root = node
		self.dico = {}

	def add_nodes(self , list_tuple):

		for i in set(list_tuple):
			Nodes.add_child(self.root , i[0])

		self.graph = list_tuple

		list_child = []

		for i , j   in self.graph :
			list_child.append(self.recursive_dfs(self.graph , i ))

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
			print('child' , self.enfant)

			for e in j :
				print('e' , e)
				if e not in self.enfant :
					stat = 'Invalid'
				if e in self.enfant:
					stat ='Valid'

				if e in self.enfant and e  in self.enfant:
						stat ='Granularity'

			self.status.update({key: stat})
		print(self.status)

	def get_parent(self, node):

		for i in range(len(self.graph)):
			if self.graph[i][0] == node:
				par = self.graph[i][1]
		return par

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




















