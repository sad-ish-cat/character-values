# Character Table Values of the symmetric and signed symmetric group

character values notebook.ipynb includes functions for calculating, storing, and retrieving the raw data for the character table of the symmetric group, as well as functions for calculating column congruence of conjugacy classes for each character table and for determining the proportion of zeroes in $Z_p$. 

signed_permutations.py is a library by the excellent Joshua Mundinger which implements the signed symmetric group as the symmetries of the hyperoctahedron; it has functions for determining the signed permutations and conjugacy classes of $B_n$.

B_n.ipynb is unfortunately buggy - it's theoretically supposed to calculate column congruences for the signed symmetric group, but unfortunately the bespoke implementation from signed_permutations.py doesn't mesh well with the (broken) functions in the SageMath symmetrica library. 
