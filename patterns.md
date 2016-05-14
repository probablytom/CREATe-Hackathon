---

title: "General Patterns"
category: pat
layout: default

---


Name: Transfer

Conflict:
Owner  has  a resource R
Receiver wants a resource R

Solution:
Receiver acquires resource R
[Receiver does not acquire resource R]

Consequence:


Further Patterns:




----------------------


Name: Giving

Conflict:
as with Transfer
also, Owner is willing to undergo the transfer

Solution:
as with Transfer

Consequence:
potential blackmail (willing to undergo transfer in avoidance of other situation)



---------------------

Name: Taking

Conflict:
as with Transfer
also, Owner's permission is unspecified or explicitly not given

Solution:
either as with Transfer (in which case, this is BAD)
or the transfer does not occur


---------------------

Name: Trade

Conflict:
As with Transfer
also,
Owner wants resource R'
Receiver  has  resource R'
(i.e. Transfer is mirrored)

Solution:
as with Transfer, mirrored

this may or may not imply giving.

---------------------


Name: Theft

Conflict:
As with Taking
Resource is constrained in that it is not clonable (i.e. has some implication of constrained clonability)
-------> CONSIDER TRANSFERS ON A BLOCKCHAIN. UNLAWFUL ACQUISITION OF RESOURCES RESULTS IN PIRACY BECOMING SIMPLE THEFT

Solutions:
as with Taking

---------------------

Name: Piracy

Conflict
As with Taking
Resource is constrained in that it is clonable (i.e. has some implication of clonability, alternatively is infinitely replicable)

Solutions:
as with Taking

---------------------

Parameters:
(i.e. things that specify and distinguish the patterns specified above)
clonability
resource transfer success or failure
permission granted, denied, not specified by Owner
mutuality

{consumability}



