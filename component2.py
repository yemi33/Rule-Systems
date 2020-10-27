from engine import RuleEngine

def component2():
    # Prepare a rule engine
    engine = RuleEngine(
        path_to_domain_file='content/c2_domain.txt',
        path_to_rules_file='content/c2_rules.txt',
        shuffle_randomly=True,
        random_seed=None
    )

    #engine.debug(action_name="NoPromotion", bindings_string="Initiator=Walker Cobb, Recipient=Warren Brantley, Location=Railroad Station")
    # Execute rules until a specific action has occurred. To ensure
    # that you generate a full murder-mystery plot, you should
    # execute rules until a specific action occurs that represents
    # the culmination of your plot. This doesn't have to be called
    # Denouement, to be clear.
    while not engine.produced_action(action_name='Confess'):
        engine.execute(n=1)


def grade():
    """The function James will be using to grade your component."""
    print("\n\n-- Component 2 -- ")
    component2()
