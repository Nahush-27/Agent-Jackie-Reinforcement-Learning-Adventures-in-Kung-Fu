# Week 2: Introduction to Reinforcement Learning
Welcome to Week 2 of our project, where we're diving headfirst into the fascinating world of Reinforcement Learning (RL). Brace yourself for an exhilarating exploration of RL concepts and algorithms that will set the stage for the thrilling challenges that lie ahead.

<p align="center" width="100%">
    <img width="60%" src="./files/RL_illustration.png"> 
</p>

1. [**What is Reinforcement Learning**](https://www.analyticsvidhya.com/blog/2021/02/introduction-to-reinforcement-learning-for-beginners/) - Dive deep into the core principles of RL with this insightful article.
2. [**A breif introduction to RL (video)**](https://www.youtube.com/watch?v=JgvyzIkgxF0) - Let's kick things off with an engaging video that brings RL to life.

## 🎰 Multi-Armed Bandits: RL's Foundation
Now, let's turn our attention to the foundational Multi-Armed Bandit problem. We'll unravel the intricacies of this crucial concept and equip ourselves with three powerful algorithms—Epsilon Greedy, Thompson Sampling, and UCB—to tackle this challenge head-on.

<p align="center" width="100%">
    <img width="40%" src="./files/multi_armed_bandit_image.png"> 
</p>

1. [**Multi Armed Bandit**](https://gibberblot.github.io/rl-notes/single-agent/multi-armed-bandits.html) - Explore the fundamentals of Multi-Armed Bandits in this comprehensive resource.

2. [**Introductory video**](https://youtu.be/9pZv3-6EUq8?feature=shared) - Immerse yourself in this video to grasp the essence of Multi-Armed Bandits.

The following are some algoirthms for solving Multi Armed Bandits: 

3. [**Epsilon Greedy Algorithm**](https://youtu.be/EjYEsbg95x0?feature=shared)

4. [**Thompson Sampling Algorithm**](https://youtu.be/GVQUGNv33LY?feature=shared)

5. [**Upper Confidence Bound (UCB) Algorithm**](https://youtu.be/s6UHInwoqb0?feature=shared)

6. [**Thompson vs UCB**](https://youtu.be/e4f0or7x5xc?feature=shared)

7. [**Formal Notes of Multi Armed Bandits**](https://courses.cs.washington.edu/courses/cse599i/18wi/resources/lecture3/lecture3.pdf) - Take your understanding to the next level with formal notes. The section "Stochastic Multi-Armed Bandits" and its algorithms provide a solid foundation. The optimal bound proof for UCB is not compulsory to read. If you're up for a challenge, explore the optimal bound for UCB in this [**in-depth explanation.**](https://banditalgs.com/2016/09/18/the-upper-confidence-bound-algorithm/)

## Assignment 2

Now after some heavy (maybe 🤔?) bombarding of info let's move onto the exciting part. This week you will write your very own algorithm to crack the multi-armed ~monster~ bandit. Officially you are supposed to use the [problem.ipynb](./problem.ipynb) as a base to implement the *Epsilon-Greedy Algorithm, the **Upper Confidence Bound(UCB) Algorithm* and the *Thompson Sampling Algorithm*.  
Make sure to make plenty use of <u>classes and objects</u> while implementing the algorithm. We want you to complete the following tasks:
1. Run the algorithms for some values of the horizon and other parameters (Your Choice Completely).
2. At the end just print the total regret accumulated and what arm do you (your algorithm) thinks is *best*. 
3. Also display a graph showing the Total Regret vs Timesteps plot. Judge them and decide which algorithm is the best. (If you can't then at least point out the worst looking one)
4. Remember to do it for all 3 Algorithms
5. For evaluation create a seperate code block where you create a custom bandit (prob. values should be changable by us). Just *running* the code block should run all 3 algorithms for bandits with same probability values and display the plot for all of them.  

The *Deadline* will be **11:59 pm, 31st Dec (Sun)**.  
For submission, you are required to create a GitHub Repository (if you don't have an account make one quickly 🐌). *Upload* the final Notebook(.ipynb) file to the repo. Remember to do the same for Week 1 submissions.
> Note that for final evaluation of WIDS, this Repository will be important so make one quickly.


## Assignment Solution

Check out the [**solution for Assignment 2 here**](./Assignment%202%20solution.ipynb)