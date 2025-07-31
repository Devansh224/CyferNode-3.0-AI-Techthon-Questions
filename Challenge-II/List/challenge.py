'''

A list has been given to you, your task is to find the maximum for every adjacent pair and store it under a list. 
Multiply the length of the list by 2430 to get the password

Good luck, Codebreakers!

'''

def adjacent(ai_innovations):
    # Your code here
    maxy = []
    for i in range(len(ai_innovations)-1):
      maxNo = max(ai_innovations[i], ai_innovations[i+1])
      maxy.append(maxNo)
    return len(maxy)*2430
ai_innovations = [
  1956,  # Dartmouth Conference
  1961,  # Perceptron
  1963,  # ELIZA
  1970,  # Expert systems
  1980,  # Connectionism and backpropagation
  1990,  # Machine learning
  2000,  # AI applications
  2010,  # Deep learning
  2012,  # AlexNet
  2015,  # AlphaGo
  2017,  # GANs
  2020,  # GPT-3
  2022,  # AI for COVID-19
  2023,  # Continued advancements
  2024,  # Continued advancements
  1958,  # Perceptron learning rule
  1964,  # Dendral
  1965,  # Michie's MENACE
  1966,  # DARTMOUTH SUMMER RESEARCH PROJECT ON ARTIFICIAL INTELLIGENCE
  1967,  # LISP programming language
  1968,  # PROLOG programming language
  1969,  # MYCIN expert system
  1971,  # Stanford Artificial Intelligence Laboratory (SAIL)
  1972,  # SHRDLU natural language understanding system
  1973,  # AMAR system
  1974,  # HEARSAY-II speech understanding system
  1975,  # MYCIN becomes operational
  1976,  # Expert systems become popular
  1977,  # PROSPECTOR expert system
  1978,  # RITA natural language understanding system
  1979,  # Expert systems applied to medicine
  1981,  # Connectionist models become popular
  1982,  # Backpropagation algorithm
  1983,  # Hopfield network
  1984,  # Boltzmann machine
  1985,  # Neural networks applied to image recognition
  1986,  # Neural networks applied to speech recognition
  1987,  # Neural networks applied to natural language processing
  1988,  # Expert systems applied to business
  1989,  # Neural networks applied to robotics
  1991,  # Machine learning applied to data mining
  1992,  # Machine learning applied to pattern recognition
  1993,  # Machine learning applied to fraud detection
  1994,  # Machine learning applied to medical diagnosis
  1995,  # Machine learning applied to financial forecasting
  1996,  # Machine learning applied to customer relationship management
  1997,  # Machine learning applied to marketing
  1998,  # Machine learning applied to search engines
  1999  # Machine learning applied to recommendation systems
]

print(adjacent(ai_innovations))