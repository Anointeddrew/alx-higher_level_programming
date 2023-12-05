#include <stdlib.h>
#include <stdio.h>
#include <Python.h>
/**
 * print_python_list_info -  function that prints some basic
 *							info about Python lists
 * @p: python list
 */
void print_python_list_info(PyObject *p)
{
	int elmt;

	printf("[*] Size of the Python List = %lu\n", Py_SIZE(p));
	printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
	for (elmt = 0; elmt < Py_SIZE(p); elmt++)
		printf("Element %d: %s\n", elmt, Py_TYPE(PyList_GetItem(p, elmt))->tp_name);
}
