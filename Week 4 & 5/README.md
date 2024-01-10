# Week 4-5 : Q-Learning Algorithm and Project Implementation

Howdy Fellas! Welcome to the final phase of our project where you will learn about the *Q-learning* algorithm, the algorithm that is the core of Reinforcement Learning. Along with this you will begin your project and train your very own agent. Happy Learning!

## Q Learning
This algorithms is just like you did in the MDP's. But now imagine that you don't know what is the transitions nor the reward functions. Your agent makes the move, you see the change and receive the reward. Thats it! Now think about using this incomplete information is it possible to learn to maximize the reward.  
1. [Intro - Reading](https://www.datacamp.com/tutorial/introduction-q-learning-beginner-tutorial)
2. [Visual Explaination](https://towardsdatascience.com/reinforcement-learning-explained-visually-part-4-q-learning-step-by-step-b65efb731d3e)
3. [Video: RL in Python](https://www.youtube.com/watch?v=iKdlKYG78j4)


## Deep Q Learning

1. [Deep Q leaning explaination](https://towardsdatascience.com/deep-q-learning-tutorial-mindqn-2a4c855abffc)
2. [DQN Algorithm](https://towardsdatascience.com/reinforcement-learning-explained-visually-part-5-deep-q-networks-step-by-step-5a5317197f4b)
3. [Video: Deep Q Learning](https://www.youtube.com/watch?v=WuuY2V475Yg)
4. [Video: DQN Algorithm](https://www.youtube.com/watch?v=Psrhxy88zww): From 25:50

##  Project Implementation
The project you are supposed to do is complicated. I would warn that it takes a lot of time(in days) to train a good RL model. So for the final project you may choose to continue with the *'Kung Fu Master'*([link](https://www.gymlibrary.dev/environments/atari/kung_fu_master/)) game or continue with a easier game like *'Breakout'* or *'Cartpole'*.  
Use the following command in the terminal to install the _Gym Environment_ 
```shell
pip install "gym[atari, accept-rom-license]"  
``````
You will have to use the DQN Algorithm to train your agent by use of OpenAI Gym. At the end there should be a demo present to show how good the agent is along with average total reward as compared to random agent.  
We will soon provide you with some tips and helper codes but in the meantime you may start writing your code.  
Best of Luck to Everyone !