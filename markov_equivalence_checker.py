class MarkovEquivalenceChecker:
	def __init__(self, file_g1, file_g2):
		"""
		Receives the files containing the DAG's and creates the adjacency matrices.
		"""
		with open(file_g1) as f:
			lines_g1 = f.readlines()
		with open(file_g2) as f:
			lines_g2 = f.readlines()

		self.g1 = [[int(char) for char in line.split()] for line in lines_g1]
		self.g2 = [[int(char) for char in line.split()] for line in lines_g2]

	def mount_adjacency_list(self, adjacency_matrix):
		"""
		Reads an adjacency matrix and returns the corres-
		ponding adjacency list (or adjacency map)
		"""
		adjacency_list = {}
		for v1 in range(len(adjacency_matrix)):
			adjacency_list.update({v1: [v2 for v2 in range(len(adjacency_matrix[v1])) if adjacency_matrix[v1][v2] == 1]})
		return adjacency_list

	def get_immoralities(self, adj_list):
		"""
		Finds the set of immoralities in the adj_list
		"""
		return [(v1, v3, v2) for v1 in adj_list for v2 in adj_list for v3 in adj_list[v1] if v3 in adj_list[v2] and v1 < v2]


	def check_skeleton(self):
		"""
		Checks if self.g1 and self.g2 have the same skeleton.
		Does it by checking whether there are pairs of nodes 
		that are connected in one of the graphs and not in 
		the other.
		"""

		# Reads the adjacency matrices and computes the list of edges for each graph
		g1_edges = [(v1, v2) for v1 in range(len(self.g1)) for v2 in range(len(self.g1[v1])) if self.g1[v1][v2] == 1]
		g2_edges = [(v1, v2) for v1 in range(len(self.g2)) for v2 in range(len(self.g2[v1])) if self.g2[v1][v2] == 1]

		# Checks if both graphs have the same pairs of nodes connected
		same_skeleton = True
		for pair in g1_edges:
			if pair not in g2_edges and (pair[1], pair[0]) not in g2_edges:
				same_skeleton = False
		for pair in g2_edges:
			if pair not in g1_edges and (pair[1], pair[0]) not in g1_edges:
				same_skeleton = False

		return same_skeleton

	def check_immoralities(self):
		"""
		Checks if self.g1 and self.g2 have the same set of
		immoralities. Does it by computing the immoralities
		in each graph and comparing them.
		"""

		# Computes adjacency lists for self.g1 and self.g2
		g1_al = self.mount_adjacency_list(self.g1)
		g2_al = self.mount_adjacency_list(self.g2)

		immoralities_g1 = self.get_immoralities(g1_al)
		immoralities_g2 = self.get_immoralities(g2_al)

		if len(immoralities_g1) != len(immoralities_g2):
			return False

		for immorality in immoralities_g1:
			if immorality not in immoralities_g2:
				return False

		for immorality in immoralities_g2:
			if immorality not in immoralities_g1:
				return False

		return True

	def are_markov_equivalent(self):
		return self.check_immoralities() and self.check_skeleton()