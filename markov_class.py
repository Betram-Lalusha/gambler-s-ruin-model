import numpy as np

class Markov:
    # Constructor with parameters p (the probability of winning a game at each stage)
    # and n (the total amount of money the gambler desires).
    def __init__(self, p, n):
        self.N = n
        self.p = p
        self.q = 1 - p  #the probability of losing $1 dollar at each state
        self.states = ["$" + str(i) for i in range(n+1)] #create the states array
        self.transition_matrix = self.create_transition_matrix(self.N, self.p, self.q)
    

    ##Creates the transition matrix
    def create_transition_matrix(self, n, p, q) -> list:
        #intiliaze the transition matrix to have zero probabilities everywhere
        transition_matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]
        transition_matrix[0][1] = p  #probability of transitioning from the $0 to $1 dollar
        for i in range(1, len(transition_matrix) - 1):
            transition_matrix[i][i - 1] = q #probability of transitioning to previous state
            transition_matrix[i][i + 1] = p #probability of transitioning to next state
        
        return transition_matrix
    
    # Simulates the transition through the markov chain repeating the experiment num_experiments times.
    # Returns the average highest amount reached before the player losses all their money or wins N dollars.
    def simulate_markov_chain(self, num_experiments) -> int:
        # simulate experiment num_experiments times
        average_highest_amount = 1
        hightest_amounts = []
        transition_states = [i for i in range(len(self.states))] #numerical representation of transition states
        for _ in range(num_experiments):
            current_state = 1  #starts with one dollar
            hightest_amount = 1 #highest amount player won
            while current_state != 0 and current_state != len(self.states) - 1:
                # Decide the next state using a random.choice()
                current_state = np.random.choice(transition_states, p=self.transition_matrix[current_state])
                # get max amount reached
                hightest_amount = max(hightest_amount, current_state)
                # printing the path of random walk
                print(self.states[current_state], "--->", end=" ")
            
            hightest_amounts.append(hightest_amount)

        average_highest_amount = sum(hightest_amounts) / len(hightest_amounts)
        print("\ln")
        print("highest average amount ", average_highest_amount)
        return average_highest_amount
        



# markov = Markov(0.5, 10)
# markov.simulate_markov_chain(100000)




# # Encoding this states to numbers as it
# # is easier to deal with numbers instead 
# # of words.
# state = ["$1", "$2"]

# # Assigning the transition matrix to a variable
# # i.e a numpy 2d matrix.
# MyMatrix = np.array([[0.6, 0.4], [0.7, 0.3]])

# # Simulating a random walk on our Markov chain 
# # with 20 steps. Random walk simply means that
# # we start with an arbitrary state and then we
# # move along our markov chain.
# n = 20

# # decide which state to start with
# StartingState = 0
# CurrentState = StartingState

# # printing the stating state using state
# # dictionary
# print(state[CurrentState], "--->", end=" ")

# while n-1:
# 	# Deciding the next state using a random.choice()
# 	# function,that takes list of states and the probability
# 	# to go to the next states from our current state
# 	CurrentState = np.random.choice([0, 1], p=MyMatrix[CurrentState])
	
# 	# printing the path of random walk
# 	print(state[CurrentState], "--->", end=" ")
# 	n -= 1
# print("stop")

# # Let us find the stationary distribution of our 
# # Markov chain by Finding Left Eigen Vectors
# # We only need the left eigen vectors
# MyValues, left = scipy.linalg.eig(MyMatrix, right=False, left=True)

# print("left eigen vectors = \n", left, "\n")
# print("eigen values = \n", MyValues)

# # Pi is a probability distribution so the sum of 
# # the probabilities should be 1 To get that from 
# # the above negative values we just have to normalize
# pi = left[:, 0]
# pi_normalized = [(x/np.sum(pi)).real for x in pi]
# pi_normalized
