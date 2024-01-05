#include "Python.h"

/**
 * print_python_string - Prints Python string info.
 * @p: A string object of type PyObject.
 */

void print_python_string(PyObject *p)
{
	long int len;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str"))
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

	len = ((PyASCIIObject *)p)->length;

	printf("  type: %s\n", PyUnicode_IS_COMPACT_ASCII(p) ?
	       "compact ascii" : "compact unicode object");
	printf("  length: %ld\n", len);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &len));
}
