class New:
    def __init__(self,coordinates,previous=None):
        self.coordinates= coordinates
        self.previous= previous
        self.g_cost=0 if previous is None else None
        self.h_cost=None
        self.f_cost=None
def exact_path(maze,initiate,goal_point):
    frontier= []
    explored= set()
    start= New(initiate)
    goal= New(goal_point)
    frontier.append(start)
    while frontier:
        curr= min(frontier, key=lambda x:x.f_cost)
        frontier.remove(curr)
        explored.add(curr.coordinates)

        if curr.coordinates==goal.coordinates:
            path=[]
            while curr:
                path.append(curr.coordinates)
                curr=curr.previous
            return path[::-1]
        moves= [(0,-1),(-1,0),(0,1),(1,0)]

        for move in moves:
            new_coordinates= (curr.coordinates[0]+move[0], curr.coordinates[1]+ move[1])
            if not (0 <= new_coordinates[0]< len(maze) and 0<= new_coordinates[1]<len(maze[0])):
                continue
            if maze[new_coordinates[0]][new_coordinates[1]]== 1 or new_coordinates in explored:
                continue

            point= New(new_coordinates,curr)
            point.g_cost =curr.g_cost +1
            point.h_cost= abs(point.coordinates[0] - goal.coordinates[0]) + abs(point.coordinates[1]- goal.coordinates[1])
            point.f_cost =point.g_cost + point.h_cost

            if any(frontier_point.coordinates==point.coordinates and frontier_point.f_cost<=point.f_cost for frontier_point in frontier):
                continue
            frontier.append(point)
    return None
example=[
    [0,0,0,0,0],
    [0,1,1,1,0],
    [0,0,0,0,0],
    [0,1,0,0,0],
    [0,0,0,1,0]
]  

start_p=(0,0)
goal_p=(4,4)
path= exact_path(example,start_p,goal_p)
print("Congratulations! Your Path is Found.....")