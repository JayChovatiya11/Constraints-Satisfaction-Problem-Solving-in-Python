#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install python-constraint


# In[2]:


from constraint import Problem, AllDifferentConstraint

def killed_agatha():
    problem = Problem()
# Define variables and domains
    problem.addVariables(['Agatha', 'Butler', 'Charles'], ['A', 'B', 'C'])
# Add all constraints
    problem.addConstraint(lambda a, b: b != 'C' and (a == 'A' or a != b), ('Agatha', 'Butler'))
    problem.addConstraint(lambda a, b, c: (a == 'A' and b != 'Butler') or (b == 'Butler' and a != 'Agatha'), ('Agatha', 'Butler', 'Charles'))
    problem.addConstraint(AllDifferentConstraint())
    problem.addConstraint(lambda a: a == 'A', ('Agatha',))
    problem.addConstraint(lambda c: c != 'A', ('Charles',))
# Solving the problem by using the getsolution function
    solutions = problem.getSolutions()
    if not solutions:
        print('No solution found.')
    else:
        # Check each soultion that who is the killed agatha
        for solution in solutions:
           if solution['Agatha'] == 'A':
                print('Agatha killed herself.')
           elif solution['Butler'] == 'B':
                print('The Butler killed Agatha.')
           elif solution['Charles'] == 'C':
                print('Charles killed Agatha.')

killed_agatha()


# In[ ]:




