# Reaction Kinetics Prediction using ML

Say you gave me a recipe made from ripping a few pages out of a cookbook (like a ransom note lol), and asked me to predict how long it'd take to make. It might be a second or a century. So I'd need to look back at other recipes I'd seen, how long specific steps within them took, finding similarities to the steps in your recipe. I tried to do that, but for chemical reactions.

### Problem Statement
   The Arrhenius rate constant equation ( k = A * exp( - E_a/ RT ) ) contains 2 parameters that specify how quickly a reaction progresses: activation energy (threshold, in Joules, for reaction to occur), and the pre-exponential factor (frequency of, and likelihood of correct orientation of, collision)
   I'm trying to decompose organic reactions into the likely mechanistic pathways (steps) taken to go from reactants to products; essentially trying to figure out the black box of chemical reactions, as predicting reaction mechanisms is an extremely difficult task
   I hope to leverage this to predict the 2 parameters above

### Relevant Background

- the US government's NIST Reaction Kinetics database has a treasure trove of data on how quickly many different reactions progress
- a new, extremely high quality dataset, on reaction pathways of organic reactions has 30k+ reaction mechanisms/steps, expertly annotated by professional chemists, in standardized (canonical SMILES) format, even specifying exactly which bounds are broken/formed, and assigning unique IDs for you to follow a single atom through a reaction

The NIST database and pathways dataset publication links are here:

- https://kinetics.nist.gov/kinetics/
- https://www.nature.com/articles/s41597-024-03709-y

### Approach and Progress

In reverse chronological order:
 -I'm trying to augment my single-step pathways dataset, creating reasonable multi-step reactions; doing this by training a Graph Neural Network (with PyTorch) to learn structural and electronic patterns that determine local reactivity compatibility. 
- I trained a Random Forest model (with scikit-learn) to classify single mechanism (step) type (eg. substitution, elimination, etc.) with 99.3% accuracy; used Morgan fingerprint reaction difference bit vectors. That's a mouthful, but that means a 1024-4096 long bit (0/1s) vector identifying different substructures, subtracted entry wise [products]-[reactants]
- Web scraped ~64k reaction kinetics info from NIST, currently working on data cleaning the kinetics data to convert to SMILES, then canonical SMILES then Morgan fingerprints among other datatypes like MACCS

  
