include 'decl.pxi'

#cimport sage.structure.element
cimport cython

@cython.final
cdef class gen:
     #cdef object _parent
     cdef GEN g	
     cdef pari_sp b
     cdef dict refers_to

cdef gen objtogen(object s)

