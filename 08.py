with open('08.txt') as f:
    lines = f.read().strip().split('\n')

nodes = {}
for line in lines:
    x,y,z = map(int, line.split(','))
    nodes[(x,y,z)] = []

def jdist(node1, node2):
    x1,y1,z1 = node1
    x2,y2,z2 = node2
    dist = (x1-x2)*(x1-x2)+(y1-y2)*(y1-y2)+(z1-z2)*(z1-z2) # Don't need the square root ...
    return(dist)

distances = []
nodelist = list(nodes.keys())
for i,node1 in enumerate(nodelist[:-1]):
    for j,node2 in enumerate(nodelist[i+1:]):
        dist = jdist(node1, node2)
        distances.append((dist, node1, node2))

distances = sorted(distances)

circuits=[]
seen = set()
amount = 1000 # for part 1
part2 = False
for a,dist in enumerate(distances):
    d, n1, n2 = dist
    if len(circuits) == 0: # First circuit
        newcirc = set()
        newcirc.add(n1)
        newcirc.add(n2)
        circuits.append((2, newcirc))
        seen.add(n1)
        seen.add(n2)
        
    else:
        connected = False
        for i,circ in enumerate(circuits): # [ (2 {(23,13,13), (234,23,4)}) ]
            size, nodes = circ
            
            # Om de ligger i olika kretsar, koppla ihop kretsarna.
            if n1 in seen and n2 in seen: # Båda finns
                if n1 in nodes and not n2 in nodes: # i olika kretsar!
                    # Find the node of n2.
                    for j,circ in enumerate(circuits):
                        #print('connecting', i,j)
                        size2, nodes2 = circ
                        if n2 in nodes2:
                            nodes = nodes.union(nodes2)
                            circuits[i] = (len(nodes), nodes)
                            circuits[j] = (0, set())
                            connected = True

                elif n2 in nodes and not n1 in nodes: # i olika kretsar!
                    # Find the node of n2.
                    for j,circ in enumerate(circuits):
                        #print('connecting', i,j)
                        size1, nodes1 = circ
                        if n1 in nodes1:
                            nodes = nodes.union(nodes1)
                            circuits[i] = (len(nodes), nodes)
                            circuits[j] = (0, set())
                            connected = True
                            
                elif n1 in nodes and n2 in nodes:
                    connected = True

            if n1 in nodes or n2 in nodes:
                nodes.add(n1)
                nodes.add(n2)
                seen.add(n1)
                seen.add(n2)
                circuits[i] = (len(nodes), nodes)
                connected = True

        if not connected:
            newnodes = set()
            newnodes.add(n1)
            newnodes.add(n2)
            circuits.append((2, newnodes))
            seen.add(n1)
            seen.add(n2)

    if part2 and 1 == sum([1 for x,_ in circuits if x > 0]):
        ans2 = n1[0] *n2[0]
        print('Advent of code, day 8, part 2:', ans2)
        exit()

    if a == amount-1:
        largest = sorted(circuits)[-3:]
        ans1 = 1
        for (size, _) in largest:
            ans1 = ans1 * size
        print('Advent of code, day 8, part 1:', ans1)
        part2 = True
