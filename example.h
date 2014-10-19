#ifndef __PYX_HAVE__example
#define __PYX_HAVE__example


#ifndef __PYX_HAVE_API__example

#ifndef __PYX_EXTERN_C
  #ifdef __cplusplus
    #define __PYX_EXTERN_C extern "C"
  #else
    #define __PYX_EXTERN_C extern
  #endif
#endif

__PYX_EXTERN_C DL_IMPORT(void) _pari_trap(long, long);

#endif /* !__PYX_HAVE_API__example */

#if PY_MAJOR_VERSION < 3
PyMODINIT_FUNC initexample(void);
#else
PyMODINIT_FUNC PyInit_example(void);
#endif

#endif /* !__PYX_HAVE__example */
