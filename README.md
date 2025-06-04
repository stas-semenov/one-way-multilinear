# one-way-multilinear

## One-way Multilinear Functions with Linear Shifts

This repository contains the implementation and research materials for a novel class of binary operations on finite-dimensional vector spaces. These operations are defined by **second-order multilinear expressions with affine shifts**.

### Key Characteristics:

* **Complexity Growth:** When a vector is repeatedly operated on itself (`a * a * ... * a`), the resulting polynomial expression's degree grows linearly, while the number of distinct monomials grows combinatorially. This rapid increase in complexity makes finding a closed-form expression for `a^n` exceptionally difficult.
* **Algebraic Properties:** Despite being generally non-associative and non-commutative, these operations exhibit **power associativity** and **internal commutativity** when applied iteratively to a single element. This ensures that `a^m * a^n = a^(m+n)` holds, making exponentiation well-defined.
* **One-Way Behavior:** The computational ease of calculating `a^n` given `a` and `n`, contrasted with the apparent difficulty of recovering `n` from `a^n` (the **Discrete Iteration Problem**), suggests a strong one-way property.
* **Cryptographic Potential:** We explore the application of these functions in finite fields, proposing a **Diffie-Hellman-like key exchange protocol**. The security of this protocol relies on the presumed hardness of the **Algebraic Diffie-Hellman Problem (ADHP)**, a new computational problem arising from this class of operations.

### Project Content:

* `M3System.ipynb`: Python implementation of the 3-dimensional multilinear operation (M3) over finite fields.
* `M4System.ipynb`: Python implementation of the 4-dimensional multilinear operation (M4) over finite fields.

This project aims to contribute to the fields of **algebraic dynamics**, **symbolic computation**, and the development of **novel cryptographic primitives**.

### Citation

If you use this code or concepts from this repository in your research, please cite:

Semenov, S. (2025). *One-way multilinear functions of the second order with linear shifts*. Zenodo.  
DOI: [10.5281/zenodo.15593332](https://doi.org/10.5281/zenodo.15593332)
