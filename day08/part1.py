# i needed a way to quickly assign unique ids, the UUID library is explicitly built for that
import uuid

# there are a bunch of ways we could build the representation of this tree but i really
# wanted to produce a flat structure -- i.e. a one dimensional list where each entry
# has some property that links it to either its parent or children id(s). i prefer a
# flat structure here for performance reasons. while we can't avoid recursion in
# building this structure, once it's built it's quite easy to sum up the metadata
# entries and get our answer. this function takes a data structure, a parent ID, and
# the list of previously parsed nodes as its inputs.
def nodes(data, pid = None, n = []):
    # we know that the first two entries in the data represent the number of children
    # and the number of metadata entries, so pull those out of the data then assign the
    # id of this node.
    cn = data.pop(0)
    me = data.pop(0)
    i = str(uuid.uuid4())
    # if there are no children
    if cn == 0:
        m = []
        # gather the metadata (while removing it from the data)
        for _ in range(0, me):
            m.append(data.pop(0))
        # add our node to the list and return the updated list
        n.append({
            'id': i,
            'parent_id': pid,
            'metadata_entries': m
        })
        return n
    else:
        m = []
        # if we do have children, then the child nodes will come BEFORE the metadata
        # entries for this node, so we need to handle those recursively. note that the
        # for _ in range() syntax is fairly common in python. the _ variable name is
        # just a handy way of signifying that you aren't going to actually use the
        # variable.
        for _ in range(0, cn):
            n = nodes(data, i, n)
        # only AFTER the child nodes are parsed can we gather the metadata entries for
        # this node
        for _ in range(0, me):
            m.append(data.pop(0))
        # add this node to the list and return it
        n.append({
            'id': i,
            'parent_id': pid,
            'metadata_entries': m
        })
        return n

# get and parse inputs
with open('./inputs/part1-2.txt') as puzzle_input:
    data = puzzle_input.readlines()[0].strip()

data = list(map(int, data.split()))
# build our tree
tree = nodes(data)
# sum up all the metadata entries and print as our answer
print('Sum of metadata entries: {}'.format(sum([sum(n['metadata_entries']) for n in tree])))
