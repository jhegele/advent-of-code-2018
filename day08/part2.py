import uuid

# ugh, well, i was HOPING to avoid further recursion but it seems that's not possible. so,
# this function takes the entire tree and a node id as an input then returns the value of
# the node identified by the id.
def node_value(tree, nid):
    # find the node, initialize value to zero, and find any children of the node
    node = [n for n in tree if n['id'] == nid][0]
    val = 0
    children = [n for n in tree if n['parent_id'] == nid]
    # per the problem description, if there are no children, the value is the sum of the
    # metadata entries
    if len(children) == 0:
        return sum(node['metadata_entries'])
    else:
        # if there ARE children, then we need to use the metadata entries to find which
        # children (if any) we need values from
        for e in node['metadata_entries']:
            # one upside to our flat structure is it enables us to quickly search for 
            # nodes with a specific parent id and child index. as an aside, there are
            # comments in the nodes() function on what the child index is here.
            child = [n for n in tree if n['parent_id'] == nid and n['child_idx'] == e]
            # if we found a valid child, send that child id through this function
            if len(child) == 1:
                val += node_value(tree, child[0]['id'])
        return val
        
# this is largely similar to the nodes() function in part 1. however, part 2 added an
# interesting twist in that you have to keep up with when children are added to a
# parent. since we have a flat structure, we need some sort of identifier to do that.
# i decided on using a child index (child_idx) property. so each node will now have
# knowledge of the order in which it was added to its parent.
def nodes(data, pid = None, n = [], child_idx = None):
    cn = data.pop(0)
    me = data.pop(0)
    i = str(uuid.uuid4())
    if cn == 0:
        m = []
        for _ in range(0, me):
            m.append(data.pop(0))
        n.append({
            'id': i,
            'child_idx': child_idx,
            'parent_id': pid,
            'metadata_entries': m
        })
        return n
    else:
        m = []
        # here is where we're applying our new child index. rather than discarding
        # the loop counter value, we use it to establish the order in which child
        # nodes are added.
        for idx in range(0, cn):
            n = nodes(data, i, n, idx + 1)
        for _ in range(0, me):
            m.append(data.pop(0))
        n.append({
            'id': i,
            'child_idx': child_idx,
            'parent_id': pid,
            'metadata_entries': m
        })
        return n

with open('./inputs/part1-2.txt') as puzzle_input:
    data = puzzle_input.readlines()[0].strip()

data = list(map(int, data.split()))
tree = nodes(data)
root_id = [n['id'] for n in tree if n['parent_id'] is None][0]
print('Root node value: {}'.format(node_value(tree, root_id)))
