import requests
import json
import heapq

class Simulator():
    def __init__(self, token, problem):
        self.url = 'https://pegkq2svv6.execute-api.ap-northeast-2.amazonaws.com/prod/users'
        self.token = token
        self.problem = problem
        if problem == 1:
            self.N = 5
            self.num = 4
            self.T_num = 5
        elif problem == 2:
            self.N = 60
            self.num = 3
            self.T_num = 10

        self.run()

    def run(self):
        self.start()
        print('start ' + str(self.problem))


        for _ in range(720):
            self.view_location()
            self.view_trucks()
            command = self.calc()
            self.simulate(command)
        self.view_score()

        print('finished')


    def calc(self):
        l_min_heap = []
        l_max_heap = []
        for l_id in range(self.N**2):
            heapq.heappush(l_min_heap,([self.location[l_id]['located_bikes_count'], [l_id//self.N, l_id%self.N]]))
            heapq.heappush(l_max_heap,([-self.location[l_id]['located_bikes_count'], [l_id//self.N, l_id%self.N]]))


        for idx in range(self.T_num):
            destination = heapq.heappop(l_min_heap)
            pick = heapq.heappop(l_max_heap)
            if destination[0] > 3:
                break
            max_dist = self.N*2
            max_tdx = 0
            for tdx in range(self.T_num):
                dist = abs(self.truck[tdx].xy[0] - pick[1][0]) + abs(self.truck[tdx].xy[1] - pick[1][1])
                if self.truck[tdx].status == 'stopped' and dist < max_dist:
                    max_tdx = tdx
                    max_dist = dist
            
            self.truck[max_tdx].status = 'to_pick'
            self.truck[max_tdx].pick.append(pick[1])
            self.truck[max_tdx].destination.append(destination[1])


        commands = self.truck_command()
        return commands


    def truck_command(self):
        commands = []
        for tdx in range(self.T_num):
            t_command = []
            if self.truck[tdx].loaded_bikes_count < 2 and self.truck[tdx].pick and self.truck[tdx].status == 'to_pick':
                move_x = self.truck[tdx].pick[0][0] - self.truck[tdx].xy[0]
                move_y = self.truck[tdx].pick[0][1] - self.truck[tdx].xy[1]
                while move_x > 0:
                    t_command.append(2)
                    move_x -= 1
                    self.truck[tdx].xy[0] -= 1
                while move_x < 0:
                    t_command.append(4)
                    move_x += 1
                    self.truck[tdx].xy[0] += 1
                while move_y > 0:
                    t_command.append(1)
                    move_y -= 1
                    self.truck[tdx].xy[1] -= 1
                while move_y < 0:
                    t_command.append(3)
                    move_y += 1
                    self.truck[tdx].xy[1] += 1
                t_command.append(5)

                if len(t_command) <11:
                    self.truck[tdx].pick.pop(0)
                    self.truck[tdx].status = 'to_dest'
                else:
                    t_command = t_command[:10]

            if len(t_command) < 10 and self.truck[tdx].destination and self.truck[tdx].status == 'to_dest':
                move_x = self.truck[tdx].destination[0][0] - self.truck[tdx].xy[0]
                move_y = self.truck[tdx].destination[0][1] - self.truck[tdx].xy[1]
                while move_x > 0:
                    t_command.append(2)
                    move_x -= 1
                while move_x < 0:
                    t_command.append(4)
                    move_x += 1
                while move_y > 0:
                    t_command.append(1)
                    move_y -= 1
                while move_y < 0:
                    t_command.append(3)
                    move_y += 1
                t_command.append(6)

                if len(t_command) <11:
                    self.truck[tdx].destination.pop(0)
                    if self.truck[tdx].destination and self.truck[tdx].pick:
                        if self.truck[tdx].loaded_bikes_count > 1:
                            self.truck[tdx].status = 'to_dest'
                        else:
                            self.truck[tdx].status = 'to_pick'
                    elif self.truck[tdx].destination:
                        self.truck[tdx].status = 'to_dest'
                    elif self.truck[tdx].pick:
                        self.truck[tdx].status = 'to_pick'
                    else:
                        self.truck[tdx].stauts = 'stopped'
                else:
                    t_command = t_command[:10]

            if len(t_command) > 0:
                commands.append({"truck_id": tdx, "command": t_command })
        
        return commands

            

    def start(self):
        #start api
        headers = {'X-Auth-Token': self.token, 'Content-Type': 'application/json'}
        data = {'problem': self.problem}

        r = requests.post(self.url + '/start', data = json.dumps(data), headers = headers).json()
        self.auth = r['auth_key']
        self.headers = {'Authorization':self.auth, 'Content-Type': 'application/json'}

        self.truck = [Truck() for _ in range(self.T_num)]

    def view_location(self):
        #locations api
        self.location = requests.get(self.url + '/locations', headers= self.headers).json()['locations']

    def view_trucks(self):
        #trucks api
        r = requests.get(self.url + '/trucks', headers = self.headers).json()['trucks']
        for tdx in range(self.T_num):
            if self.truck[tdx].location_id != r[tdx]['location_id']:
                self.truck[tdx].loaded_bikes_count = r[tdx]['loaded_bikes_count']
                self.truck[tdx].location_id = r[tdx]['location_id']
                self.truck[tdx].xy = [self.truck[tdx].location_id//self.N, self.truck[tdx].location_id%self.N]

    def simulate(self, t_command):
        #simulate api
        data = {'commands': t_command}
        r = requests.put(self.url + '/simulate', data = json.dumps(data), headers = self.headers).json()
        self.time = r['time']
        if self.time %100 == 0 or self.time == 720:
            print(self.time)
            print(r['status'])
            print(r['failed_requests_count'])
            print(r['distance'])

    def view_score(self):
        #score api
        r = requests.get(self.url + '/score', headers = self.headers).json()
        print(r)

class Truck():
    def __init__(self):
        self.xy = [0,0]
        self.location_id = 0
        self.pick = []
        self.destination = []
        self.status = 'stopped'
        self.loaded_bikes_count = 0



if __name__ == '__main__':
    token = '5811eec4c5de66ca77ebc5f6aff6efbe'
    simulator = Simulator(token, 1)
    simulator = Simulator(token, 2)