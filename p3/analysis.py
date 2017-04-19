# analysis.py
# -----------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

######################
# ANALYSIS QUESTIONS #
######################

# Change these default values to obtain the specified policies through
# value iteration.

def question2():
  answerDiscount = 0.9
  answerNoise = 0.0
  """Description:
  [Enter a description of what you did here.]
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise

def question3a():
  answerDiscount = 0.2
  answerNoise = 0.0
  answerLivingReward = 0.0
  """Description: We give the agent a smaller discount to encourage it
  to get to the closer exit.  We also don't want any noise so that the
  agent will take the path next to the cliffs.
  [Enter a description of what you did here.]
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3b():
  answerDiscount = 0.2
  answerNoise = 0.1
  answerLivingReward = -0.4
  """Description: We give a lower discount so that the agent wants to
  go towards the closer exit.  We give the agent a slight amount of noise
  to make it avoid the cliff but a slightly bad living reward so the agent
  exits as fast as possible.
  [Enter a description of what you did here.]
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3c():
  answerDiscount = 0.4
  answerNoise = 0.0
  answerLivingReward = 1
  """Description: We want a higher discount but no noise so we
  avoid the cliff.  We also want a higher living reward to give the agent
  insentive to go to the farther exit.
  [Enter a description of what you did here.]
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3d():
  answerDiscount = 0.9
  answerNoise = 0.2
  answerLivingReward = 0
  """Description: We want a high discount to get the agent to go
  further.  We want a little noise so that the agent avoids the cliff
  but no living reward.
  [Enter a description of what you did here.]
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question3e():
  answerDiscount = 0.9
  answerNoise = 0.2
  answerLivingReward = 0.0
  """Description:
  [Enter a description of what you did here.]
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return answerDiscount, answerNoise, answerLivingReward
  # If not possible, return 'NOT POSSIBLE'

def question6():
  answerEpsilon = 0
  answerLearningRate = None
  """Description:
  [Enter a description of what you did here.]
  """
  """ YOUR CODE HERE """

  """ END CODE """
  return 'NOT POSSIBLE'
  return answerEpsilon, answerLearningRate
  # If not possible, return 'NOT POSSIBLE'

if __name__ == '__main__':
  print 'Answers to analysis questions:'
  import analysis
  for q in [q for q in dir(analysis) if q.startswith('question')]:
    response = getattr(analysis, q)()
    print '  Question %s:\t%s' % (q, str(response))
