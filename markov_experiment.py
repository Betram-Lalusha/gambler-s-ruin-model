import markov_class
import random
import matplotlib.pyplot as plt

class Markov_Experiment:

    #Runs experiments of the Gambler's ruin with p = 0.5
    def fair_game_experiments(self, n):
        p_values = [0.5 for _ in range(n)]  #p will be constant through each game
        n_values = [i for i in range(1,n+1)] #generate values of n
        x_values = []  #list of the average highest amount for each p and n value
        
        for i in range(len(p_values)):
            markov = markov_class.Markov(p_values[i], n_values[i])
            x_values.append(markov.simulate_markov_chain(10000))
    
        print("x_values ", x_values)
        self.plot_results( n_values, x_values)

    #Runs experiments of the Gambler's ruin with p = 0.5 with random values of
    #n between 1 and n (inclusive)
    def fair_game_experiments_random_n(self, n):
        p_values = [0.5 for _ in range(n)]  #p will be constant through each game
        n_values = [random.randint(1,n+1) for _ in range(1,n+1)] #generate values of n
        x_values = []  #list of the average highest amount for each p and n value
        
        for i in range(len(p_values)):
            markov = markov_class.Markov(p_values[i], n_values[i])
            x_values.append(markov.simulate_markov_chain(10000))
    
        print("x_values ", x_values)
        self.plot_results( n_values, x_values)

    #Runs experiments of the Gambler's ruin with random values of p
    def random_p_experiments(self):
        p_values = [random.random() for _ in range(1000)]  #generate random values of p
        n_values = [random.randint(1, 1000) for _ in range(1000)] #generate random values of n
        x_values = []  #list of the average highest amount for each p and n value
        
        for i in range(len(p_values)):
            markov = markov_class.Markov(p_values[i], n_values[i])
            x_values.append(markov.simulate_markov_chain(10000))
    

        print("x_values ", x_values)
    
    #Creates a plot of results from an experiment
    def plot_results(self, x_values, y_values):
        # Plotting
        plt.plot(x_values, y_values, marker='o')  # 'o' for markers
        plt.xlabel('N (max amount desired)')
        plt.ylabel('x (Average highest amount achieved)')
        plt.title('Gambler\'s Ruin problem')
        plt.grid(True)  # Show grid
        plt.show()

markov_experiment = Markov_Experiment()
#markov_experiment.fair_game_experiments(200)
markov_experiment.fair_game_experiments(300)
