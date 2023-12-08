import math


def input_parser(input_data):
    
    instructions, node_block = input_data.split('\n\n')
    
    # Replace L and R with 0 and 1, respectively, as they are used to index
    # the below left/right tuples for each node
    instructions = [0 if i == 'L' else 1 for i in instructions]
    
    # Map node names to a tuple of their left and right paths
    nodes = {}
    for line in node_block.splitlines():
        node_name, paths = line.split(' = ')
        left, right = paths[1:-1].split(', ')  # remove parentheses before splitting
        nodes[node_name] = (left, right)
    
    return (instructions, nodes)


def part1(input_data):
    
    instructions, nodes = input_data
    
    steps = 0
    current_paths = nodes['AAA']
    
    while True:
        for direction in instructions:
            steps += 1
            node = current_paths[direction]
            
            if node == 'ZZZ':
                return steps
            
            current_paths = nodes[node]


def part2(input_data):
    
    instructions, nodes = input_data
    
    # Set up the "tracks" that will be followed simultaneously. A single track
    # is only followed until its end node (ending in Z) is reached. The number
    # of steps ultimately required is the least common multiple of the steps
    # required to reach the end of each track.
    tracks = []
    for node, paths in nodes.items():
        if node.endswith('A'):
            tracks.append({
                'current_paths': paths,
                'steps': 0,
                'complete': False
            })
    
    while True:
        for direction in instructions:
            for track in tracks:
                if track['complete']:  # if the track is already complete, skip it
                    continue
                
                track['steps'] += 1
                
                new_node = track['current_paths'][direction]
                if new_node.endswith('Z'):
                    # The end node is reached, this track is now complete
                    track['complete'] = True
                
                track['current_paths'] = nodes[new_node]
        
        # Once all tracks are complete, there is no need to continue
        if all([t['complete'] for t in tracks]):
            break
    
    return math.lcm(*[t['steps'] for t in tracks])
