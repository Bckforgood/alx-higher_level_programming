#include "lists.h"
#include <stdlib.h>

/**
 * check_cycle - to checks if a linked list contains a cycle
 * @list: my linked list to check
 *
 * Return: always 1 if the list has a cycle and 0 if it doesn't
 */
int check_cycle(listint_t *list)
{
	listint_t *turtle, *hare;

	if (list == NULL || list->next == NULL)
		return (0);

	tr = list->next;
	hr = list->next->next;

	while (tr && hr && hr->next)
	{
		if (tr == hr)
			return (1);

		tr = tr->next;
		hr = hr->next->next;
	}

	return (0);
}
