#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * is_palindrome - check is singly list is palindrome
 * @head: pointer to head of the linked list
 * Return: 0 if not palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
	listint_t *begin = NULL, *finish = NULL;
	unsigned int i = 0;
	unsigned int length = 0, length_cycle = 0, length_list = 0;

	if (head == NULL)
		return (0);

	if (*head == NULL)
		return (1);

	begin = *head;
	length = listint_len(begin);
	length_cycle = length * 2;
	length_list = length_cycle - 2;
	finish = *head;

	for (; i < length_cycle; i = i + 2)
	{
		if (begin[i].n != finish[length_list].n)
			return (0);

		length_list = length_list - 2;
	}

	return (1);
}

/**
 * get_nodeint_at_index - get nodes from linked list
 * @head: pointer to head of link list
 * @index: index to find linked list
 *
 * Return: specific node of linked list
 */
listint_t *get_nodeint_at_index(listint_t *head, unsigned int index)
{
	listint_t *current = head;
	unsigned int it_times = 0;

	if (head)
	{
		while (current != NULL)
		{
			if (it_times == index)
				return (current);

			current = current->next;
			++it_times;
		}
	}

	return (NULL);
}

/**
 * listint_len - number count of element in linked list
 * @h: linked list to be counted
 * Return: number of element in linked list
 */
size_t listint_len(const listint_t *h)
{
	int len = 0;

	while (h != NULL)
	{
		++len;
		h = h->next;
	}

	return (len);
}
