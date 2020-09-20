class SocialGraph:
  def __init__(self):
    self.members = {}


  def add_node(self,node):
    self.members[node] = set()


  def add_edge(self,node_a,node_b):
    self.members[node_a].add(node_b)
    self.members[node_b].add(node_a)
    
  def subgraph(self, root):
    to_visit = [root]

    visited = set()

    while to_visit:
      node = to_visit.pop(0)
      if node not in visited:
        visited.add(node)

        for neighbor in self.members[node]:
          to_visit.append(neighbor)
    return visited
    
  def suggest_friends(self, me):
    my_friends = set(self.members[me])
    potentials = {}
    # loop over all my friends
    for friend in my_friends:
      # loop over all of their friends
      for potential_friend in self.members[friend]:
      # check to make sure they aren't me, also that I am not friends with them
        if potential_friend not in my_friends and potential_friend is not me:
          # determine how many friends we have in common
          friendship_score = len(set(self.members[potential_friend]).intersection(my_friends))
          if potentials.get(friendship_score):
            potentials[friendship_score].add(potential_friend)
          else:
            potentials[friendship_score] = {potential_friend}
    friend_counts = list(potentials.keys())
    friend_counts.append(0)
    best_count = max(friend_counts)
    return potentials.get(best_count, set())
          # store in the potential buckets by their common friendship count
          # their_friends.intersection(my_friends)
  
graph = SocialGraph()

## Friend Group 1
graph.add_node('Alice')
graph.add_node('Bob')
graph.add_node('Carol')
graph.add_node('Dave')
graph.add_node('Eve')
graph.add_node('Faythe')
graph.add_node('Grace')

## Friend Group 2
graph.add_node('Zed')
graph.add_node('Xavier')
graph.add_node('Quill')
graph.add_node('Robert')


## Friend Group 3
graph.add_node('Heidi')
graph.add_node('Niaj')
graph.add_node('Ivan')
graph.add_node('Trent')


## Friendships
graph.add_edge('Alice', 'Bob')
graph.add_edge('Alice', 'Carol')
graph.add_edge('Alice', 'Dave')
graph.add_edge('Bob', 'Dave')
graph.add_edge('Carol', 'Dave')
graph.add_edge('Alice', 'Eve')
graph.add_edge('Eve', 'Grace')
graph.add_edge('Eve', 'Bob')
graph.add_edge('Faythe', 'Eve')
graph.add_edge('Dave', 'Faythe')
graph.add_edge('Grace', 'Faythe')


graph.add_edge('Xavier', 'Quill')
graph.add_edge('Robert', 'Quill')
graph.add_edge('Xavier', 'Robert')
graph.add_edge('Zed', 'Quill')
graph.add_edge('Zed', 'Xavier')

graph.add_edge('Heidi', 'Niaj')
graph.add_edge('Heidi', 'Ivan')
graph.add_edge('Heidi', 'Trent')
graph.add_edge('Niaj', 'Trent')
graph.add_edge('Ivan', 'Trent')
graph.add_edge('Niaj', 'Ivan')

print(graph.suggest_friends('Faythe'))
print(graph.suggest_friends('Robert'))
print(graph.suggest_friends('Ivan'))