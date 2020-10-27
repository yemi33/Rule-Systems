from engine import RuleEngine

def component1():
  engine = RuleEngine(path_to_domain_file='content/c1_domain.txt',
  path_to_rules_file='content/c1_rules.txt',
  shuffle_randomly=True,
  random_seed=None) 
  engine.execute(n=30)
  print#(engine.working_memory.facts)

def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 1 -- ")
    component1()

#component1()
