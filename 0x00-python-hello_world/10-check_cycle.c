#include "lists.h"

/**
 * check_cycle - function if a linked list contain a cycle,
 * @list: link list to check
 * Return: 1 if it has a link list, 0 if otherwise
 */
int check_cycle(listint_t *list)
{
	listint_t *sl_o = list;
	listint_t *fa_s = list;

	if (!list)
		return (0);

	while (sl_o && fa_s && fa_s->next)
	{
		sl_o = sl_o->next;
		fa_s = fa_s->next->next;
		if (sl_o == fa_s)
			return (1);
	}

	return (0);
}

