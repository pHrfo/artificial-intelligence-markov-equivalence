# Markov Equivalence

## Requirements
* Python3

## How to run

The first step to run this code is to import the MarkovEquivalenceChecker class and instantiate an object with the path to the graph files:

    >>> from markov_equivalence_checker import MarkovEquivalenceChecker
    >>> mkv = MarkovEquivalenceChecker("file_g1.txt", "file_g2.txt")
    
Now, there are a few methods you can use with this class. The most important is

    >>> mkv.are_markov_equivalent()
    True
    
Which verifies if the two given graphs, that represent bayesian networks, are markov equivalent, accordingto the definition given in the topic 3.3.6 of "Bayesian Reasoning and Machine Learning", by David Barber [1].

## References

[1] "Bayesian Reasoning and Machine Learning", by David Barber. http://web4.cs.ucl.ac.uk/staff/D.Barber/pmwiki/pmwiki.php?n=Brml.HomePage
