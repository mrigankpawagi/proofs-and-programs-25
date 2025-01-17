* Terms > Types (including Propositions) > Universes
* Sort 0 = Prop. proofs of p: proposition p.
* Sort (n+1) = Type n.

### Types
* Universes
* Function and dependent function types: constructed by rules.
* Inductive types & indexed inductive types (including structures).

### Terms
Constructed with 
* function application
* $\lambda$-definitions (and let declarations)
* recursion/induction on inductive types

---

### Church: Simple Theory of Types
* **Key construction:** If $\alpha$, $\beta$ are types, then $\alpha \to \beta$ is a type. If $f: \alpha \to \beta$ and $x: \alpha$, then $f x$ is a well-formed term of type $\beta$.
