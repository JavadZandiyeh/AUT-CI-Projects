import copy
import random
import math
from player import Player
from tempfile import TemporaryFile

class Evolution:
    def __init__(self):
        self.game_mode = "Neuroevolution"

    def next_population_selection(self, players, num_players):
        """
        Gets list of previous and current players (μ + λ) and returns num_players number of players based on their
        fitness value.

        :param players: list of players in the previous generation
        :param num_players: number of players that we return
        """

        # TODO (Additional: Learning curve)
        fitnesses = [p.fitness for p in players]
        max_fit = max(fitnesses)
        min_fit = min(fitnesses)
        avg_fit = sum(fitnesses)/len(players)
        print(avg_fit)

        # TODO (Implement top-k algorithm here)
        # return self.top_k(players, num_players)

        # TODO (Additional: Implement roulette wheel here)
        # return self.RW(players, num_players)

        # TODO (Additional: Implement SUS here)
        return self.SUS(players, num_players)

        # TODO (Additional: Implement Q-tournament with Q=2 here)
        # return self.Q_tournament(players, num_players)


    def top_k(self, players, num_players):
        sorted_players = sorted(players, key=lambda x: x.fitness, reverse=True)
        return sorted_players[: num_players]

    def RW(self, players, num_players):
        sum_fitness = sum([p.fitness for p in players])
        # create probability list
        front = 0
        prob = []
        for p in players:
            p_i = p.fitness/sum_fitness
            prob.append((front, front+p_i))
            front += p_i
        # choose num_players for next population
        next_population = []
        for i in range(num_players):
            rand_number = random.uniform(0, 1)
            for i in range(len(players)):
                if prob[i][0] <= rand_number < prob[i][1]:
                    next_population.append(players[i])                   
        return next_population

    def SUS(self, players, num_players):
        sum_fitness = sum([p.fitness for p in players])
        # create probability list
        front = 0
        prob = []
        for p in players:
            p_i = p.fitness/sum_fitness
            prob.append((front, front+p_i))
            front += p_i
        # choose num_players for next population
        next_population = []
        s = random.uniform(0, 1/num_players)
        for _ in range(num_players):
            for i in range(len(players)):
                if prob[i][0] <= s < prob[i][1]:
                    next_population.append(players[i]) 
            s += 1/num_players
        return next_population

    def Q_tournament(self, players, num_players):
        next_population = []
        for _ in range(num_players):
            q1 = math.floor(random.uniform(0, num_players))
            q2 = math.floor(random.uniform(0, num_players))
            while(q1 == q2):
                q2 = math.floor(random.uniform(0, num_players))
            if players[q1].fitness > players[q2].fitness:
                next_population.append(players[q1])
            else:
                next_population.append(players[q2])
        return next_population

    def generate_new_population(self, num_players, prev_players=None):
        """
        Gets survivors and returns a list containing num_players number of children.

        :param num_players: Length of returning list
        :param prev_players: List of survivors
        :return: A list of children
        """

        first_generation = prev_players is None
        if first_generation:
            return [Player(self.game_mode) for _ in range(num_players)]
        else:
            # TODO ( Parent selection and child generation )
            
            # parent selection
            parents = self.top_k(prev_players, num_players)
            
            # child selection
            children = []
            for i in range(0, len(parents), 2):
                p1 = parents[i]
                p2 = parents[i+1]
                
                    # clone children
                child1 = self.clone_player(p1)
                child2 = self.clone_player(p2)
                    
                # crossover
                for q in range(len(p1.nn.layer_sizes)-1):
                    # parent features
                    W_p1 = p1.nn.W[q]
                    b_p1 = p1.nn.b[q]
                    W_p2 = p2.nn.W[q]
                    b_p2 = p2.nn.b[q]
                    # crossover W
                    child1.nn.W.append(0.25*W_p1 + 0.75*W_p2)
                    child2.nn.W.append(0.75*W_p1 + 0.25*W_p2)
                    # crossover b
                    child1.nn.b.append(0.25*b_p1 + 0.75*b_p2)
                    child2.nn.b.append(0.75*b_p1 + 0.25*b_p2)
                    
                # mutation
                for q in range(len(p1.nn.layer_sizes)-1):
                    # child features
                    W_c_shape = child1.nn.W[q].shape
                    b_c_shape = child1.nn.b[q].shape
                    # mutation W
                    i_random = math.floor(random.uniform(0, W_c_shape[0]))
                    j_random = math.floor(random.uniform(0, W_c_shape[1]))
                    rand_num = random.uniform(0, 1)
                    if rand_num < 0.25:
                        child1.nn.W[q][i_random, j_random] *= round(random.uniform(0, 2), 2)

                    i_random = math.floor(random.uniform(0, W_c_shape[0]))
                    j_random = math.floor(random.uniform(0, W_c_shape[1]))
                    rand_num = random.uniform(0, 1)
                    if rand_num < 0.25:
                        child2.nn.W[q][i_random, j_random] *= round(random.uniform(0, 2), 2)
                        
                    # mutation b
                    i_random = math.floor(random.uniform(0, b_c_shape[0]))
                    rand_num = random.uniform(0, 1)
                    if rand_num < 0.25:
                        child1.nn.b[q][i_random] *= round(random.uniform(0, 2), 2)

                    i_random = math.floor(random.uniform(0, b_c_shape[1]))
                    rand_num = random.uniform(0, 1)
                    if rand_num < 0.25:
                        child2.nn.b[q][i_random] *= round(random.uniform(0, 2), 2)             

                children.append(child1)
                children.append(child2)

            return children

    def clone_player(self, player):
        """
        Gets a player as an input and produces a clone of that player.
        """
        new_player = Player(self.game_mode)
        new_player.nn = copy.deepcopy(player.nn)
        new_player.fitness = player.fitness
        return new_player
