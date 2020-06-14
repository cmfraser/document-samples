"""Includes a primary function that returns the complement of a DNA sequence.

This Python 3 module defines five functions: three for external use and two for
internal use. The module also defines a user-defined exception raised when an
invalid DNA base is detected.

This module is intended primarily to illustrate docstring and doctest usage.

This module has been released under the MIT License:

Copyright (c) 2020 Bioanalytical Computing, LLC

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

class Error(Exception):
    """Functions as the exception base class in this module.

    Included for extensibility.
    """
    pass

class DnaSequenceError(Error):
    """Indicates that a DNA sequence is invalid due to its type or content.

    Raise a DnaSequenceError when one of the following is encountered:
        1. A sequence that is not a string (for example, 1234)
        2. A sequence contains something other than valid bases:
           'A', 'G', 'C', 'T'

    Attributes
        message -- A string that explains the identified sequence error.
    """

    def __init__(self, message):
        """Initializes DnaSequenceError with a message explaining the identified
           error."""
        self.message = message

def get_valid_bases(return_values="bases_only"):
    """Returns the valid DNA bases used by the functions in this module.

    Arguments
        return_values -- Determines the value (and type) of what the function
                         returns. If return_values == "bases_only", the function
                         returns a list with valid bases; if
                         return_values == "base_complements", the function
                         returns a dict with valid bases as keys and base
                         complements as values.

    Raises
        ValueError, if return_values is neither 'bases_only' nor
        'base_complements'.

    Returns
        (a) A list containing valid bases (if return_values == 'bases_only'):
            ['A', 'G', 'C', 'T']
        (b) A dict containing the valid DNA bases and their complements (if
            return_values == 'base_complements'):
            {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}

    Doctests
        >>> get_valid_bases("bases_only")
        ['A', 'G', 'C', 'T']
        >>> get_valid_bases("base_complements")
        {'A': 'T', 'G': 'C', 'C': 'G', 'T': 'A'}
        >>> get_valid_bases("Whoops!")
        Traceback (most recent call last):
        ...
        ValueError: return_values must be either 'bases_only' or 'base_complements'
    """
    valid_bases = ['A', 'G', 'C', 'T']
    if return_values == "bases_only":
        return valid_bases
    elif return_values == "base_complements":
        # [::-1] reverses the list of bases
        return dict(zip(valid_bases, valid_bases[::-1]))
    else:
        raise ValueError("return_values must be either 'bases_only' or " + \
                         "'base_complements'")

def _validate_base(base, position):
    """Determines whether a DNA base is a valid base: 'A', 'G', 'C', or 'T'.

    For in-module use only.

    Note: This function ignores case (for example, both 'A' and 'a' are valid
    bases).

    Arguments
        base     -- The base to be validated.
        position -- The position of the base in a sequence; used only if
                    DnaSequenceError is raised; does not use zero indexing (for
                    the first base in a sequence, position == 1).

    Returns
        None

    Raises
        DnaSequenceError, if an invalid base is found; the message for the error
        includes the invalid base and the position of that base.

    Doctests
        >>> _validate_base('A', 1)
        >>> _validate_base('a', 1)
        >>> _validate_base('U', 4)
        Traceback (most recent call last):
        ...
        DnaSequenceError: invalid base 'U' found at sequence position 4
        >>> _validate_base('2', 1)
        Traceback (most recent call last):
        ...
        DnaSequenceError: invalid base '2' found at sequence position 1
    """
    if base.upper() not in get_valid_bases():
        raise DnaSequenceError("invalid base '" + base +  "' found at " + \
                               "sequence position " + str(position))

def _validate_type(dna_sequence):
    """Determines whether a DNA sequence has the valid type: string.

    For in-module use only.

    Arguments
        dna_sequence -- The DNA sequence to be validated.

    Returns
        None

    Raises
        DnaSequenceError, if dna_sequence is not a string. The error message
        includes the invalid type found.

    Doctests
        >>> _validate_type("AGCT")
        >>> _validate_type("aGCT")
        >>> _validate_type("AGCU")
        >>> _validate_type("2GCT")
        >>> _validate_type(1234)
        Traceback (most recent call last):
        ...
        DnaSequenceError: invalid sequence type (int)
    """
    sequence_type = type(dna_sequence).__name__
    if sequence_type != "str":
        raise DnaSequenceError("invalid sequence type (" + sequence_type + ")")

def validate_dna_sequence(dna_sequence):
    """Determines whether a dna_sequence is a string and whether the sequence
       contains only the following bases: 'A', 'G', 'C', 'T'.

    Note: variable 'position' does not use zero indexing (for the first base in
    a sequence, position == 1).

    Arguments
        dna_sequence -- The DNA sequence to be validated.

    Returns
        None

    Raises
        Nothing; only the called functions raise exceptions.

    Doctests
        >>> validate_dna_sequence("AGCT")
        >>> validate_dna_sequence("aGCT")
        >>> validate_dna_sequence("AGCU")
        Traceback (most recent call last):
        ...
        DnaSequenceError: invalid base 'U' found at sequence position 4
        >>> validate_dna_sequence("2GCT")
        Traceback (most recent call last):
        ...
        DnaSequenceError: invalid base '2' found at sequence position 1
        >>> validate_dna_sequence(1234)
        Traceback (most recent call last):
        ...
        DnaSequenceError: invalid sequence type (int)
    """
    _validate_type(dna_sequence)
    position = 0
    for base in dna_sequence:
        position += 1
        _validate_base(base, position)


def get_reverse_complement(dna_sequence):
    """Returns the reverse complement of a DNA sequence.

    The function validates the DNA sequence before finding and returning
    its complement.

    Arguments
        dna_sequence -- The DNA sequence whose reverse complement is to be
                        returned.

    Returns
        A string consisting of the reverse complement of the DNA sequence
        passed to the function.

    Raises
        Nothing; only the called functions raise exceptions.

    Doctests
        >>> get_reverse_complement("AGCT")
        'AGCT'
        >>> get_reverse_complement("aGCT")
        'AGCT'
        >>> get_reverse_complement("AGCU")
        Traceback (most recent call last):
        ...
        DnaSequenceError: invalid base 'U' found at sequence position 4
        >>> get_reverse_complement("2GCT")
        Traceback (most recent call last):
        ...
        DnaSequenceError: invalid base '2' found at sequence position 1
        >>> get_reverse_complement(1234)
        Traceback (most recent call last):
        ...
        DnaSequenceError: invalid sequence type (int)
    """
    complements = get_valid_bases("base_complements")
    validate_dna_sequence(dna_sequence)
    # [::-1] reverses the DNA sequence
    return "".join(complements[base.upper()] for base in dna_sequence[::-1])


if __name__ == "__main__":
    import doctest
    doctest.testmod()
