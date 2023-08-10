#include "lists.h"
#include <stdlib.h>

/**
 * insert_node - function that that insert a number
 * into a sorted singly linked list
 * @head: hed of sorted linked list
 * @number: number inserted into the singedly linked list
 * Return: singly linked list with newly added
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = NULL;
	listint_t *new_nodes = NULL, *temp = NULL;

	new_nodes = malloc(sizeof(listint_t));
	if (new_nodes == NULL)
		return (NULL);

	new_nodes->n = number;
	if (*head)
	{
		current = *head;
		if (number <= current->n)
		{
			new_nodes->next = current;
			*head = new_nodes;
		}
		else
		{
			while (current->next)
			{
				if (number <= current->next->n)
				{
					temp = current->next;
					current->next = new_nodes;
					new_nodes->next = temp;
					return (*head);
				}

				current = current->next;
			}
			temp = current->next;
			current->next = new_nodes;
			new_nodes->next = temp;
		}
		return (*head);
	}
	new_nodes->next = NULL;
	*head = new_nodes;
	return (*head);
}
