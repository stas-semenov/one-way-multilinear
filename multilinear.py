import collections.abc

# Define the M3System class to hold the parameters and modulus
# This encapsulates the specific algebraic system (V, *)
class M3System:
    def __init__(self, A, B, C, D, E, modulus):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.modulus = modulus

    # Override __repr__ for better readability of the system object
    def __repr__(self):
        return (f"M3System(A={self.A}, B={self.B}, C={self.C}, D={self.D}, E={self.E}, "
                f"modulus={self.modulus})")

# Define the M3Element class to represent vectors within a specific M3System
class M3Element:
    def __init__(self, value: list[int], system: M3System):
        if not isinstance(value, collections.abc.Sequence) or len(value) != 3:
            raise ValueError("Value must be a list or tuple of 3 integers.")
        if not isinstance(system, M3System):
            raise TypeError("System must be an instance of M3System.")

        self.system = system
        self.value = [x % self.system.modulus for x in value]

    # Standard vector addition for the underlying vector space
    def __add__(self, other):
        if not isinstance(other, M3Element) or self.system != other.system:
            return NotImplemented # Or raise ValueError for system mismatch
        return M3Element([(x + y) % self.system.modulus for x, y in zip(self.value, other.value)], self.system)

    # Standard vector subtraction
    def __sub__(self, other):
        if not isinstance(other, M3Element) or self.system != other.system:
            return NotImplemented
        return M3Element([(x - y) % self.system.modulus for x, y in zip(self.value, other.value)], self.system)

    # Standard unary negation
    def __neg__(self):
        return M3Element([(-x) % self.system.modulus for x in self.value], self.system)

    # The core binary operation '*' as defined in the article
    # Corresponds to (ab) in the article
    def __mul__(self, other):
        if not isinstance(other, M3Element) or self.system != other.system:
            return NotImplemented # Or raise ValueError for system mismatch

        # Components of vector 'a' (self)
        a0, a1, a2 = self.value
        # Components of vector 'b' (other)
        b0, b1, b2 = other.value
        
        # Parameters of the M3System
        A, B, C, D, E = self.system.A, self.system.B, self.system.C, self.system.D, self.system.E
        N = self.system.modulus

        # Component-wise definition of (ab)_i based on the article's K^3 formula
        # (ab)_0 = a_0 + b_0 + a_0 b_0 + A a_1 b_1 + C a_2 b_1 + B a_2 b_2
        r0 = (a0 + b0 + a0 * b0 + A * a1 * b1 + C * a2 * b1 + B * a2 * b2) % N
        
        # (ab)_1 = a_1 + b_1 + a_1 b_0 + a_0 b_1 + D a_1 b_1 + E a_1 b_2
        r1 = (a1 + b1 + a1 * b0 + a0 * b1 + D * a1 * b1 + E * a1 * b2) % N
        
        # (ab)_2 = a_2 + b_2 + a_2 b_0 + a_0 b_2 + D a_2 b_1 + E a_2 b_2
        r2 = (a2 + b2 + a2 * b0 + a0 * b2 + D * a2 * b1 + E * a2 * b2) % N

        return M3Element([r0, r1, r2], self.system)

    # Implements exponentiation a^n (repeated application of '*')
    # Uses exponentiation by squaring for efficiency
    def __pow__(self, exponent: int):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("Exponent must be a non-negative integer.")
        
        # The neutral element 'e' (multiplicative identity) as defined in the article (0,0,0)
        # a * e = e * a = a
        identity_element = M3Element([0, 0, 0], self.system) 

        if exponent == 0:
            return identity_element

        # Start with the base vector 'a'
        base = self 
        # Initialize result with the identity element
        result = identity_element

        # Exponentiation by squaring algorithm
        while exponent > 0:
            if exponent % 2 == 1: # If the current bit of the exponent is 1
                result = result * base # Multiply result by the current base power
            base = base * base       # Square the base
            exponent //= 2           # Integer division by 2 (shift exponent right)

        return result

    # String representation for debugging and printing
    def __repr__(self):
        return f"M3Element(value={self.value}, system_id={id(self.system)})" # Added system_id for clarity

    # User-friendly text representation
    def text(self):
        return str(self.value)


# Define the M4System class to hold the parameters and modulus for the 4D operation
# This encapsulates the specific algebraic system (V=K^4, *)
class M4System:
    def __init__(self, A, B, C, D, E, F, G, H, I, modulus):
        self.A = A
        self.B = B
        self.C = C
        self.D = D
        self.E = E
        self.F = F
        self.G = G
        self.H = H
        self.I = I
        self.modulus = modulus

    # Override __repr__ for better readability of the system object
    def __repr__(self):
        return (f"M4System(A={self.A}, B={self.B}, C={self.C}, D={self.D}, E={self.E}, "
                f"F={self.F}, G={self.G}, H={self.H}, I={self.I}, modulus={self.modulus})")

# Define the M4Element class to represent vectors within a specific M4System
class M4Element:
    def __init__(self, value: list[int], system: M4System):
        if not isinstance(value, collections.abc.Sequence) or len(value) != 4:
            raise ValueError("Value must be a list or tuple of 4 integers.")
        if not isinstance(system, M4System):
            raise TypeError("System must be an instance of M4System.")

        self.system = system
        self.value = [x % self.system.modulus for x in value]

    # Standard vector addition for the underlying vector space
    def __add__(self, other):
        if not isinstance(other, M4Element) or self.system != other.system:
            return NotImplemented # Or raise ValueError for system mismatch
        return M4Element([(x + y) % self.system.modulus for x, y in zip(self.value, other.value)], self.system)

    # Standard vector subtraction
    def __sub__(self, other):
        if not isinstance(other, M4Element) or self.system != other.system:
            return NotImplemented
        return M4Element([(x - y) % self.system.modulus for x, y in zip(self.value, other.value)], self.system)

    # Standard unary negation
    def __neg__(self):
        return M4Element([(-x) % self.system.modulus for x in self.value], self.system)

    # The core binary operation '*' as defined in the article for K^4
    # Corresponds to (ab) in the article
    def __mul__(self, other):
        if not isinstance(other, M4Element) or self.system != other.system:
            return NotImplemented # Or raise ValueError for system mismatch

        # Components of vector 'a' (self)
        a0, a1, a2, a3 = self.value
        # Components of vector 'b' (other)
        b0, b1, b2, b3 = other.value
        
        # Parameters of the M4System
        A, B, C, D, E, F, G, H, I = (self.system.A, self.system.B, self.system.C, self.system.D,
                                      self.system.E, self.system.F, self.system.G, self.system.H, self.system.I)
        N = self.system.modulus

        # Component-wise definition of (ab)_i based on the article's K^4 formula
        # (ab)_0 = a_0 + b_0 + a_0 b_0 + A a_1 b_1 + E a_3 b_1 + B a_2 b_2 + D a_1 b_2 + F a_3 b_2 + C a_3 b_3
        r0 = (a0 + b0 + a0 * b0 + A * a1 * b1 + E * a3 * b1 + 
              B * a2 * b2 + D * a1 * b2 + F * a3 * b2 + C * a3 * b3) % N
        
        # (ab)_1 = a_1 + b_1 + a_1 b_0 + a_0 b_1 + G a_1 b_1 + H a_1 b_2 + I a_1 b_3
        r1 = (a1 + b1 + a1 * b0 + a0 * b1 + G * a1 * b1 + H * a1 * b2 + I * a1 * b3) % N
        
        # (ab)_2 = a_2 + b_2 + a_2 b_0 + a_0 b_2 + G a_2 b_1 + H a_2 b_2 + I a_2 b_3
        r2 = (a2 + b2 + a2 * b0 + a0 * b2 + G * a2 * b1 + H * a2 * b2 + I * a2 * b3) % N

        # (ab)_3 = a_3 + b_3 + a_3 b_0 + a_0 b_3 + G a_3 b_1 + H a_3 b_2 + I a_3 b_3
        r3 = (a3 + b3 + a3 * b0 + a0 * b3 + G * a3 * b1 + H * a3 * b2 + I * a3 * b3) % N

        return M4Element([r0, r1, r2, r3], self.system)

    # Implements exponentiation a^n (repeated application of '*')
    # Uses exponentiation by squaring for efficiency
    def __pow__(self, exponent: int):
        if not isinstance(exponent, int) or exponent < 0:
            raise ValueError("Exponent must be a non-negative integer.")
        
        # The neutral element 'e' (multiplicative identity) as defined in the article (0,0,0,0)
        # a * e = e * a = a
        identity_element = M4Element([0, 0, 0, 0], self.system) 

        if exponent == 0:
            return identity_element
        
        # Start with the base vector 'a'
        base = self 
        # Initialize result with the identity element
        result = identity_element

        # Exponentiation by squaring algorithm
        while exponent > 0:
            if exponent % 2 == 1: # If the current bit of the exponent is 1
                result = result * base # Multiply result by the current base power
            base = base * base       # Square the base
            exponent //= 2           # Integer division by 2 (shift exponent right)

        return result

    # String representation for debugging and printing
    def __repr__(self):
        # Using id(self.system) to show that elements belong to the same system instance
        return f"M4Element(value={self.value}, system_id={id(self.system)})" 

    # User-friendly text representation
    def text(self):
        return str(self.value)
