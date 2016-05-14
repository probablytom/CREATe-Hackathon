---

title: "General Patterns"
category: ref
layout: default

---

## Design Patterns

Here we list a series of basic design patterns as a part of the pattern language.


### Transfer Pattern

**Conflict:**
* Owner has a resource R
* Receiver wants a resource R

**Solution:**
* Receiver acquires resource R
* [Receiver does not acquire resource R]

----------------------


### Giving Pattern

**Conflict:**
* As with Transfer
* Also, Owner is willing to undergo the transfer

**Solution:**
* As with Transfer

**Consequence:**
* Potential blackmail (willing to undergo transfer in avoidance of other situation)



---------------------

### Taking Pattern

**Conflict:**
* As with Transfer
* Also, Owner's permission is unspecified or explicitly not given

**Solution:**
* Either as with Transfer (in which case, this is BAD) or the transfer does not occur


---------------------

### Trade Pattern

**Conflict:**
* As with Transfer
* Also:  
   Owner wants resource R'  
   Receiver  has  resource R'
(i.e. Transfer is mirrored)

**Solution:**
* As with Transfer, mirrored

NB: this may or may not imply giving.

---------------------

### Theft Pattern

**Conflict:**
* As with Taking
* Resource is constrained in that it is not clonable (i.e. has some implication of constrained clonability)

**Solutions:**
* as with Taking

**Consequence:**
* Consider transfers on a blockchain. Unlawful acquisition of resources results in piracy becoming simple theft.


---------------------

### Piracy Pattern

**Conflict:**
* As with Taking
* Resource is constrained in that it is clonable (i.e. has some implication of clonability, alternatively is infinitely replicable)

**Solutions:**
* as with Taking

---------------------

## Pattern Modifying Parameters

(i.e. things that specify and distinguish the patterns specified above)
* clonability
* resource transfer success or failure
* permission granted, denied, not specified by Owner
* mutuality
* consumability (this affects the resource, not the pattern directly)
