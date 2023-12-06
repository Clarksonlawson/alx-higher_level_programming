#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - prints basic info about Python lists
 * @p: Python object
 */
void print_python_list(PyObject *p)
{
	PyListObject *list = (PyListObject *)p;
	PyVarObject *varobj = (PyVarObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", varobj->ob_size);

	if (PyList_Check(p))
	{
		printf("[*] Allocated = %ld\n", list->allocated);
	}
	else
	{
		printf("[*] Allocated = 0\n");
	}

	for (Py_ssize_t i = 0; i < varobj->ob_size; ++i)
	{
		printf("Element %ld: %s\n", i, Py_TYPE(list->ob_item[i])->tp_name);
	}
}
/**
 * print_python_bytes - prints basic info about Python bytes
 * @p: Python object
 */
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes = (PyBytesObject *)p;
	PyVarObject *varobj = (PyVarObject *)p;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", varobj->ob_size);
	printf("  trying string: %s\n", PyUnicode_AsUTF8(p));

	printf("  first 10 bytes: ");
	for (Py_ssize_t i = 0; i < 10 && i < varobj->ob_size; ++i)
	{
		printf("%02x ", (unsigned char)bytes->ob_sval[i]);
	}
	printf("\n");
}
