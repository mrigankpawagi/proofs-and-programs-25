import Mathlib

/-!
# Listable typeclass

This is a crude version of finite types. It is a typeclass that provides a list of all the elements of a type.
-/
class Listable (α : Type u) where
  elems : List α
  elemsComplete : ∀ (a : α), a ∈ elems

instance : Listable Bool where
  elems := [false, true]
  elemsComplete := by
    intro a
    cases a
    · simp
    · simp

def listableElems (α : Type u) [Listable α] : List α := Listable.elems

theorem inListableElems
    {α : Type u} [Listable α] (a : α) : a ∈ listableElems α := Listable.elemsComplete a

instance prodListable {α β : Type u} [Listable α] [Listable β] : Listable (α × β) where
  elems :=
      let as := listableElems α
      let bs := listableElems β
      as.flatMap fun a => bs.map fun b => (a, b)
  elemsComplete := by
    intro (a, b)
    sorry
