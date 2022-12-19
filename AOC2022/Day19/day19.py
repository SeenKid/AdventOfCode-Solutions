import re
lines = open('input.txt').readlines()
lines = [line.strip() for line in lines]

costs = list()
for line in lines: 
    # get all integers in line
    costs.append([int(i) for i in re.findall(r'\d+', line)])
#costs = [(1,4,2,3,14,2,7), (2,2,3,3,8,3,12)]    # Test example

def quality_heuristic(state): 
    # As the famous saying goes: 
    # 1 geode in the hand is worth 1000 in the bush
    minutes, (robots, inventory, mined) = state
    return 1000*mined[3] + 100*mined[2] + 10*mined[1] + mined[0]

def bfs(costs, robots, num_minutes, top_queue = 30000):
    queue = list()
    queue.append((0, (robots, (0,0,0,0), (0,0,0,0)))) # (minutes, (robots, inventory, mined))
    max_geodes_mined = 0
    depth = 0
    while queue:
        minutes, (robots, old_inventory, mined) = queue.pop(0)

        if minutes > depth: 
            # Prune our search space!!!
            queue.sort(key=quality_heuristic, reverse=True)
            queue = queue[:top_queue]
            depth = minutes

        if minutes == num_minutes:
            max_geodes_mined = max(max_geodes_mined, mined[3])
            continue
       
        # Mine ore with the robots
        new_inventory = tuple([old_inventory[i] + robots[i] for i in range(4)])
        new_mined = tuple([mined[i] + robots[i] for i in range(4)])
        
        # Case of not building a robot
        queue.append((minutes+1, (robots, new_inventory, new_mined)))

        # Build new robots, and try building each type of robot
        # TODO can we build more than one robot?
        for i in range(4):
            cost_robot = costs[i]

            # Check if we have enough materials to build a robot
            if all([old_inventory[j] >= cost_robot[j] for j in range(4)]): # We can build a robot!!
                new_robots = list(robots)
                new_robots[i] += 1
                new_robots = tuple(new_robots)

                new_inventory_state = tuple([new_inventory[j] - cost_robot[j] for j in range(4)])
                queue.append((minutes+1, (new_robots, new_inventory_state, new_mined)))
    return max_geodes_mined

max_minutes = 24
sum_quality = 0
# Part 1
# I used a simple queue, which was enough to find the optimal solution
# I prune everything too deep using the heuristic that having the higher up materials is better than the lower down materials
for blueprint_id, cost_ore_robot, cost_clay_robot, ob_ore, obs_clay, geode_ore, geode_ob in costs:
    cost_per_robot = [
        (cost_ore_robot, 0, 0, 0),
        (cost_clay_robot, 0, 0, 0),
        (ob_ore, obs_clay, 0, 0),
        (geode_ore, 0, geode_ob, 0)
    ]
    num_mined = bfs(cost_per_robot, (1,0,0,0), max_minutes, top_queue=1000)

    sum_quality += num_mined*blueprint_id
    print(f'Blueprint {blueprint_id}: {num_mined} geodes mined')
print("Part 1", sum_quality)

# Part 2
# We now compute for more minutes, but we need to multiply the number of geodes mined
# As the short queue I used in part 1 was not enough, I increased it to 10000
max_minutes = 32
product_geodes = 1
for blueprint_id, cost_ore_robot, cost_clay_robot, ob_ore, obs_clay, geode_ore, geode_ob in costs[:3]:
    cost_per_robot = [
        (cost_ore_robot, 0, 0, 0),
        (cost_clay_robot, 0, 0, 0),
        (ob_ore, obs_clay, 0, 0),
        (geode_ore, 0, geode_ob, 0)
    ]
    num_mined = bfs(cost_per_robot, (1,0,0,0), max_minutes, top_queue=10000)
    product_geodes *= num_mined
    print(f'Blueprint {blueprint_id}: {num_mined} geodes mined')
print("Part 2", product_geodes)