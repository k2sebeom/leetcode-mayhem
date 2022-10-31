'''

Title: Implement Trie (Prefix Tree)
Source: https://leetcode.com/problems/implement-trie-prefix-tree/
Comment: Trie is a recursive data structure as well

'''

class Trie(object):

	def __init__(self):
		self.trie = {}


	def insert(self, word):
		t = self.trie
		for c in word:
			if c not in t: t[c] = {}
			t = t[c]
		t["-"] = True


	def search(self, word):
		t = self.trie
		for c in word:
			if c not in t: return False
			t = t[c]
		return "-" in t

	def startsWith(self, prefix):
		t = self.trie
		for c in prefix:
			if c not in t: return False
			t = t[c]
		return True